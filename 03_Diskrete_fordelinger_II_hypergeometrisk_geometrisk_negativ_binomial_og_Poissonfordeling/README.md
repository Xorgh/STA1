---
tags:
    - Diskrete fordelinger
    - Hypergeometrisk fordeling
    - Poisson-fordeling
    - Geometrisk fordeling
    - Negativ binomialfordeling
    - Stikprøvetagning uden tilbagelægning
    - Ventetidsproblemer
---

<h1 align="center">Diskrete fordelinger II: hypergeometrisk, geometrisk, negativ binomial- og Poissonfordeling</h1>

## Sessionsmateriale:

Ross: 5.2., 5.3.

**Bemærk:** Geometrisk fordeling og Negativ binomialfordeling dækkes ikke i Ross, men gennemgås til forelæsningen.

[Recap og øvelser]()

[Sessionnoter]()

[Sessionsmateriale]()

---

## Sessionbeskrivelse

I denne session udvider vi paletten af **diskrete fordelinger**. Mens vi sidst fokuserede på binomialfordelingen (uafhængige forsøg/stikprøvetagning *med* tilbagelægning), ser vi nu på situationer, hvor forudsætningerne ændrer sig.

Vi starter med **den hypergeometriske fordeling**, som er essentiel, når vi arbejder med stikprøver fra små populationer *uden* tilbagelægning – et klassisk scenarie inden for kvalitetskontrol og "capture-recapture" estimering i biologi og softwaretest.

Dernæst behandler vi **Poisson-fordelingen**, som er en af de vigtigste fordelinger inden for datalogi og ingeniørkunst. Den bruges til at modellere antallet af hændelser, der sker inden for et givent tidsrum eller område, såsom ankomsten af netværkspakker til en server eller fordelingen af bugs i en kodebase. Vi ser også på sammenhængen mellem Binomial- og Poisson-fordelingen.

Til sidst introducerer vi to fordelinger, der fokuserer på "ventetiden" indtil en bestemt hændelse indtræffer: **den geometriske fordeling** (ventetid til første succes) og **den negative binomialfordeling** (ventetid til $r$-te succes). *Vær opmærksom på, at disse to fordelinger ikke beskrives i lærebogen, men præsenteres i undervisningen som en naturlig udvidelse af Bernoulli-processer.*

### Centrale begreber

- **Hypergeometrisk fordeling:** Stikprøvetagning uden tilbagelægning
- **Poisson-fordeling:** Modellering af hændelsesrater og sjældne begivenheder
- **Poisson-approksimation:** Brug af Poisson som grænseværdi for Binomialfordelingen
- **Geometrisk fordeling:** Antal forsøg indtil første succes
- **Negativ binomialfordeling:** Generalisering af den geometriske fordeling (antal forsøg indtil $r$ succeser)

!!! tip "Læringsmål"

    - Kunne identificere situationer, hvor en Hypergeometrisk fordeling skal anvendes frem for en Binomialfordeling (forskellen på med/uden tilbagelægning).
    - Kunne anvende Poisson-fordelingen til at beregne sandsynligheder for hændelser over tid eller areal.
    - Forstå sammenhængen mellem Binomial- og Poisson-fordelingen og kunne anvende Poisson som approksimation.
    - Kunne definere og regne på den Geometriske fordeling og den Negative binomialfordeling baseret på forelæsningsmaterialet.
    - Kunne vælge den korrekte diskrete fordelingsmodel til et givent praktisk problem.

## Øvelser

<!--
Indsæt bogreferencer og opgavelister her.
-->
<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

*Øvelser indsættes.*
