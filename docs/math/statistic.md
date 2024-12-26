# Statistik

## Deskriptive Statistik

Die **deskriptive** (auch: **beschreibende**) **Statistik** hat zum Ziel, empirische Daten (z. B. Ergebnisse aus Experimenten) durch Tabellen, Kennzahlen (auch: Maßzahlen oder Parameter) und Grafiken übersichtlich darzustellen und zu ordnen.

Kenngrößen (statistische Kennwerte):

- Lagemaß
- Streuungsmaß

---

## Median

Der Median gibt den Wert einer geordneten (auf-/ab- steigend) Menge wieder, der in der Mitte von dieser liegt. Bei einer geraden Kardinalität der Menge, wird der Median über den Mittelwert der beiden in der Mitte liegenden Werte gebildet.

!!! example "(ungerde): $|M|=5$"

    Menge: $M=\{6,3,4,1,9\}$

    1. Sortieren: $M=\{1,3,4,6,9\}$
    2. Mitte finde: $4$

!!! example "(gerde): $|M|=4$"

    Menge: $M=\{6,3,4,1\}$

    1. Sortieren: $M=\{1,3,4,6\}$
    2. "Mitte" finde: $3$ & $4$
    3. Mittelwert bilden: $\frac{3+4}{2}=3,5$

---

## Mittelwert

Der **Mittelwert** (auch: Durschnitt), soll hier als Synonym für den **Arithmetischer Mittelwert** stehen.

Formel:

$$\bar{x}=\frac{1}{n}\sum x_i$$

!!! example

    Menge: $M=\{2,1,3,4,7\}$

    Anzahl der Elemente (Kardinalität): $|M|=5$

    Summe der Elemente: $\sum_{x \in M}x=17$

    Mittelwert:$\mu=\frac{17}{5}=3,4$

---

## Modus

Oder auch Modalwert genannt, gibt den Wert mit der höchsten Häufigkeit an. Es sind nur die folgenden Möglichkeiten definiert:

- **ein** Wert
- kein Modus
- bi-modal

!!! example

    Modus: **1**
    
    - $M=\{1,1,3,8\}$

    Modus: **bi-modal** (1 & 8) oder **kein** Modus, je nach Definition
    
    - $M=\{1,1,3,8,8\}$

    Modus: **keiner**, bei mehr als 2
    
    - $M=\{1,1,3,3,8,8\}$

---

## Schiefe

ein Maß für die Asymmetrie der Daten.

Formel:

$$\gamma_m=\frac{\frac{1}{n}\sum(x_i-x)^3}{\sigma^3}$$

---

## Spannweite und IQA

Die **Spannweite** (eng.: **Range**) beschreibt den Abstand zwischen dem größten und dem kleinsten Wert. Hierbei handelt es sich um ein Streuungsmaß.

$$R=x_{max}-x_{min}$$

Für die **IQA** (**Interquartilabstand**, eng.: **IQR**, also **interquartile range**) wird der Datensatz sortiert und in der Mitte geteilt. Die Differenz der Median dieser Hälften ist der IQA.

!!! example

    Menge (sortiert): $M=\{2,2,4,5,6,8,8,8\}$

    Mitte zwischen ``5`` und ``6``: $L=\{2,2,4,5\}$ und $R=\{6,8,8,8\}$

    Median: von $L$ ist **3** und von $R$ ist **8**.

    $IQA=8-3=5$
