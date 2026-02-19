---
tags:
    - Stokastiske variable
    - Diskrete variable
    - Kontinuerte variable
    - Fordelingsfunktion
    - Tæthedsfunktion
    - Sandsynlighedsfunktion
    - Forventningsværdi
    - Varians
    - Uniform-fordeling
    - Bernoulli-fordeling
    - Binomialfordeling
---
<h1 align="center">Diskrete fordelinger I: uniform, Bernoulli og binomialfordeling</h1>

## Sessionsmateriale:

Ross: 4.1., 4.2., 4.4., 4.6., 5.1, 5.4

<p align="left">

  <a href="Tutorial_2_notebook/">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python introduktion" width="100" />
    <br>
    <strong>Se Tutorial 2: Diskrete fordelinger: Uniform, Bernoulli og Binomial</strong>
  </a>
</p>

<a href="Tutorial_2_notebook.ipynb" download>Download tutorial som notebook (.ipynb)</a>

[Se tutorial som markdown](Tutorial_2.md/)

[Sessionnoter](https://drive.google.com/file/d/1azFhbhkKSIiLboKuxTlyhh-41jYMtbRm/view?usp=sharing)

## Video Materiale:

**Discrete Probability Distributions**

Playliste med 13 videoer, der dækker diskrete fordelinger (også til session 3).

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=mOawtMbtwnrqVGX2&amp;list=PLvxOuBpazmsNIHP5cz37oOPZx0JKyNszN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
---

## Sessionbeskrivelse

I denne session bygger vi videre på det fundament, der blev lagt sidst, ved at formalisere begrebet **stokastiske variable**. Hvor vi sidst arbejdede med deskriptiv statistik på observerede data, dykker vi nu ned i de underliggende matematiske modeller, der beskriver, hvordan data genereres. Vi skelner skarpt mellem **diskrete** og **kontinuerte** variable og introducerer de essentielle værktøjer til at beskrive dem: sandsynlighedsfunktioner, tæthedsfunktioner og fordelingsfunktioner.

Vi arbejder videre med **forventningsværdi** og **varians**, men definerer dem nu teoretisk ud fra fordelingerne snarere end blot som gennemsnit af et datasæt. Dette gør os i stand til at forudsige egenskaber ved data, før vi har målt dem. Endelig kobler vi teorien til praksis ved at gennemgå tre fundamentale standardfordelinger: **Bernoulli-** og **binomialfordelingen**, som er hjørnestenene i modellering af binære udfald (f.eks. succes/fiasko i softwaretest), samt **Uniform-fordelingen**, der beskriver situationer med lige stor sandsynlighed over et interval.

### Centrale begreber

- **Stokastiske variable:** Diskrete vs. kontinuerte
- **Funktioner:** Tætheds- (PDF), sandsynligheds- (PMF) og fordelingsfunktioner (CDF)
- **Nøgletal:** Forventningsværdi ($E[X]$) og varians ($Var(X)$)
- **Diskrete fordelinger:** Uniform,Bernoulli- og binomialfordeling

!!! tip "Læringsmål"

    - Kunne definere en stokastisk variabel og skelne mellem diskrete og kontinuerte typer.
    - Kunne anvende og fortolke tæthedsfunktioner, sandsynlighedsfunktioner og fordelingsfunktioner til at beregne sandsynligheder.
    - Kunne beregne forventningsværdi og varians ud fra en given fordeling.
    - Kunne identificere situationer, der kan modelleres med en Binomialfordeling, og udføre beregninger herpå.
    - Forstå egenskaberne ved en Ligefordeling og kunne anvende denne i simple modelleringssammenhænge.

## Øvelser

<!--
Indsæt bogreferencer og opgavelister her.
-->
<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

Disse øvelser skal I kunne lave med og uden Python. I må gerne bruge Wolfram Alpha (se eventuelt tutorial til denne session).

<p align="left">

  <a href="Exercises_solutions/">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python løsninger" width="100" />
    <br>
    <strong>Se løsninger til øvelserne (Python + WolframAlpha)</strong>
  </a>
</p>

<a href="Exercises_solutions.ipynb" download>Download løsningsnotebook (.ipynb)</a>

#### Øvelse 1
A computer system uses passwords that are exactly six
characters and each character is one of the 26 letters (a–z) or
10 integers (0–9). Suppose that 10,000 users of the system have
unique passwords. A hacker randomly selects (with replacement)
100,000 passwords from the potential set, and a match to a user’s
password is called a hit.

1. What is the distribution of the number of hits?
2. What is the probability of no hits?
3. What are the mean and variance of the number of hits?

??? answer "&nbsp;"
    1. The distribution of the number of hits is Binomial with $n = 10^5$ and $p=\frac{10^5}{36^6}$
    2. $P(X=0) = 0.6317$
    3. $\mu = \sigma^2 = 0.4594$

#### Øvelse 2
Because all airline passengers do not show up for
their reserved seat, an airline sells 125 tickets for a flight that holds
only 120 passengers. The probability that a passenger does not
show up is 0.10, and the passengers behave independently.

1. What is the probability that every passenger who shows up can take the flight?
2. What is the probability that the flight departs with empty seats?

??? answer "&nbsp;"
    1. $p = 0.9961 $
    2. $p = 0.9886$

#### Øvelse 3
A congested computer network has a 1% chance of losing a data packet that must be resent, and packet losses are independent events. An e-mail message requires 100 packets.

1. What is the probability that at least one packet is resent?
2. What is the probability that two or more packets are resent?
3. What are the mean and standard deviation of the number of packets that are resent?
4. If there are 10 messages and each contains 100 packets, what is the probability that at least one message requires that two or more packets be resent?

??? answer "&nbsp;"
    1. $P(X \geq 1)=0.634$
    2. $P(X \geq 2)=0.2642$
    3. $\mu = 1, \sigma = 0.995$
    4. $P(Y \geq 1)=0.9535$

#### Øvelse 4
The probability that a patient recovers from a rare blood disease is 0.4. If 15 people are known to have contracted this disease, what is the probability that:

1. At least 10 survive
2. From 3 to 8 survive
3. Exactly 5 survive
4. Find the mean and variance.

??? answer "&nbsp;"
    1. $P(X \geq 10) \approx 0.0338$
    2. $P(3 \leq X \leq 8) \approx 0.8778$
    3. $P(X=5) \approx 0.1859$
    4. $\mu = 6, \sigma^2 = 3.6$

#### Øvelse 5
Let $X$ and $Y$ be two independent discrete random variables with the following PMFs:

For $X$:

$$
P_X(k) =
\begin{cases}
\frac{1}{10} & \text{for } k=0 \\
\frac{2}{10} & \text{for } k=1 \\
\frac{3}{10} & \text{for } k=2 \\
\frac{4}{10} & \text{for } k=3 \\
0 & \text{otherwise}
\end{cases}
$$

For $Y$:

$$
P_Y(k) =
\begin{cases}
\frac{1}{5} & \text{for } k=0 \\
\frac{1}{5} & \text{for } k=1 \\
\frac{2}{5} & \text{for } k=2 \\
\frac{1}{5} & \text{for } k=3 \\
0 & \text{otherwise}
\end{cases}
$$

1. Find $P(X<2 \text{ and } Y<2)$.
2. Find $P(X \ge 2 \text{ or } Y \ge 2)$.
3. Find $P(X \ge 2 \mid Y \ge 2)$.
4. Find $P(X < Y)$.

??? answer "&nbsp;"
    1. 0.12
    2. 0.88
    3. 0.70
    4. 0.26