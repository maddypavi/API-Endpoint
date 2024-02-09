from common.serializers import BaseSerializer
from dummy.models import Author


class AuthorSerializer(BaseSerializer):
    class Meta:
        model = Author
        fields = BaseSerializer.Meta.fields + ["id", "name", "age"]
