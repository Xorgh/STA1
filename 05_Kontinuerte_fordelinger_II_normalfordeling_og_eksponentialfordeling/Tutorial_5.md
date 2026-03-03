# Tutorial – Session 5

## Kontinuerte fordelinger II: Normalfordeling og Eksponentialfordeling
### Teori, Python (SciPy) og WolframAlpha

I denne tutorial bygger vi videre på de kontinuerte grundbegreber (PDF og CDF) fra Session 4. Hvor vi sidst regnede på "tilfældige" funktioner ved at integrere med SymPy, skifter vi nu fokus til de to vigtigste og mest brugte **standardiserede kontinuerte fordelinger**: **Normalfordelingen** og **Eksponentialfordelingen**.

Vi kommer primært til at bruge biblioteket `scipy.stats` i Python, da det har indbyggede funktioner for alle disse standardfordelinger. SymPy kan stadig bruges til at integrere, men i praksis slår vi værdierne op.

Vi arbejder systematisk med:

1. **Normalfordelingen** – Gauss-kurven, som beskriver rigtig mange naturlige fænomener.
2. **Standardisering og Z-scores** – Hvordan vi transformerer en normalfordeling til standardnormalfordelingen $N(0,1)$ (og brugen af $\Phi$).
3. **Lineære transformationer** – Hvad der sker, når vi definerer en ny variabel som $Y = aX + b$.
4. **Betingede sandsynligheder** – At beregne $P(A|B)$ for kontinuerte variable.
5. **Eksponentialfordelingen & Hukommelsesløshed** – Modellering af levetider og ventetider.
6. **Relationen mellem Poisson og Eksponential** – Overgangen fra "antal hændelser pr. tid" til "tid mellem hændelser".

**Notebook-version:** [Tutorial_5_notebook.ipynb](Tutorial_5_notebook.ipynb)

---

## 1. Normalfordelingen

### 1.1 Teori

Normalfordelingen (eller Gauss-fordelingen) er den berømte klokkeformede kurve. Vi skriver det som $X \sim N(\mu, \sigma^2)$, hvor:

- $\mu$ (my) er **middelværdien** (hvor kurvens top er placeret).
- $\sigma^2$ (sigma i anden) er **variansen** (hvor bred kurven er).
- $\sigma$ er den **standardafvigelsen** (kvadratroden af variansen).

### 1.2 Python (SciPy)

Når vi bruger `scipy.stats.norm`, skal vi bruge parametrene `loc` ($\mu$) og `scale` ($\sigma$). 

**Kæmpe faldgrube:** Man får ofte opgivet fordelingen som $N(\mu, \sigma^2)$, altså med *variansen*. Python forventer *standardafvigelsen* $\sigma$. Husk at tage kvadratroden!

Lad os sige, vi har $X \sim N(5, 16)$. Det betyder $\mu = 5$ og varians $= 16$, så $\sigma = \sqrt{16} = 4$.

```python
from scipy.stats import norm

mu = 5
varians = 16
sigma = varians**0.5 # Giver 4.0

# P(X > 0) 
# I python er CDF = P(X <= x). Så P(X > 0) = 1 - P(X <= 0)
p_storre_end_0 = 1 - norm.cdf(0, loc=mu, scale=sigma)
print(f"P(X > 0) = {p_storre_end_0:.4f}")

# P(2 < X < 10) = CDF(10) - CDF(2)
p_mellem = norm.cdf(10, loc=mu, scale=sigma) - norm.cdf(2, loc=mu, scale=sigma)
print(f"P(2 < X < 10) = {p_mellem:.4f}")
```

### 1.3 WolframAlpha

I WolframAlpha definerer vi distributionen. Ligesom Python forventer WolframAlpha oftest `NormalDistribution[mu, sigma]`.
For $P(X>0)$:

```
P(X>0) NormalDistribution(5, 4)
```

For $P(2 < X < 10)$:

```
P(2 < X < 10) for X~NormalDistribution(5, 4)
```

---

## 2. Standardnormalfordelingen

### 2.1 Teori

