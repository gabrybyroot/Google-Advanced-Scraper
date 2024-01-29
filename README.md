# Google Advanced Scraper

**Disclaimer:** I do not assume any responsibility for the use of these files by any user. I recommend using them solely for educational, professional, or testing purposes. Feel free to implement the code and make any necessary modifications with comments.

## Descrizione
Questo script Python ti consente di effettuare ricerche avanzate su Google utilizzando vari filtri, come il tipo di file, l'anno, il tipo di risultato, il testo all'interno della pagina, l'URL e altro ancora.

## Opzioni
--file_type: Filtro per tipo di file (es. pdf, doc).
--year: Filtro per anno.
--result_type: Filtro per tipo di risultato (es. news, images).
--in_text: Testo da cercare all'interno della pagina.
--in_url: L'URL deve contenere questa stringa.
--site: Ricerca solo in questo sito.
--feed: Ricerca feed RSS o Atom.
--language: Ricerca pagine scritte in una lingua specifica.
--num_results: Numero di risultati da visualizzare (default: 10).

## Requisiti
- Python 3.x
- Installa le dipendenze con `pip install -r requirements.txt`

## Uso
Esegui lo script `main.py` fornendo la parola chiave di ricerca e, se necessario, specifica ulteriori filtri tramite le opzioni della riga di comando.

```bash
python main.py "parola chiave" --file_type pdf --year 2023 --result_type news
