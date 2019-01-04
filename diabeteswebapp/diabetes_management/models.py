from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    Fname = models.CharField(max_length=30)
    Lname = models.CharField(max_length=50)
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)

class Roles(models.Model):
    name = models.CharField(max_length=10)

class Lab_tests(models.Model):
    glucose = models.IntegerField()
    insulin = models.IntegerField()
    bloodPressure = models.IntegerField()
    skinThickness = models.IntegerField()
    diabetesPedigreeFunction = models.DoubleField()
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

class Patients(models.Model):
    Fname = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    age = models.IntegerField()
    pregnancies = models.IntegerField()
    BMI = models.DoubleField()

class Jobs(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=)
    noti_status = models.CharField(max_length=)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

class Job_labs(models.Model):
    job_id = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    lab_id = models.ForeignKey(Lab_tests, on_delete=models.CASCADE)

class Predictions(models.Model):
    hasDiabetes = models.DoubleField()
    job_id = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    model_id = models.ForeignKey(Models, on_delete=models.CASCADE)

class Models(models.Model):
    name = models.CharField(max_length=)
    file = models.TextField(max_length=)
    features = models.TextField(max_length=)
    accuracy = models.DoubleField()
    hyperparameter = models.TextField(max_length=)
    confusion_matrix = models.TextField(max_length=)
    cross_val = models.TextField(max_length=)
    roc_pic = models.TextField(max_length=)
        
    
        
        