from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(verify_exists=False)
    email = models.EmailField()
    description = models.TextField()

    def __unicode__(self):
        return unicode(self.name)


class Talk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    day = models.DateField(blank=True)
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