**Standardnormalfordelingen** er en særlig normalfordeling, hvor $\mu=0$ og $\sigma^2=1$, altså $Z \sim N(0,1)$. Dens fordelingsfunktion (CDF) er så vigtig, at den har sit eget symbol: $\Phi(z)$ (store phi).

*Bemærk: Da arealet under hele kurven er 1, og den er symmetrisk, gælder det at $P(Z > z) = 1 - \Phi(z)$, og at $\Phi(-z) = 1 - \Phi(z)$.*

### 2.2 Python (SciPy)

I Python bruger vi `scipy.stats.norm`. Når vi ikke angiver `loc` og `scale`, antager funktionen automatisk, at vi arbejder med standardnormalfordelingen ($\mu = 0, \sigma = 1$).

```python
from scipy.stats import norm

# P(Z <= 1.96)
p_z_mindre = norm.cdf(1.96)
print(f"P(Z <= 1.96) = {p_z_mindre:.4f}")

# P(Z > 1.96)
p_z_storre = 1 - norm.cdf(1.96)
print(f"P(Z > 1.96) = {p_z_storre:.4f}")

# P(-1.96 < Z < 1.96)
p_z_mellem = norm.cdf(1.96) - norm.cdf(-1.96)
print(f"P(-1.96 < Z < 1.96) = {p_z_mellem:.4f}")
```

### 2.3 WolframAlpha

I WolframAlpha kan vi skrive `StandardNormalDistribution` eller blot `NormalDistribution(0,1)`.

For at finde arealet under kurven for $Z \leq 1.96$:

```
P(Z < 1.96) for Z~StandardNormalDistribution
```
Eller

```
P(X < 1.96) StandardNormalDistribution
```

Eller

```
P(Z < 1.96) NormalDistribution(0,1)
```

For arealet i midten:

```
P(-1.96 < Z < 1.96) for Z~StandardNormalDistribution
```
Eller  

```
P(-1.96 < X < 1.96) StandardNormalDistribution
```

Eller

```
P(-1.96 < Z < 1.96) NormalDistribution(0,1)
```

---

## 3. Standardisering (Z-scores)

### 3.1 Teori

Når vi har en variabel $X$ fra en vilkårlig normalfordeling $N(\mu, \sigma^2)$, og vi gerne vil vide, hvor usædvanlig en bestemt observation $x$ er, **standardiserer** vi den.

Vi omregner $x$ til en **Z-score**, som fortæller os, *hvor mange standardafvigelser $x$ ligger fra middelværdien*:

$$Z = \frac{x - \mu}{\sigma}$$

En Z-score på 0 betyder, at observationen ligger præcis på middelværdien. En Z-score på 2 betyder, at observationen ligger 2 standardafvigelser *over* middelværdien.

Dette giver os mulighed for at regne enhver normalfordeling om til standardnormalfordelingen:

$$P(X \leq x) = P\left(Z \leq \frac{x - \mu}{\sigma}\right) = \Phi\left(\frac{x - \mu}{\sigma}\right)$$

### 3.2 Python (SciPy)

I Python kan vi enten udregne Z-scoren manuelt, eller vi kan bruge funktionen `zscore` fra `scipy.stats`, hvis vi har et helt dataset (array) af observationer.

```python
import numpy as np
from scipy.stats import zscore

# 1. Manuel udregning for en enkelt observation
mu = 50
sigma = 10
x = 75

z = (x - mu) / sigma
print(f"Observationen {x} har en Z-score på {z:.2f}")

# 2. Udregning for et helt array (dataset) af observationer
data = np.array([30, 40, 50, 60, 70])
z_scores = zscore(data)
print(f"Z-scores for data: {z_scores}")
```

### 3.3 WolframAlpha

WolframAlpha har ikke en indbygget funktion for at udregne Z-scoren, men vi kan bare indsætte formlen direkte for at udregne Z-scoren:

```
(75 - 50) / 10
```

Hvis vi vil beregne en sandsynlighed via standardisering, kan vi skrive:

```
P(Z < (75 - 50) / 10) for Z~StandardNormalDistribution
```

eller

```
P(X < (75 - 50) / 10) for StandardNormalDistribution
```

---

## 4. Eksponentialfordelingen og Hukommelsesløshed

### 4.1 Teori

