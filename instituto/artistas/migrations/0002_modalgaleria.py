from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModalGaleria',
            fields=[
                ('id_Modal', models.AutoField(db_column='idModal', primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
