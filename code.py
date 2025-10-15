"""
Project 1: Data Analysis — Penguins
Author: Jean Yu
Student ID: 90875912
Email: jeanyu@Umich.edu
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
    out = {}
    for key in sums:
        out[key] = sums[key] / counts[key]
    return out

def calculate_bill_ratio_by_species(data):
    sums = {}
    counts = {}
    for row in data:
        sp = row.get("species")
        bl = row.get("bill_length_mm")
        bd = row.get("bill_depth_mm")
        if isinstance(sp, str) and isinstance(bl, float) and isinstance(bd, float) and bd != 0.0:
            ratio = bl / bd
            sums[sp] = sums.get(sp, 0.0) + ratio
            counts[sp] = counts.get(sp, 0) + 1

    out = {}
    for sp in sums:
        out[sp] = sums[sp] / counts[sp]
    return out

def write_avg_mass_csv(filename, results):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["species", "sex", "avg_body_mass_g"])
        for (sp, sx) in sorted(results.keys()):
            w.writerow([sp, sx, round(results[(sp, sx)], 2)])

def write_bill_ratio_csv(filename, results):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["species", "avg_bill_length_depth_ratio"])
        for sp in sorted(results.keys()):
            w.writerow([sp, round(results[sp], 4)])
    
def test_calculate_avg_mass_by_species_sex():
    d1 = [
        {"species":"adelie","sex":"male","body_mass_g":4000.0},
        {"species":"adelie","sex":"male","body_mass_g":4200.0},
        {"species":"adelie","sex":"female","body_mass_g":3400.0},
        {"species":"adelie","sex":"female","body_mass_g":3600.0},
    ]
    r1 = calculate_avg_mass_by_species_sex(d1)
    assert abs(r1[("adelie","male")] - 4100.0) < 1e-6
    assert abs(r1[("adelie","female")] - 3500.0) < 1e-6
 d2 = d1 + [
        {"species":"gentoo","sex":"male","body_mass_g":5000.0},
        {"species":"gentoo","sex":"male","body_mass_g":5200.0},
    ]
    r2 = calculate_avg_mass_by_species_sex(d2)
    assert abs(r2[("gentoo","male")] - 5100.0) < 1e-6
 d3 = [
        {"species":"adelie","sex":"male","body_mass_g":None},
        {"species":"adelie","sex":"male","body_mass_g":4200.0},
    ]
    r3 = calculate_avg_mass_by_species_sex(d3)
    assert abs(r3[("adelie","male")] - 4200.0) < 1e-6
