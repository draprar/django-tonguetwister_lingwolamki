from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import OldPolish

@registry.register_document
class OldPolishDocument(Document):
    class Index:
        name = 'oldpolish_words'

        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 1
        }

    class Django:
        model = OldPolish
        fields = ['old_text', 'new_text']