Eksponentialfordelingen bruges oftest til at modellere **levetider** (hvor lang tid der går før en komponent går i stykker) eller **ventetider** (tid mellem ankomster).

Vi skriver $T \sim \text{Exp}(\lambda)$, hvor $\lambda$ er *rate-parameteren* (hændelser pr. tidsenhed).

| Egenskab | Formel |
| :--- | :--- |
| **PDF (Tæthedsfunktion)** | $f(t) = \lambda e^{-\lambda t}$ (for $t \geq 0$) |
| **CDF (Fordelingsfunktion)** | $F(t) = P(T \leq t) = 1 - e^{-\lambda t}$ |
| **Middelværdi (Forventet ventetid)** | $E[T] = \frac{1}{\lambda}$ |
| **Varians** | $Var(T) = \frac{1}{\lambda^2}$ |

**Hukommelsesløshed (Memorylessness):**
Eksponentialfordelingen er den *eneste* kontinuerte fordeling, der er "hukommelsesløs". Det betyder, at den forventede resterende levetid ikke afhænger af, hvor længe vi allerede har ventet. Maskinen "bliver ikke ældre".
Matematisk:

$$P(T > s + t \mid T > s) = P(T > t)$$

*Eksempel: Hvis sandsynligheden for at en pære holder 10 timer er 40%. Hvis pæren allerede har lyst i 50 timer, er sandsynligheden for, at den holder 10 timer mere, stadig 40%.*

Dette er stærkt kontraintuitivt. I virkeligheden forventer vi normalt, at noget der har været i brug længe, enten er tættere på at gå i stykker (slid) — eller at det har bevist sin robusthed. Begge intuitioner indebærer, at fortiden påvirker fremtiden.

Eksponentialfordelingen siger det modsatte: fortiden er fuldstændig irrelevant.

For mange fysiske systemer — som fx pærer eller mekaniske komponenter — er eksponentialfordelingen ikke en særlig realistisk model over hele levetiden.  

I praksis har mange systemer en fejlrate, der ændrer sig over tid (fx den såkaldte *bathtub curve* med begyndelsesfejl og slid mod slutningen).  

Eksponentialfordelingen antager derimod:

- Konstant fejlrate  
- Ingen aldring  
- Ingen slitage  
- Ingen “læring”  

Derfor er den en idealiseret model.

Eksponentialfordelingen er meget velegnet i situationer, hvor hændelser opstår med konstant intensitet og uden “hukommelse”:

- **Radioaktivt henfald:**  
    Et atom “ældes” ikke. Sandsynligheden for at det henfalder i det næste minut er den samme, uanset hvor længe det allerede har eksisteret.

- **Tid mellem hændelser i en Poisson-proces:**
    
    - Tid mellem telefonopkald til en supportlinje  
    - Tid mellem kunder i en butik (ved tilfældige ankomster)  
    - Tid mellem netværkspakker i en idealiseret trafikmodel  

- **Systemer hvor fejl skyldes pludselige, tilfældige påvirkninger snarere end gradvis slitage.**

Eksponentialfordelingen er derfor ikke en “levetidsmodel” i generel forstand — den er en model for processer med konstant hazard rate.

Det er netop hukommelsesløsheden, der gør den matematisk elegant og central i sandsynlighedsteori — men også det, der gør den fysisk begrænset i mange realistiske anvendelser.

### 4.2 Python (SciPy)

I SciPy bruger vi `expon`. 
**Kæmpe faldgrube nr. 2:** SciPy definerer ikke parameteren som raten $\lambda$. Den definerer den ud fra dens `scale`, og for eksponentialfordelingen er `scale` lig med middelværdien, altså $\frac{1}{\lambda}$.

```python
from scipy.stats import expon

# Antag at der ankommer 25 requests i sekundet: lambda = 25
lam = 25
middel_ventetid = 1 / lam # scale-parameteren

# Hvad er sandsynligheden for at der går OVER 0.1 sekund mellem to requests? P(T > 0.1)
p_over_0_1 = 1 - expon.cdf(0.1, scale=middel_ventetid)
print(f"P(T > 0.1) = {p_over_0_1:.4f}")

# (Da CDF er 1 - e^(-lambda*t), kan vi også tjekke manuelt med math.exp)
import math
p_manuel = math.exp(-25 * 0.1)
print(f"Manuel P(T > 0.1) = {p_manuel:.4f}")
```

