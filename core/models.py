import datetime
from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    url = models.URLField(verify_exists=False)
    email = models.EmailField()
    description = models.TextField()

    def __unicode__(self):
        return unicode(self.name)

class TalkMorningManager(models.Manager):
    def get_query_set(self):
        return super(TalkMorningManager, self).get_query_set().filter(start_time__lt=datetime.time(12)).order_by('start_time')

class TalkAfternoonManager(models.Manager):
    def get_query_set(self):
        return super(TalkAfternoonManager, self).get_query_set().filter(start_time__gte=datetime.time(12)).order_by('start_time')

class Talk(models.Model):

    objects = models.Manager()
    morning = TalkMorningManager()
    afternoon = TalkAfternoonManager()

    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.TimeField(blank=True)

    speaker = models.ManyToManyField('Speaker')

    def __unicode__(self):
        return unicode(self.title)

class Course(Talk):
    slots = models.IntegerField()
    notes = models.TextField()

CONTACT_TYPES = (
    ('P', 'Phone'),
    ('E', 'email'),
    ('F', 'fax'),
)

class Contact(models.Model):
    speaker = models.ForeignKey('Speaker')
    type = models.CharField(max_length=5, choices=CONTACT_TYPES)
    value = models.CharField(max_length=255)
