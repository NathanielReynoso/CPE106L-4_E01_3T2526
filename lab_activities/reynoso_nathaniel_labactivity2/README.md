# Lab Activity 2: Strings, Lists, Tuples, and Dictionaries

## Course Info
* **Course:** CPE106L-4
* **Section:** E01
* **Instructor:** Sir John De Guzman Tarampi

## Description
This repository has a menu-driven Python application that manages student records. The application implements a full CRUD (Create, Read, Update, Delete/Display) in doing this software design activity.

### Data Structure:
* **Dictionaries:** Used as the primary database, mapping Student IDs with nested dictionaries.
* **Strings:** Used for standard text data. Example are ID and Names
* **Tuples:** Used to store immutable data pairs like the contact information of a student.
* **Lists:** Used to store mutable data sets like the grades in an exam that dynamically change.

## Environment Setup
This isolated virtual environment can be set up. 

```bash
mkdir lab2
cd lab2
python3 -m venv .venv
source .venv/bin/activate
mkdir src tests
