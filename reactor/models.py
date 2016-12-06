from django.db import models


class Wire(models.Model):
	area = models.FloatField()
	diameter = models.FloatField()
	ohms_per_m_min = models.FloatField()
	ohms_per_m_rated = models.FloatField()
	ohms_per_m_max = models.FloatField()
	standard = models.CharField(max_length=1)
	tolerance = models.FloatField()
	mass = models.FloatField()
	grade_1_dia_min = models.FloatField()
	grade_1_dia_max = models.FloatField()
	grade_2_dia_min = models.FloatField()
	grade_2_dia_max = models.FloatField()	