### 4.3 WolframAlpha

WolframAlpha tager direkte mod raten $\lambda$ ved at bruge `ExponentialDistribution[lambda]`:
```
P(T > 0.1) ExponentialDistribution(25)
```

---

## 5. Sammenhængen mellem Poisson og Eksponential

### 5.1 Teori

Der er en dyb matematisk sammenhæng mellem den diskrete Poisson-fordeling (Session 3) og den kontinuerte Eksponentialfordeling. De beskriver samme fænomen, blot fra to forskellige vinkler:

- **Poisson ($X$):** Tæller *antallet* af hændelser i et fast tidsrum.
- **Eksponential ($T$):** Måler *tiden* mellem to på hinanden følgende hændelser.

**Reglen er:**
Hvis hændelser sker ifølge en Poisson-proces med raten $\lambda$ pr. tidsenhed, så er tiden mellem to hændelser eksponentialfordelt med præcis samme rate $\lambda$.

**Skalering af tiden:**
Raten $\lambda$ gælder for én specifik tidsenhed (f.eks. 1 sekund). Hvis vi betragter et interval på $t$ enheder (f.eks. 0.01 sekund), er det forventede antal hændelser i intervallet $\mu = \lambda \cdot t$.

**Sammenkobling af de to verdener (Eksempel fra øvelse 1):**
Raten er $\lambda = 25$ requests/sekund. Vi ser på et interval på 10 millisekunder ($t = 0.01$ sekund).
Raten for 10 ms-intervallet bliver: $\mu = 25 \cdot 0.01 = 0.25$ requests.

- **Spørgsmål type A (Poisson):** Hvad er $P(\text{0 requests på 10 ms})$?

    $$P(X_{10ms} = 0) = \frac{e^{-0.25} \cdot 0.25^0}{0!} = e^{-0.25}$$

- **Spørgsmål type B (Eksponential):** Hvad er $P(\text{tiden til næste request er over 10 ms})$?

    $$P(T > 0.01) = e^{-\lambda \cdot 0.01} = e^{-25 \cdot 0.01} = e^{-0.25}$$

Begge spørgsmål spørger i virkeligheden om det samme rent logisk! (Hvis der er mere end 10 ms mellem requests, så er der kommet præcis 0 requests indenfor de første 10 ms).

### 5.2 Python

Her ser vi, at de to tilgange giver nøjagtig samme resultat:

```python
from scipy.stats import poisson, expon

lam_sekund = 25
t = 0.01 # 10 ms i sekunder

# Poisson-tilgang: lambda justeres til tidsintervallet
lam_interval = lam_sekund * t 
p_0_requests = poisson.pmf(0, mu=lam_interval)
print(f"Poisson: P(0 requests på 10 ms) = {p_0_requests:.4f}")

# Eksponential-tilgang: Vi udregner direkte fra ventetidsfordelingen (rate forholder sig til 1 sekund)
p_vent_mere_end_10ms = 1 - expon.cdf(t, scale=1/lam_sekund)
print(f"Eksponential: P(T > 0.01 sekunder) = {p_vent_mere_end_10ms:.4f}")
```

---

## 6. Opsummering – Hvad du nu skal kunne

Efter denne tutorial og session kan du:

- **Beregne sandsynligheder for normalfordelte variabler** ved hjælp af `scipy.stats.norm` (eller $\Phi$ symbolsk) og huske at sætte `scale` lig med *standardafvigelsen*, ikke variansen.
- **Standardisere til Z-scores** ($Z = \frac{X-\mu}{\sigma}$) for at relatere vilkårlige observationer til Standardnormalfordelingen $N(0,1)$.
- **Forstå Eksponentialfordelingen**, dens parameter $\lambda$ og dens afgørende egenskab: hukommelsesløshed.
- **Navigere problemfrit mellem Poisson og Eksponential**, alt efter om en opgave spørger til "antal på en tidsramme" eller "tid mellem to hændelser", og huske at skalere raten i forhold til det oplyste tidsvindue.
```