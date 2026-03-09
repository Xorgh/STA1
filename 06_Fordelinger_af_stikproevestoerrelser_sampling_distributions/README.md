---
tags:
    - Stikprøvefordelinger
    - Sampling distributions
    - Den Centrale Grænseværdisætning (CLT)
    - Standardfejl (Standard Error)
    - Stikprøvegennemsnit
    - Stikprøvevarians
---
<h1 align="center">Fordelinger af stikprøvestørrelser (sampling distributions)</h1>

## Sessionsmateriale:

Ross: Kapitel 6

<p align="left">

  <a href="Tutorial_6_notebook/">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python tutorial" width="100" />
    <br>
    <strong>Se Tutorial 6: Fordelinger af stikprøvestørrelser</strong>
  </a>
</p>

<a href="Tutorial_6_notebook.ipynb" download>Download tutorial som notebook (.ipynb)</a>

[Se tutorial som markdown](Tutorial_6.md/)

[Recap og øvelser]()

[Sessionnoter]()

## Video Materiale:

**Sampling Distributions**

Playliste med 3 videoer, der dækker stikprøvefordelinger.

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=nfZqrLMzDC6S3oG0&amp;list=PLvxOuBpazmsP7UN00cNZX64N1o_8635ds" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Sessionbeskrivelse

I denne session bevæger vi os fra at se på fordelinger af enkeltstående observationer til at undersøge egenskaberne ved stikprøver. Når vi indsamler data i praksis (for eksempel svartider for en server, mængden af fejl i en kodebase eller brugernes adfærd på en platform), beregner vi ofte stikprøvemål som gennemsnit eller varians for at drage konklusioner om hele populationen. Disse stikprøvemål (statistics) er i sig selv stokastiske variable og har derfor deres egne fordelinger – de såkaldte stikprøvefordelinger (sampling distributions).

Vi introducerer et af de absolut vigtigste resultater inden for sandsynlighedsregning og statistik: **Den Centrale Grænseværdisætning (Central Limit Theorem, CLT)**. Denne sætning fortæller os, at uanset hvordan den oprindelige population er fordelt, vil fordelingen af stikprøvegennemsnittet nærme sig en normalfordeling, når stikprøvestørrelsen bliver tilstrækkeligt stor. Dette gennembrud er fundamentet for meget af den statistiske inferens og hypotesetestning, vi skal arbejde med i resten af kurset. Vi ser desuden på begreber som standardfejl (standard error) som et mål for estimaters usikkerhed.

### Centrale begreber

- **Population vs. Stikprøve:** Parametre (f.eks. $\mu, \sigma^2$) over for stikprøve-statistikker (f.eks. $\bar{X}, S^2$)
- **Stikprøvefordelinger (Sampling distributions):** Fordelingen af en stikprøve-statistik
- **Stikprøvegennemsnittet ($\bar{X}$):** Forventningsværdi og varians for gennemsnittet
- **Standardfejl (Standard Error, SE):** Forskellen på standardafvigelse i data og standardfejl på gennemsnittet ($\sigma / \sqrt{n}$)
- **Den Centrale Grænseværdisætning (CLT):** Hvorfor og hvornår vi kan antage normalfordeling

!!! tip "Læringsmål"

    - Forstå forskellen mellem en populationsfordeling og en stikprøvefordeling.
    - Kunne anvende Den Centrale Grænseværdisætning (CLT) til at tilnærme fordelingen af et stikprøvegennemsnit.
    - Forstå begrebet standardfejl (standard error) og forklare, hvordan det adskiller sig fra almindelig standardafvigelse.
    - Kunne beregne sandsynligheder relateret til stikprøvegennemsnit ved brug af normalfordelingen.
    - Opnå en intuitiv forståelse for, hvordan stikprøvestørrelsen ($n$) påvirker usikkerheden og fordelingen af vores estimater.

## Øvelser

<!--
Indsæt bogreferencer og opgavelister her.
-->
<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

*Øvelser indsættes.*
