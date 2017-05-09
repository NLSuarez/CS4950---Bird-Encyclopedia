from apps.birds.models import Bird
from django.core.files import File

birdObjects = Bird.objects.all()

for bird in birdObjects:
    imagePath = "UploadData/Media/Picture/%s/male.jpg" % (bird.name)
    audioPath = "UploadData/Media/Audio/%s.mp3" % (bird.name)
    newaudioname = "%s.mp3" % (bird.name)
    newimagename = "%s.jpg" % (bird.name)
    #Add sound first
    f=File(open(audioPath, 'rb'))
    bird.sound.save(newaudioname, f)
    f.close()
    #Now add image
    f=File(open(imagePath, 'rb'))
    bird.image.save(newimagename, f)
    f.close()
