# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Course'
        db.create_table('core_course', (
            ('talk_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Talk'], unique=True, primary_key=True)),
            ('slots', self.gf('django.db.models.fields.IntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Course'])


    def backwards(self, orm):
        
        # Deleting model 'Course'
        db.delete_table('core_course')


    models = {
        'core.course': {
            'Meta': {'object_name': 'Course', '_ormbases': ['core.Talk']},
            'notes': ('django.db.models.fields.TextField', [], {}),
            'slots': ('django.db.models.fields.IntegerField', [], {}),
            'talk_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Talk']", 'unique': 'True', 'primary_key': 'True'})
        },
        'core.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'core.talk': {
            'Meta': {'object_name': 'Talk'},
            'day': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speaker': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Speaker']", 'symmetrical': 'False'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']
