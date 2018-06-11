import factory
import random
from .societyfixture import SocietyFactory
from .userfixture import UserProfileFactory

COLOUR = ["yellow", "black", "purple", "red", "orange", "green", '#084594', '#2171b5', '#4292c6', '#6baed6', '#9ecae1',
          '#c6dbef', '#deebf7', '#f7fbff'
          ]
SKIN = [
    'white-skin', 'black-skin', 'cyan-skin', 'mdb-skin', 'deep-purple-skin', 'navy-blue-skin', 'pink-skin',
    'indigo-skin', 'light-blue-skin', 'grey-skin']


class ClubFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'main.Club'
        django_get_or_create = ('name',)

    name = factory.Faker('sentence', nb_words=2)
    society = factory.SubFactory(SocietyFactory)
    ctype = random.choice(['C', 'T'])
    description = factory.Faker('sentence', nb_words=30)
    cover = factory.django.ImageField(color=random.choice(COLOUR))
    skin = random.choice(SKIN)
    captain = factory.SubFactory(UserProfileFactory)
    vice_captain_one = factory.SubFactory(UserProfileFactory)
    vice_captain_two = factory.SubFactory(UserProfileFactory)
    mentor = factory.SubFactory(UserProfileFactory)
    # core_members.objects.set(UserProfile.objects.all()[random.randint(0, 30)])
    # gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL,
    resources_link = factory.Faker('url')
    custom_html = factory.Faker('sentence', nb_words=20)
    slug = factory.Sequence(lambda n: 'club-%d' % n)
    published = True
