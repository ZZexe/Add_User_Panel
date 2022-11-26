import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Fetch the service account key JSON file contents
cred = credentials.Certificate('key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred)

db = firestore.client()




def AddUser():

    name = input("Name : ")
    surname = input("Surname : ")
    age = input("Age : ")

    db.collection("users").add({
        "name":name,
        "surname":surname,
        "age":age
    })
    print(title)
    question
    

def DeleteAllUser():

    lenght = db.collection("users").get()

    for dd in lenght:
        db.collection("users").document(dd.id).delete()

def ShowUsers():
    users = db.collection("users").get()
    
    for user in users:
        print("ad soyad: " + user.to_dict()["name"], user.to_dict()["surname"],  "\nage: " + user.to_dict()[
          "age"], "\n", "--------------------------------------------------------------------")

title = "\n[1] Add User\n[2] Delete Users\n[3] Show Users\n[4] Exit\n"
print(title)
question = int(input("What do you want do? "))


if question == "1":
    print("\nAdd User Screen\n")
    AddUser()
    if question == "2":
        print("\nDeleting Users\n")
        DeleteAllUser()
    if question == "3":
        print("\nUSERS TABLE\n")
        ShowUsers()
    if question == "4":
        print("\nExiting....\n")
        exit()
    else :
        question
    
        