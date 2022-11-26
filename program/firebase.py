
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Fetch the service account key JSON file contents
cred = credentials.Certificate('key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred)


db = firestore.client()

doc = db.collection("users").get()
a = 0
for user in doc:
    print("ad soyad: " + user.to_dict()["name"], user.to_dict()["surname"],  "\nage: " + user.to_dict()[
          "age"], "\n", "--------------------------------------------------------------------")
