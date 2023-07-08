from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0002_rename_id_area_areagaleria_idarea_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='fecha_creacion',
            field=models.DateField(),
        ),
    ]
