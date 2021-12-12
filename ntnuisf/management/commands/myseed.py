# imports
import random

from django_seed import Seed
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from accounts import models as account_models
from ...models import wiki as wiki_models
from ...models import songs as song_models
from ...models import events as event_models
from ...models import videos as video_models
from ...models import courses as course_models

User = get_user_model()

# End: imports -----------------------------------------------------------------

# OBS: seed() on instance was depricated for Faker module.
# Manually edited django-seed module __init__.py on line 35 from seed to seed_instance


# pylint: disable=all
class Command(BaseCommand):

    def i(self, x, y):  # pylint: disable=no-self-use
        return random.randint(x, y)

    def fake_rgba(self, x=0, y=255):
        r, g, b, a = self.i(x, y), self.i(x, y), self.i(x, y), random.choice([0.6, 0.7, 0.8, 0.9, 1])
        return f"rgba({r},{g},{b},{a})"

    def f(self):
        seeder = Seed.seeder()

        seeder.faker.seed_instance(1234)

        seeder.add_entity(User, 8, {})
        seeder.add_entity(
            account_models.Theme, 10, {
                'user': lambda x: None,
                'name': lambda x: seeder.faker.safe_color_name(),
                'background_color': lambda x: self.fake_rgba(),
                'text_color': lambda x: seeder.faker.safe_color_name(),
                'link_color': lambda x: seeder.faker.safe_color_name(),
                'link_hover_color': lambda x: seeder.faker.safe_color_name(),
            }
        )
        seeder.add_entity(video_models.Video, 5, {})
        seeder.add_entity(wiki_models.Folder, 5, {
            'title': lambda x: seeder.faker.word(),
            'root_folder': lambda x: None,
            'perm': lambda x: None,
        })
        seeder.add_entity(
            wiki_models.Page, 20, {
                'title': lambda x: seeder.faker.sentence(nb_words=2),
                'path': lambda x: seeder.faker.word() + f"{random.randint(0, 10000)}",
                'content': lambda x: seeder.faker.text(max_nb_chars=9000),
            }
        )
        seeder.add_entity(song_models.Tag, 10, {
            'title': lambda x: seeder.faker.word(),
            'context': lambda x: None,
        })
        seeder.add_entity(
            song_models.Song, 100, {
                'artist': lambda x: seeder.faker.word(),
                'title': lambda x: seeder.faker.sentence(nb_words=2),
                'bpm': lambda x: random.randint(60, 80),
            }
        )
        seeder.add_entity(
            course_models.Course, 25, {
                'title': lambda x: seeder.faker.sentence(nb_words=2),
                'comments': lambda x: seeder.faker.sentence(nb_words=4),
                'date': lambda x: seeder.faker.date_this_year(after_today=True),
                'day': lambda x: random.randint(1, 3),
                'bulk': lambda x: random.randint(1, 10),
                'comments': lambda x: seeder.faker.paragraphs(nb=2),
                'place': lambda x: seeder.faker.sentence(nb_words=3),
            }
        )
        seeder.add_entity(
            course_models.Section, 100, {
                'title': lambda x: seeder.faker.sentence(nb_words=2),
                'description': lambda x: seeder.faker.sentence(nb_words=50),
                'duration': lambda x: random.choice([5, 7.5, 7.5, 7.5, 10, 12, 15]),
            }
        )
        seeder.add_entity(
            event_models.Event, 4, {
                'title': lambda x: seeder.faker.sentence(nb_words=2),
                'description': lambda x: seeder.faker.sentence(nb_words=50),
                'place': lambda x: seeder.faker.sentence(nb_words=3),
            }
        )

        seeder.execute()

    def handle(self, *args, **options):
        self.f()
        # End of handle
