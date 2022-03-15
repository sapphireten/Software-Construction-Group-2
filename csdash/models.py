from django.db import models

class facultyModel(models.Model):
    id = models.IntegerField(primary_key=True)
    honorific = models.CharField(max_length=100)
    first = models.CharField(max_length=100)
    mi = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    researchinterests = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)

    class Meta:
        db_table="deptfaculty"