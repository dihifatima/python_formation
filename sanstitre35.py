# -*- coding: utf-8 -*-
"""
json(javaScript object Notation)
est un format pour stocker et échanger des données
{
  "nom": "Fatima",
  "age": 22,
  "cours": ["Python", "ML", "React"]
}
En Python, ça correspond à un dictionnaire (dict).
"""
#list of student
import json
student=[
    {"nom":"fatima","age":22},
    {"nom":"ali","age":20},
    {"nom":"sara","age":21}    
    ]
#transformer cette liste python en json
json_str=json.dumps(student,indent=4)
print("JSON formaté:")
print(json_str)


json_str = '''
[
    {"nom": "Fatima", "age": 22},
    {"nom": "Ali", "age": 20},
    {"nom": "Sara", "age": 21}
]
'''

# 3️⃣ Convertir JSON → Python
data = json.loads(json_str)
print("Liste Python :", data)
print("Nom du premier étudiant :", data[0]["nom"])
