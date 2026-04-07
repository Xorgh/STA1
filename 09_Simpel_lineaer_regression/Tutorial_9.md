# Tutorial – Session 9

## Simpel lineær regression (Ross kap. 9)

Denne tutorial følger **Ross, kapitel 9**, afsnit **9.1**–**9.6**: introduktion, mindste kvadraters estimation, fordelinger af estimatore, inferens om koefficienterne, $R^2$ og korrelation, samt residualanalyse.

**Notebook-version:** [Tutorial_9_notebook.ipynb](Tutorial_9_notebook.ipynb)

**Udledninger og formler** (hældning, skæring, $r$, $r^2$, sumkvadrater): se også [Calculating_metrics.md](Calculating_metrics.md) (supplerende reference på engelsk med samme notation som i mange opgaver).

!!! info "Python-pakker"

    Tutorialen bruger **NumPy**, **pandas**, **SciPy**, **matplotlib**, **statsmodels** og (i afsnittet om andre biblioteker) **scikit-learn**. SciPy og matplotlib følger ofte med Anaconda; **statsmodels** og **scikit-learn** skal nogle gange installeres selv. Får I `ModuleNotFoundError`, kør i det miljø hvor Jupyter kører:

    ```bash
    pip install statsmodels scikit-learn
    ```

    (eller `conda install -c conda-forge statsmodels scikit-learn` i Conda.) Brug evt. **celle 0** nedenfor — den installerer i **samme kernel** som notebook'en.

---

## 0. Pakker (valgfrit)

Kør cellen nedenfor **én gang**, hvis I mangler `statsmodels` eller `sklearn` (fx `No module named 'statsmodels'`). Den installerer i **samme miljø som jeres Jupyter-kernel**.


```python
%pip install statsmodels scikit-learn -q
```

---

## 1. Introduktion (Ross 9.1)

Vi antager modellen

$$Y = \beta_0 + \beta_1 x + \varepsilon,$$

hvor $\varepsilon$ er tilfældig fejl (typisk $E[\varepsilon]=0$, konstant spredning, uafhængige observationer). Målet er at **estimere** $\beta_0$ (skæring) og $\beta_1$ (hældning) ud fra data $(x_i, y_i)$, $i=1,\ldots,n$.

---

## 2. Mindste kvadraters estimater (Ross 9.2)

Fittede værdier $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ vælges så **residualkvadratsummen** $SSE = \sum_i (y_i - \hat{y}_i)^2$ minimeres. Det giver

$$\hat{\beta}_1 = \frac{S_{xy}}{S_{xx}}, \qquad \hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x},$$

med $S_{xx} = \sum_i (x_i-\bar{x})^2$, $S_{xy} = \sum_i (x_i-\bar{x})(y_i-\bar{y})$ — eller ækvivalente formler med $\sum x_i y_i$, $\sum x_i^2$ (se [Calculating_metrics.md](Calculating_metrics.md)).

**Øvelse 1** i sessionen: indsæt $n$, $\bar{x}$, $\bar{y}$, $\sum x_i^2$, $\sum x_i y_i$ i formlerne (ingen rå datapunkter).


```python
import numpy as np

n, xbar, ybar = 12, 4.0, 12.0
sum_x2, sum_xy = 232.0, 318.0
sum_x = n * xbar
sum_y = n * ybar
b1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
b0 = ybar - b1 * xbar
print(f"b1_hat = {b1:.4f}, b0_hat = {b0:.4f}")
```

---

## 3. Fordeling af estimatore (Ross 9.3, kort)

Under normalitetsantagelse for fejlleddet gælder at $\hat{\beta}_1$ og $\hat{\beta}_0$ er normalfordelte omkring de sande værdier. Variansen $\sigma^2$ estimeres med **middelkvadratfejlen**

$$\hat{\sigma}^2 = \frac{SSE}{n-2} = MSE,$$

med $n-2$ frihedsgrader i simpel linear regression.

---

## 4. Statistisk inferens om $\beta_0$ og $\beta_1$ (Ross 9.4)

- **$t$-test** for $H_0: \beta_1 = 0$ (ingen lineær sammenhæng): $t = \hat{\beta}_1 / \mathrm{SE}(\hat{\beta}_1)$ med $n-2$ frihedsgrader.
- **Konfidensintervaller** for $\beta_1$ (og $\beta_0$) fås med $t$-fraktiler og standardfejl fra den samme model.

I Python giver **statsmodels** `OLS` typisk de samme tal som i mange eksamenssvar (koefficienter, $t$, $p$, CI i `.summary()`).


