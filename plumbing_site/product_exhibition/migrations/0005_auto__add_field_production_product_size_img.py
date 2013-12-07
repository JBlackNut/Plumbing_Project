# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Production.product_size_img'
        db.add_column(u'product_exhibition_production', 'product_size_img',
                      self.gf('django.db.models.fields.files.ImageField')(default='pic_folder/default_image.jpg', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Production.product_size_img'
        db.delete_column(u'product_exhibition_production', 'product_size_img')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'product_exhibition.author': {
            'Meta': {'object_name': 'Author'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_profile': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '50'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name_eng': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '15'}),
            'profile_img': ('django.db.models.fields.files.ImageField', [], {'default': "'pic_folder/default_image.jpg'", 'max_length': '100'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'product_exhibition.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_ch': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '50'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '50'})
        },
        u'product_exhibition.elementary': {
            'Meta': {'object_name': 'Elementary'},
            'characteristic_ch': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '150'}),
            'characteristic_en': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_ch': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '50'}),
            'material_en': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '80'}),
            'name_ch': ('django.db.models.fields.CharField', [], {'default': "'None'", 'unique': 'True', 'max_length': '50'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': "'None'", 'unique': 'True', 'max_length': '80'})
        },
        u'product_exhibition.new': {
            'Meta': {'object_name': 'New'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'product_exhibition.production': {
            'Meta': {'object_name': 'Production'},
            'detail_ch': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '150'}),
            'detail_en': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_ch': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '100'}),
            'material_en': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '80'}),
            'product_brand_ch': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '50'}),
            'product_brand_en': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '80'}),
            'product_category_en': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product_exhibition.Category']"}),
            'product_char_ch': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '150'}),
            'product_char_en': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '150'}),
            'product_img': ('django.db.models.fields.files.ImageField', [], {'default': "'pic_folder/default_image.jpg'", 'max_length': '100'}),
            'product_name_ch': ('django.db.models.fields.CharField', [], {'default': "'None'", 'unique': 'True', 'max_length': '50'}),
            'product_name_en': ('django.db.models.fields.CharField', [], {'default': "'None'", 'unique': 'True', 'max_length': '80'}),
            'product_performance_ch': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '80'}),
            'product_performance_en': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '150'}),
            'product_price_en': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '100'}),
            'product_size_ch': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '100'}),
            'product_size_en': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '150'}),
            'product_size_img': ('django.db.models.fields.files.ImageField', [], {'default': "'pic_folder/default_image.jpg'", 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'None'", 'unique': 'True', 'max_length': '50'}),
            'work_environment_ch': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '150'}),
            'work_environment_en': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '100'})
        }
    }

    complete_apps = ['product_exhibition']