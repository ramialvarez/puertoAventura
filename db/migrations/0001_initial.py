# Generated by Django 5.0.4 on 2024-05-18 23:50

import db.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Conversacion',
                'verbose_name_plural': 'Conversaciones',
                'db_table': 'conversations',
            },
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Puerto',
                'verbose_name_plural': 'Puertos',
                'db_table': 'ports',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, verbose_name='Email')),
                ('password', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('surname', models.CharField(max_length=20, verbose_name='Apellido')),
                ('birthdate', models.DateField(verbose_name='Fecha de nacimiento')),
                ('type_user', models.IntegerField(default=0, verbose_name='Tipo de usuario')),
                ('phone_number', models.PositiveBigIntegerField(verbose_name='Número de teléfono')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('is_blocked', models.BooleanField(default=False, verbose_name='Bloquear')),
                ('verification_requested', models.BooleanField(default=False, verbose_name='Solicita verificacion')),
                ('recovery_ID', models.IntegerField(blank=True, null=True, verbose_name='Id de recuperacion')),
                ('tries_left', models.IntegerField(default=5, verbose_name='Intentos restantes')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eslora', models.DecimalField(decimal_places=3, max_digits=12)),
                ('patent', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=db.models.Post.get_image_upload_path, verbose_name='Imagen')),
                ('title', models.CharField(max_length=30, verbose_name='Titulo')),
                ('value', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor')),
                ('ship_type', models.CharField(choices=[('Barco Motor', 'Barco Motor'), ('Velero', 'Velero'), ('Yate', 'Yate'), ('Catamaran', 'Catamaran'), ('Semirigida', 'Semirigida'), ('Gomon', 'Gomon'), ('Pesca paseo', 'Pesca paseo'), ('Lancha', 'Lancha'), ('Goleta', 'Goleta'), ('Bote', 'Bote'), ('Otro', 'Otro')], max_length=11, verbose_name='Tipo de embarcación')),
                ('model', models.CharField(max_length=20, verbose_name='Modelo')),
                ('state', models.IntegerField(default=0, verbose_name='Estado')),
                ('post_date', models.DateField(auto_now_add=True, verbose_name='Fecha de publicacion')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Fecha de finalizacion')),
                ('port', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.port', verbose_name='Puerto')),
                ('saved_by', models.ManyToManyField(related_name='saved_posts', to='db.user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.user')),
            ],
            options={
                'verbose_name': 'Publicacion',
                'verbose_name_plural': 'Publicaciones',
                'db_table': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=db.models.Offer.get_image_upload_path, verbose_name='Imagen')),
                ('description', models.CharField(max_length=300, verbose_name='Descripción')),
                ('answer', models.IntegerField(blank=True, default=0)),
                ('date', models.DateField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.user')),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Ofertas',
                'db_table': 'offers',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300, verbose_name='Ingrese el mensaje')),
                ('date', models.DateField()),
                ('answer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.user')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=1, max_digits=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='db.user')),
            ],
            options={
                'verbose_name': 'Calificacion',
                'verbose_name_plural': 'Calificaciones',
                'db_table': 'rating',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db.comment')),
                ('conversation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db.conversation')),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db.offer')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.user')),
            ],
            options={
                'verbose_name': 'Notificacion',
                'verbose_name_plural': 'Notificaciones',
                'db_table': 'notifications',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('sent_at', models.DateTimeField()),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.conversation')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='db.user')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='db.user')),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
                'db_table': 'messages',
            },
        ),
        migrations.AddField(
            model_name='conversation',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_conversations', to='db.user'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_conversations', to='db.user'),
        ),
    ]
