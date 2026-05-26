from django.db import models

# Create your models here.
#one to one  ......1 stu=lads
class student(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)

def __str__(self):
    return self.name


class address(models.Model):
    student=models.OneToOneField(student,on_delete=models.CASCADE) #inherit
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)

#many to many  ......many stu=many skills

class Skills (models.Model):
    profile=models.CharField(max_length=100)
    # contact=models.CharField(max_length=100)
     
    def __str__(self):
        return self.profile
    
    class candidate(models.Model):
        name=models.CharField(max_length=100)
        contact=models.CharField(max_length=100)
        Skills=models.ManyToManyField(Skills)
    
    class parent(models.Model):
        name=models.CharField(max_length=100)
        contact=models.CharField(max_length=100)
        Skills=models.ManyToManyField(Skills)

        class meta:
            abstract=True
    class child1(parent):
        c1_name=models.CharField(max_length=100)

    class child2(parent):
        c2_name=models.CharField(max_length=100)
