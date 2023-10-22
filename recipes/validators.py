import pint

from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError


def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    try:
        ureg[value]
    except UndefinedUnitError:
        raise ValidationError(f"'{value}' is not a valid unit of measure")
