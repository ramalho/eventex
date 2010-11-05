#-*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Speaker(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    url = models.URLField(verify_exists=False)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class KindContactManager(models.Manager):
    def __init__(self, kind):
        super(KindContactManager, self).__init__()
        self.kind = kind

    def get_query_set(self):
        qs = super(KindContactManager, self).get_query_set()
        qs = qs.filter(kind=self.kind)
        return qs

class Contact(models.Model):
    KINDS = (
        ('P', _('Telefone')),
        ('E', _('E-mail')),
        ('F', _('Fax')),
    )

    speaker = models.ForeignKey('Speaker')
    kind = models.CharField(max_length=1, choices=KINDS)
    value = models.CharField(max_length=255)

    objects = models.Manager()
    phones = KindContactManager('P')
    emails = KindContactManager('E')
    faxes = KindContactManager('F')

    def __unicode__(self):
        return u'%s, %s' % (self.kind, self.value)


class PeriodManager(models.Manager):
    midday = datetime.time(12)

    def at_morning(self):
        qs = self.filter(start_time__lt=self.midday)
        qs = qs.order_by('start_time')
        return qs

    def at_afternoon(self):
        qs = self.filter(start_time__gte=self.midday)
        qs = qs.order_by('start_time')
        return qs


class Talk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.TimeField(blank=True)

    objects = PeriodManager()

    speaker = models.ManyToManyField('Speaker')

    def __unicode__(self):
        return unicode(self.title)


class Course(Talk):
    slots = models.IntegerField()
    notes = models.TextField()


class CodingCourse(Course):
    class Meta:
        proxy = True

    def do_some_python_stuff(self):
        return "Let's hack! at %s" % self.title


MEDIA_TYPES = (
    ('SL', 'SlideShare'),
    ('YT', 'Youtube'),
)
class Media(models.Model):
    talk = models.ForeignKey('Talk')
    type = models.CharField(max_length=3, choices=MEDIA_TYPES)
    title = models.CharField(u'Título (no caso do slideshare será usado como doc_id)', max_length=255)
    media_id = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s - %s' % (self.talk.title, self.title)
