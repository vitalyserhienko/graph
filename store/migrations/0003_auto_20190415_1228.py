# Generated by Django 2.2 on 2019-04-15 12:28

from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20190414_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(upload_to='product/images/'),
        ),
    ]
