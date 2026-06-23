from django.db import models
from django.contrib.auth.models import User


GROUP_CHOICES = [
    ('ГД-22', 'ГД-22'),
    ('ГДп-22', 'ГДп-22'),
    ('ПД-22', 'ПД-22'),
    ('ГД-23', 'ГД-23'),
    ('ГДп-23', 'ГДп-23'),
    ('ИСВ-23', 'ИСВ-23'),
    ('ИСП-23', 'ИСП-23'),
    ('Кп-23', 'Кп-23'),
    ('ОДЛу-23', 'ОДЛу-23'),
    ('ПК-23', 'ПК-23'),
    ('ПКп-23', 'ПКп-23'),
    ('ПСОп-23', 'ПСОп-23'),
    ('СП-23', 'СП-23'),
    ('ГД-24', 'ГД-24'),
    ('ГДп-24', 'ГДп-24'),
    ('ЖКХп-24', 'ЖКХп-24'),
    ('ИС-24', 'ИС-24'),
    ('ЛК-24', 'ЛК-24'),
    ('МСР-24', 'МСР-24'),
    ('ОДЛу-24', 'ОДЛу-24'),
    ('ОИБ-24', 'ОИБ-24'),
    ('ПКп-24', 'ПКп-24'),
    ('РЗХ-24', 'РЗХ-24'),
    ('ТАКХС-24', 'ТАКХС-24'),
    ('ТМ-24', 'ТМ-24'),
    ('ГД-25', 'ГД-25'),
    ('ЖКХ-25', 'ЖКХ-25'),
    ('ИС1-25', 'ИС1-25'),
    ('ИС2-25', 'ИС2-25'),
    ('ЛК-25', 'ЛК-25'),
    ('МСР-25', 'МСР-25'),
    ('ОДЛу-25', 'ОДЛу-25'),
    ('СПм-25', 'СПм-25'),
    ('ТАКХС-25', 'ТАКХС-25'),
    ('ТМ-25', 'ТМ-25'),
]

KURS_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
]

OBUCH_CHOICES = [
    ('Очная', 'Очная'),
    ('Заочная', 'Заочная'),
    ('Очно-заочная', 'Очно-заочная'),
]


SPECIALTY_CHOICES = [
    ('Информационные системы и программирование', 'Информационные системы и программирование'),
    ('Обеспечение информационной безопасности автоматизированных систем', 'Обеспечение информационной безопасности автоматизированных систем'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    fio = models.CharField('ФИО', max_length=200, blank=True)
    spec = models.CharField('Специальность', max_length=200, choices=SPECIALTY_CHOICES, blank=True)
    grupa = models.CharField('Группа', max_length=50, choices=GROUP_CHOICES, blank=True)

    kurs = models.IntegerField('Курс', choices=KURS_CHOICES, null=True, blank=True)
    obuch = models.CharField('Форма обучения', max_length=100, choices=OBUCH_CHOICES, blank=True)

    vid = models.CharField('Вид практики', max_length=100, blank=True)
    kod = models.CharField('Код модуля', max_length=50, blank=True)
    mesto = models.CharField('Место прохождения', max_length=300, blank=True)
    adress = models.CharField('Адрес', max_length=300, blank=True)
    ruka = models.CharField('Руководитель', max_length=200, blank=True)

    date_begin = models.DateField('Дата начала', null=True, blank=True)
    date_finish = models.DateField('Дата окончания', null=True, blank=True)

    number = models.CharField('Количество дней', max_length=10, blank=True)
    not_day_one = models.CharField('Пропущено дней', max_length=10, blank=True)
    not_day_two = models.CharField('По неуважительной причине', max_length=10, blank=True)
    special = models.CharField('Специальность для характеристики', max_length=200, blank=True)
    good = models.CharField('Качество выполнения работы', max_length=200, blank=True)

    attestation_date = models.DateField('Дата аттестации', null=True, blank=True)
    boss_organization = models.CharField('Руководитель от организации', max_length=200, blank=True)
    library = models.CharField('Подразделение', max_length=200, blank=True)

    def __str__(self):
        return self.fio or self.user.username


class DownloadHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    document_name = models.CharField('Документ', max_length=200)
    action = models.CharField('Действие', max_length=100, default='download')
    created_at = models.DateTimeField('Дата и время', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} — {self.document_name}'