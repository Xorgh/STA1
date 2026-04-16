---
tags:
    - Goodness-of-fit
    - Tilpasningstest
    - Chi-i-anden test
    - Kategoriske data
    - Multinomialfordeling
    - Forventede frekvenser
    - Frihedsgrader
    - Kontingenstabel
    - Test for uafhængighed
    - Simulering (hypotesetest)
---
<h1 align="center">Goodness-of-fit og analyse af kategoriske data</h1>

## Sessionsmateriale:

Ross: 11.1–11.4

[Recap og øvelser]()

<p align="left">

  <a href="Tutorial_10_notebook/">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python tutorial" width="100" />
    <br>
    <strong>Se Tutorial 10: Goodness-of-fit og kategoriske data</strong>
  </a>
</p>

<a href="Tutorial_10_notebook.ipynb" download>Download tutorial som notebook (.ipynb)</a>

[Se tutorial som markdown](Tutorial_10.md/)

[Sessionsmateriale](https://viaucdk-my.sharepoint.com/:f:/g/personal/rib_viauc_dk/IgCYtkGifsarR7EZ7jXQlSz5AY6Ci4pTawfCd4_q96mfH28?e=hBJXT6)

## Video Materiale:

Der er én playliste med 3 videoer. Videoerne gennemgår de grundlæggende begreber og metoder for goodness-of-fit og analyse af kategoriske data.

**Chi-square Tests for Count Data**

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=B4TPKA89me07fvPY&amp;list=PLvxOuBpazmsN5B0UrQaASorbf2v2KqGSt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Sessionbeskrivelse

I denne session arbejder vi med kategoriske data og hvordan man tester, om observerede tællinger passer til en antaget fordeling eller til en model om uafhængighed mellem to kategoriske variable. Vi følger Ross, kapitel 11 — Goodness of fit tests and categorical data analysis — med fokus på 11.1 (introduktion), 11.2 (goodness-of-fit når alle parametre i $H_0$ er specificeret), 11.2.1 (bestemmelse af kritisk område ved simulering), 11.3 (goodness-of-fit når nogle parametre er uspecificeret og må estimeres fra data, med tilsvarende justering af frihedsgrader), og 11.4 (test for uafhængighed i kontingenstabeller).

Idéen i Pearsons $\chi^2$-tilpasningstest er at sammenligne observerede frekvenser med forventede frekvenser under $H_0$; den resulterende teststørrelse kan under passende betingelser approksimeres med en $\chi^2$-fordeling, eller — som i 11.2.1 — vurderes ved simulation af fordelingen under $H_0$. I 11.4 udvider vi til to-vejs tabeller: under uafhængighed beregnes forventede cellefrekvenser ud fra marginalerne, og vi fortolker afvisning af $H_0$ som evidens for association mellem række- og søjlevariablen.

Afsnit 11.5 og 11.6 i Ross indgår ikke i pensum for denne session.

### Centrale begreber

- Kategoriske udfald og multinomial-tænkning (tællinger fordelt på $k$ kategorier)
- $H_0$ som en fuldt specificeret fordeling vs. $H_0$ med parametre estimeret fra stikprøven (færre frihedsgrader)
- Observerede ($O_i$ eller $O_{ij}$) og forventede ($E_i$ eller $E_{ij}$) frekvenser under $H_0$
- Pearsons $\chi^2$-statistik af formen $\sum \frac{(O-E)^2}{E}$ og valg af frihedsgrader (fx $k-1$ ved fuldt specificeret multinomial; reduktion når $m$ parametre estimeres)
- Simulering til kritisk område eller $p$-værdi når den teoretiske $\chi^2$-tilnærmelse er tvivlsom eller som pædagogisk metode (11.2.1)
- Kontingenstabel (to kategoriske variable), marginalfordelinger, forventede under uafhængighed: $E_{ij} = \dfrac{(\text{rækkesum}_i)(\text{søjlesum}_j)}{n}$
- Fortolkning af test for uafhængighed vs. association mellem variable

!!! tip "Læringsmål"

    - Kunne forklare idéen i en goodness-of-fit-test som sammenligning af observerede og forventede frekvenser.
    - Kunne gennemføre og fortolke $\chi^2$-goodness-of-fit når fordelingen under $H_0$ er fuldt specificeret (Ross 11.2).
    - Kunne forklare, hvordan simulering kan bruges til at bestemme kritisk område eller $p$-værdi (11.2.1).
    - Kunne skitsere, hvad det betyder, at parametre estimeres fra data i GOF-testen, og at frihedsgrader skal justeres (11.3).
    - Kunne opstille $H_0$ og $H_1$ for uafhængighed i en kontingenstabel, beregne forventede frekvenser og fortolke $\chi^2$-testet (Ross 11.4).
    - Kunne skelne mellem GOF (én kategorisk variabel / fordeling) og uafhængighedstest (to kategoriske variable).

## Øvelser

<!--
Indsæt bogreferencer og opgavelister her.
-->
<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

**Python løsninger til øvelse 1-6 kan findes i sessionsmaterialet.**

#### Øvelse 1
The past output of a machine indicates that each unit it produces will be

\[
\begin{array}{lcl}
\text{top grade}    & \text{with probability} & 0.40 \\
\text{high grade}   & \text{with probability} & 0.30 \\
\text{medium grade} & \text{with probability} & 0.20 \\
\text{low grade}    & \text{with probability} & 0.10 \\
\end{array}
\]

A new machine, designed to perform the same job, has produced 500 units with the following results.

\[
\begin{array}{l r}
\text{top grade} & 234 \\
\text{high grade} & 117 \\
\text{medium grade} & 81 \\
\text{low grade} & 68 \\
\end{array}
\]

Can the difference in output be ascribed solely to chance?

??? answer "&nbsp;"
    \(T=23.13 \quad p\)-value \(=.00004\).

    We reject the null hypothesis and conclude that the difference in output cannot be ascribed solely to chance at both the 0.01 and 0.05 significance levels.

#### Øvelse 2
It is believed that the daily number of electrical power failures in a certain Midwestern city is a Poisson random variable with mean 4.2. Test this hypothesis if over 150 days the number of days having \(i\) power failures is as follows:

| Failures | Number of Days |
| :---: | :---: |
| 0 | 0 |
| 1 | 5 |
| 2 | 22 |
| 3 | 23 |
| 4 | 32 |
| 5 | 22 |
| 6 | 19 |
| 7 | 13 |
| 8 | 6 |
| 9 | 4 |
| 10 | 4 |
| 11 | 0 |

To perform the test, group the data into the following four categories: 0–3, 4–5, 6–7, and 8 or more failures.

??? answer "&nbsp;"
    \(T=4.2488 \quad p\)-value \(=.2358\)

    Fail to reject the null hypothesis and conclude that we have no reason to doubt that the daily number of electrical power failures is a Poisson random variable with mean 4.2.


#### Øvelse 3

1. A sample of size 120 had a sample mean of 100 and a sample standard deviation of 15. Of these 120 data values, 3 were less than 70; 18 were between 70 and 85; 30 were between 85 and 100; 35 were between 100 and 115; 32 were between 115 and 130; and 2 were greater than 130. Test the hypothesis that the sample distribution was normal. 
*(Note: Use the 6 specified intervals as your bins and assume the mean and standard deviation are known constants for the purpose of the test.)*

2. In øvelse 2, test the hypothesis that the daily number of failures has a Poisson distribution. 
*(Note: Estimate the mean ($\lambda$) from the provided data. To perform the test, group the data into 9 categories: [0–1], [2], [3], [4], [5], [6], [7], [8], and [9 or more] failures.)*

??? answer "&nbsp;"
    1. \(TS=19.295 \quad p\)-value \(=.0017\)
        With \(df=5\), we reject the null hypothesis and conclude that the sample distribution was not normal both at the 0.01 and 0.05 significance levels.

    2. \(T=5.3683 \quad p\)-value \(=.6151\)
        Using the estimated mean \(\hat{\lambda} \approx 4.5667\) and \(df=7\), we fail to reject the null hypothesis. There is no reason to doubt that the daily number of electrical power failures follows a Poisson distribution.

#### Øvelse 4 (Tidligere eksamensopgave)

An IT company receives its printed circuit boards from two different suppliers, 1 and 2. Records show that 5% of the circuit boards from supplier 1 and 3% of the circuit boards from supplier 2 are defective. 60% of the company’s current circuit boards come from supplier 2, and the remaining from supplier 1. The company usually keeps a stock of 2000 circuit boards.

1. Is there sufficient evidence to support the claim that the rate of defectives depends very significantly on supplier?

??? answer "&nbsp;"
    1.
        $\mathrm{H}_0$ : Rate of defectives are independent of supplier

        $\mathrm{H}_1$ : Rate of defectives are dependent of supplier

        Level of significance $=0,01$

        P-value $= 0,0298$

        We fail to reject and conclude that we do not have sufficient evidence to support the claim that rate of defectives and suppliers are not very significantly independent .We would, however, be able to conclude this with alpha $=0,05$

#### Øvelse 5
A 1992 article in the Journal of the American Medical Association ("A Critical Appraisal of 98.6 Degrees F, the Upper Limit of the Normal Body Temperature, and Other Legacies of Carl Reinhold August Wunderlich") reported body temperature, gender, and heart rate for a number of subjects. The body temperatures for 25 female subjects follow: $97.8,97.2$, $97.4,97.6,97.8,97.9,98.0,98.0,98.0,98.1,98.2,98.3,98.3$, $98.4,98.4,98.4,98.5,98.6,98.6,98.7,98.8,98.8,98.9,98.9$, and 99.0.


Test the assumption that female body temperature is normally distributed.

??? answer "&nbsp;"
    p-value (Anderson-Darling): 0.7754

    Result: Fail to reject H0. The body temperature data follows a normal distribution.

#### Øvelse 6 (Tidligere eksamensopgave)

Different screens and their hue bias were tested and the result is displayed in the following table:

<div class="center-table" markdown>
|  | Blueish | Reddish | Greenish |
| :--- | :--- | :--- | :--- |
| Display 1 | 46 | 82 | 72 |
| Display 2 | 42 | 38 | 20 |
| Display 3 | 52 | 40 | 8 |
</div>

Is there sufficient evidence to conclude that screens and hue bias depend significantly?Design an appropriate test to answer this question.

??? answer "&nbsp;"
    $H_0$ : Screens and hue bias are independent

    $H_1$ : Screens and hue bias are dependent

    We obtain a p-value $= 0.0000$. From this we reject the null hypothesis and conclude that screens and hue bias are dependent.

#### Øvelse 7 (Tidligere eksamensopgave)

The dataset for this assignment is [Wages_and_Work_Hour.xlsx](Wages_and_Work_Hour.xlsx). This workbook contains data on fulltime workers in East North Central United States from the March 1999 CPS. The objective is to determine whether Education, Income, and Gender differ.

Variable notes:

- Education Level: Group 1 has less than 13 years of education. Group 2 has between 13 and 15 years of education (both included). Group 3 has 16 years or more of education.
- Income Group: Group 1 has less than or equal to $\$ 20,000$ in income. Group 2 has between $\$ 20,000$ and $\$ 48,000$ in income (both included). Group 3 has more than $\$ 48,000$ in income.

<br>

  1. Create a contingency table, placing Gender on the vertical axis and Education Level on the horizontal axis, and test whether gender is independent of level of education.
  2. Create a contingency table, placing Gender on the vertical axis and Income Group on the horizontal axis, and test whether gender is independent of income.
  3. Create a contingency table, placing Education Level on the vertical axis and Income Group on the horizontal axis, and test whether Education Level is independent of Income Group.

??? answer "&nbsp;"
    1.

        Contingency Table

        | Income Group | 1 | 2 | 3 |
        |--------|--------------------|--------------------|--------------------|
        | Female | 1044           | 727	            | 720            |
        | Male   | 1577           | 922            | 1060           |

        Critical Value: 5.9915  
        Chi-squared Statistic: 8.1127, Degrees of Freedom: 2  
        Expected Frequencies:

        | Gender | Education Level 1 | Education Level 2 | Education Level 3 |
        |--------|--------------------|--------------------|--------------------|
        | Female | 1079.16           | 678.95            | 732.89            |
        | Male   | 1541.84           | 970.05            | 1047.11           |

        Test Conclusion: Reject $H_0$ since p-value $=0.0173<0.05$

    2.

        Contingency Table

        | Gender | Income Group 1 | Income Group 2 | Income Group 3 |
        |--------|----------------|----------------|----------------|
        | Female | 957            | 1202           | 332            |
        | Male   | 679            | 1651           | 1229           |

        Critical Value: 5.9915  
        Chi-squared Statistic: 459.1215, Degrees of Freedom: 2  
        Expected Frequencies:

        | Gender | Income Group 1 | Income Group 2 | Income Group 3 |
        |--------|----------------|----------------|----------------|
        | Female | 673.60         | 1174.68        | 642.72         |
        | Male   | 962.40         | 1678.32        | 918.28         |

        Test Conclusion: Reject $H_0$ since p-value $=0.0000<0.05$

    3.

        Contingency Table

        | Income Group | 1    | 2    | 3    |
        |--------------|------|------|------|
        | Education Level 1 | 1025 | 1279 | 317  |
        | Education Level 2 | 437  | 861  | 351  |
        | Education Level 3 | 174  | 713  | 893  |

        Critical Value: 9.4877  
        Chi-squared Statistic: 980.4959, Degrees of Freedom: 4  

        Expected Frequencies:

        | Income Group | 1         | 2         | 3         |
        |--------------|-----------|-----------|-----------|
        | Education Level 1 | 708.75   | 1235.99  | 676.26   |
        | Education Level 2 | 445.91   | 777.62   | 425.47   |
        | Education Level 3 | 481.34   | 839.40   | 459.27   |

        Test Conclusion: Reject $H_0$ since p-value $=0.0000<0.05$

#### Øvelse 8 (Tidligere eksamensopgave)

The dataset for this assignment is the infamous Titanic data set (please see [Titanic.xlsx](Titanic.xlsx)). The objective is to determine whether the survival rates differ between selected variables.

Variable notes:

- pclass: A proxy for socio-economic status
- 1st $=$ Upper
- 2nd $=$ Middle
- 3rd $=$ Lower
- age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5
- sibsp: The dataset defines family relations in this way...
- Sibling = brother, sister, stepbrother, stepsister
- Spouse $=$ husband, wife (mistresses and fiancés were ignored)
- parch: The dataset defines family relations in this way...
    - Parent $=$ mother, father
    - Child $=$ daughter, son, stepdaughter, stepson
    - Some children travelled only with a nanny, therefore parch=0 for them.
- alone: is a variable that was created from combining sibsp and parch.

<br>

  1. Create a contingency table, placing survived on the vertical axis and pclass on the horizontal axis.
  2. Test whether survival rate is independent of pclass.
  3. Create a contingency table, placing survived on the vertical axis and sex (gender) on the horizontal axis.
  4. Test whether survival rate is independent of sex (gender).
  5. Create a contingency table, placing survived on the vertical axis and alone on the horizontal axis.
  6. Test whether survival rate is independent of whether a person travelled alone or not.

??? answer "&nbsp;"
    1.

        | pclass <br> survived | 1 | 2 | 3 |
        | :--- | ---: | ---: | ---: |
        | 0 | 123 | 158 | 528 |
        | 1 | 200 | 119 | 181 |

    2.

        Reject the null hypothesis: 'pclass' and 'survived' are not independent

    3.

        | survived | 0 | 1 |
        | :--- | ---: | ---: |
        | sex |  |  |
        | female | 127 | 339 |
        | male | 682 | 161 |

    4.

        Reject the null hypothesis: 'sex' and 'survived' are not independent

    5.

        | survived <br> alone | 0 | 1 |
        | :--- | ---: | ---: |
        | $\theta$ | 258 | 261 |
        | 1 | 551 | 239 |

    6.

        Reject the null hypothesis: 'alone' and 'survived' are not independent
