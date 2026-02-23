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

**Bemærk:** Alle dagens øvelser er taget fra eksamensopgaver. Du kan derfor forvente lignende opgaver på eksamen.

#### Øvelse 1
Let \(X\) denote a continuous stochastic variable with the following probability density function:

\[
    f(x) =
    \begin{cases}
    c x^4 & \text{for } -1 \leq x \leq 1, \\
    0 & \text{otherwise,}
    \end{cases}
\]

where \(c\) is a constant.

1. Show that the cumulative probability function of \(X\) is:

    \[
    F(x) =
    \begin{cases}
    0 & \text{for } x < -1, \\
    \frac{1}{5} c\left(x^5 + 1\right) & \text{for } -1 \leq x \leq 1, \\
    1 & \text{for } x > 1.
    \end{cases}
    \]

2. Determine the constant \(c\) and restate both the probability density function and the cumulative probability function using the actual value of \(c\).

3. Compute \(P\left(-\frac{1}{2} < X < \frac{1}{2}\right)\) and \(P(X > 0)\).

4. Find the expected value and variance of \(X\).

??? answer "&nbsp;"
    1. Can be shown either by integrating the probability density function or by differentiating the cumulative probability function.
    2. \(c = \frac{5}{2}\)
    3. \(P\left(-\frac{1}{2} < X < \frac{1}{2}\right) = \frac{1}{32} = 0.0315\) and \(P(X > 0) = \frac{1}{2} = 0.5\)
    4. \(E[X] = 0\) and \(VAR(X) = \frac{5}{7}\)

#### Øvelse 2
Let \(X\) denote a continuous stochastic variable with the following density function

$$
f(x)= \begin{cases}c\left(1-x^2\right) & \text { for }-1<x<1 \\ 0 & \text { otherwise }\end{cases}
$$

1. Determine the value of \(c\) and state the cumulative distribution function of \(X\).
2. Determine \(P\left(X \leq \frac{1}{2}\right)\) and \(P\left(X \leq-\frac{1}{4}\right)\)
3. Determine the expected value and the variance of \(X\).

??? answer "&nbsp;"
    a. \(c = \frac{3}{4}\) and \(F(x) = \begin{cases}0 & \text { for } x<-1 \\ \frac{3}{4}\left(x-\frac{x^3}{3}\right) + \frac{1}{2} & \text { for }-1 \leq x \leq 1 \\ 1 & \text { for } x>1\end{cases}\)

    b. \(P\left(X \leq \frac{1}{2}\right) = 0.8438\) and \(P\left(X \leq-\frac{1}{4}\right) = 0.3164\)

    c. \(E[X] = 0\) and \(VAR(X) = 0.2\)

#### Øvelse 3
Compute the expected value, \(E(X)\), if \(X\) has a density function as follows:

1. \(f(x)= \begin{cases}\frac{1}{4} x e^{-\frac{x}{2}} & x>0 \\ 0 & \text { otherwise }\end{cases}\)
2. \(f(x)= \begin{cases}5 x^{-2} & x>5 \\ 0 & \text { otherwise }\end{cases}\)

    The density function of \(X\) is given by

    $$
    f(x)= \begin{cases}a+b x^2 & 0 \leq x \leq 1 \\ 0 & \text { otherwise }\end{cases}
    $$

3. If \(E(X)=\frac{3}{5}\), find \(a\) and \(b\).

??? answer
    1. \(E(X) = 4\)
    2. \(E(X) = \infty \)
    3. \(a = \frac{3}{5}\) and \(b = \frac{6}{5}\)

#### Øvelse 4
The length of time \(X\) (in hours), needed by students in the STA1 course to complete the three-hour Part 1 exam is a continuous random variable with the following density function:

\[
f(x) =
\begin{cases}
q\left(x^2 + x\right) & \text{if } 0 \leq x \leq 3, \\
0 & \text{else}.
\end{cases}
\]

1. Find the value of \(q\) that makes \(f(x)\) a probability density function.

2. Find the cumulative distribution function.

3. Find the probability that a student will complete the Part 1 exam in:
    - (i) Less than an hour.
    - (ii) Between one and two hours.
    - (iii) More than two hours.
    - (iv) During the final ten minutes of the exam.

4. Find the mean time needed to complete the three-hour STA1 Part 1 exam.

5. Find the variance and standard deviation of \(X\).

??? answer
    1. \(q = \frac{2}{27} \approx 0.0741\)
    2. \(F(x) = \begin{cases}0 & \text{if } x < 0, \\ \frac{2 x^3}{81}+\frac{x^2}{27} & \text{if } 0 \leq x \leq 3, \\ 1 & \text{if } x > 3.\end{cases}\)
    3. (i) \(P(X<1)=5 / 81=0.0617\), (ii) \(P(1<X<2)=23 / 81=0.284\), (iii) \(P(X>2)=53 / 81=0.6543\), (iv) \(P(X>17 / 6)=0.1411\)
    4. \(E[X] = 13/6 =2.1667 \text { hours } \)
    5. \(\operatorname{Var}(X)=0.4056\) hours \(^2\) and \(\mathrm{SD}(X)=0.6368\) hours