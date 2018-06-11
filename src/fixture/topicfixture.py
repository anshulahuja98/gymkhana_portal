import factory
import random
from fixture.userfixture import UserProfileFactory

TAG = ['android', 'win', 'ios', 'mac', 'tv', 'mi', 'cube', 'django', 'python', 'c', 'c++', 'perl', 'neo4j'

       ]


class TopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'forum.Topic'

    author = factory.SubFactory(UserProfileFactory)
    category = random.choice(['Q', 'F'])
    title = factory.Faker('sentence', nb_words=4)
    content = factory.Faker('sentence', nb_words=30)
    tags = random.choice(TAG) + ',' + random.choice(TAG) + ',' + random.choice(TAG)
    # upvotes = models.ManyToManyField(UserProfile, blank=True, related_name='topic_upvotes')
    slug = factory.Sequence(lambda n: 'topic-%d' % n)
