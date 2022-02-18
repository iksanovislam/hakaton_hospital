from django.db import models
from django.db import models


class Hospital(models.Model):
    name = models.CharField("Название Госпиталя", max_length=100)
    descriptions = models.TextField("Описание", unique=True)
    region_name = models.CharField(verbose_name='Регион', max_length=100)
    city_name = models.CharField(verbose_name='Город', max_length=100)
    category = models.BooleanField("Выбор: -", default=False)

    def __str__(self):
        return self.name


class GlavVrach(models.Model):
    name = models.CharField("Ф.И.О Глав-Врача", max_length=100)
    doctor = models.ForeignKey(Hospital,  on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    number = models.CharField("Номер телефона", max_length=30)

    def __str__(self):
        return self.name


class Hirurg(models.Model):
    name = models.CharField("Ф.И.О - Врача", max_length=60)
    position = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    skill = models.TextField("Стаж работы")
    number = models.CharField("Номер телефона", max_length=30)

    def __str__(self):
        return self.name


class Terapevt(models.Model):
    name = models.CharField("Ф.И.О - Врача", max_length=100)
    position = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    age = models.IntegerField("Возраст", default=0)
    skill = models.TextField("Опыт работы")
    number = models.CharField("Номер телефона", max_length=30)

    def __str__(self):
        return self.name


class Medsestra(models.Model):
    name = models.CharField("Ф.И.О - Медсестры", max_length=100)
    position = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    age = models.IntegerField("Возраст", default=0)
    access_to_terapevt = models.OneToOneField(Terapevt, on_delete=models.CASCADE)
    access_to_hirurg = models.OneToOneField(Hirurg, on_delete=models.CASCADE)
    number = models.CharField("Номер телефона", max_length=30)

    def __str__(self):
        return self.name


class Patients(models.Model):
    name = models.CharField("Ф.И.О - Пациента", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    Reason_for_going_to_the_hospital = models.TextField("Причина обращения в больницу")
    access = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    number = models.CharField("Номер телефона", max_length=30)

    def __str__(self):
        return self.name

