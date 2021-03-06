from django.db import models

class Community(models.Model):
	name = models.CharField(max_length=100)
	locationId = models.CharField(max_length=10, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class Building(models.Model):
	name = models.CharField(max_length=100)
	locationId = models.CharField(max_length=10, blank=True)
	community = models.ForeignKey(Community, null=True)
	fetched = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class Side(models.Model):
	name = models.CharField(max_length=100)
	locationId = models.CharField(max_length=10, blank=True)
	building = models.ForeignKey(Building, null=True)

	dryerTotal = models.IntegerField(blank=True, null=True)
	dryerAvail = models.IntegerField(blank=True, null=True)
	dryerTimes = models.CharField(max_length=255, null=True)
	dryerInUse = models.IntegerField(blank=True, null=True)
	dryerComplete = models.IntegerField(blank=True, null=True)

	washerTotal = models.IntegerField(blank=True, null=True)
	washerAvail = models.IntegerField(blank=True, null=True)
	washerTimes = models.CharField(max_length=255, null=True)
	washerInUse = models.IntegerField(blank=True, null=True)
	washerComplete = models.IntegerField(blank=True, null=True)
	
	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)
