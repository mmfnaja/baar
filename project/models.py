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
    project_name = models.CharField(max_length=200)
    members = models.ManyToManyField(staff, blank=True, null=True, related_name="members")

class activity_log(models.Model):
    project = models.ForeignKey(project, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=1000)

class task(models.Model):
    project_name = models.ForeignKey(project, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    person_incharge = models.ForeignKey(staff, on_delete=models.CASCADE)
    project_status_enum = (
        ('Closed', 'Closed'),
        ('InProgress', 'InProgress'),
        ('Completed', 'Completed'),
        ('Terminated', 'Terminated'),
        ('Due', 'Due')
    )
    status = models.CharField(max_length=10, choices=project_status_enum, default='Closed')

class task_deliverables(models.Model):
    file = models.FileField(upload_to='deliverables/')
    related_task = models.ForeignKey(task, on_delete=models.CASCADE)

# 1 - M Relation (1 Project can have multiple asset's path(images, file etc) --
class projectasset(models.Model):
    projectid = models.ForeignKey(project, on_delete=models.CASCADE)
    assetpath = models.CharField(max_length=200)

# 1 - M Relation (1 Project may have many staffs assigned --
class projectres(models.Model):
    projectid = models.ForeignKey(project, on_delete=models.CASCADE)
    staffid = models.ForeignKey(staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
