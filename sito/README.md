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
- [x] Frutta: ciliegie, prugne, pesche, melograni, castagne, in vendita diretta in azienda
- [x] P.IVA, sede, REA, PEC ed email aziendale, dal documento "Dati di base Costa del Bosco" su Drive
- [x] Telefono: 333 537 6501
- [ ] Instagram
- [ ] Frase manifesto: ora è "Due terre, un nome."; si cambia nell'`<h1>`

Bottiglie: **980** ovunque (sito, piattaforma di brand, identità visiva, controetichetta), come il certificato Valoritalia (lotto L. 15326).

## Prossimi passi consigliati

- **Foto**: vigna Scavet, Matteo e Sara, le due colline. Andrebbero nella hero, nella storia e accanto alla bottiglia.
- **Font in locale**: ora i font arrivano da Google Fonts. Per il GDPR è meglio scaricarli e servirli dal proprio dominio.
- **Pubblicazione**: va bene un qualsiasi hosting statico (Netlify, Cloudflare Pages, GitHub Pages, o l'hosting del dominio).
- **Privacy e cookie**: il sito non usa cookie né tracciamento; se aggiungete analytics o mappe servirà un banner.
