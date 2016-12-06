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

class Laminations(models.Model):

	lam_size = models.CharField(max_length=20)
	measure_A = models.FloatField()
	measure_B = models.FloatField()
	measure_C = models.FloatField()
	measure_D = models.FloatField()
	measure_E = models.FloatField()
	measure_F = models.FloatField()
	measure_G = models.FloatField()
	path_length = models.FloatField()
	window_area = models.FloatField()
