from __future__ import with_statement
import csv
from apps.birds.models import Bird
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Uploads objects generated from a csv file that aren\'t already in the database.'

    def add_arguments(self, parser):
        parser.add_argument('file_id', type=str)

    def handle(self, *args, **options):
        #Debug statement
        #self.stdout.write(options['file_id'])
        with open(options['file_id'], encoding="utf8") as csvfile:
            birdreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            row_num = 1
            for row in birdreader:
                if row_num > 1:
                    try:
                        Bird.objects.get(name=row[0])
                        self.stdout.write(self.style.NOTICE("Bird %s already exists!" % (row[0])))
                    except Bird.DoesNotExist:
                        new_bird = Bird()
                        new_bird.name = row[0]
                        #Take the name and replace spaces with -
                        hyphenatedSlug = "-".join(new_bird.name.split())
                        #Then take that string and remove all apostrophes
                        new_bird.slug = hyphenatedSlug.replace("\'", "")
                        new_bird.species = row[1]
                        new_bird.description = row[2]
                        #There are two fields that will never be filled out here, so skip them to row[5]
                        new_bird.diet = row[5]
                        new_bird.sleep = row[6]
                        new_bird.habitat = row[7]
                        try:
                            new_bird.save()
                            self.stdout.write(self.style.SUCCESS("%s was successfully added!" % (new_bird.name)))
                            """
                            #Add these in and comment out save for debugging.
                            self.stdout.write(self.style.SUCCESS(new_bird.slug))
                            self.stdout.write(self.style.SUCCESS(new_bird.species))
                            self.stdout.write(self.style.SUCCESS(new_bird.description))
                            self.stdout.write(self.style.SUCCESS(new_bird.diet))
                            self.stdout.write(self.style.SUCCESS(new_bird.sleep))
                            self.stdout.write(self.style.SUCCESS(new_bird.habitat))
                            """
                        except:
                            self.stdout.write(self.style.NOTICE("An error occurred at row %d" % (row_num)))
                row_num += 1

            csvfile.close()
