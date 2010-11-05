# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Speaker.email'
        db.delete_column('core_speaker', 'email')


    def backwards(self, orm):
        
        # We cannot add back in field 'Speaker.email'
        raise RuntimeError(
            "Cannot reverse this migration. 'Speaker.email' and its values cannot be restored.")


    models = {
        'core.contact': {
            'Meta': {'object_name': 'Contact'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Speaker']"}),
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
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
