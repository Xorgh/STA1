---
tags:
    - Normalfordeling
    - Eksponentialfordeling
    - Standardnormalfordeling
    - Standardisering
    - Z-score
    - Hukommelsesløshed
    - Rate-parameter
    - Levetidsanalyse
    - Poisson-process
    - Lineære transformationer
---
<h1 align="center">Kontinuerte fordelinger II: normalfordeling og eksponentialfordeling</h1>

## Sessionsmateriale:

Ross: 5.5., 5.6.

Videoserien giver en hurtig gennemgang af kontinuerte fordelinger, og er en god introduktion til kurset og kan bruges som erstatning for læsestoffet. Det samme gælder for videoen om eksponentialfordelingen.

[Recap og øvelser]()

[Sessionnoter]()

[Sessionsmateriale]()

## Video Materiale:

**Exponential Distribution**

En enkelt video, der dækker eksponentialfordelingen, som supplement til videoserien om kontinuerte fordelinger.

<iframe width="560" height="315" src="https://www.youtube.com/embed/C7V3d2yB58U?si=twLlJkku_rxrojdH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Sessionbeskrivelse

I denne session arbejder vi målrettet med to centrale kontinuerte standardfordelinger: **normalfordelingen** og **eksponentialfordelingen**.

Først behandler vi **normalfordelingen** (Gauss-kurven): parametrene $\mu$ og $\sigma^2$, standardnormalfordelingen $N(0,1)$, standardisering med Z-scores samt beregning af sandsynligheder og fraktiler. Vi ser også på lineære transformationer af normalfordelte variable (f.eks. $Y = aX + b$), som er en vigtig egenskab i dataanalyse.

Derefter arbejder vi med **eksponentialfordelingen**. Hvor normalfordelingen ofte beskriver *målinger*, beskriver eksponentialfordelingen typisk *levetider* eller *ventetider* mellem hændelser (f.eks. tiden mellem to servernedbrud). Den har en unik egenskab kaldet **hukommelsesløshed** (memorylessness), og vi kobler den til Poisson-processer: Hvis ankomster er Poisson-fordelte, er tiden mellem dem eksponentialfordelt.

### Centrale begreber

- **Normalfordeling:** Parametre, standardisering og anvendelse
- **Standardnormalfordeling:** $N(0,1)$ og Z-score
- **Eksponentialfordeling:** Tæthedsfunktion $f(x) = \lambda e^{-\lambda x}$
- **Rate-parameteren ($\lambda$):** Sammenhæng med middelværdi ($1/\lambda$)
- **Hukommelsesløshed:** $P(X > s+t | X > s) = P(X > t)$
- **Relationen mellem Poisson og Eksponential:** Antal vs. tid

!!! tip "Læringsmål"

    - Opnå rutine i beregninger med normalfordelingen (inkl. Z-standardisering).
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
