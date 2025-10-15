#Penguin Data Analysis Project
#Name: Jean Yu
#Student ID: 90875912
#Email: jeanyu@umich.edu
#Collaborators: chatgpt 

import csv
def convert_numeric_fields(row):
    numeric_fields = {
        'bill_length_mm': float,
        'bill_depth_mm': float,
        'flipper_length_mm': float,
        'body_mass_g': int
    }

