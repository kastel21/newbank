
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Study(models.Model):
    statuses = [("On going","On going"),("Ended","Ended"),("n/a","n/a")]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    narrative_name= models.CharField(max_length=500, default="sadf asd fadfg arsg dvadhf dgjhbn")
    status = models.CharField(choices=statuses,max_length=200, default="On going")
    # sample_id = models.ForeignKey(Sample, on_delete=models.CASCADE)
    # patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name


class Patient(models.Model):
    sex = [("Male","Male"),("Female","Female"),("n/a","n/a")]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200) 
    dob = models.CharField(max_length=200)
    gender = models.CharField(choices=sex,max_length=10)
    phone = models.CharField(max_length=20, default="0783872345")
    age = models.CharField(max_length=20, default="1")

    study = models.ForeignKey(Study, on_delete=models.CASCADE, default=1)
    def __str__(self) -> str:
        return self.name



class Freezer(models.Model):
    id = models.AutoField(primary_key=True)
    capacity = models.IntegerField()
    name = models.CharField(max_length=200)
    shelves = models.IntegerField()
    def __str__(self) -> str:
        return self.name

class Shelf(models.Model):
    id = models.AutoField(primary_key=True)
    capacity = models.IntegerField()
    name = models.CharField(max_length=200)
    racks = models.IntegerField()
    freezer = models.ForeignKey(Freezer, on_delete=models.CASCADE)
    def __str__(self) -> str:
        name = str(self.freezer)+" - "+str(self.name)
        return name

class Rack(models.Model):
    id = models.AutoField(primary_key=True)
    capacity = models.IntegerField()
    name = models.CharField(max_length=100, default="rack 1")
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, default=1)
    def __str__(self) -> str:
        name = str(self.shelf)+"-"+str(self.name)
        return name


class Box(models.Model):
    id = models.AutoField(primary_key=True)
    capacity = models.IntegerField()
    name = models.CharField(max_length=200,default="box 1")
    rack= models.ForeignKey(Rack, on_delete=models.CASCADE)
    # shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    # freezer = models.ForeignKey(Freezer, on_delete=models.CASCADE)
    def __str__(self) -> str:
        name = str(self.rack)+"-"+str(self.name)
        return name



class Sample(models.Model):

    # id = models.CharField(primary_key=True,max_length=100)
    name = models.CharField(max_length=100)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    aliquoted = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    date_of_archive = models.CharField(max_length=200)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    allocated = models.BooleanField(default=False)
    cube = models.ForeignKey('Cube',related_name='myCube', on_delete=models.CASCADE,null=True, blank=True)


    def __str__(self) -> str:
        return self.name

class Sample_Aliquote(models.Model):

    # id = models.CharField(primary_key=True,max_length=100)
    name = models.CharField(max_length=100)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, null=False)
    date_of_archive = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.main_sample.name+"_aliquote"

class Cube(models.Model):
    id = models.AutoField(primary_key=True)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    # rack= models.ForeignKey(Rack, on_delete=models.CASCADE)
    # shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    # freezer = models.ForeignKey(Freezer, on_delete=models.CASCADE)
    occupied = models.BooleanField(default=False)
    sample = models.ForeignKey(Sample, blank=True,null=True,on_delete=models.CASCADE,related_name='mySample')
    name = models.CharField(max_length=200, default="cube 1")
    def __str__(self) -> str:
        name = str(self.box)+"-"+str(self.name)
        return name




