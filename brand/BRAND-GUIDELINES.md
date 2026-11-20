# Using-IT Brand Guidelines - v1.0

**Retning:** Nordisk Ro · hvid, luftig, én blå accent.
**Godkendt:** 19. nov 2026. Gyldig for website, thumbnails, mail-signatur og fremtidige materialer.
This file is the single source of truth for the visual identity of using-it.dk.
Implementation lives in `src/styles/tokens.css`; change tokens there, never hard-code colors.

## 1. Kerneidentitet

Using-IT er et **roligt, teknisk troværdigt, skandinavisk publisher-mærke**.

- Tone: præcis, hjælpsom, uden hype. Vi forklarer, vi sælger ikke (undtagen hvor licens-CTA'en står).
- Visuelt motto: "hvile til øjet, præcision i detaljen".
- Vi undgår: cyber-æstetik, tunge gradienter, stockfotos af serverrum, blinkende elementer.

## 2. Farver (light mode)

| Token | Hex | RGB | Brug |
| --- | --- | --- | --- |
| `--color-bg` | `#FFFFFF` | 255,255,255 | sidebaggrund, flader |
| `--color-bg-subtle` | `#F4F7FB` | 244,247,251 | kodeblokke, paneler, citater |
| `--color-border` | `#E1E8F2` | 225,232,242 | kanter, adskillere |
| `--color-text` | `#2C3648` | 44,54,72 | brødtekst |
| `--color-text-strong` | `#101A2B` | 16,26,43 | overskrifter, "-IT" i wordmark |
| `--color-text-muted` | `#7C8AA0` | 124,138,160 | metadata, captions, datolinje |
| `--color-accent` | `#1D5FD6` | 29,95,214 | links, primærknap, logo-flise, "using-" i wordmark |
| `--color-accent-hover` | `#174AA8` | 23,74,168 | hover på accent |
| `--color-accent-subtle` | `#E8F0FC` | 232,240,252 | badge-baggrunde, CTA-blok |
| `--color-warn` | `#B4611C` | kun til advarsels-callouts: den eneste sekundære signal-farve | |

### Dark mode

| Token | Hex |
| --- | --- |
| `--color-bg` | `#101A2B` |
| `--color-bg-subtle` | `#17233A` |
| `--color-border` | `#24334E` |
| `--color-text` | `#C8D2E2` |
| `--color-text-strong` | `#F0F4FA` |
| `--color-text-muted` | `#7C8AA0` |
| `--color-accent` | `#5B8FEB` |
| `--color-accent-subtle` | `#1B2C4A` |

### Emnefarver (thumbnails/kategorier)

| Emne | Token-kategori | Hex |
| --- | --- | --- |
| Intune (hovedaccent) | `intune` | `#1D5FD6` |
| Windows | `windows` | `#46648A` |
| Autopilot | `autopilot` | `#157A8C` |
| Defender | `defender` | `#2E6B4F` |
| Conditional Access | `conditionalaccess` | `#3D7BB5` |
| Windows 365 | `windows365` | `#4A5FBF` |
| Edge | `edge` | `#46648A` |
| PowerShell | `powershell` | `#2E6B4F` |
| OSDCloud | `osdcloud` | `#0F3D73` |

(Kategorinavne normaliseres med små bogstaver, se konverteringen i `scripts/wxr-to-md.py`.)

### Kontrastregler (WCAG 2.2 AA)

- Brødtekst `#2C3648` på `#FFFFFF`: kontrast 11,3:1 ✔
- Accent `#1D5FD6` på hvid: 5,0:1; kun til links/knapper/ikoner, aldrig lang brødtekst.
- Muted `#7C8AA0`: kun ikke-væsenlig tekst (metadata, captions).

## 3. Typografi

| Rolle | Skrift | Fallback |
| --- | --- | --- |
| UI + brødtekst | **Inter Variable** (OFL, self-hostet via @fontsource) | `system-ui, -apple-system, "Segoe UI", sans-serif` |
| Kode | **JetBrains Mono** (OFL) | `ui-monospace, "SF Mono", Menlo, Consolas, monospace` |

**Tegnsætningsregler:** Em-dash er strengt forbudt i alt indhold. Brug `-` i prosa, kolon eller komma hvor teksten ellers ville have et em-dash, og `·` som separator i titler og meta-linjer.

Skala: H1 32-38px/700/1.2 · H2 24px/700 · H3 20px/600 · H4 17px/600 · brødtekst **17-19px, linjehøjde 1.6-1.65, maks. 70 tegn** · meta 12px uppercase ls 0.05em · kode 13.5px.

Regel: font-licenser er OFL: ingen betalte skrifter, ingen CDN-afhængighed (privacy).

## 4. Logo og wordmark

- **Primær wordmark (vandret):** `using-` i `--color-accent` + `IT` i `--color-text-strong`, Inter 700, ls -0.02em.
- **Compact symbol:** afrundet flise (radius 1/4 af siden) i `--color-accent` med `u` i hvid, Inter 750. Favicon/social avatar/mail-signatur.
- **Varianter:** monokrom mørk, monokrom lys (hvid flise på accent/mørk), omrids.
- **Clearspace:** minimum halv flise-bredde omkring wordmarket. Min. størrelse: wordmark 88px bred, symbol 20px.
- **Forkert brug:** ingen gradienter på logo, ingen alternative accentfarver, ingen rotation/skygge, aldri strakt.

## 5. Spacing, radius, skygge

`4 · 8 · 12 · 16 · 24 · 32 · 48 · 64` px. Radius: paneler 12, knapper/badges 6, kode 8.
Én skygge: `0 6px 24px rgba(20,30,50,.08)`. I øvrigt kanter, ikke skygger.

## 6. Komponenter

- **Primærknap:** accent-baggrund, hvid tekst, radius 6, hover `--color-accent-hover`, focus-ring 2px accent/2px offset.
- **Kodeblok:** subtle baggrund, 1px kant, venstreaccent 3px, sproglabel muted uppercase, copy-knap (client-side, progressive enhancement).
- **Callout:** venstreaccent 3px; tip = accent, advarsel = `--color-warn`.
- **Licens-CTA:** accent-subtle blok, flise + én linie + pil-knap til `https://minelicenser.dk/`. Aldrig popup, aldrig fuldbredde-banner.
- **Thumbnail (16:9/OG):** lys gradient 135° (`bg-subtle → accent-subtle`), emne-flise 96px i emnefarve med hvidt ikon/forkortelse, sætningstitel Inter 700 i `--color-text-strong`, maks. 2 linier + muted emne-label. Ingen Microsoft-logoer. Eksport 1200×630 PNG til OG.

## 7. Screenshots og diagrammer

Skærmbilleder: fuldbredde ind i artiklen, WebP, caption i muted, alt-tekst altid, lightbox/zoom. Alle kundedata redacteres før upload. Diagrammer: flade SVG i palet-farver, tekst ≥14px, dark-mode-variant.

## 8. Motion

Kun mikro-animationer: fade-in artikler (200 ms), hover (150 ms). Respekter altid `prefers-reduced-motion`.

## 9. Mail-signatur

Se `signature.html` (tabelbaseret, inline-CSS, ingen tracking-pixels, testes i Outlook Win/Web/macOS/mobil + dark mode).

## 10. Godelkender

Godkendt af Alexander, 19. nov 2026. Revisions sker via PR til denne fil.