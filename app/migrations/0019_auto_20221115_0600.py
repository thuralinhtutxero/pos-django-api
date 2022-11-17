# Generated by Django 3.2.9 on 2022-11-14 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20221110_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='is_digits',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='salesthreedigits',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='luckyNumber_three', to='app.threedigitsgroup'),
        ),
        migrations.AlterField(
            model_name='salestwodigits',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='luckyNumber_two', to='app.twodigitsgroup'),
        ),
        migrations.AlterField(
            model_name='threedigits',
            name='sales',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='three_sales_digits', to='app.salesthreedigits'),
        ),
        migrations.AlterField(
            model_name='twodigits',
            name='sales',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='two_sales_digits', to='app.salestwodigits'),
        ),
    ]
