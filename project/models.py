from django.db import models

# Create your models here.

class staff(models.Model):
    loginid = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    competency = models.CharField(max_length=30)
    start_date = models.DateField()

    DEVELOPER = 'DEV'
    PROMAN = 'PG'

    STAFF_JOBS = (
        (DEVELOPER, 'DEVELOPER'),
        (PROMAN, 'PROJECT MANAGER'),
    )

    staff = models.CharField(
        max_length=20,
        choices=STAFF_JOBS,
        default=DEVELOPER,
    )


    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)


# 1 - M Relation (1 any User can message multiple types) --
class realtime(models.Model):
    staffid = models.ForeignKey(staff, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

# 1 - M Relation (1 project-leader creates many projects) --
class project(models.Model):
    staffid = models.ForeignKey(staff, on_delete=models.CASCADE)
    projectname = models.CharField(max_length=200)
    startdate = models.DateField()
    enddate = models.DateField()

# 1 - M Relation (1 Project can have multiple asset's path(images, file etc) --
class projectasset(models.Model):
    projectid = models.ForeignKey(project, on_delete=models.CASCADE)
    assetpath = models.CharField(max_length=200)

# 1 - M Relation (1 Project may have many staffs assigned --
class projectres(models.Model):
    projectid = models.ForeignKey(project, on_delete=models.CASCADE)
    staffid = models.ForeignKey(staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
