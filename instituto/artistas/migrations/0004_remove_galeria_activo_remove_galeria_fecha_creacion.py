from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0003_alter_galeria_fecha_creacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galeria',
            name='activo',
        ),
        migrations.RemoveField(
            model_name='galeria',
            name='fecha_creacion',
        ),
    ]
