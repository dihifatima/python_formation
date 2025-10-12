class Personne:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=age
    
    def parler(self):
       print(f"Bonjour , je suis  {self.nom} et j ai {self.age}")
    
p1= Personne("Fatima", 22)
p1.parler()    
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
