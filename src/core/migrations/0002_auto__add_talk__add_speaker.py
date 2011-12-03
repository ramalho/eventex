# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Talk'
        db.create_table('core_talk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('day', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')(blank=True)),
        ))
        db.send_create_signal('core', ['Talk'])

        # Adding M2M table for field speaker on 'Talk'
        db.create_table('core_talk_speaker', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('talk', models.ForeignKey(orm['core.talk'], null=False)),
            ('speaker', models.ForeignKey(orm['core.speaker'], null=False))
        ))
        db.create_unique('core_talk_speaker', ['talk_id', 'speaker_id'])

        # Adding model 'Speaker'
        db.create_table('core_speaker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Speaker'])


    def backwards(self, orm):
        
        # Deleting model 'Talk'
        db.delete_table('core_talk')

        # Removing M2M table for field speaker on 'Talk'
        db.delete_table('core_talk_speaker')

        # Deleting model 'Speaker'
        db.delete_table('core_speaker')


    models = {
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
