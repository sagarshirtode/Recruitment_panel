from django.db import models

# Table:1
class jobseeker_registration(models.Model):
    userName = models.CharField(primary_key = True , max_length = 15)
    email = models.EmailField()
    password = models.CharField(max_length = 10)
    c_password = models.CharField(max_length= 10)
    #instance
    class Meta:
        db_table = "jobseeker_registration"

# table:2
class admin_details(models.Model):
    admin_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 20)
    company = models.CharField(max_length = 20)
    email_id = models.EmailField()
    password = models.CharField(max_length = 16)
    c_password= models.CharField(max_length = 16)
    # instance or object
    class Meta:
        db_table = "admin_details"

# table:3
class requirement_statistics(models.Model):
    id=models.IntegerField(primary_key = True)
    post_name = models.CharField(max_length=20)
    vacancies = models.IntegerField()
    post_description = models.CharField(max_length=20)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    qualification = models.CharField(max_length=50)
    #create instance (meta class)
    class Meta:
        db_table = "requirement_statistics"


# table:4
class jobseeker_p_details(models.Model):
    j_id = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length = 20)
    first_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    contact = models.CharField(max_length = 10)
    gender = models.CharField(max_length=5)
    birth_date =  models.DateField()
    state = models.CharField(max_length = 15)
    distric = models.CharField(max_length = 15)
    tahashil = models.CharField(max_length = 15)
    city = models.CharField(max_length=15)
    pin = models.CharField(max_length = 7)
    date = models.DateField()
    # instance or object
    class Meta:
        db_table = "jobseeker_p_details"

# table:5

class jobseeker_a_details(models.Model):
    j_id = models.IntegerField(primary_key=True)
    branch = models.CharField(max_length = 10)
    degree = models.CharField(max_length = 15)
    university = models.CharField(max_length = 30)
    institute = models.CharField(max_length = 50)
    status = models.CharField(max_length = 15)
    semester = models.CharField(max_length = 10)
    cpi = models.CharField(max_length = 5)
    experience = models.CharField(max_length = 10)
    # object
    class Meta:
        db_table = "jobseeker_a_details"
# table:6 
class recruit_experience(models.Model):
    j_id = models.IntegerField(primary_key=True)
    month_of_experience = models.IntegerField()
    company = models.CharField(max_length = 20)
    designation = models.CharField(max_length = 30)
    job_leaving_reason = models.CharField(max_length = 100)
    # object
    class meta:
        db_table = "recruit_experience"

# table: 7
class analysis_point(models.Model):
    j_id = models.IntegerField(primary_key=True)
    communication = models.IntegerField()
    personality = models.IntegerField()
    mentalability =models.IntegerField()
    integrity = models.IntegerField()
    job_knowledge = models.IntegerField()
    situational_judgement = models.IntegerField()
    t_analysis_point = models.IntegerField()
    # object
    class Meta:
        db_table = "analysis_point"

#table: 8
class document_details(models.Model):
    j_id = models.IntegerField(primary_key=True)
    aadhar = models.URLField()
    photo = models.URLField()
    signature = models.URLField()
    resume = models.URLField()


# table: 9
class training_table(models.Model):
    j_id = models.IntegerField(primary_key=True)
    type_of_training = models.CharField(max_length = 30)
    branch = models.CharField(max_length = 20)
    department = models.CharField(max_length = 20)
    training_period = models.IntegerField()
    start_training = models.DateField()
    end_training = models.DateField()
    t_analysis_point = models.IntegerField()
    feedback = models.CharField(max_length = 100)
    
    # object
    class Meta:
        db_table = "training_table"

# table: 10

class progress_report(models.Model):
    j_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length = 20)
    level = models.IntegerField()
    n_date = models.DateField()
    # object
    class Meta:
        db_table = "progress_report"

#table :11
class application_hit(models.Model):
    application_id = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length = 20)
    post_id = models.IntegerField()
    post_name = models.CharField(max_length = 40)
    application_date = models.DateField()

    class Meta:
        db_table = "application_hit"

class ischedule(models.Model):
    post = models.CharField(primary_key=True,max_length = 20)
    iDate = models.DateField()
    startDate = models.DateField()
    endDate = models.DateField()
    class Meta:
        db_table = "ischedule"

class posts(models.Model):
    post_name = models.CharField(primary_key=True,max_length = 20)
    class Meta:
        db_table = "posts"

class notice(models.Model):
    notice_head = models.CharField(primary_key=True,max_length = 20)
    notice_data = models.CharField(max_length = 300)
    ndate = models.DateField()
    class Meta:
        db_table = "notice" 
