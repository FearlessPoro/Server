from django.contrib.auth.models import User
from django.db import models


class Stations(models.Model):
    Name = models.CharField(max_length=200)
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = "stations"


class Measurements(models.Model):
    Station = models.ForeignKey(Stations, on_delete=models.CASCADE)
    Time_of_measurement = models.DateTimeField()

    class Meta:
        db_table = "measurements"


class TemperatureMeasurements(models.Model):
    Measurement = models.OneToOneField(Measurements, primary_key=True, on_delete=models.CASCADE,
                                          parent_link=True)
    Value = models.FloatField()
    Unit = models.CharField(max_length=20)

    class Meta:
        db_table = "temperature_measurements"


class HumidityMeasurements(models.Model):
    Measurement = models.OneToOneField(Measurements, primary_key=True, on_delete=models.CASCADE,
                                          parent_link=True)
    Value = models.FloatField()

    class Meta:
        db_table = "humidity_measurements"


class PressureMeasurements(models.Model):
    Measurement = models.OneToOneField(Measurements, primary_key=True, on_delete=models.CASCADE,
                                          parent_link=True)
    Value = models.FloatField()
    Unit = models.CharField(max_length=20)

    class Meta:
        db_table = "pressure_measurements"


class BigParticlesMeasurements(models.Model):
    Measurement = models.OneToOneField(Measurements, primary_key=True, on_delete=models.CASCADE,
                                          parent_link=True)
    Value = models.FloatField()
    Unit = models.CharField(max_length=20)

    class Meta:
        db_table = "big_particle_measurements"


class SmallParticlesMeasurements(models.Model):
    Measurement = models.OneToOneField(Measurements, primary_key=True, on_delete=models.CASCADE,
                                          parent_link=True)
    Value = models.FloatField()
    Unit = models.CharField(max_length=20)

    class Meta:
        db_table = "small_particle_measurements"


class AllMeasurements(models.Model):
    Stacja = models.CharField(max_length=200)
    id = models.BigIntegerField(primary_key=True)
    Czas_pomiaru = models.DateTimeField()
    Temperatura = models.FloatField()
    Temperatura_jednostka = models.CharField(max_length=20)
    Cisnienie = models.FloatField()
    Cisnienie_jednostka = models.CharField(max_length=20)
    Wilgotnosc = models.FloatField()
    Wilgotnosc_jednostka = models.CharField(max_length=20)
    PM2_5 = models.FloatField()
    PM2_5_jednostka = models.CharField(max_length=20)
    PM10 = models.FloatField()
    PM10_jednostka = models.CharField(max_length=20)

    class Meta:
        db_table = "all_measurements"
        managed = False
