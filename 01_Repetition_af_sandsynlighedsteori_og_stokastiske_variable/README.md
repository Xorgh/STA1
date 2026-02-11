---
tags:
    - Sandsynlighedsteori
    - Stokastiske variable
    - Deskriptiv statistik
    - Normalfordeling
    - Gennemsnit
    - Median
    - IQR
    - Standardafvigelse
    - Varians
---
<h1 align="center">Repetition af sandsynlighedsteori og stokastiske variable</h1>

## Sessionsmateriale:

Ross: Kapitel 1-3. Bemærk, kapitel 2-3 er repetition af tidligere stof, mens kapitel 1 introducerer nye statistiske begreber.

<p align="left">

  <a href="Tutorial_1_notebook/">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python introduktion" width="100" />
    <br>
    <strong>Se Tutorial 1: Python, sandsynlighedsregning og statistik</strong>
  </a>
</p>

[Download tutorial som notebook (.ipynb)](https://raw.githubusercontent.com/RBrooksDK/STA_26/main/01_Repetition_af_sandsynlighedsteori_og_stokastiske_variable/Tutorial_1_notebook.ipynb)

[Sessionnoter]()

[Sessionsmateriale]()

---

## Sessionbeskrivelse

I denne session etablerer vi det fælles faglige fundament for resten af kurset. Sessionen fungerer som en samlet repetition af centrale begreber fra sandsynlighedsteori og statistik, som I tidligere har arbejdet med, men som nu sættes ind i en tydelig software- og dataanalytisk kontekst. Vi starter med at placere statistik som disciplin og diskutere forskellen mellem beskrivende statistik og statistisk inferens, herunder hvorfor statistik er et centralt værktøj i analyse og beslutningstagning baseret på data.

Herefter genopfrisker vi grundlæggende sandsynlighedsbegreber såsom udfaldsrum, hændelser og sandsynlighedsregler. Fokus er på forståelse og anvendelse frem for formelle beviser. Vi introducerer stokastiske variable som bindeled mellem sandsynlighed og data og arbejder med forventningsværdi og varians som mål for henholdsvis central tendens og spredning. Gennem simple eksempler og simulationer vises, hvordan disse begreber optræder i praksis, og hvordan de danner grundlag for den statistiske analyse, der arbejdes videre med i resten af kurset.

### Centrale begreber

- Statistik som disciplin og anvendelsesområde  
- Beskrivende statistik og statistisk inferens  
- Sandsynlighedsrum, hændelser og sandsynlighedsregler  
- Stokastiske variable  
- Forventningsværdi og varians  
- Sammenhængen mellem sandsynlighed, data og analyse  

!!! tip "Læringsmål"

    - Forstå statistikens rolle i softwareteknologiske og dataanalytiske problemstillinger.
    - Kunne redegøre for grundlæggende sandsynlighedsbegreber og deres fortolkning.
    - Forstå og anvende begrebet stokastisk variabel.
    - Kunne beregne og fortolke forventningsværdi og varians.
    - Kunne skelne mellem beskrivende statistik og statistisk inferens.
    - Opnå et fælles begrebsapparat og en fælles faglig referenceramme for resten af kurset.

## Øvelser

<!--
Indsæt bogreferencer og opgavelister her.
-->
<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

#### Øvelse 1
An election will be held next week and, by polling a sample of the voting population, we are trying to predict whether the Republican or Democratic candidate will prevail. Which of the following methods of selection is likely to yield a representative sample?

1. Poll all people of voting age attending a college basketball game.
2. Poll all people of voting age leaving a fancy midtown restaurant.
3. Obtain a copy of the voter registration list, randomly choose 100 names, and question them.
4. Use the results of a television call-in poll, in which the station asked its listeners to call in and name their choice.
5. Choose names from the telephone directory and call these people.

??? answer "&nbsp;"
    Method c is probably best, with e being the second best.

#### Øvelse 2
The approach used in Problem 1(e) led to a disastrous prediction in the 1936 presidential election, in which Franklin Roosevelt defeated Alfred Landon by a landslide. A Landon victory had been predicted by the *Literary Digest*. The magazine based its prediction on the preferences of a
sample of voters chosen from lists of automobile and telephone owners.

1. Why do you think the *Literary Digest's* prediction was so far off?
2. Has anything changed between 1936 and now that would make you believe that the approach used by the *Literary Digest* would work better today?

??? answer "&nbsp;"
     In 1936 only upper middle class and rich people had telephones. Almost all voters have telephones today.

#### Øvelse 3 (MSE Reeksamen 2025, Del 2)
The following dataset represents the final exam scores of 30 students:

```
data = [42, 55, 58, 60, 62, 65, 66, 68, 70, 70, 71, 72, 73, 74, 75, 75, 76, 77, 78, 80, 80, 81, 82, 84, 85, 88, 90, 92, 95, 98]
```

Use Python and the `numpy` library to calculate the following metrics.  
*Note: When calculating Variance and Standard Deviation, ensure you calculate the sample statistics.*

1. Compute the range of the scores.  

2. Calculate the mean, median, sample variance, and sample standard deviation.  

3. Find the 20th percentile ($P_{20}$), the 80th percentile ($P_{80}$), and the Interquartile Range (IQR).  

4. Find the lower and upper bounds for mild outliers.  

5. Empirical Rule Check: Calculate the proportion of students falling within 1 and 2 standard deviations of the mean.  

6. The grade 12 is given at 90 or more points. What proportion of students did not receive a 12?  

State your answers as decimals rounded to 2 decimal places. Do not state any answers as percentages.  

You must upload the code for this assignment and all other assignments in part 2 in **one single Jupyter Notebook**.

??? answer "&nbsp;"
    1. Range: 98 - 42 = 56.00
    2. Mean: 74.73, Median: 75.00, Sample Variance: 152.48, Sample Standard Deviation: 12.35
    3. ($P_{20} = 65.8$), ($P_{80} = 84.20$), IQR = 13.25
    4. Lower: 48.625, Upper: 101.625
    5. Within 1: 0.67, Within 2: 0.97
    6. Not 12: 0.8667

#### Øvelse 4 (Tilpasset efter MSE eeksamen 2025, Del 1)
​
A large corporation conducted a sustainability survey to determine the primary mode of transportation used by employees to get to work. The modes of transport were categorized into three groups: Private Vehicle ('Car'), Public Transit ('Transit'), and Active Transport ('Active' - walking or cycling). The employees surveyed came from four different departments: Sales, IT, Human Resources (HR), and Operations. A total of 650 employees participated in the survey. The Operations department is the largest, with the same number of employees as the Sales department. 100 employees work in HR. A total of 280 employees commute by Car, and of these, only 20 form part of the HR department. 80 of the 150 employees working in IT use Public Transit. Among the employees using Active transport, 40 are from Sales and 60 are from Operations. In total, 220 employees use Public Transit. There are exactly half as many IT employees using Active transport as there are Operations employees using Active transport. Finally, there are 80 more Sales employees who commute by Car than there are Operations employees who commute by Car.

Based on the above information, create a contingency table using a Pandas DataFrame. Please place the Departments on the horizontal axis. Remember that a contingency table contains frequencies and not probabilities. All inputs must be positive integers. The DataFrame must include column names and row names.

??? answer "&nbsp;"
    Den bør være magen til den, der er i Tutorial - Session 1, afsnit 4.
​
#### Øvelse 5 ([Monty Hall](https://en.wikipedia.org/wiki/Monty_Hall_problem) - klassisk sandsynlighedsproblem)

I et gameshow står der tre lukkede døre. Bag én dør er en bil (gevinst), og bag de to andre er der geder.

i. Du vælger først én dør.

ii. Værten, som ved hvor bilen er, åbner derefter altid en af de to andre døre med en ged bag.

iii. Du får nu valget mellem at **holde fast** i din oprindelige dør eller **skifte** til den anden lukkede dør.

Besvar følgende:

1. Hvad er sandsynligheden for at vinde bilen, hvis du **holder fast**?
2. Hvad er sandsynligheden for at vinde bilen, hvis du **skifter**?
3. Hvilken strategi er bedst, og hvorfor?
4. Verificer svaret med en simulation i Python med 10, 100 og 10.000 gentagelser. Brug koden nedenfor, men tilpas den gerne.

```python
import random

# Number of simulations
n_trials = # Fyld ud med et tal

wins_stay = 0
wins_switch = 0

doors = [0, 1, 2]

for _ in range(n_trials):

    # Randomly place the prize
    prize = random.choice(doors)

    # Contestant makes an initial choice
    choice = random.choice(doors)

    # Host opens a door that:
    # - is not the contestant's choice
    # - does not contain the prize
    host_options = [d for d in doors if d != choice and d != prize]
    host_opens = random.choice(host_options)

    # --- Strategy 1: Stay ---
    if choice == prize:
        wins_stay += 1

    # --- Strategy 2: Switch ---
    remaining = [d for d in doors if d not in (choice, host_opens)]
    switched_choice = remaining[0]

    if switched_choice == prize:
        wins_switch += 1


print(f"Number of trials: {n_trials}")
print(f"Win rate (stay):   {wins_stay / n_trials:.4f}")
print(f"Win rate (switch): {wins_switch / n_trials:.4f}")
```


??? answer "&nbsp;"
    Hold fast: 1/3. Skift: 2/3. Det er derfor bedst at skifte.

