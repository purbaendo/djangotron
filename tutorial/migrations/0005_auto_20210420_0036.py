# Generated by Django 3.1.7 on 2021-04-19 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0004_auto_20210419_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('', ''), ('html', 'HTML'), ('css', 'CSS'), ('bootstrap', 'BOOTSTRAP'), ('sass', 'SASS'), ('flexbox', 'FLEXBOX'), ('javascript', 'JAVASCRIPT'), ('jquery', 'JQUERY'), ('ajax', 'AJAX'), ('json', 'JSON'), ('react', 'REACT'), ('angular', 'ANGULAR'), ('nodejs', 'NODEJS'), ('vuejs', 'VUEJS'), ('graphql', 'GRAPHQL'), ('php', 'PHP'), ('laravel', 'LARAVEL'), ('codeigniter', 'CODEIGNITER'), ('python', 'PYTHON'), ('django', 'DJANGO'), ('flask', 'FLASK'), ('numpy', 'NUMPY'), ('scipy', 'SCIPY'), ('pandas', 'PANDAS'), ('matplotlib', 'MATPLOTLIB'), ('tensorflow', 'TENSORFLOW'), ('pytorch', 'PYTORCH'), ('scikitlearn', 'SCIKITLEARN'), ('keras', 'KERAS'), ('opencv', 'OPENCV'), ('tkinter', 'TKINTER'), ('qt', 'QT'), ('pygame', 'PYGAME'), ('kivy', 'KIVY'), ('sql', 'SQL'), ('mysql', 'MYSQL'), ('postgresql', 'POSTGRESQL'), ('java', 'JAVA'), ('git', 'GIT'), ('android', 'ANDROID'), ('ios', 'IOS')], max_length=20),
        ),
    ]