import firebase_admin
from firebase_admin import auth, credentials
import os

cred = credentials.Certificate(os.getenv("FIREBASE_CREDENTIALS_JSON", "path/to/firebase_credentials.json"))
firebase_admin.initialize_app(cred)

def verify_token(token: str):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception:
        return None
