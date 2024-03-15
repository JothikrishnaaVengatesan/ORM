from django.db import models
from django.contrib import admin
class Railway(models.Model):
    Train_no=models.IntegerField(primary_key=True)
    Train_Name=models.CharField(max_length=100)
    start_Date=models.DateTimeField()
    end_Date=models.DateTimeField()
    Start_Station_Code=models.CharField(max_length=20)
    End_Station_Code=models.CharField(max_length=20)
    
class RailwayAdmin(admin.ModelAdmin):
    list_display=('Train_no','Train_Name','start_Date','end_Date','Start_Station_Code','End_Station_Code')
