from django.db import models

# Create your models here.

class Person(models.Model):
	CreatedTime = models.DateTimeField(auto_now_add=True)
	ModifiedTime = models.DateTimeField(auto_now=True)
	BadgeNumber = models.CharField(max_length = 200, null=True, blank=True)
	FirstName = models.CharField(max_length = 50, null=True, blank=True)
	LastName = models.CharField(max_length = 50)
	IsBusiness = models.BooleanField(default=False)
	Suffix = models.CharField(max_length = 10, null=True, blank=True)
	Phone = models.CharField(max_length = 15, null=True, blank=True)
	Address = models.CharField(max_length = 100, null=True, blank=True)
	City = models.CharField(max_length = 50, null=True, blank=True)
	State = models.CharField(max_length = 2, null=True, blank=True)
	Zip = models.CharField(max_length = 5, null=True, blank=True)
	EmailAddress = models.EmailField(null=True, blank=True)
	ReceiveNewsletter = models.BooleanField(default=False)
	NewsletterFrequencyCode = models.CharField(max_length = 1, null=True, blank=True)

	def __str__(self):
		return "%s, %s" % (self.LastName, self.FirstName)

class Boardgame(models.Model):
	CreatedTime = models.DateTimeField(auto_now_add=True)
	ModifiedTime = models.DateTimeField(auto_now=True)
	BGGRef = models.URLField(null=True, blank=True)
	Name = models.CharField(max_length = 100)
	UPC = models.CharField(max_length = 30, null=True, blank=True)

	def __str__(self):
		return self.Name

class Collection(models.Model):
	CreatedTime = models.DateTimeField(auto_now_add=True)
	ModifiedTime = models.DateTimeField(auto_now=True)
	Person = models.ForeignKey(Person, on_delete=models.CASCADE)
	Boardgame = models.ForeignKey(Boardgame, on_delete=models.CASCADE)
	RFIDTag = models.BigIntegerField(null=True, blank=True)
	PreWeight = models.DecimalField(decimal_places=6, max_digits=8, null=True, blank=True)
	RegisteredPersonalGame = models.BooleanField(default=False)

	def __str__(self):
		return "%s, %s: %s" % (self.Person.LastName, self.Person.FirstName, self.Boardgame.Name)