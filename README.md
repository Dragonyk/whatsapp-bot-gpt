# 🤖 WhatsApp Message Sender Bot com GPT

Este projeto é um **bot automatizado de envio de mensagens via WhatsApp Web**, utilizando o **Selenium WebDriver** e integração com uma **API do GPT** para geração dinâmica de mensagens personalizadas.

---

## ⚠️ Aviso Legal

> Este projeto é apenas para fins educacionais e experimentais.  
> O uso pode violar os [Termos de Serviço do WhatsApp](https://www.whatsapp.com/legal/terms-of-service).  
> **Utilize por sua conta e risco.**

---

## 📦 Requisitos

- Python 3.7+
- Google Chrome (ou Microsoft Edge, com ajustes)
- [Selenium](https://pypi.org/project/selenium/)
- API do GPT (OpenAI, local ou outro backend via `text_generator.py`)
- Arquivos CSV para contatos e tipos de mensagem

---

## 📁 Estrutura do Projeto

project/
│
├── main.py # Código principal de envio
├── io_utils.py # Funções utilitárias de I/O (não incluído neste repositório)
├── text_generator.py # Geração de mensagens via GPT
├── _res/
│ ├── lista2.csv # Lista de contatos
│ └── lista_tipos.csv # Tipos de mensagens e rótulos


---

## 🧠 Geração de Mensagens com GPT

O módulo `text_generator.py` é responsável por criar mensagens personalizadas com base no tipo de mensagem informado em `lista_tipos.csv`.  
Você pode usar qualquer backend GPT compatível com Python (ex: OpenAI API) para gerar os textos.

python
import text_generator
mensagem = text_generator.gerar_mensagem(tipo)

## 🛡️ Boas Práticas

    Teste com poucos contatos antes de executar em massa.

    Evite spam. Isso pode causar bloqueios da conta.

    Use delays entre os envios para parecer mais humano.
