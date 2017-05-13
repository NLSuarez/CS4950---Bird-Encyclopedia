from __future__ import with_statement
from django.core.files import File
from apps.birds.models import Bird
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Uploads media files from the UploadData directory for birds that don\'t already have them in the database.'

    def handle(self, *args, **options):
        birdObjects = Bird.objects.all()

        for bird in birdObjects:
            if not bird.image: #If no image
                try:
                    imagePath = "UploadData/Media/Picture/%s/male.jpg" % (bird.name)
                    newimagename = "%s.jpg" % (bird.name)
                    f=File(open(imagePath, 'rb'))
                    bird.image.save(newimagename, f)
                    f.close()
                    self.stdout.write(self.style.SUCCESS("%s now has an image!" % (bird.name)))
                except:
                    self.stdout.write(self.style.NOTICE("An error occurred with the image of %s" % (bird.name)))
            if not bird.sound: #If no sound
                try:
                    audioPath = "UploadData/Media/Audio/%s.mp3" % (bird.name)
                    newaudioname = "%s.mp3" % (bird.name)
                    f=File(open(audioPath, 'rb'))
                    bird.sound.save(newaudioname, f)
                    f.close()
                    self.stdout.write(self.style.SUCCESS("%s now has sound!" % (bird.name)))
                except:
                    self.stdout.write(self.style.NOTICE("An error occurred with the sound of %s" % (bird.name)))
