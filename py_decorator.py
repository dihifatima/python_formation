
    
def decorateur(func):
     def wrapper():
           print("--------")
           func()
           print("--------")
     return wrapper
@decorateur
def say_hello():
    print("hello,Fatima !") 
      
say_hello()