from common.http import make_request
from pathlib import Path
import json
from django.db.models import Q, Case, When, Value, BooleanField
from dummy.models import Author

def get_legal_authors():
    return Author.objects.annotate(
        legal=Case(
            When(
                Q(age__gt=18),
                then=Value(True)
            ),
            default=Value(False),
            output_field=BooleanField()
        )
    ).filter(legal=True)

def run():
    legal_authors = get_legal_authors()
    print(legal_authors)
