from django.db import models

# Create your models here.

class AppFieldUser(models.Model):
    name = models.TextField()
    phone_number = models.CharField(max_length=64, null=True, blank=True)
    id_number = models.CharField(max_length=64)
    active_status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    pass_phrase = models.TextField(null=True, blank=True)
    prefix = models.CharField(max_length=64, null=True, blank=True)
    company = models.IntegerField()  # ForeignKey to Company, can be updated later
    office = models.IntegerField()  # ForeignKey to CompanyOffice, can be updated later
    receipt_format = models.IntegerField(default=1)
    printer_name = models.CharField(max_length=64)
    profile_photo = models.TextField(null=True, blank=True)
    user_level = models.CharField(max_length=64, default='TELLER')
    preview_stages = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_field_user'
