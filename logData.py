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


def read_events(eventType):
    db = firestore.Client()
    query = db.collection(eventType).order_by("dateTime")
    docs = query.stream()
    docs = list(map(document_to_data, docs))


def document_to_data(doc):
    if not doc.exists:
        return None
    doc_dict = doc.to_dict()
    doc_dict['id'] = doc.id
    return doc_dict