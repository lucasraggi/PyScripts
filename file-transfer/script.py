#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

def extract_params(line):
    line = line.split("-")
    path_complement = line[0]
    patient_number = line[1]
    first_name = line[2]
    last_name = line[3]
    last_name = last_name[:-1]
    return path_complement, patient_number, first_name, last_name

with open('input') as pacientes:
    count = 0
    root_path = "E:/HOB/Pacientes - coleta Roberto/"
    outpath = []
    for line in pacientes:
        path_complement, patient_number, first_name, last_name = extract_params(line)
        path = root_path + path_complement
        print(line.split("-"))
        for filename in os.listdir(path):
            if filename == first_name:
                print(filename)
            if filename == last_name:
                print(filename)

        count += 1
        if count == 1:
            break

