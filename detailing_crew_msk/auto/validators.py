from django.core.exceptions import ValidationError


def plate_validator(value):
    SYMBOLS = 'ABEKMHOPCTYX'
    RU_SYMBS = 'АВЕКМНОРСТУХ'
    HELP_TEXT = 'Введите корректный ГРЗ в формате X999XX99 или X999XX199.'

    if len(value) not in [8, 9] or value[1:4] == '000':
        raise ValidationError(HELP_TEXT)
    if value[-2:] == '00' or (len(value) == 9 and value[6:] == '0'):
        raise ValidationError(HELP_TEXT)

    for index, sym in enumerate(value):
        if sym in RU_SYMBS:
            raise ValidationError(f'Используйте латинские буквы. \n{HELP_TEXT}')
        nums_indexes = [1, 2, 3]
        if (index not in nums_indexes
            and index < 6
            and sym not in SYMBOLS):
            raise ValidationError(HELP_TEXT)
        if index in nums_indexes and not sym.isdigit():
            raise ValidationError(HELP_TEXT)
