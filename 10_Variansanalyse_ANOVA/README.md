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

[Se tutorial som markdown](Tutorial_10.md/)

[Recap og øvelser]()

[Sessionnoter]()

[Sessionsmateriale]()

## Video Materiale:

Der er én playliste med 5 videoer. Videoerne gennemgår de grundlæggende begreber og metoder for variansanalyse.

**One-way ANOVA**

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=1BoXz_UIw58GL12F&amp;list=PLvxOuBpazmsNqPdvhkF_l55tHdDNW3z-7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Sessionbeskrivelse

Når vi skal sammenligne middelværdier for mere end to grupper, bliver mange separate $t$-tests problematiske (øget risiko for type I-fejl). Ensidig variansanalyse (one-way ANOVA) samler spørgsmålet i én omnibus-$F$-test: $H_0$: alle gruppemiddelværdier er ens mod $H_1$: mindst én gruppe adskiller sig.

Vi gennemgår modellen med fælles fejlvarians, opdeling af den totale variation (mellem grupper vs. inden for grupper), ANOVA-tabellen ($F = \mathrm{MSB}/\mathrm{MSW}$), $F$-fordelingen med de rette frihedsgrader, og hvordan I fortolker resultatet. Under Ross 10.3 ser vi kort på parvise sammenligninger (fx Tukey HSD), når $H_0$ er forkastet eller når I vil undersøge hvilke grupper der adskiller sig.


