from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='areagaleria',
            old_name='id_Area',
            new_name='idArea',
        ),
        migrations.RenameField(
            model_name='galeria',
            old_name='id_Area',
            new_name='idArea',
        ),
    ]
