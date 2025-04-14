# 📞 Transcrição Automática de Chamadas com Whisper

Este projeto foi desenvolvido para **monitorar gravações de chamadas** em um sistema **PABX Asterisk**, transcrever automaticamente os arquivos de áudio usando o modelo **Whisper** da OpenAI e armazenar os textos gerados.

---

## ⚙️ Como Funciona

- O script monitora o diretório `/etc/asterisk/rec` em busca de arquivos `.wav`.
- Quando um novo arquivo é detectado e finalizado, ele é processado pelo modelo **Whisper**.
- A transcrição é salva no diretório `/etc/asterisk/rec/text`, com o mesmo nome do arquivo original.
- O arquivo de áudio é movido para o diretório `/etc/asterisk/rec/hst` após ser processado.

---

## 📦 Requisitos

- Python **3.8+**
- Bibliotecas necessárias (instale com `pip install openai-whisper`)
- Um servidor **Asterisk** configurado para salvar gravações de chamadas no diretório `/etc/asterisk/rec`

---

## 🚀 Instalação

1. Clone o repositório:


git clone https://github.com/gabrielpiaia/whisper
cd whisper



## 🔧 Configuração

O script utiliza os seguintes diretórios:

/etc/asterisk/rec: Diretório onde as gravações de chamadas são salvas.

/etc/asterisk/rec/hst: Arquivos de áudio processados são movidos para cá.

/etc/asterisk/rec/text: As transcrições são salvas neste diretório.
