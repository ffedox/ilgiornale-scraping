# corpus_ilgiornale

Note generali:

- Articoli del 2017 di due giornali e di questi testi tutti i commenti, con i metadati dei commenti (per es. https://www.ilgiornale.it/news/politica/rula-talebana-dello-ius-soli-e-chi-critica-nazista-1442362.html)
- Articoli sullo ius soli del Giornale (www.ilgiornale.it) tra 01/01/17 e 31/12/17 con minimo 100 commenti /forse 80/
- Articoli sullo ius soli di Repubblica (www.repubblica.it) tra 01/01/17 e 31/12/17 con minimo 100 commenti /forse 80/
- Metadati articoli: data, nome giornale, numero articolo, autore 
- Metadati commenti: data, commento / commento a commento, username(s)

Query con wildcard:

site:www.ilgiornale.it intitle:"ius soli" after:2017-01-01 before:2017-12-31
O anche senza intitle e solo "ius soli"

# Selenium per i commenti

- Da capire come non farsi blacklistare(?) 
- Usando ublock origin su chrome lo script ricomincia a funzionare 
- Sicuramente andrà fatto ad-hoc per la repubblica purtroppo

# Idea generale

Tirare giù i link degli articoli da google (save as > e poi si trova un modo per estrarli dall'.html) -> Per ogni link, aprire il link e vedere se ha almeno 80 commenti -> Se ha 80 commenti, tirare giù l'articolo e i metadati + commenti più metadati -> Processare le cose in modo che siano nel formato corretto (tipo nome del .txt ecc.) -> Rinse and repeat

<img src="https://github.com/ffedox/corpus_ilgiornale/blob/main/esempio_corpus.jpg" width="700" class="center">
