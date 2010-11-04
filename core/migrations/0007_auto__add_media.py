# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Media'
        db.create_table('core_media', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('talk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Talk'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('media_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['Media'])


    def backwards(self, orm):
        
        # Deleting model 'Media'
        db.delete_table('core_media')


    models = {
        'core.contact': {
            'Meta': {'object_name': 'Contact'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Speaker']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.course': {
            'Meta': {'object_name': 'Course', '_ormbases': ['core.Talk']},
            'notes': ('django.db.models.fields.TextField', [], {}),
            'slots': ('django.db.models.fields.IntegerField', [], {}),
            'talk_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Talk']", 'unique': 'True', 'primary_key': 'True'})
        },
        'core.media': {
            'Meta': {'object_name': 'Media'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Talk']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'core.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'core.talk': {
            'Meta': {'object_name': 'Talk'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speaker': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Speaker']", 'symmetrical': 'False'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']
