import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from pprint import pprint

#use a service acc
project_id = "hack-finnovate"
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred,{
    'projectId' : project_id,
})

db = firestore.client()

def trialDataInsert():
    doc_ref = db.collection(u'form_storage').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })
    # doc = db.collection('form_storage').document('vnO74wmGUi6n6v3ZY9uZ').get()
    # pprint(doc)
    
  