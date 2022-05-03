# Generated by Django 2.1.1 on 2018-10-24 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('accountNumber', models.AutoField(primary_key=True, serialize=False)),
                ('accountBalance', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Indian amount')),
                ('accountType', models.CharField(choices=[('SB', 'Savings'), ('LB', 'Loan'), ('IB', 'Insurance')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerID', models.AutoField(primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('customerAge', models.IntegerField(max_length=30)),
                ('profileImage', models.ImageField(blank=True, null=True, upload_to='customerImages')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Accounts', to='customerInfo.Customer'),
        ),
    ]