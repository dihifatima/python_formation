# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 21:28:07 2025

@author: Admin
"""

import json

x='{"name":"John","age":30,"city":"New York"}'
y=json.loads(x)
print(y["age"])
json_str = '{"nom": "Fatima", "age": 22, "cours": ["Python", "ML", "React"]}'
data = json.loads(json_str)  # Convertit la chaîne JSON en dict
print(data)
print(data["nom"])  # Fatima
