#Run on python 3.5 in django 1.11

from apps.birds.models import Bird

birdObjects = Bird.objects.all()

for bird in birdObjects:
    hyphenatedSlug = "-".join(bird.name.split())
    bird.slug = hyphenatedSlug.replace("\'", "")
    print(bird.slug)
    bird.save()
