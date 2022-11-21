import threading
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

status = 0

cred = credentials.Certificate(
    'D:\Academic\Semester 4\Softwares Engineering\Coursework\Project\Embedded System\Test01\parking-me-154d6-firebase-adminsdk-83xzc-ddbdadc714.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def arrived():
    data = db.collection(u'S001').document(u'Slot002')

    data.set({
        u'status': 3,
        u'arrived_time': time.time()
    }, merge=True)
    global status
    status = 3


def departed():
    data = db.collection(u'S001').document(u'Slot002')

    data.set({
        u'status': 4,
        u'departure_time': time.time()
    }, merge=True)
    global status
    status = 4


# Create an Event for notifying main thread.
callback_done = threading.Event()


# Create a callback on_snapshot function to capture changes
def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        global status
        status = doc.to_dict().get(u'status')
    callback_done.set()


doc_ref = db.collection(u'S001').document(u'Slot002')

# Watch the document
doc_watch = doc_ref.on_snapshot(on_snapshot)
