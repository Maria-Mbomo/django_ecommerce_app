# Generated by Django 3.2.5 on 2021-07-30 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210729_1604'),
    ]

    operations = [
        migrations.RunSQL("""
         insert into store_collection (title) 
         values ('collection1' )                 
                          """,
                          """ 
        delete from store_collection
        where title = 'collection1' 
                          """
                          )
    ]
