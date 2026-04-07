# Tutorial – Session 10

## One-way ANOVA (Ross kap. 10.1–10.3)

Denne tutorial følger **Ross, kapitel 10**, afsnit **10.1** (introduktion), **10.2** ($F$-test og ANOVA-tabel) og **10.3** (parvise sammenligninger). Kun **ensidig** (one-way) ANOVA — ét faktor-layout med $k$ grupper.

**Notebook-version:** [Tutorial_10_notebook.ipynb](Tutorial_10_notebook.ipynb)

!!! info "Python-pakker"

    Koden her bruger **NumPy**, **pandas**, **SciPy** og **statsmodels**. SciPy følger ofte med Anaconda; **statsmodels** skal nogle gange installeres selv. Får I `ModuleNotFoundError: No module named 'statsmodels'`, kør i det miljø hvor Jupyter kører:

    ```bash
    pip install statsmodels
    ```

    (eller `conda install -c conda-forge statsmodels` i Conda.)

---

## 0. Pakker (valgfrit)

Kør cellen nedenfor **én gang**, hvis notebook'en skriver `No module named 'statsmodels'`. Den installerer i **samme miljø som jeres Jupyter-kernel** (som kan være forskelligt fra `python` i en vilkårlig terminal).


```python
%pip install statsmodels -q
```

---

## 1. Introduktion (Ross 10.1)

Vi har $k$ uafhængige grupper (fx $k$ behandlinger eller $k$ populationer). I gruppe $i$ observerer vi $n_i$ værdier $Y_{i1},\ldots,Y_{in_i}$.

**Spørgsmål:** Er der evidens for, at **gruppemiddelværdierne** ikke alle er ens?

Et naturligt estimat for middelværdien i gruppe $i$ er stikprøvegennemsnittet $\bar{Y}_i$. **ANOVA** (Analysis of Variance) tester hypotesen

$$H_0: \mu_1 = \mu_2 = \cdots = \mu_k$$

mod

$$H_1: \text{ikke alle } \mu_i \text{ er ens},$$

ved at sammenligne variation **mellem** grupper med variation **inden for** grupper. Navnet kommer af, at teststørrelsen bygger på **sumkvadrater** (variationskomponenter).

**Hvorfor ikke bare mange $t$-tests?** Ved at sammenligne alle par med $t$-test uden korrektion øger I risikoen for **type I-fejl** (falsk positiv). ANOVA giver ét samlet test på $\alpha$-niveau; **parvise tests** (afsnit 7) bruges **efter** en plan (fx Tukey), så multiple sammenligninger kontrolleres bedre.

---

## 2. $F$-test og ANOVA-tabel (Ross 10.2)

Lad $N = \sum_{i=1}^k n_i$ være det samlede antal observationer og $\bar{Y}_{\cdot\cdot}$ det **samlede** gennemsnit.

**Sumkvadrater** (notation som i mange lærebøger):

- **Total:** $\mathrm{SST} = \sum_{i,j} (Y_{ij} - \bar{Y}_{\cdot\cdot})^2$
- **Mellem grupper:** $\mathrm{SSB} = \sum_{i=1}^k n_i (\bar{Y}_{i\cdot} - \bar{Y}_{\cdot\cdot})^2$
- **Inden for grupper:** $\mathrm{SSW} = \sum_{i=1}^k \sum_{j=1}^{n_i} (Y_{ij} - \bar{Y}_{i\cdot})^2$

Det gælder **$\mathrm{SST} = \mathrm{SSB} + \mathrm{SSW}$**.

**Frihedsgrader:**

- Mellem: $k-1$
- Inden for: $N-k$
- Total: $N-1$

**Middelkvadrater:** $\mathrm{MSB} = \mathrm{SSB}/(k-1)$, $\mathrm{MSW} = \mathrm{SSW}/(N-k)$.

Under $H_0$ og standardantagelser (uafhængighed, normalitet inden for grupper, **ens varians** $\sigma^2$) gælder at teststørrelsen

$$F = \frac{\mathrm{MSB}}{\mathrm{MSW}}$$

er **$F$-fordelt** med $(k-1,\, N-k)$ frihedsgrader. Store værdier af $F$ taler imod $H_0$.

**Skøn over fælles varians:** $\mathrm{MSW}$ (også kaldet MSE) er et unbiased estimat for $\sigma^2$ under ens varians-antagelsen.

Nedenfor: **manuel beregning** til kontrol og forståelse — derefter de samme tal via biblioteker.


```python
import numpy as np

rng = np.random.default_rng(42)
# Tre grupper med lidt forskellige middelværdier (syntetisk eksempel)
g1 = rng.normal(10.0, 2.0, 12)
g2 = rng.normal(12.0, 2.0, 10)
g3 = rng.normal(10.5, 2.0, 11)

groups = [g1, g2, g3]
k = len(groups)
n_per = [len(g) for g in groups]
N = sum(n_per)

all_y = np.concatenate(groups)
grand_mean = all_y.mean()

SSB = sum(n * (g.mean() - grand_mean) ** 2 for g, n in zip(groups, n_per))
SSW = sum(((g - g.mean()) ** 2).sum() for g in groups)
SST = ((all_y - grand_mean) ** 2).sum()

df_between, df_within = k - 1, N - k
MSB = SSB / df_between
MSW = SSW / df_within
F_manual = MSB / MSW

print(f"SST={SST:.4f}, SSB={SSB:.4f}, SSW={SSW:.4f}")
print(f"F = {F_manual:.4f}, df = ({df_between}, {df_within})")
```

---

## 3. SciPy: `f_oneway`

