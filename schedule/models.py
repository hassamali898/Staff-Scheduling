from typing import Any
from django.db import models

# Create your models here.

class Schedule(models.Model):
    user = models.CharField(max_length=50)
    room = models.PositiveIntegerField()
    building = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    objects = models.Manager()

    class Meta:
        db_table = 'schedule'
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
        ordering = ['user']


    def __str__(self):
        return self.user
    @property
    def is_active(self):
        return self.is_active

    

# class Period(models.Model):
#     name = models.CharField(max_length=50)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     availability = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['start_time']

#     def __str__(self):
#         return self.name
    
#     def check_availability(self):
#         return self.availability

# class Building(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

# class Room(models.Model):
#     number = models.PositiveIntegerField()
#     building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='rooms')
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['building', 'number']
#         unique_together = ['number', 'building', 'created_at']
    
#     def __str__(self):
#         return self.number
