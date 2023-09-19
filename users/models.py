from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(help_text="User Unique key", primary_key=True, default=0, editable=False)
    email = models.EmailField(help_text="User e-mail", blank=False, null=False)
    name = models.CharField(help_text="User Full Name", max_length=15, blank=False, null=False)
    password = models.CharField(help_text="User Password", max_length=20, blank=False, null=False)

    class Meta:
        verbose_name = "유저 정보"
        verbose_name_plural = "유저 정보"
        ordering = ["name"]