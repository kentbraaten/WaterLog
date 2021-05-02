from google.cloud import firestore


READINGS_COLLECTION = "Event"
ACTIONS_COLLECTION = "Actions"
SETTINGS_COLLECTION = "Settings"
SYSTEM_EVENTS_COLLECTION = "SystemEvent"


def add_event(data, eventType):
    db = firestore.Client()
    event_ref = db.collection(eventType).document(None)
    event_ref.set(data)
    return document_to_data(event_ref.get())


def add_event_array(data, eventType):
    db = firestore.Client()
    event_ref = db.collection(eventType).document(None)
    event_ref.set(data)
    return document_to_data(event_ref.get())


def read_settings():
    db = firestore.Client()
    query = db.collection(SETTINGS_COLLECTION).order_by("dateTime","DESCENDING")
    docs = query.stream()
    docs = list(map(document_to_data, docs))
    return docs[0]


def document_to_data(doc):
    if not doc.exists:
        return None
    doc_dict = doc.to_dict()
    doc_dict['id'] = doc.id
    return doc_dict