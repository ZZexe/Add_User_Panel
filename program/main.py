import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

db  = firestore.client()




def AddUser():

    name = input("Name : ")
    surname = input("Surname : ")
    age = int(input("Age : "))
    
    db.collection("users").document("{x}").set({
        "name": name,
        "surname": surname,
        "age": age
    })



i = 1
for i in range:
    def addUser():
        name = input("Name : ")
        surname = input("Surname : ")
        age = int(input("Age : "))
    
        db.collection("users").document("{i}").set({
            "name": name,
            "surname": surname,
            "age": age
            })
    addUser()

    i = i + 1