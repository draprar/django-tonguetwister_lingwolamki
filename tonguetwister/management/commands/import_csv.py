import csv
import os
from django.core.management.base import BaseCommand
from tonguetwister.models import Twister, OldPolish


class Command(BaseCommand):
    help = 'Import data from CSV files into the MySQL database'

    def handle(self, *args, **kwargs):
        files = {
            'twister': '/home/lingwolamki/django-tonguetwister/twister.csv',
            'old_polish': '/home/lingwolamki/django-tonguetwister/oldpolish.csv'
        }

        for label, file_path in files.items():
            if not os.path.exists(file_path):
                self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
                continue

            model = Twister if label == 'twister' else OldPolish

            records = []
            try:
                with open(file_path, mode='r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        records.append(model(**row))

                model.objects.bulk_create(records)
                self.stdout.write(self.style.SUCCESS(f"{label.capitalize()} data imported successfully!"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error importing {label}: {e}"))
