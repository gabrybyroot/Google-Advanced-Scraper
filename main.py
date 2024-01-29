import argparse
from googlesearch import search

def advanced_search(query, file_type=None, year=None, result_type=None, in_text=None, in_url=None, site=None, feed=None, language=None, num_results=10):
    search_query = f"{query} "

    if file_type:
        search_query += f"filetype:{file_type} "
    if year:
        search_query += f"{year} "
    if result_type:
        search_query += f"{result_type} "
    if in_text:
        search_query += f"intext:{in_text} "
    if in_url:
        search_query += f"inurl:{in_url} "
    if site:
        search_query += f"site:{site} "
    if feed:
        search_query += f"feed:{feed} "
    if language:
        search_query += f"language:{language} "
        
    print(f"\nRicerca avanzata su Google di {search_query.strip()}...\n")

    try:
        urls = list(search(search_query, num=num_results, stop=num_results, pause=2))
        print(f"URL trovati: {len(urls)}")
        for url in urls:
            print(url)
    except Exception as e:
        print(f"Si è verificato un errore durante la ricerca: {e}")

def main():
    parser = argparse.ArgumentParser(description='Ricerca avanzata su Google')
    parser.add_argument('query', help='La parola chiave da cercare')
    parser.add_argument('--file_type', help='Filtro per tipo di file')
    parser.add_argument('--year', help='Filtro per anno')
    parser.add_argument('--result_type', help='Filtro per tipo di risultato')
    parser.add_argument('--in_text', help='Testo da cercare nella pagina')
    parser.add_argument('--in_url', help='L\'URL deve contenere questa stringa')
    parser.add_argument('--site', help='Ricerca solo in questo sito')
    parser.add_argument('--feed', help='Ricerca feed RSS o Atom')
    parser.add_argument('--language', help='Ricerca pagine scritte in una lingua specifica')
    parser.add_argument('--num_results', type=int, default=10, help='Numero di risultati da visualizzare')
    args = parser.parse_args()

    print("\n------------------------------------------")
    print("RICERCA AVANZATA SU GOOGLE by @gabrybyroot")
    print("------------------------------------------\n")

    if args.query:
        advanced_search(args.query, args.file_type, args.year, args.result_type,
                        args.in_text, args.in_url, args.site, args.feed, args.language,
                        num_results=args.num_results)
    else:
        print("Errore: Inserire una parola chiave per la ricerca.")

if __name__ == '__main__':
    main()
