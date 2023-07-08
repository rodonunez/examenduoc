from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0002_modalgaleria'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeria',
            name='modalidad',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
