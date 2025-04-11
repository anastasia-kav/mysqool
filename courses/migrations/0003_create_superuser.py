from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.create(
        username='admin',
        email='admin@example.com',
        password=make_password('adminpassword123'),
        is_superuser=True,
        is_staff=True,
        is_active=True
    )


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_rename_title_course_name_remove_course_author_and_more'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
