import logging
import os

from pymongo import MongoClient

DATABASE = "stof"
FORM_TEMPLATE_COLLECTION = "form_template"
FORM_STORAGE_COLLECTION = "form_storage"


def check_native_health():
    collection_obj = init_mongo_client(DATABASE, FORM_STORAGE_COLLECTION)
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


def init_mongo_client(db: str, collection: str):
    try:
        client = MongoClient(os.getenv("MONGO-URL", "mongodb://localhost:27017"))
        collection_obj = client.get_database(db).get_collection(collection)
        return collection_obj
    except Exception as e:
        logging.error(f"Database connection failed : {e}")
        return None


def form_template_service(id: int):
    collection_obj = init_mongo_client(DATABASE, FORM_TEMPLATE_COLLECTION)
    form_template = collection_obj.find_one({
        "form_id": id
    }, projection={'_id': False})
    if form_template is not None:
        return form_template
    else:
        return None


async def form_posting_service(json_body):
    collection_obj = init_mongo_client(DATABASE, FORM_STORAGE_COLLECTION)
    try:
        collection_obj.save(json_body)
        return None
    except Exception as e:
        return {
            "exception": str(e)
        }
