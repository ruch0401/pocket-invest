from datetime import date
from email.mime import image
from multiprocessing import parent_process
from pyexpat import model
from random import random
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    user_name = models.CharField(max_length=100, null=True, blank=True)
    email_id = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    random_id = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    real_money_balance = models.IntegerField(null=True, blank=True)
    virtual_money_balance = models.IntegerField(null=True, blank=True)
    # 0 - child, 1 = parent, and 2 = vendor
    user_type = models.IntegerField(null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)
    vendor_category = models.CharField(max_length=100, null=True, blank=True)
    vendor_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email_id


class Relationship(models.Model):
    parent = models.ForeignKey(
        User, related_name='parent2child', on_delete=models.CASCADE)
    child = models.ForeignKey(
        User, related_name='child2parent', on_delete=models.CASCADE)
    random_id = models.CharField(max_length=100, null=True, blank=True)


class Transaction(models.Model):
    sender = models.ForeignKey(User, related_name='sender2receiver', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver2sender', on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
    date = models.DateField()
    details = models.TextField()
    outcome = models.CharField(max_length=20)
    type_of_transaction = models.IntegerField()


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    image = models.ImageField()
    topic = models.CharField(max_length=100)
    age_group = models.CharField(max_length=10)
    total_modules = models.IntegerField()

    def __str__(self):
        return self.course_name


class Module(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=100)
    video_url = models.CharField(max_length=200)
    module_content = models.TextField()

    def __str__(self):
        return self.module_name


class Question(models.Model):
    course_id = models.CharField(max_length=100)
    text_field = models.CharField(max_length=100)
    option_1=models.CharField(max_length=100)
    option_2=models.CharField(max_length=100)
    option_3=models.CharField(max_length=100)


    def __str__(self):
        return self.course_id + " " + self.text_field


class ModuleProg(models.Model):
    module_count=models.IntegerField()
    course_id = models.IntegerField()
    user_id = models.IntegerField()

class CourseProgress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    modules_completed = models.IntegerField()

    def __str__(self):
        return self.user_id + " " + self.course_id


class Article(models.Model):
    article_title = models.CharField(max_length=100)
    article_content = models.TextField()
    article_image = models.ImageField()

    def __str__(self):
        return self.article_title


class InvestmentCategory(models.Model):
    investment_risk = models.CharField(max_length=100)
    investment_type = models.CharField(max_length=50)

    def __str__(self):
        return self.investment_type + " " + self.investment_risk


class Investment(models.Model):
    child = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_name = models.CharField(max_length=100)
    amount_invested = models.IntegerField()
    current_investment_value = models.IntegerField()

class Portfolio(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_id = models.ForeignKey(Investment, on_delete=models.CASCADE)
    investment_amount = models.IntegerField()

    def __str__(self):
        return self.user_id + " " + self.investment_id + " " + self.investment_amount

class CaseStudies(models.Model):
    case_study_title = models.CharField(max_length=100)
    case_study_investment_name = models.CharField(max_length=100)
    case_study_content = models.TextField()
    case_study_value = models.IntegerField()
    
