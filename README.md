# Rss Telegram Bot

## Descrizione
**Rss Telegram Bot** è un programma scritto in python per gestire un bot telegram come updater da applicare ad un sito/blog che sfrutta l'rss.

## Installazione
### Requisiti
- **Software**: Python e librerie richieste (da installare tramite pip):
    - feedparser
    - python-telegram-bot
    - python-dotenv
    - asyncio

### Procedura di Installazione
1. Scarica il file `bot.py` e posizionalo in una cartella
2. Crea un file `.env` nella stessa cartella
3. Inserisci l'api del bot telegram all'interno del file `.env` nel formato TOKEN="123456"
4. Inserisci nel listato l'url del sito da cui ricavare i post.
5. Inserisci nel listato l'id della chat telegram a cui il bot deve inviare i post
6. Avvia il file `bot.py`
