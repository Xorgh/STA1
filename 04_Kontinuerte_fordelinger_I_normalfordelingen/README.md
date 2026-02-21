---
tags:
    - Kontinuerte variable
    - Tæthedsfunktion (PDF)
    - Fordelingsfunktion (CDF)
    - Forventningsværdi og varians (integral)
---
<h1 align="center">Kontinuerte fordelinger I: grundbegreber og modeller</h1>

## Sessionsmateriale:

Ross: 4.1., 4.2., 4.4., 4.6. (fokus på det kontinuerte).

Videoserien giver en hurtig gennemgang af kontinuerte fordelinger, og er en god introduktion til kurset og kan bruges som erstatning for læsestoffet.

<p align="left">

  <a href="Tutorial_4_notebook/">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python tutorial" width="100" />
    <br>
    <strong>Se Tutorial 4: Kontinuerte fordelinger I (foundations)</strong>
  </a>
</p>

<a href="Tutorial_4_notebook.ipynb" download>Download tutorial som notebook (.ipynb)</a>

[Se tutorial som markdown](Tutorial_4.md/)

[Recap og øvelser]()

[Sessionnoter]()

[Sessionsmateriale]()

## Video Materiale:

**Continuous Probability Distributions**

Playliste med 10 videoer, der dækker kontinuerte fordelinger - også til session 5.

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=jiGDsott_rQOGdWe&amp;list=PLvxOuBpazmsPDZGwqhhjE3KkLWnTD34R0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Sessionbeskrivelse

I denne session skifter vi gear fra den diskrete verden (hvor vi tæller antal) til den **kontinuerte verden** (hvor vi måler størrelser som tid, højde, temperatur eller strøm). Det betyder, at vi matematisk går fra at bruge summer ($\sum$) til at bruge **integraler** ($\int$). Vi genbesøger begreberne tætheds- og fordelingsfunktioner, men nu med fokus på, at sandsynligheden for et enkelt punkt i en kontinuert fordeling altid er 0 – i stedet regner vi på intervaller og arealer under kurven.

Fokus i denne session er derfor **generelle principper for kontinuerte fordelinger**: hvordan man læser en tæthedsfunktion, hvordan man bruger CDF'en, og hvordan forventningsværdi/varians defineres via integraler. Vi træner modeltænkning og fortolkning på tværs af kontinuerte fordelinger, så fundamentet er stærkt, før vi dykker ned i specifikke standardfordelinger i næste session.

### Centrale begreber

- **Fra diskret til kontinuert:** Areal som sandsynlighed
- **Kontinuert tæthedsfunktion:** $f(x)$ og betingelsen $\int f(x)dx = 1$
- **Fordelingsfunktion (CDF):** $F(x)=P(X\leq x)$ for kontinuerte variable
- **Middelværdi og varians:** Defineret via integraler
- **Modelvalg:** Hvornår en kontinuert model giver mening i praksis

!!! tip "Læringsmål"

    - Forstå forskellen på sandsynlighedsberegning for diskrete og kontinuerte variable.
    - Kunne beregne sandsynligheder som arealer under tæthedsfunktionen ved hjælp af integration (for simple funktioner).
    - Kunne bruge både PDF og CDF korrekt i beregninger.
    - Kunne beregne forventningsværdi og varians for simple kontinuerte fordelinger.
    - Opbygge et stærkt fundament til normal- og eksponentialfordelingen i næste session.

---

## Øvelser

<!--
Indsæt bogreferencer og opgavelister her.
-->
<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

*Øvelser indsættes.*

