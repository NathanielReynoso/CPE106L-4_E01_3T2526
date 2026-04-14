# Lab Activity 2: Strings, Lists, Tuples, and Dictionaries

## Course Info
* **Course:** CPE106L-4 Software Design Laboratory
* **Instructor:** Dr. John De Guzman Tarampi

## Description
This repository contains a menu-driven Python command-line application that manages structured student records. The application demonstrates core software design principles by implementing full CRUD (Create, Read, Update, Delete/Display) operations utilizing Python's built-in data structures.

### Data Structure Utilization:
* **Dictionaries:** Used as the primary database, mapping String keys (Student IDs) to nested dictionaries.
* **Strings:** Used for standard text data (IDs, Names).
* **Tuples:** Used to store immutable data pairs, such as a student's `(Degree, Major)` program designation.
* **Lists:** Used to store mutable data sets, such as dynamically appending exam `[grades]` over time.

## Environment Setup
This project follows professional Python standards using an isolated virtual environment. 

```bash
mkdir lab2
cd lab2
python3 -m venv .venv
source .venv/bin/activate
mkdir src tests
