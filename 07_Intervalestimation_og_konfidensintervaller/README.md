---
tags:
    - Intervalestimation
    - Konfidensintervaller
    - Konfidensniveau
    - Punktestimation
    - t-fordeling
    - Chi-i-anden-fordeling (χ²)
    - z-intervaller
    - Prædiktionsintervaller
    - To stikprøver (forskel mellem middelværdier)
---
<h1 align="center">Intervalestimation og konfidensintervaller</h1>

## Sessionsmateriale:

Ross: 7.1, 7.3, 7.4, 7.5.

[Recap og øvelser]()

[Sessionnoter]()

[Sessionsmateriale]()

---

## Sessionbeskrivelse

I denne session går vi fra **stikprøvefordelinger** (session 6) til at bruge dem til at sige noget kontrolleret om ukendte **populationsparametre**. Med udgangspunkt i Ross, kapitel 7 (*Parameter estimation*), afsnit **7.1**, **7.3**, **7.4** og **7.5**, skelner vi mellem **punktestimation** (ét tal som “bedste gæt”, fx stikprøvegennemsnit) og **intervalestimation**, hvor vi angiver et interval, der med en valgt sandsynlighed vil indeholde parameteren, når vi gentager forsøget under samme dataindsamling — det er idéen bag **konfidensintervaller** og det tilhørende **konfidensniveau** ($1-\alpha$).

I **7.3** arbejder vi med **konfidensintervaller for middelværdien** i normalmodellen: når populationsvariansen er kendt, bruges normalfordelingen (**z-baserede** intervaller); når den er ukendt, bruges typisk **t-fordelingen** med passende frihedsgrader. Vi ser også **prædiktionsintervaller** for en ny observation (ikke det samme som et CI for middelværdien). I **7.4** konstruerer vi intervaller for **forskellen mellem to normalpopulationsmiddelværdier** under de antagelser, bogen angiver. I **7.5** behandler vi **variansen** (og dermed standardafvigelsen) i en normalpopulation via intervaller knyttet til **$\chi^2$-fordelingen** for $(n-1)S^2/\sigma^2$. Afsnit om **maksimal likelihood** og **eksponentielle livstidsmodeller** springes over.

### Centrale begreber

- **Punktestimation vs. intervalestimation:** Estimat/statistik over for interval med konfidensniveau og gentagelsesfortolkning
- **Konfidensinterval og konfidensniveau ($1-\alpha$):** Hvad der er (og ikke er) sandsynligt for parameteren efter observerede data
- **CI for $\mu$ (normalmodel):** z-interval når $\sigma$ er kendt; t-interval når $\sigma$ estimeres med $S$
- **Prædiktionsinterval:** Usikkerhed for en *ny* observation frem for middelværdien
- **To stikprøver / differens:** Konfidensinterval for forskel mellem middelværdier under relevante antagelser
- **Varians i normalpopulation:** Intervaller baseret på $\chi^2$-fordelingen for $(n-1)S^2/\sigma^2$

!!! tip "Læringsmål"

    - Kunne forklare forskellen mellem punktestimation og intervalestimation og give en korrekt fortolkning af et konfidensniveau.
    - Kunne udlede og beregne konfidensintervaller for populationsmiddelværdien i normaltilfældet (kendt $\sigma$: z; ukendt $\sigma$: t).
    - Kunne vælge relevant fordeling (normal, t, $\chi^2$) ud fra model, antagelser og hvilken parameter der estimeres.
    - Kunne skelne mellem konfidensinterval for middelværdien og prædiktionsinterval for en enkelt fremtidig observation.
    - Kunne opstille og fortolke konfidensintervaller for forskellen mellem middelværdier i to normalpopulationer (som i pensum/antagelser for sessionen).
    - Kunne konstruere og fortolke konfidensintervaller for variansen (eller standardafvigelsen) i en normalpopulation.

## Øvelser

<!--
Indsæt bogreferencer og opgavelister her.
-->
<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

*Øvelser indsættes.*
