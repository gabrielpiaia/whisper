Transcrição Automática de Chamadas com Whisper

Este projeto foi desenvolvido para monitorar gravações de chamadas em um sistema PABX Asterisk, transcrever automaticamente os arquivos de áudio usando o modelo Whisper da OpenAI e armazenar os textos gerados.

Como Funciona

O script monitora o diretório /etc/asterisk/rec em busca de arquivos .wav.

Quando um novo arquivo é detectado e finalizado, ele é processado pelo modelo Whisper.

A transcrição é salva no diretório /etc/asterisk/rec/text com o mesmo nome do arquivo original.

O arquivo de áudio é movido para o diretório /etc/asterisk/rec/hst após ser processado.

Requisitos

Python 3.8+

Bibliotecas necessárias (instale com pip install openai-whisper)

Um servidor Asterisk configurado para salvar gravações de chamadas no diretório /etc/asterisk/rec

Instalação

Clone o repositório:

git clone https://github.com/seu-repositorio/transcricao-pabx.git
cd transcricao-pabx

Instale as dependências:

pip install -r requirements.txt

Execute o script:

python transcribe.py

Configuração

O script usa os seguintes diretórios:

/etc/asterisk/rec: Diretório onde as gravações de chamadas são salvas.

/etc/asterisk/rec/hst: Arquivos de áudio processados são movidos para cá.

/etc/asterisk/rec/text: As transcrições são salvas neste diretório.

Caso precise alterar os diretórios, edite as constantes MONITOR_DIR, HST_DIR e TEXT_DIR no código.

Observações

O modelo padrão usado é o Whisper Medium. Caso queira mudar para outro modelo, edite a linha:

model = whisper.load_model("medium")

e substitua "medium" por "tiny", "base", "small" ou "large".

O script aguarda o fim da gravação antes de processar os arquivos.

Ele roda continuamente em um loop infinito para monitoramento constante.