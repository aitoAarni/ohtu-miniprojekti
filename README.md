# ohtu-miniprojekti

![workflow](https://github.com/aitoAarni/ohtu-miniprojekti/actions/workflows/main.yml/badge.svg)
[![codecov](https://codecov.io/gh/aitoAarni/ohtu-miniprojekti/branch/main/graph/badge.svg?token=Y13KH8K0M0)](https://codecov.io/gh/aitoAarni/ohtu-miniprojekti)

## Asennus

Lataa projekti git clone - kommennolla ja asenna projekti seuraavilla komennoilla:

```
poetry install
```

```
poetry run invoke build
```

## Sovelluksen käynnistäminen

Käynnistä sovellus komennolla

```
poetry run invoke start
```

## Muita komentoja

Testit voi ajaa komennolla
```
poetry run invoke test
```

Testikattavuusraportin saa luotua komennolla
```
poetry run invoke coverage-report
```

Pylintin voi suorittaa komennolla
```
poetry run invoke lint
```

## Sovelluksen rakenne

Paketoidaan sovelluksen toimintalogiikka

- UI
- Sovelluslogiikka
- repositoriosta huolehtiva koodi

## Dokumentaatio

[Sovelluksen arkkitehtuuri](/documentation/architecture.md)  
[Käyttöohje](/documentation/operation-manual.md)

## Linkit

[Structured Backlog](https://docs.google.com/spreadsheets/d/1XYFtrZ4NT5crDIYqlv-1CX1kRro6Nn1QrsbifLbLkDY/edit?usp=sharing)

## Definiton of Done

- määritelty: user story purettu taskien tasolle yhteisymmärryksessä
- suunniteltu: taskien yksityiskohdat sovittu ja suunnitelty yhdessä, taskit jaettu
- toteutettu: toiminnallisuus toteuttaa user storyn vaatimukset
- yksikkötestattu: 80% testikattavuus
- integraatiotestattu: hyväksytysti CI ja testit läpi
- otettu tuotantoon: toiminnallisuus implementoitu tuotteesseen
