#-*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Speaker(models.Model):
    name = models.CharField(_(u'nome'), max_length=255)
    slug = models.SlugField()
    url = models.URLField(verify_exists=False)
    description = models.TextField(_(u'descrição'), blank=True)
    avatar = models.FileField(_('foto'), upload_to='palestrantes', blank=True, null=True)

    class Meta:
        verbose_name = _('Palestrante')

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

    speaker = models.ForeignKey('Speaker', verbose_name=_('Palestrante'))
    kind = models.CharField(_('Tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('Valor'), max_length=255)

    objects = models.Manager()
    phones = KindContactManager('P')
    emails = KindContactManager('E')
    faxes = KindContactManager('F')

    class Meta:
        verbose_name = _('Contato')

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
    title = models.CharField(_(u'título'), max_length=200)
    description = models.TextField(_(u'descrição'), blank=True)
    start_time = models.TimeField(_(u'horário'), blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_('palestrante'))

    objects = PeriodManager()

    class Meta:
        verbose_name = _('Palestra')

    def __unicode__(self):
        return unicode(self.title)


class Course(Talk):
    slots = models.IntegerField()
    notes = models.TextField()

    class Meta:
        verbose_name = _('Curso')


class CodingCourse(Course):
    class Meta:
        proxy = True

    def do_some_python_stuff(self):
        return "Let's hack! at %s" % self.title


class Media(models.Model):
    MEDIAS = (
        ('SL', 'SlideShare'),
        ('YT', 'Youtube'),
    )

    talk = models.ForeignKey('Talk')
    type = models.CharField(max_length=3, choices=MEDIAS)
    title = models.CharField(u'Título', max_length=255, help_text=u'No caso do slideshare será usado como doc_id.')
    media_id = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s - %s' % (self.talk.title, self.title)
