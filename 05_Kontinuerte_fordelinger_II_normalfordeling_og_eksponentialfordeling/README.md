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

<p align="left">

  <a href="Tutorial_5_notebook/">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python tutorial" width="100" />
    <br>
    <strong>Se Tutorial 5: Kontinuerte fordelinger II (normalfordeling og eksponentialfordeling)</strong>
  </a>
</p>

<a href="Tutorial_5_notebook.ipynb" download>Download tutorial som notebook (.ipynb)</a>

[Se tutorial som markdown](Tutorial_5.md/)

[Recap og øvelser](https://drive.google.com/file/d/1zB5wOkh3L3f_ckAaEpSEahkDrFnL-gwB/view?usp=sharing)

[Sessionnoter](https://drive.google.com/file/d/1qTGWWIihQLTLNe0e-0nUwGIbpkH7XWkS/view?usp=sharing)


## Video Materiale:

**Continuous Probability Distributions** (5-7)

Playliste med 10 videoer, der dækker kontinuerte fordelinger - også til session 4.

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=jiGDsott_rQOGdWe&amp;list=PLvxOuBpazmsPDZGwqhhjE3KkLWnTD34R0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

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

**Bemærk:** Alle dagens øvelser er taget fra eksamensopgaver. Du kan derfor forvente lignende opgaver på eksamen.

#### Øvelse 1
Let $X \sim N(3,9)$.

1. Find $P(X>0)$.
2. Find $P(-3<X<8)$.
3. Find $P(X>5 | X>3)$.

??? answer "&nbsp;"
    1. \(P(X>0)=\Phi(1) \approx 0.8413\)
    2. \(P(-3<X<8)=\Phi\left(\frac{5}{3}\right)-\Phi(-2) \approx 0.9295\).
    3. \(P(X>5 \mid X>3)=2 \times\left(1-\Phi\left(\frac{2}{3}\right)\right) \approx 0.5050\)

#### Øvelse 2
Let $X \sim N(3,9)$ and $Y=5-X$.

1. Find $P(X>2)$.
2. Find $P(-1<Y<3)$.
3. Find $P(X>4 |Y<2)$.

??? answer "&nbsp;"
    1. \(P(X>2)=1-\Phi\left(\frac{1}{3}\right) \approx 0.6306\)
    2. \(P(-1<Y<3)=\Phi\left(\frac{1}{3}\right)-\Phi(-1) \approx 0.4719 \).
    3. \(P(X>4 \mid Y<2)=2\left(1-\Phi\left(\frac{1}{3}\right)\right) \approx 0.7389 .\)

#### Øvelse 3

Let \(X \sim N(2,4)\) and \(Y=3-2 X\).

1. Find \(P(X>1)\).
2. Find \(P(-2<Y<1)\).
3. Find \(P(X>2 \mid Y<1)\).

??? answer "&nbsp;"
    1. 0.6915
    2. 0.2902
    3. 0.7231

#### Øvelse 4
A central database server receives, on the average, 25 requests per second from its clients. Assuming that requests received by a database follow a Poisson distribution

<ol start="1">
    <li>What is the probability that the server will receive no requests in a 10-millisecond interval?</li>
    <li>What is the probability that the server will receive more than 2 requests in a 10-millisecond interval?</li>
    <li>What is the probability that the server will receive between 2 and 4 (both included) requests in a 20-millisecond interval?</li>
</ol>

Let T be the time in seconds between requests.

<ol start="4">
    <li>What is the probability that less than or equal to 10 milliseconds will elapse between job requests?</li>
    <li>What is the probability that more than 100 milliseconds will elapse between requests?</li>
</ol>


??? answer "&nbsp;"
    1. \(P(X=0) = 0.7788\)
    2. \(P(X>2) = 0.0022\)
    3. \(P(2 \leq X \leq 4) = 0.09\)
    4. \(P(T \leq 0.01) = 0.2212\)
    5. \(P(T > 0.1) = 0.0821\)

#### Øvelse 5
Empirical evidence suggests that the number of battery charges of a Tesla Model S ( 85 kWh ) follows a Poisson distribution with an average of 2.1 charges per 1,000 km.

<ol start="1">
    <li>What is the probability that you will need to charge the Tesla more than five times during a \(2,000 \mathrm{~km}\) trip?</li>
    <li>What is the probability that you will not need to charge the Tesla during a 500 km trip?</li>
</ol>

Now, let \(K\) denote the range in kilometers between charges.

<ol start="3">
    <li>Which distribution must be used to model \(K\) and what is the average range in kilometers between charges?</li>
    <li>Suppose someone has to travel from Horsens to Copenhagen - a distance of 270 km. What is the probability that the person will be able to complete the trip without having to charge the car battery?</li>
</ol>

??? answer "&nbsp;"
    1. 0.2469
    2. 0.3499
    3. 476.19
    4. 0.5672