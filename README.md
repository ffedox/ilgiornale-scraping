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

# Problemi/note

- Da capire come non farsi blacklistare(?) 
- Usando ublock origin su chrome lo script ricomincia a funzionare 
- Da vedere cosa fa il codice quando trova commenti in risposta a commenti
- Esempio di articolo con commenti https://www.repubblica.it/politica/2017/06/21/news/ius_soli_ecco_come_funziona_nel_resto_d_europa-168672635/
- Il coso dei commenti di repubblica è qui:
<img src="https://github.com/ffedox/corpus_ilgiornale/blob/main/commentirepubblica.png">
<img src="https://github.com/ffedox/corpus_ilgiornale/blob/main/commentirepubblica2.png">
<img src="https://github.com/ffedox/corpus_ilgiornale/blob/main/commentirepubblica3.png">

# Idea generale

Da adattare in base al giornale

## Il Giornale

1. Tirare giù i link degli articoli da google -> [google_link_extractor.py](https://github.com/ffedox/corpus_ilgiornale/blob/main/google_link_extractor.py)
2. Per ogni link, aprire il link e vedere quanti commenti ha -> [check_comment_amount.py](https://github.com/ffedox/corpus_ilgiornale/blob/main/check_comment_amount.py)
3. Se ha 80 commenti, tirare giù l'articolo e i metadati + commenti più metadati -> da finire [test_selenium6.py](https://github.com/ffedox/corpus_ilgiornale/blob/main/test_selenium6.py), che per il momento estrae solo commenti e metadati
4. Processare le cose in modo che siano nel formato corretto (tipo nome del .txt ecc.) ->

## La Repubblica

1. Tirare giù i link degli articoli da google -> [google_link_extractor.py](https://github.com/ffedox/corpus_ilgiornale/blob/main/google_link_extractor.py)
2. Per ogni link, aprire il link e vedere quanti commenti ha -> da finire [check_comment_amount.py](https://github.com/ffedox/corpus_ilgiornale/blob/main/check_comment_amount.py)
3. Se ha 80 commenti, tirare giù l'articolo e i metadati + commenti più metadati -> da finire [larepubblica.ipynb](https://github.com/ffedox/corpus_ilgiornale/blob/main/larepubblica.ipynb), che per il momento estrae solo articolo e metadati
4. Processare le cose in modo che siano nel formato corretto (tipo nome del .txt ecc.) ->

<img src="https://github.com/ffedox/corpus_ilgiornale/blob/main/esempio_corpus.jpg" width="700" class="center">