```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Eksempel: syntetiske data (erstat med jeres Excel-kolonner)
rng = np.random.default_rng(0)
x = rng.uniform(0, 10, 40)
y = 2.5 + 1.3 * x + rng.normal(0, 1.5, 40)

X = sm.add_constant(x)
model = sm.OLS(y, X).fit()
print(model.summary(alpha=0.05))
```

**Bemærk:** I opgavesvar med `sm.OLS` er **figurerne** (`src/ex8_*.png`, `ex11_*.png` osv.) genereret med den tilgang. Hvis I kun bruger `scipy.stats.linregress`, kan $p$-værdier og CI **afvige** i detaljer — til eksamenslayout: hold jer til én metode pr. opgave.

Alternativ (kompakt, uden statsmodels):


```python
from scipy import stats

res = stats.linregress(x, y)
print(f"slope={res.slope:.4f}, intercept={res.intercept:.4f}, r={res.rvalue:.4f}, p={res.pvalue:.4e}")
```

---

## 5. Bestemmelseskoefficient og korrelation (Ross 9.5)

- **Pearson $r$** måler lineær korrelation mellem $x$ og $y$.
- **$R^2$** (bestemmelseskoefficient) i simpel regression er $r^2$: andel af variation i $y$ forklaret af den lineære model.


```python
from scipy import stats

r, p = stats.pearsonr(x, y)
print(f"r = {r:.6f}, r^2 = {r**2:.6f}")
# I statsmodels: model.rsquared
```

---

## 6. Residualanalyse (Ross 9.6)

Residualer $e_i = y_i - \hat{y}_i$ bruges til at **vurdere modelantagelser**:

- **Plot:** $e_i$ mod $\hat{y}_i$ eller mod $x_i$ — mønstre (kurve, kegleform) tyder på brud mod linearitet eller konstant varians.
- **QQ-plot** af residualer: grov check af normalitet (som i Tutorial 7–8).


```python
from scipy.stats import probplot

fit = sm.OLS(y, X).fit()
resid = fit.resid
fig, ax = plt.subplots()
ax.scatter(fit.fittedvalues, resid, alpha=0.7)
ax.axhline(0, color="k", ls="--")
ax.set_xlabel("Fitted værdi")
ax.set_ylabel("Residual")
plt.show()

fig, ax = plt.subplots()
probplot(resid, dist="norm", plot=ax)
ax.set_title("QQ-plot af residualer")
plt.show()
```

---

## 7. Python-biblioteker til lineær regression (overblik)

I praksis findes der mange måder at lave **simpel lineær regression** i Python. Her er de vigtigste, grupperet efter bibliotek og typisk brug — med korte fordele og begrænsninger.

### 7.1 SciPy

**`scipy.stats.linregress`** — én forklarende variabel (simpel linear regression).

- Returnerer blandt andet hældning, skæring, $r$, $p$-værdi for hældningen og standardfejl.
- Meget letvægt; fint til hurtige resultater og til at matche “klassisk” fortolkning af $r$ og $p$ for hældningen.

**`scipy.optimize.curve_fit`** — generel **kurvetilpasning** (kan være lineær, men også eksponentialer, logistiske kurver osv.).

- Fleksibel til ikke-lineære modeller; lineær model er ofte **overkill**.
- Giver **ikke** det samme som en fuld regressionsdiagnostik (ingen standard `summary` med alle CI osv. som i statsmodels).


```python
from scipy.optimize import curve_fit

def linear(x, a, b):
    return a * x + b

popt, pcov = curve_fit(linear, x, y)
a_hat, b_hat = popt  # hældning, skæring (rækkefølge som i funktionen)
```

### 7.2 Statsmodels (mest “statistisk”)

**`statsmodels.api.OLS`** — klassisk **OLS** med designmatrix (`sm.add_constant` til skæring).

- Fuld statistisk output: $p$-værdier, konfidensintervaller, $R^2$, justeret $R^2$, $F$-test m.m.
- Det I typisk vil citere i en **statistik-/eksamensopgave** med inferens.

**`statsmodels.formula.api.ols`** — samme model, men med **R-lignende formel** (`"y ~ x"`), praktisk med `DataFrame` og mange kolonner.


```python
import statsmodels.formula.api as smf
import pandas as pd

df_ex = pd.DataFrame({"y": y, "x": x})
m_formula = smf.ols("y ~ x", data=df_ex).fit()
print(m_formula.summary())
```

