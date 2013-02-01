# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Book.subject'
        db.delete_column('books_book', 'subject')

        # Deleting field 'Book.language'
        db.delete_column('books_book', 'language')

        # Deleting field 'Book.notes'
        db.delete_column('books_book', 'notes')

        # Adding field 'Book.start_date'
        db.add_column('books_book', 'start_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Book.subject'
        db.add_column('books_book', 'subject',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True),
                      keep_default=False)

        # Adding field 'Book.language'
        db.add_column('books_book', 'language',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True),
                      keep_default=False)

        # Adding field 'Book.notes'
        db.add_column('books_book', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=1000, blank=True),
                      keep_default=False)

        # Deleting field 'Book.start_date'
        db.delete_column('books_book', 'start_date')


    models = {
        'books.author': {
            'Meta': {'object_name': 'Author'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'another_field': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['books.Author']", 'symmetrical': 'False'}),
            'date_finished': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['books']