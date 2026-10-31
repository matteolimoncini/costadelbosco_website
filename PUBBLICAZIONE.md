# Mettere online il sito

Come funziona: i file stanno su **GitHub** (repository privato), **Cloudflare Pages** pubblica la cartella `sito/` sul dominio registrato su **Aruba**. Ogni modifica salvata su GitHub va online da sola in circa un minuto.

Costo: zero. Il dominio resta su Aruba e si rinnova lì.

## 1. GitHub: crea il repository

1. Vai su https://github.com/new
2. Nome: `costa-del-bosco`, visibilità **Private**
3. **Non** spuntare README, .gitignore né licenza: il repository deve essere vuoto
4. Crea, e copia l'indirizzo (tipo `https://github.com/TUO-UTENTE/costa-del-bosco.git`)

Poi Claude collega la cartella e carica i file. Al primo invio si apre una finestra del browser per l'accesso a GitHub: accedi e autorizza.

## 2. Cloudflare: aggiungi il dominio

1. Crea un account gratuito su https://dash.cloudflare.com/sign-up
2. **Add a domain** → scrivi il dominio (senza www) → piano **Free**
3. Cloudflare importa i record DNS esistenti. Non c'è posta attiva, quindi puoi eliminare quelli che puntano alla pagina di parcheggio Aruba (record A e CNAME di `@` e `www`)
4. Alla fine Cloudflare mostra **due name server**, tipo `anna.ns.cloudflare.com` e `bob.ns.cloudflare.com`. Tienili a portata di mano

## 3. Aruba: cambia i name server

1. Accedi su https://admin.aruba.it → seleziona il dominio
2. Cerca la sezione **Gestione DNS e name server** (o "Modifica DNS")
3. Scegli di usare **name server esterni / personalizzati** e inserisci i due di Cloudflare al posto di quelli Aruba
4. Salva. Per i domini .it il cambio può richiedere da qualche ora a 24–48 ore. Cloudflare manda una email quando il dominio è attivo

L'ordine conta: prima aggiungi il dominio su Cloudflare (punto 2), poi cambi i name server su Aruba. Il registro .it controlla che i nuovi server rispondano già per il dominio.

## 4. Cloudflare Pages: collega il repository

Si può fare mentre aspetti il punto 3.

1. Nel pannello Cloudflare: **Workers & Pages** → **Create** → scheda **Pages** (se vedi solo Workers, cerca il link "Looking to deploy Pages?")
2. **Connect to Git** / **Import an existing Git repository** → autorizza GitHub, dando accesso solo al repository `costa-del-bosco`
3. Impostazioni di build:
   - Framework preset: **None**
   - Build command: *(vuoto)*
   - Build output directory: **`sito`**
4. **Save and Deploy**. Dopo un minuto il sito è visibile su `costa-del-bosco.pages.dev`

## 5. Collega il dominio

Quando Cloudflare conferma che il dominio è attivo:

1. Nel progetto Pages → **Custom domains** → **Set up a custom domain**
2. Aggiungi `tuodominio.it`, poi ripeti per `www.tuodominio.it`
3. Cloudflare crea da solo i record DNS e il certificato HTTPS

## Dopo: come si modifica

- **Tu**: su github.com apri il repository → cartella `sito` → file (per esempio `index.html`) → icona matita → modifica → **Commit changes**. Il sito si aggiorna da solo.
- **Claude**: modifica i file in locale e li carica su GitHub.
- Se hai modificato qualcosa su GitHub, dillo a Claude prima di nuove modifiche, così parte dalla versione aggiornata.
- Ogni versione resta nello storico di GitHub: si può sempre tornare indietro.