### 7.3 Scikit-learn (maskinlæringsstil)

**`sklearn.linear_model.LinearRegression`** — meget brugt i **ML**-pipelines.

- Hurtig til ren **prediction** og preprocessing (`Pipeline`).
- **Ingen** $p$-værdier eller klassisk inferens “out of the box” — fokus er estimation og generalisering, ikke hypotesetest i samme forstand som i pensum.


```python
from sklearn.linear_model import LinearRegression

X_col = x.reshape(-1, 1)
reg = LinearRegression().fit(X_col, y)
print(reg.coef_, reg.intercept_)
```

### 7.4 NumPy (“manuel” MK)

**`numpy.polyfit(x, y, 1)`** — polynomium af grad 1 = lineær tilpasning.

- Hurtig og udbredt; returnerer koefficienter **højeste grad først** ($\hat{\beta}_1$, så $\hat{\beta}_0$).
- **Ingen** standardfejl eller $p$-værdier med i kaldet.

**`numpy.linalg.lstsq`** — rå **mindste kvadraters** løsning på matrixform $X\beta \approx y$.

- Meget **pædagogisk** til at se sammenhængen med lineær algebra.
- Ikke en “færdig regressionspakke” med diagnostik — men den **numeriske** MK-løsning er den samme idé som OLS.


```python
# polyfit: [hældning, skæring]
b1_pf, b0_pf = np.polyfit(x, y, 1)

# lstsq: søjler [konstant, x]
X_mat = np.column_stack([np.ones_like(x), x])
coef_lstsq, residuals, rank, s = np.linalg.lstsq(X_mat, y, rcond=None)
b0_ls, b1_ls = coef_lstsq
```

### 7.5 Ofte brugt i praksis (kort liste)

Mange vælger én af disse:

1. **`statsmodels.formula.api.ols`** — ofte bedst til **undervisning og inferens** med formler og `summary`.
2. **`statsmodels.api.OLS`** — samme statistik, matrix-/array-tilgang.
3. **`scipy.stats.linregress`** — **simplest** ved én $x$.
4. **`sklearn.linear_model.LinearRegression`** — **ML** og produktion uden fokus på $p$-værdier.
5. **`numpy.polyfit`** — **hurtig** tilpasning uden ekstra afhængigheder.

### 7.6 Anbefaling til jeres kursus

- Til **statistik / inferens / eksamen** (som i denne session): prioriter **statsmodels** (`ols` eller `OLS`).
- Til **hurtig simpel regression** på én $x$: **`scipy.stats.linregress`** er helt fin.
- Til **maskinlæring** og ren forudsigelse: **sklearn** `LinearRegression`.

Brug **én hovedmetode pr. opgave**, så tal og fortolkning (fx $p$-værdier og CI) hænger sammen.

---

## 8. Kort arbejdsgang i Python (typisk eksamensopgave)

1. `pd.read_excel(...)` — tjek kolonnenavne og outliers.  
2. Scatterplot + eventuel fjernelse af åbenlyse outliers (begrund).  
3. `sm.add_constant`, `sm.OLS(y, X).fit()` — læs `coef`, `std err`, `t`, `P>|t|`, `95% CI`.  
4. `model.rsquared`, `pearsonr` — fortolk $R^2$ og $r$.  
5. Residualplots + QQ — diskuter antagelser og modelkvalitet.  
6. **Forudsigelse:** $\hat{y}(x_0) = \hat{\beta}_0 + \hat{\beta}_1 x_0$; prediktionsintervaller findes i statsmodels via `get_prediction`.

---

## 9. Oversigt: begreber og Python

| Emne | Idé | Python (typisk) |
|------|-----|------------------|
| MK-estimat $\hat{\beta}_1$, $\hat{\beta}_0$ | Minimer $SSE$ | Manuel formler; `np.polyfit` (grad 1); `stats.linregress`; `sm.OLS` |
| Inferens på $\beta_1$ | $t$-test, CI | `sm.OLS().summary()` eller `linregress` ($p$ for hældning) |
| $r$, $R^2$ | Korrelation, forklaret variation | `pearsonr`; `model.rsquared` |
| Residualer | Modelkontrol | `fit.resid`, scatter, `probplot` |

Øvelsesopgaverne i session 9 er fire regressionssæt: MK med summeringer (**øvelse 1**), **Smoking and Cancer**, **Salary.xlsx** og **CPU_order_lines.xlsx** (**øvelse 4**); detaljer står i opgaveteksterne og i jeres svarfiler med figurer under `src/`.
