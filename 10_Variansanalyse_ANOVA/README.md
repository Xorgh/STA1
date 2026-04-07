---
tags:
    - ANOVA
    - Variansanalyse
    - Oneway ANOVA
    - F-test
    - Middelværdier (flere grupper)
    - Tukey HSD
---
<h1 align="center">Variansanalyse (ANOVA)</h1>

## Sessionsmateriale:

Ross: 10.1-10.3

<p align="left">

  <a href="Tutorial_10_notebook/">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python tutorial" width="100" />
    <br>
    <strong>Se Tutorial 10: One-way ANOVA</strong>
  </a>
</p>

<a href="Tutorial_10_notebook.ipynb" download>Download tutorial som notebook (.ipynb)</a>

[Se tutorial som markdown](Tutorial_10.md/) (genereret fra notebook — **ret i `.ipynb`**, kør derefter `python sync_tutorial10_md.py`).

[Recap og øvelser]()

[Sessionnoter]()

[Sessionsmateriale]()

---

## Sessionbeskrivelse

Når vi skal sammenligne middelværdier for mere end to grupper, bliver mange separate $t$-tests problematiske (øget risiko for type I-fejl). Ensidig variansanalyse (one-way ANOVA) samler spørgsmålet i én omnibus-$F$-test: $H_0$: alle gruppemiddelværdier er ens mod $H_1$: mindst én gruppe adskiller sig.

Vi gennemgår modellen med fælles fejlvarians, opdeling af den totale variation (mellem grupper vs. inden for grupper), ANOVA-tabellen ($F = \mathrm{MSB}/\mathrm{MSW}$), $F$-fordelingen med de rette frihedsgrader, og hvordan I fortolker resultatet. Under Ross 10.3 ser vi kort på parvise sammenligninger (fx Tukey HSD), når $H_0$ er forkastet eller når I vil undersøge hvilke grupper der adskiller sig.


* Python-gennemgang: Tutorial 10 (SciPy, statsmodels — kør `pip install statsmodels` eller første celle i notebook'en med `%pip`, hvis import fejler; kort om alternativer).

### Centrale begreber

- **Ensidet layout:** én kategorisk faktor med $k$ niveauer (grupper)
- **Model:** $Y_{ij} = \mu_i + \varepsilon_{ij}$ (Ross’ notation) / effektform med $\mu + \alpha_i$
- **$H_0$: $\mu_1 = \cdots = \mu_k$** mod **$H_1$:** ikke alle $\mu_i$ ens
- **SST**, **SSW** (indenfor), **SSB** (mellem), **df**, **MSB**, **MSW**, **$F$-teststørrelse**
- **Antagelser:** uafhængige observationer, ca. normalitet inden for hver gruppe, **ens varians** ($\sigma^2$) på tværs af grupper
- **Efter ANOVA:** justerede **parvise sammenligninger** (fx Tukey) for at undgå “datadyrkning”

!!! tip "Læringsmål"

    - Kunne forklare hvorfor ANOVA bruges ved $k>2$ grupper i stedet for mange $t$-tests.
    - Kunne opstille $H_0$ og $H_1$ for en ensidig ANOVA og fortolke en $F$-teststørrelse og tilhørende $p$-værdi.
    - Kunne skitsere opbygningen af ANOVA-tabellen (sumkvadrater, frihedsgrader, middelkvadrater).
    - Kunne gennemføre one-way ANOVA i Python med **SciPy** (`f_oneway`) og **statsmodels** (`ols` + `anova_lm`).
    - Kunne efter en signifikant ANOVA bruge **Tukey HSD** (eller tilsvarende) til parvise sammenligninger og fortolke output.

## Øvelser

!!! note "Kommer senere"

    Øvelser til session 10 tilføjes, når de er klar. Indtil da kan I træne på eksemplerne i **Tutorial 10**.

<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>
