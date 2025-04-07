from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    event_name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.event_name


class Ticket(models.Model):
    ticket_holder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users_tickets"
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="event_tickets"
    )
    date_issued = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket for {self.ticket_holder} to {self.event}"
