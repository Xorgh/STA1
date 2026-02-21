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

Videoen giver en hurtig gennemgang af sandsynlighedsregning og statistik, og er en god introduktion til kurset.

<p align="left">

  <a href="Tutorial_1_notebook/">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python introduktion" width="100" />
    <br>
    <strong>Se Tutorial 1: Python, sandsynlighedsregning og statistik</strong>
  </a>
</p>

[Download tutorial som notebook (.ipynb)](https://raw.githubusercontent.com/RBrooksDK/STA_26/main/01_Repetition_af_sandsynlighedsteori_og_stokastiske_variable/Tutorial_1_notebook.ipynb)

[Se tutorial som markdown](Tutorial_1.md/)

[Sessionnoter](https://drive.google.com/file/d/1D20cFjJA9CmBZQGu_rESr4u4jqoc_x7a/view?usp=sharing)

[Sessionsmateriale](https://viaucdk-my.sharepoint.com/:f:/g/personal/rib_viauc_dk/IgD9ITWOtgoOSJJQFfZOslRtAen5QiivW73BLyPj_it1PUo?e=JHXkHj)

## Video Materiale:


**Basics of Probability**

Playliste med 7 videoer, der dækker grundlæggende sandsynlighedsbegreber.

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=Tm0zx7xWdYH3B_T1&amp;list=PLvxOuBpazmsOGOursPoofaHyz_1NpxbhA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

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
#### Øvelse 5 ([Monty Hall](https://en.wikipedia.org/wiki/Monty_Hall_problem) - classic probability problem)

In a game show, there are three closed doors. Behind one door is a car (the prize), and behind the other two are goats.

i. You first choose one door.

ii. The host, who knows where the car is, always opens one of the two other doors that has a goat behind it.

iii. You are then given the choice to **stay** with your original door or **switch** to the other unopened door.

Answer the following:

1. What is the probability of winning the car if you **stay**?
2. What is the probability of winning the car if you **switch**?
3. Which strategy is best, and why?
4. Verify your result with a Python simulation using 10, 100, 10,000, and 100,000 trials - run the simulation for each n-trials value multiple times and see what happens when n-trials is increased. Use the code below, but feel free to adapt it.

```python
import random

# Number of simulations
n_trials = # Fill in a number

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
    Stay: 1/3. Switch: 2/3. Therefore, switching is the better strategy.

#### Øvelse 6 (Scales of Measurement)

For each of the following descriptions, identify whether the data is measured on a **nominal**, **ordinal**, **interval**, or **ratio** scale.

1. The jersey numbers of players on a football team (e.g. 7, 10, 23).
2. IQ scores from a group of test subjects (e.g. 95, 110, 130).
3. Customer satisfaction rated as *Very Dissatisfied*, *Dissatisfied*, *Neutral*, *Satisfied*, *Very Satisfied*.
4. The distance in kilometres from each student's home to campus.
5. The postal codes (zip codes) of customers in a database (e.g. 8000, 2100, 5000).
6. The finishing positions in a marathon (1st, 2nd, 3rd, ...).
7. Annual income of employees in a company measured in DKK.
8. The year in which major historical events occurred (e.g. 1066, 1776, 1945).
9. The bus route numbers in a city's transit system (e.g. 1, 3, 42, 150).
10. The elapsed time (in seconds) for a sprinter to complete a 100-metre dash.

??? answer "&nbsp;"
    1. Nominal — jersey numbers are labels; arithmetic on them is meaningless.
    2. Interval — differences are meaningful (a 10-point gap means the same anywhere on the scale), but an IQ of 0 does not mean "no intelligence", and ratios are not meaningful.
    3. Ordinal — the categories have a clear order, but the gaps between levels are not necessarily equal.
    4. Ratio — distance has a true zero and meaningful ratios (10 km is twice 5 km).
    5. Nominal — postal codes are numeric labels for geographic areas; arithmetic on them is meaningless (8000 + 2100 does not produce a meaningful result).
    6. Ordinal — positions indicate order, but the time difference between 1st and 2nd may differ from that between 2nd and 3rd.
    7. Ratio — income has a true zero and meaningful ratios.
    8. Interval — differences between years are meaningful, but year 0 is not a true absence of time.
    9. Nominal — route numbers are identifiers, not quantities; "route 42" is not more or less than "route 3C".
    10. Ratio — elapsed time has a true zero and meaningful ratios (10 s is twice 5 s).

