from django.db import models

# Create your model


class PlayOffPenyisihanSD (models.Model):
    id_peserta = models.CharField(max_length=50)
    nama_peserrta = models.CharField(max_length=255)
    jawaban = models.CharField(max_length=255)
    submit_time = models.DateTimeField(auto_now=True)


class PlayOffPenyisihanSMP (models.Model):
    id_peserta = models.CharField(max_length=50)
    nama_peserrta = models.CharField(max_length=255)
    jawaban = models.CharField(max_length=255)
    submit_time = models.DateTimeField(auto_now=True)


class PlayOffPenyisihanSMA (models.Model):
    id_peserta = models.CharField(max_length=50)
    nama_peserrta = models.CharField(max_length=255)
    jawaban = models.CharField(max_length=255)
    submit_time = models.DateTimeField(auto_now=True)


class PlayoffSemifinalSD (models.Model):
    id_peserta = models.CharField(max_length=50)
    nama_peserta = models.models.CharField(max_length=255)
    jawaban = models.models.CharField(max_length=255)
    submit_time = models.models.DateField(auto_now=True)


class PlayoffSemifinalSMP (models.Model):
    id_peserta = models.CharField(max_length=50)
    nama_peserta = models.models.CharField(max_length=255)
    jawaban = models.models.CharField(max_length=255)
    submit_time = models.models.DateField(auto_now=True)


class PlayoffSemifinalSMA (models.Model):
    id_peserta = models.CharField(max_length=50)
    nama_peserta = models.models.CharField(max_length=255)
    jawaban = models.models.CharField(max_length=255)
    submit_time = models.models.DateField(auto_now=True)
