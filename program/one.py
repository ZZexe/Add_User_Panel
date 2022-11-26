import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Fetch the service account key JSON file contents
cred = credentials.Certificate('key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred)

db = firestore.client()


# document id kendin verioun
# db.collection("users").document("sea").set({
#     "name":"Hamza"
#
# })

name = input("Name : ")
surname = input("Surname : ")

a = 0


def l():

    sonuc = 1+a

    db.collection("users").document("{sonuc}").set({
        "name": name,
        "surname": surname
    })
    question = input("Do U wanna continue? (Y/N) ")
    if question == "N":
        print("Added!")

    else:
        print("sa")
        l()
        return


l()
