# Generated by Django 2.0.6 on 2018-06-27 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadd', '0007_auto_20180627_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comissao',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comissao_curso', to='sca.Curso'),
        ),
    ]