from django.db import models

# Create your models here.

class Kelompok(models.Model):
    judul = models.CharField(max_length=9)
    keterangan = models.TextField()

    def __str__(self):
        return self.judul

class Web(models.Model):
    nama = models.CharField(max_length=50)
    ling = models.CharField(max_length=40)
    tipe = models.CharField(max_length=40)
    pembuat = models.CharField(max_length=40)
    pemilik = models.CharField(max_length=40)
    kolom = models.IntegerField(null=True)
    keamanan_id = models.ForeignKey(Kelompok, on_delete=models.CASCADE, null=True)

    
    def __str__(self):
        return self.nama
