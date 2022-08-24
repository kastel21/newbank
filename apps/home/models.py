
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Study(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    # sample_id = models.ForeignKey(Sample, on_delete=models.CASCADE)
    # patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name


class Patient(models.Model):
    sex = [("Male","Male"),("Female","Female"),("n/a","n/a")]
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200) 
    dob = models.CharField(max_length=200)
    gender = models.CharField(choices=sex,max_length=10)
    study = models.ForeignKey(Study, on_delete=models.CASCADE, default=1)
    def __str__(self) -> str:
        return self.name



class Freezer(models.Model):
    _id = models.AutoField(primary_key=True)
    capacity = models.IntegerField()
    name = models.CharField(max_length=200)
    shelves = models.IntegerField()
    def __str__(self) -> str:
        return self._id

class Shelf(models.Model):
    _id = models.AutoField(primary_key=True)
    capacity = models.IntegerField()
    name = models.CharField(max_length=200)
    racks = models.IntegerField()
    freezer = models.ForeignKey(Freezer, on_delete=models.CASCADE)
    def __str__(self) -> str:
        name = str(self.freezer)+"-"+str(self._id)
        return name

class Rack(models.Model):
    _id = models.AutoField(primary_key=True)
    capacity = models.IntegerField()
    def __str__(self) -> str:
        name = str(self.freezer)+"-"+str(self.shelf)+"-"+str(self._id)
        return name


class Box(models.Model):
    _id = models.AutoField(primary_key=True)
    capacity = models.IntegerField()
    rack= models.ForeignKey(Rack, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    freezer = models.ForeignKey(Freezer, on_delete=models.CASCADE)
    def __str__(self) -> str:
        name = str(self.freezer)+"-"+str(self.shelf)+"-"+str(self.rack)+"-"+str(self._id)
        return name


class Sample(models.Model):
    _id = models.CharField(primary_key=True, max_length=200)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    date_of_archive = models.DateField(null=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self._id

class Cube(models.Model):
    _id = models.AutoField(primary_key=True)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    rack= models.ForeignKey(Rack, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    freezer = models.ForeignKey(Freezer, on_delete=models.CASCADE)
    occupied = models.BooleanField(default=False)
    sample = models.ForeignKey(Sample, null=True,on_delete=models.CASCADE)
    def __str__(self) -> str:
        name = str(self.freezer)+"-"+str(self.shelf)+"-"+str(self.rack)+"-"+str(self.box)+"-"+str(self._id)
        return name






