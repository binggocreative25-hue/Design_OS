# TEST CLIENT SCORING

Phase:
3B Client Scoring

Status:
PENDING

---

## TEST 1

Client dengan banyak project

### Setup

Client:

ABC COFFEE

Projects:

10

Categories:

Branding
Logo
Packaging
Social Media
Marketing

Notes:

10

### Expected

Score >= 90

Tier:

PLATINUM

---

## TEST 2

Client menengah

### Setup

Client:

XYZ STUDIO

Projects:

6

Categories:

Logo
Branding
Packaging

Notes:

4

### Expected

Score 75-89

Tier:

GOLD

---

## TEST 3

Client baru

### Setup

Client:

STARTUP A

Projects:

1

Categories:

Logo

Notes:

0

### Expected

Score < 60

Tier:

BRONZE

---

## TEST 4

No Relationship Notes

### Setup

Projects:

5

Categories:

3

Notes:

0

### Expected

Scoring tetap berjalan

Tidak error

---

## TEST 5

No Projects

### Setup

Projects:

0

Categories:

0

Notes:

0

### Expected

Score:

0

Tier:

BRONZE

---

## TEST 6

Reason Generator

### Setup

Projects:

8

Categories:

4

Notes:

5

### Expected

Reasons:

- repeat client
- multiple service categories
- active relationship history

---

## TEST 7

Tier Validation

### Expected

0-59
BRONZE

60-74
SILVER

75-89
GOLD

90-100
PLATINUM

---

## PASS CRITERIA

- Score calculation valid
- Tier classification valid
- Reason generation valid
- No crash on empty data
- Compatible with ClientManager
- Compatible with Phase 2C Intelligence