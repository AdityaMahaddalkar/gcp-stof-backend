import logging
import os
from pymongo import MongoClient
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

project_id = "hack-finnovate"
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred,{
    'projectId' : project_id,
})


DATABASE = "stof"
FORM_TEMPLATE_COLLECTION = "form_template"
FORM_STORAGE_COLLECTION = "form_storage"


def check_native_health():
    db = firestore.client()
    if collection_obj is None:
        return {
            "health": "red",
            "database": "NC"
        }
    else:
        return {
            "health": "green",
            "database": "CC"
        }

def form_template_service(id: str):
    db = firestore.client()
    form_template = db.collection(FORM_TEMPLATE_COLLECTION).document(id).get()
    if form_template is not None:
        return form_template
    else:
        return None


async def form_posting_service(json_body):
    db = firestore.client()
    try:
        db.collection(FORM_STORAGE_COLLECTION).document(id).set(json.loads(json_body))
        return None
    except Exception as e:
        return {
            "exception": str(e)
        }
