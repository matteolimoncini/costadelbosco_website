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

- [x] Annata (2025), grado alcolico e analisi di Scavet, dal rapporto di prova e dal certificato Valoritalia
- [x] Ragione sociale: Costa del Bosco S.S. Società Agricola
- [ ] Età della vigna Scavet
- [ ] Ettari totali di vigneto
- [ ] Foto di nonno Natalino e nonno Luciano (riquadri tratteggiati nella sezione "Le terre")
- [ ] Quali frutti coltivate, e se li vendete al pubblico
- [ ] Email (ora `info@costadelbosco.it`, da verificare), telefono, Instagram, indirizzo
- [ ] P.IVA nel footer (obbligatoria per legge su un sito aziendale)
- [ ] Frase manifesto: ora è "Due terre, un nome."; si cambia nell'`<h1>`

Bottiglie: il sito dice **980**, come il certificato Valoritalia (lotto L. 15326). La piattaforma di brand e la bozza di controetichetta dicevano 1.000.

## Prossimi passi consigliati

- **Foto**: vigna Scavet, Matteo e Sara, le due colline. Andrebbero nella hero, nella storia e accanto alla bottiglia.
- **Font in locale**: ora i font arrivano da Google Fonts. Per il GDPR è meglio scaricarli e servirli dal proprio dominio.
- **Pubblicazione**: va bene un qualsiasi hosting statico (Netlify, Cloudflare Pages, GitHub Pages, o l'hosting del dominio).
- **Privacy e cookie**: il sito non usa cookie né tracciamento; se aggiungete analytics o mappe servirà un banner.
