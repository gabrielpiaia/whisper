import os
import time
import shutil
import whisper

# Diretórios base
MONITOR_DIR = '/etc/asterisk/rec'
HST_DIR = os.path.join(MONITOR_DIR, 'hst')
TEXT_DIR = os.path.join(MONITOR_DIR, 'text')

# Cria os diretórios se não existirem
os.makedirs(HST_DIR, exist_ok=True)
os.makedirs(TEXT_DIR, exist_ok=True)

# Carrega o modelo Whisper (você pode escolher "tiny", "base", "small", "medium" ou "large")
model = whisper.load_model("medium")

def wait_for_file_completion(file_path, timeout=10):
    """Verifica se o arquivo foi finalizado (tamanho não muda por um tempo)."""
    if not os.path.exists(file_path):
        return False

    initial_size = os.path.getsize(file_path)
    time_waited = 0

    while time_waited < timeout:
        time.sleep(1)  # Aguardar 1 segundo antes de checar novamente
        current_size = os.path.getsize(file_path)

        if current_size == initial_size:
            return True  # O arquivo parou de crescer, podemos processá-lo
        initial_size = current_size
        time_waited += 1

    return False  # Timeout alcançado, o arquivo ainda está mudando

def process_audio_file(filepath):
    """
    Transcreve o áudio usando o modelo Whisper.
    Retorna a transcrição ou None se ocorrer erro.
    """
    try:
        result = model.transcribe(filepath, language="pt")
        transcription = result["text"]
        return transcription
    except Exception as e:
        print(f"Erro ao processar {filepath}: {e}")
        return None

def move_file(src, dest_dir):
    """
    Move o arquivo src para o diretório dest_dir.
    """
    try:
        shutil.move(src, dest_dir)
    except Exception as e:
        print(f"Erro ao mover o arquivo {src}: {e}")
    
def main_loop():
    """
    Loop principal: verifica o diretório de monitoramento, processa e move os arquivos.
    """
    while True:
        try:
            # Lista apenas os arquivos .wav que estejam diretamente em MONITOR_DIR
            files = [f for f in os.listdir(MONITOR_DIR)
                     if f.endswith('.wav') and os.path.isfile(os.path.join(MONITOR_DIR, f))]
            
            for filename in files:
                filepath = os.path.join(MONITOR_DIR, filename)

                # Verificar se o arquivo foi finalizado
                if not wait_for_file_completion(filepath):
                    print(f"Arquivo {filename} ainda está sendo gravado, aguardando...")
                    continue  # Ignora esse arquivo e continua com os outros

                print(f"Processando arquivo: {filename}")

                transcription = process_audio_file(filepath)
                
                if transcription is not None and transcription.strip() != "":
                    # Salva a transcrição no diretório TEXT_DIR com a mesma base do nome do arquivo
                    base_name = os.path.splitext(filename)[0]
                    text_filename = base_name + '.txt'
                    text_filepath = os.path.join(TEXT_DIR, text_filename)
                    
                    with open(text_filepath, 'w', encoding='utf-8') as f:
                        f.write(transcription)
                    
                    print(f"Transcrição salva em: {text_filepath}")
                    
                    # Move o arquivo de áudio para o diretório HST_DIR
                    move_file(filepath, HST_DIR)
                    print(f"Arquivo movido para hst: {filename}")
                else:
                    print(f"Transcrição vazia ou inválida para: {filename}")
            print(f"Transcrição finalizada!")
            # Aguarda 10 segundos antes de verificar novamente
            time.sleep(10)
        except Exception as e:
            print("Erro no loop principal:", e)
            time.sleep(10)

if __name__ == '__main__':
    main_loop()

