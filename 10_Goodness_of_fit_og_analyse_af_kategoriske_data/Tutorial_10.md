# Tutorial – Session 10

## Goodness-of-fit og analyse af kategoriske data (Ross kap. 11.1–11.4)

Denne tutorial følger **Ross, kapitel 11**, afsnit **11.1** (introduktion), **11.2** (goodness-of-fit når alle parametre i $H_0$ er specificeret), **11.3** (goodness-of-fit når nogle parametre er uspecificeret og må estimeres fra data), og **11.4** (test for uafhængighed i kontingenstabeller).

Vi introducerer også en 5. testtype til rå kontinuerte data ved hjælp af `scipy.stats.goodness_of_fit`.

**Notebook-version:** [Tutorial_10_notebook.ipynb](Tutorial_10_notebook.ipynb)

---

## 1. Goodness-of-fit for en fast fordeling (fuldt specificeret)

Vi tester om observerede tællinger passer til en specifik fordeling, hvor alle parametre er kendte. Vi bruger Pearsons $\chi^2$-teststørrelse:

$$ \chi^2 = \sum \frac{(O_i - E_i)^2}{E_i} $$

Hvor $O_i$ er de observerede frekvenser og $E_i$ er de forventede frekvenser under $H_0$.
Frihedsgrader: $k - 1$, hvor $k$ er antallet af kategorier.

Vi bruger `scipy.stats.chisquare`.


```python
import numpy as np
from scipy import stats

# Eksempel: Markedsandele for 4 forskellige brands (A, B, C, D)
# Forventede markedsandele under H0 (f.eks. fra sidste år)
p_expected = np.array([0.50, 0.25, 0.15, 0.10])

# Observerede tællinger i en ny stikprøve (n = 400)
observed = np.array([210, 90, 65, 35])
n = observed.sum()

# Forventede tællinger
expected = n * p_expected

# Udfør Chi-i-anden test
chi2_stat, p_value = stats.chisquare(f_obs=observed, f_exp=expected)

print(f"Observerede: {observed}")
print(f"Forventede : {expected}")
print(f"Chi2-statistik: {chi2_stat:.4f}")
print(f"p-værdi       : {p_value:.4f}")
```

---

## 2. Goodness-of-fit for en fordeling med kendt parameter

Her tester vi om data følger en bestemt fordeling, f.eks. en Poisson-fordeling, hvor parameteren er givet på forhånd (ikke estimeret fra data). Frihedsgraderne er stadig $k - 1$.


```python
# Eksempel: Kunder der ankommer til en bank pr. time.
# Vi forventer en Poisson-fordeling med lambda = 3.5
# Antal kunder: 0, 1, 2, 3, 4, 5, 6, 7 eller flere
# Observerede timer (n = 100)
obs_hours = np.array([3, 12, 20, 25, 18, 12, 7, 3])
n_hours = obs_hours.sum()
k = len(obs_hours)

# Forventede sandsynligheder under Poisson(3.5)
lam = 3.5
p_poisson = np.array([stats.poisson.pmf(i, lam) for i in range(k)])

# Da den sidste kategori er "7 eller flere", samler vi resten af sandsynligheden her
p_poisson[-1] = 1 - p_poisson[:-1].sum()

exp_hours = n_hours * p_poisson

chi2_stat, p_value = stats.chisquare(f_obs=obs_hours, f_exp=exp_hours)

print(f"Observerede: {obs_hours}")
print(f"Forventede : {np.round(exp_hours, 2)}")
print(f"Chi2-statistik: {chi2_stat:.4f}")
print(f"p-værdi       : {p_value:.4f}")
```

---

## 3. Goodness-of-fit for en fordeling med ukendt parameter (estimeret fra data)

Hvis vi estimerer $m$ parametre fra data, mister vi yderligere $m$ frihedsgrader. De samlede frihedsgrader bliver $k - 1 - m$.
I `scipy.stats.chisquare` angives dette med parameteren `ddof` (Delta Degrees of Freedom), som sættes til $m$.


