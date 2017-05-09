#This file was used on python 2.7. It will not work if run in python 3.

from __future__ import with_statement
import csv
from apps.birds.models import Bird

'''While I might wish to add customizable file inputs to this later, this will
take a properly formatted csv file and upload it as a bird object to the database.'''

def upload_csv():
    csvfilepath = '/home/stefan/Documents/CS4950GroupProject/StanislausBirds/Scripts/waterfowl.csv'

    with open(csvfilepath) as csvfile:
        birdreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        row_num = 1
        for row in birdreader:
            if row_num > 1:
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
                except:
                    print "An error occurred at row %d" % (row_num)
            row_num += 1

upload_csv()
