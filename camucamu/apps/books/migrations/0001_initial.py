# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('books_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('books', ['Author'])

        # Adding model 'Book'
        db.create_table('books_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_finished', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_started', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('pages', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('publication_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
        ))
        db.send_create_signal('books', ['Book'])

        # Adding M2M table for field authors on 'Book'
        db.create_table('books_book_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['books.book'], null=False)),
            ('author', models.ForeignKey(orm['books.author'], null=False))
        ))
        db.create_unique('books_book_authors', ['book_id', 'author_id'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('books_author')

        # Deleting model 'Book'
        db.delete_table('books_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table('books_book_authors')


    models = {
        'books.author': {
            'Meta': {'object_name': 'Author'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['books.Author']", 'symmetrical': 'False'}),
            'date_finished': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_started': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'pages': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['books']