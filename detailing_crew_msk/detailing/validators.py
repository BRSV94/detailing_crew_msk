import re
from django.core.exceptions import ValidationError

def phone_number_validator(value):
    pattern = re.compile(r'^(\+7|8)\d{10}$')
    if not bool(pattern.match(value)):
        raise ValidationError(
            'Введите корректный номер телефона в формате '
            '+7XXXXXXXXXX или 8XXXXXXXXXX.')
