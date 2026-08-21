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

* Todos-Liste anzeigen
* Todo erstellen
* Todo ändern
* Todo löschen
* Todo anzeigen


* Tasks-Liste eines Todo anzeigen
* Task erstellen
* Task anzeigen
* Task ändern
* Task löschen
* Task als erledigt markieren

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


## 6. Datenbank-Erstellung

Erstellen Sie ein Python-Skript, das eine leere SQLite-Datenbank erzeugt.

Das Skript soll:

1. die SQLite-Datenbank anlegen,
2. die Tabelle `todos` erstellen,
3. die Tabelle `tasks` erstellen,
4. Primärschlüssel definieren,
5. Fremdschlüssel definieren,
6. notwendige Constraints definieren.

```text
create_database.py
```
Das Skript soll mehrfach ausgeführt werden können, ohne Fehler zu verursachen.

## 7. Projektstruktur

Planen Sie eine sinnvolle Projektstruktur.

``` 
├── main.py
├── database.py
├── create_database.py
├── requirements.txt
├── README.txt
├── models/
│   ├── todo.py
│   └── task.py
│ 
├── routers/
│   ├── todo.py
│   └── task.py
│
├── services/
│   ├── todo.py
│   └── task.py
│
└── tests/
    ├── test_todos.py
    └── test_tasks.py
```

| Verzeichnis | Inhalt                  |
|-------------|-------------------------|
| models      | pydantic Datenmodelle   |
| routers     | api routen (controller) |
| services    | Datenbankzugriff, SQL   |
| tests       | tests                   |

## 8. Pydantic-Modelle

Für die API sollen Pydantic-Modelle verwendet werden.

Es sollen mindestens Modelle für folgende Aufgaben erstellt werden:

* Erstellen eines Todos
* Ändern eines Todos
* Rückgabe eines Todos
* Erstellen eines Tasks
* Ändern eines Tasks
* Rückgabe eines Tasks

Dabei sollen die Daten validiert werden.

Validierungen:

* Titel darf nicht leer sein.
* Titel besitzt eine maximale Länge.
* Status darf nur definierte Werte enthalten.
* Priorität darf nur definierte Werte enthalten.
* Pflichtfelder müssen vorhanden sein.
* ...weitere Sinvolle Validierungen


