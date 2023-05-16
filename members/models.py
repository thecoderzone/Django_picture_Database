from django.db import models


# Create your models here.
class Members(models.Model):
    """
    Models for members
    """

    title = models.CharField(verbose_name="Title", max_length=3)
    fullname = models.CharField(verbose_name="fullname", max_length=50)
    member = models.BooleanField(default=False)
    address = models.TextField(verbose_name="address of member", max_length=150)
    image = models.FilePathField(path="/image")
    phone = models.BigIntegerField(default=False)

    def __str__(self):
        """
        Returning instance in database
        """
        return f"Member detail {self.fullname} {self.address} {self.image}"
