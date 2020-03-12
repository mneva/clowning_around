from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    is_troupe_leader = models.BooleanField(default=False)
    is_clown = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Troupe(models.Model):
    name = models.CharField(max_length=128)
    max_capacity = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class TroupeLeader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    troupe = models.ForeignKey(Troupe, on_delete=models.PROTECT)

    def __str__(self):
        return "{} leads {}".format(self.user.name, self.troupe)


class Clown(models.Model):
    CLOWN_RANKS = (
        (1, "Top Dan"),
        (2, "Some Bob"),
        (3, "Maybe Harry")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    rank = models.IntegerField()
    troupe = models.ForeignKey(Troupe, on_delete=models.PROTECT)

    def __str__(self):
        return "{} from {}".format(self.user.name, self.troupe.name)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    contact_name = models.CharField(_("Name"), max_length=128)
    contact_email = models.EmailField(_("Email"), unique=True)
    contact_number = models.CharField(_("Contact Number"), max_length=16)

    def __str__(self):
        return self.user.name


class Appointment(models.Model):
    STATUSES = (
        ("UPCOMING", "upcoming"),
        ("INCIPIENT", "incipient"),
        ("COMPLETED", "completed"),
        ("CANCELLED", "cancelled")
    )

    RATINGS = (
        (1, "disappointed"),
        (2, "slightly disappointed"),
        (3, "neither happy nor disappointed"),
        (4, "slightly happy"),
        (5, "happy"),
    )

    title = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUSES, default="UPCOMING")
    appointment_date = models.DateTimeField()
    rating = models.IntegerField(null=True, blank=True, choices=RATINGS)
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)


class Incident(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.PROTECT)
    incident_type = models.CharField(max_length=100)
    description = models.CharField(max_length=255)


class RequestContact(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.PROTECT)
    client = models.OneToOneField(Client, on_delete=models.PROTECT)
    reason = models.CharField(max_length=255)
