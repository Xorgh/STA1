---
tags:
    - Normalfordeling
    - Eksponentialfordeling
    - Hukommelsesløshed
    - Rate-parameter
    - Levetidsanalyse
    - Poisson-process
    - Lineære transformationer
---
<h1 align="center">Kontinuerte fordelinger II: eksponentialfordelingen og normalfordeling fortsat</h1>

## Sessionsmateriale:

Ross: 5.5. (fortsat), 5.6.

[Recap og øvelser]()

[Sessionnoter]()

[Sessionsmateriale]()

## Video Materiale:

**Exponential Distribution**

En enkelt video, der dækker eksponentialfordelingen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/C7V3d2yB58U?si=twLlJkku_rxrojdH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Sessionbeskrivelse

Denne session har to formål. For det første samler vi op på **normalfordelingen** fra sidst. Det er et omfattende emne, og vi bruger tid på at sikre, at forståelsen af standardisering og brug af fordelingen sidder fast. Vi ser evt. på lineære transformationer af normalfordelte variable (f.eks. $Y = aX + b$), som er en vigtig egenskab i dataanalyse.

Herefter introducerer vi **eksponentialfordelingen**. Hvor normalfordelingen ofte beskriver *målinger*, beskriver eksponentialfordelingen typisk *levetider* eller *ventetider* mellem hændelser (f.eks. tiden mellem to servernedbrud). Den har en unik og kontraintuitiv egenskab kaldet **hukommelsesløshed** (memorylessness), som vi skal forstå betydningen af. Vi vil også kort berøre sammenhængen til Poisson-fordelingen: Hvis ankomster (f.eks. bugs) er Poisson-fordelte, er tiden mellem dem eksponentialfordelt.

### Centrale begreber

- **Normalfordeling (fortsat):** Anvendelse og egenskaber
- **Eksponentialfordeling:** Tæthedsfunktion $f(x) = \lambda e^{-\lambda x}$
- **Rate-parameteren ($\lambda$):** Sammenhæng med middelværdi ($1/\lambda$)
- **Hukommelsesløshed:** $P(X > s+t | X > s) = P(X > t)$
- **Relationen mellem Poisson og Eksponential:** Antal vs. tid

!!! tip "Læringsmål"

    - Opnå rutine i beregninger med normalfordelingen.
    - Kunne genkende situationer, hvor eksponentialfordelingen er en passende model (ventetider/levetider).
    - Forstå og forklare begrebet hukommelsesløshed, og hvorfor det er centralt for eksponentialfordelingen.
    - Kunne veksle mellem at beskrive en proces via hændelsesrate (Poisson) og ventetid (Eksponential).
    - Kunne beregne sandsynligheder for, at en proces "overlever" længere end et givet tidsrum.


## Øvelser

<!--
Indsæt bogreferencer og opgavelister her.
-->
<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

*Øvelser indsættes.*
