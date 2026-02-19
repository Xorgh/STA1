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

<p align="left">

  <a href="Tutorial_3_notebook">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python tutorial" width="100" />
    <br>
    <strong>Se Tutorial 3: Diskrete fordelinger II – Hypergeometrisk, Geometrisk, Negativ binomial og Poisson</strong>
  </a>
</p>

<a href="Tutorial_3_notebook.ipynb" download>Download tutorial som notebook (.ipynb)</a>

[Se tutorial som markdown](Tutorial_3.md)

[Recap](https://docs.google.com/presentation/d/1vRt7Sr3yVYMuP5WRlOv29226cPdmMrPR/edit?usp=sharing&ouid=116219961489076460261&rtpof=true&sd=true)

[Sessionnoter](https://drive.google.com/file/d/1laRKIxHLa2DBjmzVMQuKyc6vilaPrFNx/view?usp=sharing)


## Video Materiale:

**Discrete Probability Distributions**

Playliste med 13 videoer, der dækker diskrete fordelinger (også til session 3).

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=mOawtMbtwnrqVGX2&amp;list=PLvxOuBpazmsNIHP5cz37oOPZx0JKyNszN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

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

<p align="left">

  <a href="Exercises_solutions/">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python løsninger" width="100" />
    <br>
    <strong>Se løsninger til øvelserne (Python + WolframAlpha)</strong>
  </a>
</p>

<a href="Exercises_solutions.ipynb" download>Download løsningsnotebook (.ipynb)</a>

#### Øvelse 1

In each of the following cases, determine which probability distribution to use and calculate the stated probability:

1. The worldwide average number of airplane crashes of commercial airlines is 3.5 crashes per month. Find the probability that there will be at least two crashes within the next month.
2. Suppose a batch of 100 items contains 6 that are defective. If you randomly select 10 items, what is the probability that you will select more than two defectives?
3. It is known that USB drives produced by a certain company will be defective with probability .01, independent of each other. The company sells the USBs in packages of size 10. If someone buys 3 packages, what is the probability that one or more of the packages contains at least one defective USB? *Hint*: This is a two-step problem.

??? answer "&nbsp;"
    1. Poisson distribution with lambda = 3.5. p = 0.864112
    2. Hypergeometric distribution with N = 100, K = 6, n = 10. p = 0.0123
    3. Binomial. Step 1: n=10, p = 0.01, X >=1.  Step 2: n = 3, p = p_step1, Y >=1. p = 0.2603


#### Øvelse 2
A player of a video game is confronted with a series
of opponents and has an 80% probability of defeating each one.
Success with any opponent is independent of previous encounters.
Until defeated, the player continues to contest opponents.

1. What is the probability mass function of the number of opponents contested in a game?
2. What is the probability that a player defeats at least two opponents in a game?
3. What is the expected number of opponents contested in a game?
4. What is the probability that a player contests four or more opponents in a game?
5. What is the expected number of game plays until a player contests four or more opponents?

??? answer "&nbsp;"
    1. \(P(X=k) = 0.8^{k-1} \cdot 0.2\)
    2. \(p = 0.64\)
    3. \(E[X] = 5\)
    4. \(p = 0.512\)
    5. \(E[Y] \approx 1.9531\)

#### Øvelse 3
High flows result in the closure of a causeway. From past records, the road is closed for this reason on 10 days during a 20-year period. At an adjoining village, there is concern about the closure of the causeway because it provides the only access. The villagers assume that the probability of a closure of the road for more than one day during a year is less than 0.10. Is this correct? Please show using the Poisson distribution.

??? answer "&nbsp;"
    The probability of a closure of the road for more than one day during a year is 0.0902.

#### Øvelse 4
The number of errors in a textbook follows a Poisson distribution with a
mean of 0.01 error per page. What is the probability that there are three
or less errors in 100 pages?

??? answer "&nbsp;"
    \(P(X \leq 3) \approx 0.981\)

#### Øvelse 5

A startup’s sales team cold-calls potential customers. Each call results in a sale with probability \(p = 0.30\), independently of other calls. Let \(X\) be the number of calls needed until the team has made \(r=4\) sales.

1. What is the probability that the team needs at most 12 calls to make 4 sales?
2. What is the probability that the 4th sale occurs exactly on call 12?
3. Find \(E[X]\) and \(\mathrm{Var}(X)\).
4. What is the probability that the team needs more than 20 calls to make 4 sales?

??? answer "&nbsp;"
    Brug modellen: $X$ = antal kald indtil 4 salg (negativ binomial / Pascal med $r=4$, $p=0.30$).

    1. $P(X \le 12)\approx 0.5075$
    2. $P(X = 12)\approx 0.0770$
    3. $E[X]=13.3333$ og $\mathrm{Var}(X)=31.1111$
    4. $P(X > 20)\approx 0.1071$

#### Øvelse 6
Astronomers treat the number of stars in a given volume of space as a Poisson random variable. The density in the Milky Way Galaxy in the vicinity of our solar system is one star per 16 cubic light-years.

1. What is the probability of no stars in 16 cubic light-years?
2. What is the probability of two or more stars in 16 cubic light-years?
3. How many cubic light-years of space must be studied so that the probability of one or more stars exceeds 0.95?

??? answer "&nbsp;"
    1. $P(X = 0)\approx 0.367879$
    2. $P(X \geq 2) = 0.264241$
    3. Around 48
