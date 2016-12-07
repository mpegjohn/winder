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

class Lamination(models.Model):

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

class Bobbin(models.Model):

	size = models.CharField(max_length=20)
	us_name = models.CharField(max_length=20)
	section_type = models.CharField(max_length=20)
	terminals = models.CharField(max_length=20)
	measure_A = models.FloatField()
	measure_B = models.FloatField()
	measure_C = models.FloatField()
	measure_D = models.FloatField()
	measure_E = models.FloatField()
	measure_F = models.FloatField()
	measure_G = models.FloatField()
	measure_H = models.FloatField()
	measure_J = models.FloatField()
	measure_K = models.FloatField()
	measure_L = models.FloatField()
	measure_M = models.FloatField()
	measure_N = models.FloatField()
	measure_P = models.FloatField()
	core_material = models.CharField(max_length=20)
	frame_va =models.FloatField()
	mp_part_number = models.CharField(max_length=20)