```python
# Eksempel: Vægten af æbler (Normalfordeling, hvor middelværdi og standardafvigelse estimeres)
# Antag vi har n=200 observationer, inddelt i 5 intervaller.
# Vi har estimeret mu = 150g og sigma = 20g fra data.
n_obs = 200
obs_counts = np.array([15, 45, 80, 45, 15])

# Intervaller: (-inf, 120], (120, 140], (140, 160], (160, 180], (180, inf)
mu_est = 150
sigma_est = 20

# Beregn forventede sandsynligheder for hvert interval
edges = [-np.inf, 120, 140, 160, 180, np.inf]
p_norm = np.zeros(5)
for i in range(5):
    p_norm[i] = stats.norm.cdf(edges[i+1], loc=mu_est, scale=sigma_est) - stats.norm.cdf(edges[i], loc=mu_est, scale=sigma_est)

exp_counts = n_obs * p_norm

# Vi estimerede 2 parametre (mu og sigma), så ddof = 2
chi2_stat, p_value = stats.chisquare(f_obs=obs_counts, f_exp=exp_counts, ddof=2)

print(f"Observerede: {obs_counts}")
print(f"Forventede : {np.round(exp_counts, 2)}")
print(f"Chi2-statistik: {chi2_stat:.4f}")
print(f"p-værdi (ddof=2): {p_value:.4f}")
```

---

## 4. Kontingenstabel-test for uafhængighed

Når vi har to kategoriske variable, kan vi opstille en kontingenstabel (krydstabel) og teste om de to variable er uafhængige.
Vi bruger `scipy.stats.chi2_contingency`, som automatisk beregner de forventede frekvenser og frihedsgraderne $(r-1)(c-1)$.


```python
# Eksempel: Sammenhæng mellem aldersgruppe og politisk præference
# Rækker: Ung, Mellem, Ældre
# Kolonner: Kandidat A, Kandidat B, Kandidat C
contingency_table = np.array([
    [45, 30, 25],
    [35, 50, 15],
    [20, 40, 40]
])

# Udfør test for uafhængighed
chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table, correction=False)

print(f"Chi2-statistik: {chi2_stat:.4f}")
print(f"p-værdi       : {p_value:.4f}")
print(f"Frihedsgrader : {dof}")
print("Forventede frekvenser:")
print(np.round(expected, 2))
```

---

## 5. Test for rå kontinuerte data (`stats.goodness_of_fit`)

Hvis vi har de rå kontinuerte data (ikke inddelt i intervaller/bins), kan vi bruge mere avancerede tests som f.eks. Anderson-Darling eller Kolmogorov-Smirnov.
`scipy.stats.goodness_of_fit` (introduceret i nyere versioner af SciPy) udfører en Monte Carlo-baseret goodness-of-fit test, som er meget stærk til rå data.


```python
# Eksempel: Test om 50 målte højder (i cm) er normalfordelte.
np.random.seed(42)
# Vi genererer 50 tilfældige højder fra en normalfordeling for eksemplets skyld
raw_data = stats.norm.rvs(loc=175, scale=10, size=50)

# Brug stats.goodness_of_fit til at teste om data er normalfordelt.
# Funktionen estimerer selv parametrene (loc og scale) fra data.
# Vi bruger Anderson-Darling (ad) statistikken.
res = stats.goodness_of_fit(stats.norm, raw_data, statistic="ad", random_state=42)

print(f"Test-statistik (Anderson-Darling): {res.statistic:.4f}")
print(f"p-værdi: {res.pvalue:.4f}")

if res.pvalue > 0.05:
    print("Vi kan ikke afvise H0: Data ser ud til at være normalfordelt.")
else:
    print("Vi afviser H0: Data er ikke normalfordelt.")
```
