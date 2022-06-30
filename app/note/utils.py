import uuid
from datetime import datetime
import os


def random_address_generator():
    return uuid.uuid4().hex


def timeout_occurred(added_datetime):
    now = datetime.now()
    interval_seconds = (now - added_datetime.replace(tzinfo=None)).total_seconds()

    return interval_seconds >= int(os.getenv('POST_TIMEOUT', 60))
