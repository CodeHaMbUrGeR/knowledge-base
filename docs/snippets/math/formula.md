# Formeln

## Geradengleichung

<!-- --8<-- [start:linear-equation] -->
$$ y = m \cdot x + b $$

??? note "Parameter"

    | Parameter | Beschreibung                                                                                  |
    | --------- | --------------------------------------------------------------------------------------------- |
    | $n$       | Anzahl der Datenpunkte                                                                        |
    | $m$       | Steigung der Geraden: Gibt an, wie stark und in welcher Richtung die Gerade geneigt ist.      |
    | $b$       | Achsenabschnitt (y-Intercept): Gibt den Punkt an, wo die Gerade die y-Achse schneidet.        |
    | $x$       | Unabhängige Variable: Eine beliebige x-Koordinate eines Punktes auf der Geraden.              |
    | $y$       | Abhängige Variable: Die y-Koordinate des Punktes, der zur entsprechenden x-Koordinate gehört. |
<!-- --8<-- [end:linear-equation] -->

## Mittlerer Absoluter Fehler

<!-- --8<-- [start:mean-absolute-error] -->
$$ \text{MAE} = \frac{1}{n} \sum_{i=1}^n | y_i - \hat{y}_i | $$

??? note "Parameter"

    | Parameter   | Beschreibung                                |
    | ----------- | ------------------------------------------- |
    | $n$         | Anzahl der Datenpunkte                      |
    | $y_i$       | Tatsächlicher Wert des $i$-ten Datenpunkts  |
    | $\hat{y}_i$ | Vorhergesagter Wert des $i$-ten Datenpunkts |
<!-- --8<-- [end:mean-absolute-error] -->

## Mittlerer Quadratischer Fehler

<!-- --8<-- [start:mean-squared-error] -->
$$ \text{MSE} = \frac{1}{n} \sum_{i=1}^n ( y_i - \hat{y}_i )^2 $$

??? note "Parameter"

    | Parameter   | Beschreibung                                |
    | ----------- | ------------------------------------------- |
    | $n$         | Anzahl der Datenpunkte                      |
    | $y_i$       | Tatsächlicher Wert des $i$-ten Datenpunkts  |
    | $\hat{y}_i$ | Vorhergesagter Wert des $i$-ten Datenpunkts |
<!-- --8<-- [end:mean-squared-error] -->
