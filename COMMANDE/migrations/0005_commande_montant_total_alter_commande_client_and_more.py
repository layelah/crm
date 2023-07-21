# Generated by Django 4.1.7 on 2023-06-29 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CLIENT', '0005_client_email'),
        ('PRODUIT', '0004_produit_quantite_stock_alter_tags_nom'),
        ('COMMANDE', '0004_alter_commande_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='montant_total',
            field=models.FloatField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='commande',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CLIENT.client'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='produit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PRODUIT.produit'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='status',
            field=models.CharField(choices=[('livraison en cours', 'Livraison en cours'), ('non livré', 'Non livré'), ('livré', 'Livré')], max_length=200, null=True),
        ),
    ]