import pint

from django.conf import settings
from django.db import models

from .utils import number_str_to_float
from .validators import validate_unit_of_measure


class Recipe(models.Model):
    """
    A model representing a recipe.

    Attributes:
        user (ForeignKey): The user who created the recipe.
        name (CharField): The name of the recipe.
        description (TextField): The description of the recipe.
        directions (TextField): The directions for making the recipe.
        timestamp (DateTimeField): The date and time the recipe was created.
        updated (DateTimeField): The date and time the recipe was last updated.
        active (BooleanField): Whether the recipe is active or not.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class RecipeIngredient(models.Model):
    """
    A model representing an ingredient used in a recipe.

    Attributes:
        recipe (ForeignKey): The recipe that this ingredient belongs to.
        name (CharField): The name of the ingredient.
        description (TextField): A description of the ingredient (optional).
        quanity (CharField): The quantity of the ingredient.
        unit (CharField): The unit of measurement for the quantity.
        directions (TextField): Directions for using the ingredient (optional).
        timestamp (DateTimeField): The date and time that this ingredient was created.
        updated (DateTimeField): The date and time that this ingredient was last updated.
        active (BooleanField): Whether this ingredient is currently active.
    """

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50, validators=[validate_unit_of_measure])
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def convert_to_system(self, system="mks"):
        if self.quantity_as_float is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurement = self.quantity_as_float * ureg[self.unit]
        return measurement  # .to_base_units()

    def as_mks(self):
        # meter, kilogram, second
        measurement = self.convert_to_system(system="mks")
        return measurement.to_base_units()

    def as_imperial(self):
        # miles, pounds, seconds
        measurement = self.convert_to_system(system="imperial")
        return measurement.to_base_units()

    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float, qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float = None
        super().save(*args, **kwargs)
