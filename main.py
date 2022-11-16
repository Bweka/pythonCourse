#def show_student(first_name,last_name):
  #  print("hello, " +first_name +" "+ last_name)
"""
def produit(pr,dx):
   pr=int(pr)
   dx=int(dx)
   p=pr*dx
   return(p)
   
def Produit():
    a=int(input("entrer un nombre a: "))
    b=int(input("entrer un nombre b: "))
    c=a*b
    print (str(c))
"""
class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model       




if __name__=="__main__" : 
    pass
    """
    a=34
    b=45
    c=70
    if b < a :
        print("je suis malade")
    elif c >= b :
        print("tu vas guerir ne t'en fait pas")
    else :
        print("je ne suis pas malade")

    i=1
    while i < 10 :
        i=i+1
        print(i)

    fruits=["ananas","mangue","avocat"]
    for f in fruits :
     
     
    fruits=("ananas","mangue","avocat")
    for f in fruits :
        print(f)
        
    fruits={"ananas","mangue","avocat"}
    for f in fruits :
        print(f)
       
    #les dictionnaires

    student={
        "name":"jhon",
        "age":21,
        "adresse":"kamenge",

    }
   #pour afficher seulement les clés
    student ["age"]=30
   # print(student["age"])
    for s in student.keys(): 
     print(s)
     """
    """
    a=input("entrer la premiere valeur")
    b=input("entrer la deuxieme valeur")
    c = produit(a,b)
    c = str(c)
    print("le produit de a et b est:" + c)
    """
    #Produit()
    #POO 
c=car("TOYOTA","TX")
print(c)
        

 