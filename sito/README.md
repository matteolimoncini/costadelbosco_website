# Sito Costa del Bosco

Sito statico di una pagina, costruito sulla [piattaforma di brand](../piattaforma_di_brand.md). Non richiede installazioni né build.

## File

- `index.html`: tutti i contenuti, sezione per sezione
- `styles.css`: palette (verde bosco, bianco calce, giallo paglierino), tipografia, layout
- `script.js`: menu mobile e animazioni di comparsa
- `assets/favicon.svg`: icona del sito, con il segno delle due colline

## Vederlo in locale

Dalla cartella `costa_del_bosco`:

```
python -m http.server 8080 --directory sito
```

poi apri http://localhost:8080

## Da completare

Nel sito i segnaposto sono evidenziati in giallo (classe `todo`). Cerca `class="todo"` in `index.html`.

- [ ] Età della vigna Scavet, annata, grado alcolico
- [ ] Ettari totali di vigneto
- [ ] Quali frutti coltivate, e se li vendete al pubblico
- [ ] Email (ora `info@costadelbosco.it`, da verificare), telefono, Instagram, indirizzo
- [ ] Ragione sociale e P.IVA nel footer (obbligatori per legge su un sito aziendale)
- [ ] Frase manifesto: ora è "Due terre, un nome."; si cambia nell'`<h1>`

## Prossimi passi consigliati

- **Foto**: vigna Scavet, Matteo e Sara, le due colline. Andrebbero nella hero, nella storia e accanto alla bottiglia.
- **Font in locale**: ora i font arrivano da Google Fonts. Per il GDPR è meglio scaricarli e servirli dal proprio dominio.
- **Pubblicazione**: va bene un qualsiasi hosting statico (Netlify, Cloudflare Pages, GitHub Pages, o l'hosting del dominio).
- **Privacy e cookie**: il sito non usa cookie né tracciamento; se aggiungete analytics o mappe servirà un banner.