* Python-gennemgang: **Tutorial 10** (SciPy, statsmodels — kør `pip install statsmodels` eller første celle i notebook'en med `%pip`, hvis import fejler; kort om alternativer).
* **Øvelse 1:** three resin types, impurity concentration — [Resin_impurities.xlsx](Resin_impurities.xlsx).
* **Øvelse 2:** three oscilloscope filters (radar operator) — [Scope_filter_intensity.xlsx](Scope_filter_intensity.xlsx).
* **Øvelse 3:** two weight-loss diets (lb) — [Diet_weight_loss.xlsx](Diet_weight_loss.xlsx); ANOVA with $k=2$ plus an alternative test.
* **Øvelse 4:** complete a partially given one-way ANOVA table (four factor levels); replicates, missing SS/MS/DF, $P$-value bounds, conclusion.

### Centrale begreber

- **Ensidet layout:** én kategorisk faktor med $k$ niveauer (grupper)
- **Model:** $Y_{ij} = \mu_i + \varepsilon_{ij}$ (Ross’ notation) / effektform med $\mu + \alpha_i$
- **$H_0$: $\mu_1 = \cdots = \mu_k$** mod **$H_1$:** ikke alle $\mu_i$ ens
- SST, SSW (indenfor), SSB (mellem), df, MSB, MSW, $F$-teststørrelse
- **Antagelser:** uafhængige observationer, ca. normalitet inden for hver gruppe, ens varians ($\sigma^2$) på tværs af grupper
- **Efter ANOVA:** justerede parvise sammenligninger (fx Tukey) for at undgå “datadyrkning”

!!! tip "Læringsmål"

    - Kunne forklare hvorfor ANOVA bruges ved $k>2$ grupper i stedet for mange $t$-tests.
    - Kunne opstille $H_0$ og $H_1$ for en ensidig ANOVA og fortolke en $F$-teststørrelse og tilhørende $p$-værdi.
    - Kunne skitsere opbygningen af ANOVA-tabellen (sumkvadrater, frihedsgrader, middelkvadrater).
    - Kunne gennemføre one-way ANOVA i Python med SciPy (`f_oneway`) og statsmodels (`ols` + `anova_lm`).
    - Kunne efter en signifikant ANOVA bruge Tukey HSD (eller tilsvarende) til parvise sammenligninger og fortolke output.

## Øvelser

<style type="text/css">
    ol { list-style-type: decimal; }
</style>

Gennemgang i Python: **Tutorial 10**.

#### Øvelse 1

A laboratory measures **impurity concentration** in samples from three resin products (Resin I, II, and III). Five independent measurements per resin gave the following values (same numbers as in the spreadsheet):

<div class="center-table" markdown>
| Resin I | Resin II | Resin III |
| :---: | :---: | :---: |
| .046 | .038 | .031 |
| .025 | .035 | .042 |
| .014 | .031 | .020 |
| .017 | .022 | .018 |
| .043 | .012 | .039 |
</div>

**Long-format** data: [Resin_impurities.xlsx](Resin_impurities.xlsx) (columns `resin`, `impurity`).

1. State $H_0$ and $H_1$ for a one-way ANOVA (one factor: resin type, three levels). Carry out the test at $\alpha = 0.05$ and interpret $F$ and the $p$-value.
2. Use Levene’s test as a rough check of whether the equal variance assumption across groups is plausible.
3. Perform Tukey HSD (pairwise comparisons). Relate the result to the outcome of the ANOVA.

??? answer "&nbsp;"

    **Sample means:** $\bar{y}_{I} \approx 0.0290$, $\bar{y}_{II} \approx 0.0276$, $\bar{y}_{III} \approx 0.0300$. Grand mean $\bar{y}_{\cdot\cdot} \approx 0.0289$.

    **1. ANOVA**

    $H_0$: $\mu_I = \mu_{II} = \mu_{III}$ (the same expected impurity concentration for all three resin types).

    $H_1$: not all $\mu$ are equal.

    With $k=3$ groups and $n=5$ observations per group, $N=15$, $\mathrm{df}_{\text{between}} = 2$, $\mathrm{df}_{\text{within}} = 12$.

    Sum of squares (between / within): $\mathrm{SSB} \approx 1.45\times 10^{-5}$, $\mathrm{SSW} \approx 1.79\times 10^{-3}$ (and $\mathrm{SST} \approx 1.80\times 10^{-3}$).

    Mean squares: $\mathrm{MSB} = \mathrm{SSB}/2 \approx 7.27\times 10^{-6}$, $\mathrm{MSW} = \mathrm{SSW}/12 \approx 1.49\times 10^{-4}$.

    $$F = \frac{\mathrm{MSB}}{\mathrm{MSW}} \approx 0.0487$$

    Under $H_0$, $F \sim F_{2,12}$. $p$-value $\approx 0.953$ (e.g. `scipy.stats.f_oneway` or `statsmodels` `anova_lm` gives the same numbers).

    **Conclusion:** $p > 0.05$ — **do not reject** $H_0$. There is **no** significant evidence of a difference in mean impurity among the three resin types in this experiment.

    **2. Levene**

    Levene’s test (e.g. `scipy.stats.levene` on the three samples): statistic $\approx 0.41$, $p \approx 0.67$. No strong indication of unequal variances; the **equal variance** assumption is **not** obviously contradicted by the data (interpret cautiously with small $n$ per group).

    **3. Tukey HSD**

    `pairwise_tukeyhsd` (or `scipy.stats.tukey_hsd`): no pairwise comparison is significant at family-wise $\alpha = 0.05$ (all `reject` are **False**; adjusted $p$-values $\gg 0.05$). This **agrees** with the non-significant omnibus ANOVA — no pair of groups separates.

    ```python
    import numpy as np
    import pandas as pd
    from scipy import stats
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    from statsmodels.stats.multicomp import pairwise_tukeyhsd

    g1 = np.array([0.046, 0.025, 0.014, 0.017, 0.043])
    g2 = np.array([0.038, 0.035, 0.031, 0.022, 0.012])
    g3 = np.array([0.031, 0.042, 0.020, 0.018, 0.039])

    F, p = stats.f_oneway(g1, g2, g3)
    print("F =", F, "p =", p)
    print(stats.levene(g1, g2, g3))

    df = pd.DataFrame({
        "impurity": np.concatenate([g1, g2, g3]),
        "resin": np.repeat(["I", "II", "III"], 5),
    })
    m = ols("impurity ~ C(resin)", data=df).fit()
    print(sm.stats.anova_lm(m, typ=2))
    print(pairwise_tukeyhsd(df["impurity"], df["resin"], alpha=0.05))
    ```

#### Øvelse 2

We want to know what type of filter should be used over the screen of a cathode-ray oscilloscope in order to have a radar operator easily pick out targets on the presentation. A test to accomplish this has been set up. A noise is first applied to the scope to make it difficult to pick out a target. A second signal, representing the target, is put into the scope, and its intensity is increased from zero until detected by the observer. The intensity setting at which the observer first notices the target signal is then recorded. This experiment is repeated **20 times with each filter**. The numerical value of each reading listed in the table of data is proportional to the target intensity at the time the operator first detects the target.

<div class="center-table" markdown>
| Filter No. 1 | Filter No. 2 | Filter No. 3 |
| :---: | :---: | :---: |
| 90 | 88 | 95 |
| 87 | 90 | 95 |
| 93 | 97 | 89 |
| 96 | 87 | 98 |
| 94 | 90 | 96 |
| 88 | 96 | 81 |
| 90 | 90 | 92 |
| 84 | 90 | 79 |
| 101 | 100 | 105 |
| 96 | 93 | 98 |
| 90 | 95 | 92 |
| 82 | 86 | 85 |
| 93 | 89 | 97 |
| 90 | 92 | 90 |
| 96 | 98 | 87 |
| 87 | 95 | 90 |
| 99 | 102 | 101 |
| 101 | 105 | 100 |
| 79 | 85 | 84 |
| 98 | 97 | 102 |
</div>

**Long-format** data: [Scope_filter_intensity.xlsx](Scope_filter_intensity.xlsx) (columns `filter` with values 1, 2, or 3, and `intensity`).

At the 5% significance level, test the hypothesis that the filters are the same (i.e. the same expected detection intensity for the three filter types). You may add Levene’s test and Tukey HSD as in Øvelse 1.

??? answer "&nbsp;"

    Let $Y_{ij}$ be the recorded intensity for filter $i$ ($i=1,2,3$), replicate $j$ ($j=1,\ldots,20$). We assume independent observations and equal variance across filters for the ANOVA.

    **Sample means:** $\bar{y}_{1\cdot} = 91.7$, $\bar{y}_{2\cdot} = 93.25$, $\bar{y}_{3\cdot} = 92.8$. Grand mean $\bar{y}_{\cdot\cdot} \approx 92.58$.

    **Hypotheses**

    $H_0$: $\mu_1 = \mu_2 = \mu_3$ (the filters are the same with respect to expected detection intensity).

    $H_1$: not all $\mu_i$ are equal.

    **ANOVA:** $k=3$, $n=20$ per group, $N=60$, $\mathrm{df}_{\text{between}} = 2$, $\mathrm{df}_{\text{within}} = 57$.

    $\mathrm{SSB} \approx 25.43$, $\mathrm{SSW} \approx 2265.15$, $\mathrm{SST} \approx 2290.58$.

    $\mathrm{MSB} = \mathrm{SSB}/2 \approx 12.72$, $\mathrm{MSW} = \mathrm{SSW}/57 \approx 39.74$.

    $$F = \frac{\mathrm{MSB}}{\mathrm{MSW}} \approx 0.32$$

    Under $H_0$, $F \sim F_{2,57}$. $p$-value $\approx 0.727$.

    **Conclusion at $\alpha = 0.05$:** $p > 0.05$ — **do not reject** $H_0$. The data do **not** support a difference in mean intensity at first detection among the filters; at the 5% level the hypothesis that the **filters are the same** cannot be rejected.

    **Levene:** statistic $\approx 0.80$, $p \approx 0.46$ — no strong evidence against equal variances.

    **Tukey HSD:** no significant pairs (all `reject` **False**), consistent with the non-significant omnibus test.

    ```python
    import numpy as np
    import pandas as pd
    from scipy import stats
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    from statsmodels.stats.multicomp import pairwise_tukeyhsd

    g1 = np.array([90, 87, 93, 96, 94, 88, 90, 84, 101, 96, 90, 82, 93, 90, 96, 87, 99, 101, 79, 98])
    g2 = np.array([88, 90, 97, 87, 90, 96, 90, 90, 100, 93, 95, 86, 89, 92, 98, 95, 102, 105, 85, 97])
    g3 = np.array([95, 95, 89, 98, 96, 81, 92, 79, 105, 98, 92, 85, 97, 90, 87, 90, 101, 100, 84, 102])

    print(stats.f_oneway(g1, g2, g3))
    print(stats.levene(g1, g2, g3))

    df = pd.DataFrame({
        "intensity": np.concatenate([g1, g2, g3]),
        "filter": np.repeat([1, 2, 3], 20),
    })
    m = ols("intensity ~ C(filter)", data=df).fit()
    print(sm.stats.anova_lm(m, typ=2))
    print(pairwise_tukeyhsd(df["intensity"], df["filter"].astype(str), alpha=0.05))
    ```

#### Øvelse 3

Twenty overweight individuals were randomly assigned to one of two diets. After 10 weeks, the weight losses (in pounds) were recorded:

<div class="center-table" markdown>
| Diet 1 | Diet 2 |
| ------ | ------ |
| 22.2   | 24.2   |
| 23.4   | 16.8   |
| 24.2   | 14.6   |
| 16.1   | 13.7   |
| 9.4    | 19.5   |
| 12.5   | 17.6   |
| 18.6   | 11.2   |
| 32.2   | 9.5    |
| 8.8    | 30.1   |
| 7.6    | 21.5   |
</div>

**Long-format** data: [Diet_weight_loss.xlsx](Diet_weight_loss.xlsx) (columns `diet` with 1 or 2, and `weight_loss`).

1. Use one-way ANOVA at the 5% level to test whether the two diets have the same expected mean weight loss.
2. Suggest another statistical test that could be used to test the same hypothesis. State the null and alternative hypotheses for that test.

??? answer "&nbsp;"

    **Sample means:** $\bar{y}_{1\cdot} = 17.5$ lb, $\bar{y}_{2\cdot} \approx 17.87$ lb (10 subjects per diet).

    1. **One-way ANOVA with $k=2$.** The factor is **diet** with two levels. One-way ANOVA is **well defined** for $k=2$ as well; here $\mathrm{df}_{\text{between}} = 1$, $\mathrm{df}_{\text{within}} = N-k = 18$ ($N=20$).

        $H_0$: $\mu_1 = \mu_2$ (the same expected mean weight loss for diet 1 and diet 2).

        $H_1$: $\mu_1 \neq \mu_2$ (as in a two-sided comparison of two means — ANOVA with $k=2$ corresponds to a **two-sided** test on the difference).

        $\mathrm{SSB} \approx 0.6845$, $\mathrm{SSW} \approx 934.68$, $\mathrm{MSB} \approx 0.6845$, $\mathrm{MSW} = \mathrm{SSW}/18 \approx 51.93$.

        $$F = \frac{\mathrm{MSB}}{\mathrm{MSW}} \approx 0.0132$$

        Under $H_0$, $F \sim F_{1,18}$. $p$-value $\approx 0.910$ (e.g. `scipy.stats.f_oneway`).

        **Conclusion at $\alpha = 0.05$:** $p > 0.05$ — **do not reject** $H_0$. No significant difference in mean weight loss between the two diets in this study.

    2. **Alternative test.** **Two independent samples — pooled $t$-test** (same **equal variance** assumption in the two populations as in ANOVA):

        - $H_0$: $\mu_1 = \mu_2$
        - $H_1$: $\mu_1 \neq \mu_2$ (two-sided)

        The test statistic is the standard $t$ with $n_1+n_2-2 = 18$ degrees of freedom. For $k=2$, **mathematically** $F = t^2$ and the **same $p$-value** as in ANOVA (here $t \approx -0.115$, $p \approx 0.910$).

        **Alternative (different assumption):** **Welch’s $t$-test** (`equal_var=False` in SciPy) — same $H_0$ and $H_1$ about the means, but **without** requiring equal variances; degrees of freedom are approximated (can yield a slightly different $p$ than ANOVA if variances differ).

    ```python
    import numpy as np
    from scipy import stats

    d1 = np.array([22.2, 23.4, 24.2, 16.1, 9.4, 12.5, 18.6, 32.2, 8.8, 7.6])
    d2 = np.array([24.2, 16.8, 14.6, 13.7, 19.5, 17.6, 11.2, 9.5, 30.1, 21.5])

    F, p_anova = stats.f_oneway(d1, d2)
    t, p_t = stats.ttest_ind(d1, d2, equal_var=True)
    print("ANOVA F, p:", F, p_anova)
    print("pooled t, p:", t, p_t)
    print("F equals t^2:", F, t**2)
    print("Welch:", stats.ttest_ind(d1, d2, equal_var=False))
    ```

#### Øvelse 4

Consider the following computer output for an experiment in which **one factor was tested at four levels**:

$$
\begin{array}{lccccc}
\text{Source} & \text{DF} & \text{SS} & \text{MS} & F & P\text{-value} \\
\hline
\text{Factor} & ? & ? & 330.4716 & 4.42 & ? \\
\text{Error} & ? & ? & ? & & \\
\text{Total} & 31 & ? & & &
\end{array}
$$

**Recipe (fill gaps + $P$-value):** see **Tutorial 10**, **§2.1** (*Ufuldstændig ANOVA-tabel*), with the same numerical example in Python.

1. How many observations (replicates) per factor level were used?
2. **Fill in** the missing entries in the ANOVA table. Give **bounds** for the $P$-value (using $F$-tables or software).
3. What **conclusions** can you draw about differences among the factor-level means? (State $H_0$ and $H_1$, and relate to a typical $\alpha = 0.05$.)

??? answer "&nbsp;"

    One-way ANOVA with **$a = 4$** factor levels (balanced layout).

    1. **Replicates.** Total df is $N - 1 = 31$, so **$N = 32$** observations. With four levels and a balanced design, observations per level are

        $$r = \frac{N}{a} = \frac{32}{4} = 8.$$

        The experimenter used **8 observations per factor level**.

    2. **Completed table.** $\mathrm{DF}_{\text{Factor}} = a - 1 = 3$, $\mathrm{DF}_{\text{Error}} = N - a = 28$.

        $$SS_{\text{Factor}} = MS_{\text{Factor}} \cdot \mathrm{DF}_{\text{Factor}} = 330.4716 \times 3 = 991.4148.$$

        From $F = MS_{\text{Factor}} / MS_{\text{Error}}$,

        $$MS_{\text{Error}} = \frac{330.4716}{4.42} \approx 74.7673, \qquad SS_{\text{Error}} = MS_{\text{Error}} \times 28 \approx 2093.49.$$

        $$SS_{\text{Total}} = SS_{\text{Factor}} + SS_{\text{Error}} \approx 3084.90.$$

        Completed table:

        $$
        \begin{array}{lccccc}
        \text{Source} & \text{DF} & \text{SS} & \text{MS} & F & P\text{-value} \\
        \hline
        \text{Factor} & 3 & 991.4148 & 330.4716 & 4.42 & \approx 0.0115 \\
        \text{Error} & 28 & \approx 2093.49 & \approx 74.7673 & & \\
        \text{Total} & 31 & \approx 3084.90 & & &
        \end{array}
        $$

        For $F = 4.42$ with $(3,\,28)$ df, the exact upper-tail $p$-value is about **$0.0115$** (e.g. `scipy.stats.f.sf(4.42, 3, 28)`). **Bounds** from $F$-tables: **$0.01 < P\text{-value} < 0.025$** (since $4.42$ lies between the critical values for $\alpha = 0.025$ and $\alpha = 0.01$ in the upper tail).

    3. **Conclusion.** $H_0$: $\mu_1 = \mu_2 = \mu_3 = \mu_4$. $H_1$: not all factor-level means are equal.

        Since $P\text{-value} < 0.05$, **reject $H_0$**. There is **significant evidence** at the 5% level that the factor-level means are **not** all equal.

        ANOVA does **not** say **which** means differ; use a multiple-comparison procedure (e.g. **Tukey HSD**) as a follow-up.

    ```python
    from scipy import stats

    F, dfn, dfd = 4.42, 3, 28
    print("P-value (upper tail):", stats.f.sf(F, dfn, dfd))
    ```
