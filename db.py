import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the credentials stored in keys.json
cred = credentials.Certificate("./keys.json")
firebase_admin.initialize_app(cred)

# create firestore db
db = firestore.client()

# adding a collection
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})