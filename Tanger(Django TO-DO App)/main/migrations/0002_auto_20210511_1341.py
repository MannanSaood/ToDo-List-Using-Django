# Generated by Django 3.2.2 on 2021-05-11 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('delete_user_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.todolist')),
            ],
        ),
    ]
