# Generated by Django 4.2.20 on 2025-04-19 21:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Medida",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre_corto",
                    models.CharField(default="Actualizar", max_length=300),
                ),
                ("indicador", models.CharField(max_length=300)),
                ("forma_calculo", models.CharField(max_length=300)),
                ("frecuencia_reporte", models.CharField(max_length=300)),
                (
                    "medios_verificacion",
                    models.CharField(default="Actualizar", max_length=300),
                ),
                (
                    "tipo_regulatoria",
                    models.CharField(default="Actualizar", max_length=300),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="OrganismoSectorial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100, unique=True)),
                ("tipo", models.CharField(max_length=100)),
                ("contacto", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100, unique=True)),
                ("descripcion", models.CharField(max_length=100)),
                ("fecha_inicio", models.DateField()),
                ("fecha_termino", models.DateField()),
                ("responsable", models.CharField(max_length=100)),
                ("estado", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="PlanOrganismoSectorial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id_media",
                    models.ForeignKey(
                        db_column="id_media",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="api.medida",
                    ),
                ),
                (
                    "id_organismo_sectorial",
                    models.ForeignKey(
                        db_column="id_organismo_sectorial",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="api.organismosectorial",
                    ),
                ),
                (
                    "id_plan",
                    models.ForeignKey(
                        db_column="id_plan",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="api.plan",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TipoMedida",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100, unique=True)),
                ("descripcion", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Reporte",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "valor_reportado",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("fecha_reporte", models.DateField()),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id_plan_organismo_sectorial",
                    models.ForeignKey(
                        db_column="id_plan_organismo_sectorial",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="api.planorganismosectorial",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="medida",
            name="id_tipo_medida",
            field=models.ForeignKey(
                db_column="id_tipo_medida",
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="api.tipomedida",
            ),
        ),
    ]
