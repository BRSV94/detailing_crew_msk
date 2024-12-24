from django.contrib.auth.models import AbstractUser
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

# from autos.models import Auto

from .validators import phone_number_validator


class ClientUser(models.Model):
    first_name = models.CharField(
        max_length=32,
        blank=False,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=32,
        blank=True,
        verbose_name='Фамилия'
    )
    phone_number = models.CharField(
        max_length=12,
        blank=True,
        null=True,
        validators=[phone_number_validator],
        verbose_name='Номер телефона'
    )
    friendly = models.BooleanField(
        default=True,
        help_text='Дружелюбный?'
    )
    solvent = models.BooleanField(
        default=True,
        help_text='Платежеспособный?'
    )
    next_visit = models.DateField(
        verbose_name='Планируемая дата следующего посещения',
        blank=True,
        null=True,
    )
    additional_phone_number = models.CharField(
        max_length=12,
        blank=True,
        null=True,
        validators=[phone_number_validator],
        verbose_name='Доп. номер телефона'
    )

    def __str__(self) -> str:
        return str(f'{self.first_name} {self.last_name}\n'
                f'{self.phone_number}')
    
    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'Клиенты'


class StaffUser(AbstractUser):
    phone_number = models.CharField(
        max_length=12,
        blank=True,
        validators=[phone_number_validator],
        verbose_name='Номер телефона'
    )
    additional_phone_number = models.CharField(
        max_length=12,
        blank=True,
        validators=[phone_number_validator],
        verbose_name='Доп. номер телефона'
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'Сотрудники'


class Work(models.Model):
    title = models.CharField(
        max_length=128,
        blank=False,
        verbose_name='Наименование услуги'
    )
    price = models.PositiveIntegerField(
        verbose_name='Стоимость услуги'
    )
    description = models.CharField(
        max_length=1024,
        blank=False,
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self) -> str:
        return self.title


class FlawTitle(models.Model):
    title = models.CharField(
        max_length=64,
        blank=False,
        verbose_name='Название недостатка'
    )
    
    class Meta:
        verbose_name = 'недостаток'
        verbose_name_plural = 'Недостатки'

    def __str__(self) -> str:
        return self.title
    

class Flaw(models.Model):
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='З/н',
    )
    title = models.ForeignKey(
        FlawTitle,
        on_delete=models.CASCADE,
        related_name='flaws',
        blank=False,
        verbose_name='Название недостатка',
    )
    photo = models.ImageField(
        upload_to='detailing/flaws/',
        verbose_name='Фото нестотатков',
        null=False,
        blank=False
    )


class Order(models.Model):
    from autos.models import Auto
    client = models.ForeignKey(
        ClientUser,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Заказчик/клиент'
    )
    auto = ChainedForeignKey(
        Auto,
        chained_field='client',
        chained_model_field='owner',
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name='Авто, с которым проводятся работы',
        # https://django-smart-selects.readthedocs.io/en/latest/usage.html
    )
    executor = models.ForeignKey(
        StaffUser,
        on_delete=models.SET_NULL,
        related_name='orders',
        verbose_name='Ответственный сотрудник',
        null=True
    )
    works = models.ManyToManyField(
        Work,
        blank=True,
        related_name='orders',
        verbose_name='Проводимые работы'
    )
    price = models.PositiveIntegerField(
        verbose_name='Общая стоимость по заказ-наряду',
        blank=True,
        null=True,
    )
    discount = models.PositiveIntegerField(
        verbose_name='Скидка',
        blank=True,
        null=True,
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания заказ-наряда'
    )
    is_done = models.BooleanField(
        verbose_name='Выполнены ли работы в полном объеме',
        default=False,
    )
    flaws = models.ManyToManyField(
        FlawTitle,
        verbose_name='Недостатки/повреждения',
        blank=True,
        through=Flaw,
        through_fields=('order', 'title')
    )
    description = models.CharField(
        max_length=1024,
        blank=True,
        verbose_name='Примечания',
    )

    class Meta:
        verbose_name = 'заказ-наряд'
        verbose_name_plural = 'Заказ-наряды'

    def __str__(self) -> str:
        return f'З/н №{str(self.id).zfill(6)} от {self.date} на {self.auto}.'

    def price(obj):
        price = 0
        works = obj.works.all()
        for work in works:
            price += work.price
        if obj.discount:
            price -= obj.discount
            if price < 0:
                return 0
        return price



class Appointment(models.Model):
    from autos.models import Auto
    client = models.ForeignKey(
        ClientUser,
        on_delete=models.CASCADE,
        related_name='appointments',
        verbose_name='Заказчик/клиент'
    )
    auto = ChainedForeignKey(
        Auto,
        chained_field='client',
        chained_model_field='owner',
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name='Авто, с которым будут проводиться работы',
        # https://django-smart-selects.readthedocs.io/en/latest/usage.html
    )
    visit_time = models.DateTimeField(
        verbose_name='Планируемая дата и время посещения',
        auto_now_add=False,
    )
    description = models.CharField(
        max_length=1024,
        blank=True,
        verbose_name='Описание',
    )
    
    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'Записи'

    def __str__(self) -> str:
        visit_time = self.visit_time.strftime('%d.%m.%y %H:%M')
        return (f'Запись на {visit_time}: '
                f'{self.client} - {self.auto}.')
    

class AppointmentThroughTg(models.Model):
    phone_number = models.CharField(
        max_length=12,
        blank=False,
        verbose_name='Номер телефона для связи',
    )
    name = models.CharField(
        max_length=64,
        blank=False,
        verbose_name='Как обращаться при звонке',
    )
    desired_time = models.CharField(
        max_length=128,
        blank=False,
        verbose_name='Удобное клиенту время для звонка',
    )
    
    class Meta:
        verbose_name = 'запись из телеграма'
        verbose_name_plural = 'Записи из телеграма'

    def __str__(self) -> str:
        return (f'{self.name} ({self.phone_number}) желает записаться. '
                f'Клиенту удобно, чтобы ему позвонили: {self.desired_time}')


class ReviewChoices(models.IntegerChoices):
    GREAT = 5, 'Отлично'
    WELL = 4, 'Хорошо'
    MEDIUM = 3, 'Средне'
    BAD = 2, 'Плохо'
    WTF = 1, 'Ужасно'


class Review(models.Model):
    client = models.ForeignKey(
        ClientUser,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Заказчик/клиент'
    )
    stars = models.IntegerField(
        choices=ReviewChoices.choices,
        default=ReviewChoices.GREAT,
        verbose_name='Оценка'
    )
    description = models.TextField(
        verbose_name='Текст отзыва',
        max_length=256,
    )