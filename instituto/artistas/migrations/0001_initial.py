from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaGaleria',
            fields=[
                ('id_Area', models.AutoField(db_column='idArea', primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=10)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('modalidad', models.CharField(blank=True, max_length=30, null=True)),
                ('historia', models.CharField(blank=True, max_length=200, null=True)),
                ('precio', models.IntegerField()),
                ('activo', models.IntegerField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('id_Area', models.ForeignKey(db_column='idArea', on_delete=django.db.models.deletion.CASCADE, to='artistas.areagaleria')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]
