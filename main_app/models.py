from django.db import models
from django.urls import reverse


# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
class Pokemon(models.Model):
    name = models.CharField(max_length= 100, default='SOME CHAR')
    description = models.TextField(max_length= 100, default='SOME TEXT')
    attack = models.CharField(max_length= 100, default='SOME CHAR')
    weakness = models.CharField(max_length= 100, default='SOME CHAR')
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})


class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0])
    # Create a cat_id FK
pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"
            class Meta:
            ordering = ['-date']

class Toy(models.Model):
    name: models.CharField(max_length= 100, default="Name")
    color: models.CharField(max_length= 100, default="Color")