# Generated by Django 4.1.4 on 2022-12-24 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_alter_document_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='logo',
            field=models.ImageField(blank=True, default='pdflogo.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='ExtractedText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True, null=True)),
                ('file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.document')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
