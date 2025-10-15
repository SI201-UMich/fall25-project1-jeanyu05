"""
Project 1: Data Analysis — Penguins
Author: [Your Name Here]
Student ID: [Your ID]
Email: [Your Email]
Collaborators: [List classmates and/or GenAI; specify who wrote which functions]
GenAI usage: Code generated with assistance from ChatGPT (GPT-5 Thinking). I verified outputs and added tests.

Dataset: penguins.csv (Palmer Penguins)
This program:
  1) Imports the CSV into a list of dictionaries with typed values
  2) Performs two calculations using at least three columns each
     A) Average body mass by (species, sex)
     B) Average bill length / bill depth ratio by species
  3) Writes the results to CSV files
  4) Includes four tests per calculation (2 general + 2 edge cases)
"""

import csv
def to_float(x):
    if x is None:
        return None
    s = str(x).strip()
    if s == "" or s.lower() in ["na", "nan", "none"]:
        return None
    try:
        return float(s)
    except ValueError:
        return None
def norm_str(x):
    if x is None:
        return None
    s = str(x).strip()
    return s.lower() if s != "" else None

def read_penguin_data(filename):
    rows = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({
                "species": norm_str(r.get("species")),
                "island": norm_str(r.get("island")),
                "sex": norm_str(r.get("sex")),
                "bill_length_mm": to_float(r.get("bill_length_mm")),
                "bill_depth_mm": to_float(r.get("bill_depth_mm")),
                "flipper_length_mm": to_float(r.get("flipper_length_mm")),
                "body_mass_g": to_float(r.get("body_mass_g")),
            })
    return rows

def calculate_avg_mass_by_species_sex(data):
    sums = {}
    counts = {}
    for row in data:
        sp = row.get("species")
        sx = row.get("sex")
        mass = row.get("body_mass_g")
        if isinstance(sp, str) and isinstance(sx, str) and isinstance(mass, float):
            key = (sp, sx)
            sums[key] = sums.get(key, 0.0) + mass
            counts[key] = counts.get(key, 0) + 1
