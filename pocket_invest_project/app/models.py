from datetime import date
from email.mime import image
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


class Transaction(models.Model):
    sender = models.ForeignKey(
        User, related_name='sender2receiver', on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        User, related_name='receiver2sender', on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
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
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)
    course_id = models.CharField(max_length=100)
    text_field = models.CharField(max_length=100)
    completion_status = models.BooleanField()

    def __str__(self):
        return self.module_id + " " + self.course_id + " " + self.text_field


class ModuleProgress(models.Model):
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    completion_status = models.BooleanField()

    def __str__(self):
        return self.module_id + " " + self.completion_status


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
    investment_category = models.ForeignKey(
        InvestmentCategory, on_delete=models.CASCADE)
    investment_name = models.CharField(max_length=100)
    investment_text = models.CharField(max_length=100)

    def __str__(self):
        return self.investment_category + " " + self.investment_name + " " + self.investment_text + " " + self.investment_media


class Portfolio(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_id = models.ForeignKey(Investment, on_delete=models.CASCADE)
    investment_amount = models.IntegerField()

    def __str__(self):
        return self.user_id + " " + self.investment_id + " " + self.investment_amount
