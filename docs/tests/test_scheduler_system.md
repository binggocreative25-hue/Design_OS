# Scheduler System Test

## Test 1
Command:

schedule add Follow Up MFI 2026-06-10

Expected:
Task created

PASS

---

## Test 2

Command:

schedule list

Expected:
Task appears

PASS

---

## Test 3

Command:

schedule done 1

Expected:
Status becomes DONE

PASS

---

## Test 4

Command:

schedule dashboard

Expected:
Dashboard metrics displayed

PASS

---

## Test 5

Command:

schedule analytics

Expected:
Analytics displayed

PASS

---

## Test 6

Command:

schedule upcoming

Expected:
Only pending tasks displayed

PASS

---

## Test 7

Command:

schedule completed

Expected:
Only completed tasks displayed

PASS