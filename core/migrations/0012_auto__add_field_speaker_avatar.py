# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing M2M table for field speaker on 'Talk'
        db.delete_table('core_talk_speaker')

        # Adding M2M table for field speakers on 'Talk'
        db.create_table('core_talk_speakers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('talk', models.ForeignKey(orm['core.talk'], null=False)),
            ('speaker', models.ForeignKey(orm['core.speaker'], null=False))
        ))
        db.create_unique('core_talk_speakers', ['talk_id', 'speaker_id'])

        # Adding field 'Speaker.avatar'
        db.add_column('core_speaker', 'avatar', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding M2M table for field speaker on 'Talk'
        db.create_table('core_talk_speaker', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('talk', models.ForeignKey(orm['core.talk'], null=False)),
            ('speaker', models.ForeignKey(orm['core.speaker'], null=False))
        ))
        db.create_unique('core_talk_speaker', ['talk_id', 'speaker_id'])

        # Removing M2M table for field speakers on 'Talk'
        db.delete_table('core_talk_speakers')

        # Deleting field 'Speaker.avatar'
        db.delete_column('core_speaker', 'avatar')


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
            'avatar': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'core.talk': {
            'Meta': {'object_name': 'Talk'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Speaker']", 'symmetrical': 'False'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']
