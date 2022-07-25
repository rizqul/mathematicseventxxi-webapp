from django.db import models

# Create your models here.


class Event(models.Model):
    nama_event = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return "{}. {}".format(self.id, self.nama_event)


class SoalPenyisihanSD(models.Model):
    foto_soal = models.ImageField(upload_to='img/img_soal')
    paket = (
        ('A', 'Paket A'),
        ('B', 'Paket B'),
        ('C', 'Paket C'),
        ('D', 'Paket D'),
        ('E', 'Paket E'),
    )
    paket_soal = models.CharField(max_length=10, choices=paket)
    jawaban_soal = models.CharField(max_length=10)

    def __str__(self):
        return "{}. {}".format(self.id, self.paket_soal)


class JawabanPenyisihanSD(models.Model):
    id_peserta = models.CharField(max_length=255)
    nama_peserta = models.CharField(max_length=255)
    exam_code = models.CharField(max_length=255)
    paket_soal = models.CharField(max_length=10)
    jawaban_peserta = models.CharField(max_length=255)
    result_peserta = models.PositiveIntegerField(blank=True, null=True)
    jawaban_benar = models.PositiveIntegerField(blank=True, null=True)
    jawaban_salah = models.PositiveIntegerField(blank=True, null=True)
    jawaban_kosong = models.PositiveIntegerField(blank=True, null=True)
    submit_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {}".format(self.id_peserta, self.nama_peserta, self.paket_soal)


class SoalPenyisihanSMP(models.Model):
    foto_soal = models.ImageField(upload_to='img/img_soal')
    paket = (
        ('A', 'Paket A'),
        ('B', 'Paket B'),
        ('C', 'Paket C'),
        ('D', 'Paket D'),
        ('E', 'Paket E'),
    )
    paket_soal = models.CharField(max_length=10, choices=paket)
    jawaban_soal = models.CharField(max_length=10)

    def __str__(self):
        return "{}. {}".format(self.id, self.paket_soal)