Den hurtigste standardvej, når I allerede har **én array pr. gruppe**: `scipy.stats.f_oneway`.


```python
from scipy import stats

F_stat, p_value = stats.f_oneway(g1, g2, g3)
print(f"SciPy f_oneway: F={F_stat:.4f}, p={p_value:.4e}")
```

- Returnerer **$F$** og **$p$-værdi** for omnibus-testen.
- **Ingen** ANOVA-tabel eller effektstørrelser — kun testet.

---

## 4. Statsmodels: `ols` + `anova_lm` (typisk til pensum og rapporter)

I kan formulere modellen som **lineær model** med **dummy-variable** for faktoren. Med **sum-to-zero** eller **reference-kategori** (standard i `patsy`/`C(group)`) får I den samme $F$-test for faktoren.


```python
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.DataFrame(
    {
        "y": np.concatenate(groups),
        "grp": np.repeat(["A", "B", "C"], n_per),
    }
)

model = ols("y ~ C(grp)", data=df).fit()
anova_tbl = sm.stats.anova_lm(model, typ=2)
print(anova_tbl)
print(model.summary())
```

- **`anova_lm(..., typ=2)`:** for **ensidig** ANOVA med balanceret eller ubalanceret design er typ 2 (og ofte typ 1) passende til faktorens $F$-test.
- **`summary()`:** giver koefficienter (fx referencegruppe + effekter); fortolkning af enkeltkoefficienter er **ikke** det samme som parvise gruppeforskelle — brug Tukey til det.

---

## 5. Parvise sammenligninger (Ross 10.3)

Når $H_0$ forkastes (eller som planlagt **efter** ANOVA), vil I ofte vide **hvilke par** af middelværdier der adskiller sig. **Tukey HSD** (Honestly Significant Difference) kontrollerer **familievis** fejlrate for alle par under standardantagelser.

### 5.1 Statsmodels: `pairwise_tukeyhsd`


```python
from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey = pairwise_tukeyhsd(endog=df["y"], groups=df["grp"], alpha=0.05)
print(tukey)
```

### 5.2 SciPy (nyere versioner): `tukey_hsd`

Fra **SciPy 1.9+** findes `scipy.stats.tukey_hsd`, som tager grupperne som separate arrays:


```python
from scipy.stats import tukey_hsd

tukey_res = tukey_hsd(g1, g2, g3)
print(tukey_res)
```

Begge giver konfidensintervaller / p-værdier for parvise forskelle; læs dokumentationen for den SciPy-version I har installeret.

---

## 6. Antagelser (kort)

1. **Uafhængighed** — observationer er ikke parrede på tværs af grupper (i one-way layout).
2. **Normalitet** inden for hver gruppe — grov check med histogram/QQ pr. gruppe ved små $n_i$.
3. **Ens varians** ($\sigma^2$) — kan undersøges med fx **Levenes test** (`scipy.stats.levene`) som grov orientering; ved stærkt brud kan ANOVA være upålidelig eller I kan overveje transformation / robuste metoder (udover denne sessions pensum).


```python
from scipy import stats

lev_stat, lev_p = stats.levene(g1, g2, g3)
print(f"Levene: stat={lev_stat:.4f}, p={lev_p:.4f}")
```

---

## 7. Andre gængse Python-tilgange (overblik)

| Tilgang | Pakke / funktion | Typisk brug |
|--------|-------------------|-------------|
| Omnibus $F$ | `scipy.stats.f_oneway` | Hurtigt resultat, få afhængigheder |
| ANOVA-tabel + model | `statsmodels` `ols` + `anova_lm` | Rapportering, koefficienter, residualer |
| Tukey | `statsmodels.stats.multicomp.pairwise_tukeyhsd` | Parvise sammenligninger efter ANOVA |
| Tukey | `scipy.stats.tukey_hsd` | Alternativ, array-pr. gruppe |
| Kruskal–Wallis | `scipy.stats.kruskal` | **Ikke** ANOVA, men ikke-parametrisk analog ved mistanke om kraftige afvigelser fra normalitet |

**Pingouin** (`pip install pingouin`) bruges ofte i undervisning (`pingouin.anova`, `pairwise_tukey`); det er et ekstra lag oven på statsmodels/scipy — valgfrit hvis I vil have ensartet “stats-API”.

---

## 8. Kort arbejdsgang (typisk opgave)

1. Indlæs data: én kolonne med **respons**, én med **gruppe/faktor** (eller split i arrays).  
2. Beskrivende statistik og evt. plots (boksplot pr. gruppe).  
3. Tjek antagelser groft (normalitet inden for grupper, ens varians).  
4. Kør **one-way ANOVA** (`f_oneway` eller `ols` + `anova_lm`).  
5. Fortolk $F$ og $p$: forkast eller forkast ikke $H_0$ på valgt $\alpha$.  
6. Ved behov: **Tukey HSD** for at finde hvilke par der adskiller sig.  
7. Formuler **konklusion** i sprog, ikke kun tal.

---

## 9. Oversigt: begreber og Python

| Emne | Idé | Python (typisk) |
|------|-----|-------------------|
| Omnibus-test | $H_0$: alle $\mu_i$ ens | `scipy.stats.f_oneway` |
| ANOVA-tabel | SSB, SSW, MSB, MSW, $F$ | `ols("y ~ C(grp)")` + `sm.stats.anova_lm` |
| Parvise forskelle | Efter signifikant ANOVA | `pairwise_tukeyhsd` eller `tukey_hsd` |
| Ens varians (groft) | Levene | `scipy.stats.levene` |

Når øvelser til session 10 lægges ind, følger de samme konventioner som øvrige sessioner på kurset.
