# Übung Git Stash

### Ihr müsst keine Dateien von Hand anfassen! Die Gesamte Übung kann (und sollte) nur mit `git ...` Kommandos gelöst werden!

- Hier ein Überblick über `git stash`:
  - `git stash`: Aktuelle Änderungen in den Stash legen
    - FLAGS: 
      + `-m NACHRICHT` um dem Stash eine Beschreibung zu geben
      + `-p` (patch) um nur bestimmte Änderungen auszuwählen
      + `-u` (untracked) um auch Dateien, die von git nicht getracked werden (gerade frisch erstellt, noch nie mit `git add` hinzugefügt) in den Stash gelegt werden
      + `-k` (keep index) um Dateien die schon zum commit vorgemerkt sind (git add) NICHT mit in den Stash zu legen, sondern nur geänderte, nicht vorgemerkte Dateien
    - mit `git stash push <Dateipfad>` können auch einzelne Dateien oder mehrere (zB *.md) gezielt in den Stash gelegt werden

  - `git stash list`: Den Stash anschauen. `stash@{0}` ist immer der neuste Eintrag. (stash == LIFO Stack)

  - `git stash apply`: Änderungen aus dem neusten Stash Eintrag übernehmen. Stash Eintrag NICHT löschen.
      - geht nur, wenn es KEINE Konflikte gibt -> aktuelle Änderungen vorher commiten, stashen oder reverten!
      - mit `git stash apply x` kann auch der x-te anstatt der neuste Eintrag übernommen werden.
 
  - `git stash pop`: Änderungen des neusten Eintrags übernehmen, Stash Eintrag nach ERFOLGREICHEM Übernehmen löschen.
      - geht nur wenn keine Konflikte -> aktuelle Änderungen vorher commiten, stashen oder reverten
      - mit `git stash pop x` kann der x-te anstatt der neuste Eintrag übernommen werden

  - `git drop x`: x-ten Eintrag aus dem Stash löschen ohne die Änderungen zu übernehmen

- dieses Repo hat 2 Branches:
  - master  - hier darf und kann nicht commited werden (branch ist protected) ; neuster Stand des Projekts
  - develop  - hier werden features entwickelt und per MR auf master gezogen
  - Makefile Änderungen dürfen nicht commited werden, weil sonst die Pipeline streikt. Lokale Änderungen stashen!

- Aufgabe:
  - die Anwendung ist aktuell kaputt ; die wirft einen Fehler, wenn ihr `make run` ausführt
  - ihr habt bereits einen fix geschrieben, und mit `git add` hinzugefügt.
  - allerdings habt ihr vergessen die Branch zu wechseln! Der fix muss auf `develop` committed werden!
  - nutzt die verschiedenen `git stash` Kommandos, um den fix auf `develop` zu verschieben und das Programm lauffähig zu machen
