import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Fetch the service account key JSON file contents
cred = credentials.Certificate('key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred)

db = firestore.client()


title = "\n    [1] Add User\n    [2] Delete Users\n    [3] Show Users\n    [4] Exit\n" 

def AddUser():

    name = input("Name : ")
    surname = input("Surname : ")
    age = input("Age : ")

    db.collection("users").add({
        "name":name,
        "surname":surname,
        "age":age
    })
    

def DeleteAllUser():

    lenght = db.collection("users").get()

    for dd in lenght:
        db.collection("users").document(dd.id).delete()

def ShowUsers():
    users = db.collection("users").get()
    
    for user in users:
        print("\n    Name : " + user.to_dict()["name"], "\n    Surname : ",user.to_dict()["surname"],  "\n    Age : " + user.to_dict()[
          "age"], "\n\n", "--------------------------------------------------------------------")

def Menu():
    
      
    print(title)
    question = int(input("""What do you want do? 
                         Answer : """))

    while True:
        if question == 1:
            AddUser()
            adduserques = input("""Do you wanna contuniu? (Y/N) 
                                Answer : """)
            if adduserques == "Y":
                AddUser()
            if adduserques == "N":
                print(title)
                question = int(input("""What do you want do? 
                         Answer : """))
            else :
                adduserques = input("""Do you wanna contuniu? (Y/N) 
                                Answer : """)
        if question == 2:
            DeleteAllUser()
            print("\nDeleted All User!!!!!!\n")
            print(title)
            question = int(input("""What do you want do? 
                         Answer : """))
        if question == 3:
            ShowUsers()
            print(title)
            question = int(input("""What do you want do? 
                         Answer : """))
        if question == 4:
            exit()
        else :
            print(title)
            question = int(input("""What do you want do? 
                         Answer : """))

    
Menu()
    
    
    