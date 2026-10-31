"""Genera la bottiglia conica di Scavet (SVG inline) e la inserisce in sito/index.html."""
import re
import sys

html_path = sys.argv[1]

# Profilo del corpo: largo 80 mm alle spalle (y=130), 66 mm alla base (y=298)
def half_width(y):
    return 40 - (y - 130) * (6.5 / 168)

# Etichetta: vista frontale ~93% del diametro, si stringe con il vetro
LABEL_TOP, N = 170.0, 48
top_w = 2 * half_width(LABEL_TOP) * 0.93
label_h = top_w / (1063 / 1300)
strips = []
for i in range(N):
    y0 = LABEL_TOP + i * label_h / N
    w = 2 * half_width(y0 + label_h / N / 2) * 0.93
    sy = i * 1300 / N
    strips.append(
        # ogni striscia sborda di 0,4 mm sotto la successiva, così non si vedono le giunte
        f'<svg x="{50 - w / 2:.3f}" y="{y0:.3f}" width="{w:.3f}" height="{label_h / N + 0.4:.3f}" '
        f'viewBox="0 {sy:.3f} 1063 {(label_h / N + 0.4) * 1300 / label_h:.3f}" preserveAspectRatio="none">'
        f'<use href="#label-img"/></svg>'
    )
bot_w = 2 * half_width(LABEL_TOP + label_h) * 0.93
label_poly = (
    f"{50 - top_w / 2:.2f},{LABEL_TOP:.2f} {50 + top_w / 2:.2f},{LABEL_TOP:.2f} "
    f"{50 + bot_w / 2:.2f},{LABEL_TOP + label_h:.2f} {50 - bot_w / 2:.2f},{LABEL_TOP + label_h:.2f}"
)

