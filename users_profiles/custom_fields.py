from django.db.models import Field
from datetime import datetime

class EpochDateTimeField(Field):
    def to_python(self, value):
        if value is None:
            return None
        return datetime.fromtimestamp(value)

    def get_prep_value(self, value):
        if value is None:
            return None
        return int(value.timestamp())
