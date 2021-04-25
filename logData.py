from google.cloud import firestore

EVENTS_COLLECTION = "Event"

def add_event(data):
    db = firestore.Client()
    event_ref = db.collection(EVENTS_COLLECTION).document(None)
    event_ref.set(data)
    return document_to_data(event_ref.get())


def read_events():
    db = firestore.Client()
    query = db.collection(EVENTS_COLLECTION).order_by("date")
    docs = query.stream()
    docs = list(map(documentToDict, docs))


def document_to_data(doc):
    if not doc.exists:
        return None
    doc_dict = doc.to_dict()
    doc_dict['id'] = doc.id
    return doc_dict