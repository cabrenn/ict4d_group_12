import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Offer(models.Model):
    RICE = 'RE'
    COTTON = 'CN'
    SORGHUM = 'SM'
    SEED_TYPES_CHOICES = (
        (RICE, 'Rice'),
        (COTTON, 'Cotton'),
        (SORGHUM, 'Sorghum'),
    )
    seed_type = models.CharField(
        max_length=2,
        choices=SEED_TYPES_CHOICES,
        default=RICE,
    )
    amount_of_seeds = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(999),
            MinValueValidator(1)
        ]
    )
    days_online = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(90),
            MinValueValidator(1)
        ]
    )