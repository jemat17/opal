"""
Clear the local lookup lists
"""
from django.core.management.base import BaseCommand

from opal.models import Synonym
from opal.core.lookuplists import LookupList

class Command(BaseCommand):
    """
    Management command to delete all lookuplists and related
    synonyms.
    """
    def delete(self):
        for model in LookupList.__subclasses__():
            try:
                for item in model.objects.all():
                    item.delete()
            except: 
                continue
        for item in Synonym.objects.all():
            item.delete()
        
    def handle(self, *args, **kw):
        self.delete()
