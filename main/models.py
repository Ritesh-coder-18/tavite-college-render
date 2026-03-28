from django.db import models

class Subject(models.Model):
    SEMESTER_CHOICES = [(i, f'Semester {i}') for i in range(1, 7)]
    
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return f"Sem {self.semester} - {self.name}"

class Note(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    unit1 = models.FileField(upload_to='notes/', blank=True, null=True)
    unit2 = models.FileField(upload_to='notes/', blank=True, null=True)
    unit3 = models.FileField(upload_to='notes/', blank=True, null=True)
    unit4 = models.FileField(upload_to='notes/', blank=True, null=True)
    unit5 = models.FileField(upload_to='notes/', blank=True, null=True)

    def __str__(self):
        return f"Notes - {self.subject.name}"

class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Topper(models.Model):
    CLASS_CHOICES = [
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
    ]

    student_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=20, choices=CLASS_CHOICES)
    percentage = models.FloatField()
    image = models.ImageField(upload_to='toppers/')  # passport image

    def __str__(self):
        return f"{self.student_name} ({self.class_name})"
    
class ClassResult(models.Model):
    CLASS_CHOICES = [
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
    ]

    class_name = models.CharField(max_length=20, choices=CLASS_CHOICES)
    result_image = models.ImageField(upload_to='results/')

    def __str__(self):
        return self.class_name    


# class Result(models.Model):
#     CLASS_CHOICES = [
#         ('1st Year', '1st Year'),
#         ('2nd Year', '2nd Year'),
#         ('3rd Year', '3rd Year'),
#     ]

#     student_name = models.CharField(max_length=100)
#     class_name = models.CharField(max_length=20, choices=CLASS_CHOICES)
#     percentage = models.FloatField()
#     is_topper = models.BooleanField(default=False)
#     result_image = models.ImageField(upload_to='results/', blank=True, null=True)

#     def __str__(self):
#         return self.student_name


class TeacherMessage(models.Model):
    teacher_name = models.CharField(max_length=100)
    
    POST_CHOICES = [
        ('HOD', 'HOD'),
        ('Founder', 'Founder'),
        ('Owner', 'Owner'),
        ('Faculty', 'Faculty'),
    ]
    
    post = models.CharField(max_length=50, choices=POST_CHOICES)
    message = models.TextField()
    image = models.ImageField(upload_to='teachers/', blank=True, null=True)

    def __str__(self):
        return f"{self.teacher_name} ({self.post})"                    


class BCAPaper(models.Model):
    SEMESTER_CHOICES = [
        ('Sem 1', 'Sem 1'),
        ('Sem 2', 'Sem 2'),
        ('Sem 3', 'Sem 3'),
        ('Sem 4', 'Sem 4'),
        ('Sem 5', 'Sem 5'),
        ('Sem 6', 'Sem 6'),
    ]

    subject_name = models.CharField(max_length=100)
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)
    year = models.IntegerField()
    paper_file = models.FileField(upload_to='bca_papers/')

    def __str__(self):
        return f"{self.subject_name} - {self.semester} ({self.year})"