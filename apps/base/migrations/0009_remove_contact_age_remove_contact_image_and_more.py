# Generated by Django 5.0.7 on 2024-07-28 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0008_alter_contact_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="age",
        ),
        migrations.RemoveField(
            model_name="contact",
            name="image",
        ),
        migrations.RemoveField(
            model_name="contact",
            name="kastrasya",
        ),
    ]
