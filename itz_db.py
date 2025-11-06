"""
raika_db.py
MongoDB connection helper for Raika bot.
Automatically detects TLS requirement.
"""

import os
import time
from pymongo import MongoClient, errors

MONGO_URL = os.environ.get("MONGO_URL", "")
DB_NAME = os.environ.get("MONGO_DBNAME", "raika_db")


def get_client(retries=5, delay=2):
    if not MONGO_URL:
        raise RuntimeError("❌ MONGO_URL environment variable is not set.")
    last_exc = None

    # Automatically decide TLS mode
    use_tls = "mongodb+srv://" not in MONGO_URL
    print(f"[RaikaDB] Connecting to MongoDB (TLS={use_tls})...")

    for attempt in range(1, retries + 1):
        try:
            client = MongoClient(
                MONGO_URL,
                serverSelectionTimeoutMS=5000,
                tls=use_tls,
                tlsAllowInvalidCertificates=True,
            )
            client.server_info()  # Force connection test
            print("✅ Connected to MongoDB successfully!")
            return client
        except errors.ServerSelectionTimeoutError as e:
            last_exc = e
            print(f"[RaikaDB] Attempt {attempt}/{retries} failed: {e}")
            time.sleep(delay)

    raise last_exc


def get_db():
    client = get_client(retries=10, delay=3)
    return client[DB_NAME]
