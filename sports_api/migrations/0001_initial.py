# Generated by Django 2.1.2 on 2018-10-23 06:48

from django.db import migrations, models
import djongo.models.fields
import sports_api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('text', models.CharField(max_length=200)),
                ('id_str', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('created_at', models.CharField(max_length=200)),
                ('links', djongo.models.fields.ArrayModelField(model_container=sports_api.models.Link, model_form_class=sports_api.models.LinkForm)),
            ],
        ),
    ]