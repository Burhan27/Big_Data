# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file."""

import pandas as pd

data = pd.read_csv("befkbhalderstatkode.csv")

row_count = sum(1 for row in data)

print("pp ", row_count)
