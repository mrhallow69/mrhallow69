# Generated by Django 4.1.5 on 2023-01-22 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=89)),
                ('Author_Name', models.CharField(max_length=89)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=89)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stud_Password', models.IntegerField()),
                ('Stud_Name', models.CharField(max_length=90)),
                ('Stud_Phno', models.BigIntegerField()),
                ('Stud_Sems', models.IntegerField()),
                ('Course_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryD.course')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_Date', models.DateField()),
                ('End_Date', models.DateField()),
                ('Book_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryD.books')),
                ('Stud_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryD.student')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='Course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryD.course'),
        ),
    ]
