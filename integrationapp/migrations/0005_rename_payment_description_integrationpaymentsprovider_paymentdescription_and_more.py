# Generated by Django 5.0.6 on 2024-08-15 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "integrationapp",
            "0004_rename_paymentdescription_integrationpaymentsprovider_payment_description_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="integrationpaymentsprovider",
            old_name="payment_description",
            new_name="paymentDescription",
        ),
        migrations.RenameField(
            model_name="integrationpaymentsprovider",
            old_name="payment_method",
            new_name="paymentMethod",
        ),
        migrations.RenameField(
            model_name="integrationpaymentsprovider",
            old_name="payment_periods",
            new_name="paymentPeriods",
        ),
        migrations.RenameField(
            model_name="integrationpaymentsprovider",
            old_name="pk_integration_eva_status",
            new_name="pkintegrationevastatus",
        ),
        migrations.RenameField(
            model_name="integrationpaymentsprovider",
            old_name="policy_number",
            new_name="policyNumber",
        ),
        migrations.RenameField(
            model_name="integrationpaymentsprovider",
            old_name="provider_name",
            new_name="providerName",
        ),
        migrations.RenameField(
            model_name="integrationpaymentsprovider",
            old_name="send_notification",
            new_name="sendNotification",
        ),
        migrations.RenameField(
            model_name="integrationpaymentsprovider",
            old_name="total_paid",
            new_name="totalPaid",
        ),
        migrations.RenameField(
            model_name="integrationpaymentsprovider",
            old_name="transaction_date",
            new_name="transactionDate",
        ),
        migrations.RenameField(
            model_name="integrationpaymentsprovider",
            old_name="transaction_id",
            new_name="transactionId",
        ),
    ]