svg = f'''<figure class="wine-visual reveal">
          <!-- Bottiglia conica in vetro verde (GL 71), 0,75 l: spalle 80 mm, base 66 mm, altezza 300 mm. Generata da uno script: l'etichetta è tagliata a strisce per seguire la rastremazione -->
          <svg class="bottle" viewBox="0 0 100 322" role="img" aria-label="Bottiglia di Scavet in vetro verde, conica, con capsula verde e l'etichetta della vigna">
            <defs>
              <path id="bottle-shape" d="M36 9 Q36 5 39.5 5 L60.5 5 Q64 5 64 9 L64.8 76 C65 98 90 104 90 130 L83.5 298 Q83.2 306 76 306 L24 306 Q16.8 306 16.5 298 L10 130 C10 104 35 98 35.2 76 Z" />
              <clipPath id="bottle-clip"><use href="#bottle-shape" /></clipPath>
              <clipPath id="label-clip"><polygon points="{label_poly}" /></clipPath>
              <image id="label-img" href="assets/scavet-etichetta.jpg" width="1063" height="1300" />
              <linearGradient id="glass" x1="0" x2="1">
                <stop offset="0" stop-color="#020402" />
                <stop offset=".1" stop-color="#071009" />
                <stop offset=".24" stop-color="#11210f" />
                <stop offset=".34" stop-color="#1a2e17" />
                <stop offset=".5" stop-color="#0e1b0d" />
                <stop offset=".78" stop-color="#091409" />
                <stop offset=".93" stop-color="#040905" />
                <stop offset="1" stop-color="#010201" />
              </linearGradient>
              <linearGradient id="glass-depth" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0" stop-color="#7fae78" stop-opacity=".1" />
                <stop offset=".35" stop-color="#000" stop-opacity="0" />
                <stop offset=".9" stop-color="#000" stop-opacity=".3" />
                <stop offset="1" stop-color="#4f7a48" stop-opacity=".2" />
              </linearGradient>
              <linearGradient id="capsule" x1="0" x2="1">
                <stop offset="0" stop-color="#083d15" />
                <stop offset=".18" stop-color="#14792c" />
                <stop offset=".32" stop-color="#5fd07c" />
                <stop offset=".42" stop-color="#1B9238" />
                <stop offset=".75" stop-color="#127a2d" />
                <stop offset="1" stop-color="#062f10" />
              </linearGradient>
              <radialGradient id="capsule-top" cx=".4" cy=".4" r=".7">
                <stop offset="0" stop-color="#5fd07c" />
                <stop offset="1" stop-color="#127a2d" />
              </radialGradient>
              <linearGradient id="label-shade" x1="0" x2="1">
                <stop offset="0" stop-color="#000" stop-opacity=".5" />
                <stop offset=".12" stop-color="#000" stop-opacity=".08" />
                <stop offset=".27" stop-color="#fff" stop-opacity=".22" />
                <stop offset=".36" stop-color="#fff" stop-opacity="0" />
                <stop offset=".84" stop-color="#000" stop-opacity=".06" />
                <stop offset="1" stop-color="#000" stop-opacity=".55" />
              </linearGradient>
              <radialGradient id="floor" cx=".5" cy=".5" r=".5">
                <stop offset="0" stop-color="#000" stop-opacity=".55" />
                <stop offset="1" stop-color="#000" stop-opacity="0" />
              </radialGradient>
              <filter id="soft" x="-50%" y="-10%" width="200%" height="120%"><feGaussianBlur stdDeviation="1.1" /></filter>
              <filter id="softer" x="-50%" y="-10%" width="200%" height="120%"><feGaussianBlur stdDeviation="2.4" /></filter>
            </defs>

            <!-- ombra a terra -->
            <ellipse cx="50" cy="307" rx="40" ry="6" fill="url(#floor)" />

            <!-- vetro -->
            <use href="#bottle-shape" fill="url(#glass)" />
            <g clip-path="url(#bottle-clip)">
              <rect width="100" height="322" fill="url(#glass-depth)" />
              <!-- riflessi lunghi: finestra a sinistra, controluce a destra -->
              <path d="M24.5 136 L29 298" stroke="#e9f5e4" stroke-opacity=".55" stroke-width="3.2" stroke-linecap="round" filter="url(#soft)" />
              <path d="M26 140 L30 292" stroke="#fff" stroke-opacity=".75" stroke-width=".9" stroke-linecap="round" />
              <path d="M78.5 140 L74.5 290" stroke="#bfe6b8" stroke-opacity=".18" stroke-width="2" stroke-linecap="round" filter="url(#soft)" />
              <path d="M38 112 C29 116 21 122 18.5 132" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="2" stroke-linecap="round" filter="url(#soft)" />
              <path d="M12.5 140 L18.6 298" stroke="#6f9f68" stroke-opacity=".22" stroke-width="1.4" filter="url(#soft)" />
              <path d="M87.5 140 L81.4 298" stroke="#6f9f68" stroke-opacity=".18" stroke-width="1.4" filter="url(#soft)" />
              <!-- fondo spesso del vetro -->
              <ellipse cx="50" cy="301" rx="31" ry="4.5" fill="#4f7a48" opacity=".25" filter="url(#softer)" />
            </g>
            <use href="#bottle-shape" fill="none" stroke="#a9dca2" stroke-opacity=".18" stroke-width=".45" />

            <!-- etichetta conica -->
            <g clip-path="url(#label-clip)">
              {"".join(strips)}
              <rect x="0" y="{LABEL_TOP:.2f}" width="100" height="{label_h:.2f}" fill="url(#label-shade)" />
            </g>

            <!-- capsula nel verde dell'etichetta, con anello oro -->
            <path d="M35.2 7 Q35.2 2 39.5 2 L60.5 2 Q64.8 2 64.8 7 L65.3 60 Q65.3 62 64 62 L36 62 Q34.7 62 34.7 60 Z" fill="url(#capsule)" />
            <ellipse cx="50" cy="2.8" rx="12.6" ry="1.5" fill="url(#capsule-top)" />
            <ellipse cx="50" cy="2.8" rx="5" ry=".6" fill="none" stroke="#0b5a1d" stroke-width=".3" />
            <rect x="35" y="9" width="30" height=".35" fill="#000" opacity=".22" />
            <rect x="35" y="11.2" width="30" height=".25" fill="#fff" opacity=".18" />
            <rect x="34.8" y="57.2" width="30.4" height=".8" fill="#B18D13" />
            <rect x="34.8" y="57.2" width="30.4" height=".25" fill="#f1d36a" opacity=".7" />
            <path d="M40 4 L40.6 56" stroke="#fff" stroke-opacity=".35" stroke-width=".9" filter="url(#soft)" />
          </svg>
        </figure>'''

html = open(html_path, encoding="utf-8").read()
new, n = re.subn(r'<figure class="wine-visual reveal">.*?</figure>', svg, html, count=1, flags=re.S)
assert n == 1, "figura non trovata"
open(html_path, "w", encoding="utf-8", newline="\n").write(new)
print(f"etichetta {top_w:.1f}-{bot_w:.1f} mm, alta {label_h:.1f} mm, {N} strisce")
