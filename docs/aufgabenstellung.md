# Projektaufgabe: Entwicklung einer Todo-Management-API

## 1. Ausgangssituation

Ein Unternehmen möchte eine einfache REST-API zur Verwaltung von Aufgaben entwickeln.

Aufgaben (`Tasks`) sollen in Todo-Listen (`Todos`) organisiert werden können.

Eine Todo-Liste kann **eine oder mehrere Aufgaben** enthalten.

Ein Task gehört **immer genau einer Todo-Liste**.

Die Anwendung soll als REST-API mit Python und FastAPI umgesetzt werden. Die Datenhaltung erfolgt in einer SQLite-Datenbank.

## 2. Ziel des Projekts

Entwickeln Sie eine funktionsfähige REST-API, mit der Todo-Listen und deren Aufgaben erstellt, gelesen, geändert und gelöscht werden können.

Für die Entwicklung sollen folgende Technologien eingesetzt werden:

* Python
* FastAPI
* Pydantic
* Uvicorn
* SQLite
* REST
* OpenAPI / Swagger
* unittest 

## 3. Fachliche Anforderungen

### Todo-Liste

Eine Todo-Liste besitzt mindestens:

* ID
* Titel
* Beschreibung
* Erstellungsdatum

### Task

Ein Task besitzt mindestens:

* ID
* Titel
* Beschreibung
* Status
* Priorität
* Erstellungsdatum
* Fälligkeitsdatum
* Zugehörige Todo-Liste

Der Status eines Tasks kann beispielsweise folgende Werte besitzen:

* `open`
* `in_progress`
* `done`

Die Priorität kann beispielsweise folgende Werte besitzen:

* `low`
* `medium`
* `high`

### Beziehungen

Es gelten folgende Regeln:

* Eine Todo-Liste kann mehrere Tasks enthalten.
* Ein Task gehört genau einer Todo-Liste.
* Wird eine Todo-Liste gelöscht, muss definiert werden, was mit den zugehörigen Tasks passiert.

Für die Löschlogik ist eine sinnvolle Lösung zu planen und zu dokumentieren

> Beim Löschen einer Todo-Liste werden auch alle zugehörigen Tasks gelöscht.

## 4. UML-Modellierung

Vor der Implementierung sollen die fachlichen Anforderungen modelliert werden.

### 4.1 UML-Use-Case-Diagramm

Erstellen Sie ein Use-Case-Diagramm.

Mindestens folgende Anwendungsfälle sollen dargestellt werden:

XXXXX HIER die Anwendungsfälle beschreiben XXXX

### 4.2 UML-Klassendiagramm

Erstellen Sie ein UML-Klassendiagramm für die fachlichen Modelle.


## 5. Datenbankplanung

Vor der Programmierung soll die Datenbank entworfen werden.

Erstellen Sie ein Datenbankmodell für SQLite.

- Alles in Englisch
- Alles kleingeschrieben
- Spaltennamen bekommen den Tabellennamen als Prefix in singular

# Tabellen

- tasks
  - task_id
  - task_title
  - ....
- todos
  - todo_id
  - todo_title
  - ...



