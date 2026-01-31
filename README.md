# Aplicație de Gestionare a Taskurilor

O aplicație de linie de comandă pentru gestionarea taskurilor cu priorități, categorii, deadline-uri și stare.

## Cerințe

- Python 3.11 sau mai nou
- Biblioteca `tabulate`

## Instalare

### Local

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### Docker

**Din DockerHub (recomandat):**

```bash
docker pull virgiistegaru/proiect-map
docker run -it virgiistegaru/proiect-map
```

**Sau construiți local:**

```bash
docker build -t task-manager .
docker run -it task-manager
```

## Rulare

```bash
python main.py
```

## Opțiuni Meniu

1. Afișare taskuri (cu filtrare opțională)
2. Adaugare task nou
3. Ștergere task
4. Modificare stare task (complet/incomplet)
5. Ștergere toate taskurile
6. Editare task
7. Filtrare după categorie
8. Căutare task
9. Export CSV
10. Import CSV
11. Ieșire

## Adaugare Task

- **Nume**: Fără virgule sau puncte
- **Descriere**: Detalii task
- **Prioritate**: 1-5 (implicit 3)
- **Deadline**: Format `ZZ-LL-AAAA` (astazi sau viitor)
- **Categorii**: Separate cu `|` (ex: work|urgent)

## Format Stocaj

Taskurile sunt salvate în `taskuri.txt` cu formatul:
```
Nume,Descriere,Prioritate,Deadline,Stare,Categorii
```

Exemplu:
```
Proiect,Initializare repo,4,31-01-2026,Necompletat,work|urgent
```

## Filtrare

- Taskuri necompletate
- Taskuri completate
- Prioritate mare (4-5)
- Deadline apropiat (3 zile)

## Export/Import

- **Export**: Salvează în `taskuri_export.csv`
- **Import**: Citește din `taskuri_import.csv` și adaugă taskuri

## Notificări

După fiecare acțiune se afișează:
- Total taskuri
- Procent finalizare
- Taskuri depășite
- Alertă pentru taskuri cu deadline astazi
