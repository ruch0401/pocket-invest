from email.mime import image
from pyexpat import model
from random import random
from django.db import models


class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    random_id = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email_id


class Child(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    secret_key = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.IntegerField()
    real_money_balance = models.IntegerField()
    virtual_money_balance = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Transaction(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    type_of_transaction = models.IntegerField()

    def __str__(self):
        return self.sender + " " + self.receiver + " " + self.amount + " " + self.type_of_transaction


class VendorDetails(models.Model):
    vendor_name = models.CharField(max_length=100)
    value = models.IntegerField()
    vendor_category = models.CharField(max_length=100)
    vendor_image = models.ImageField()

    def __str__(self):
        return self.vendor_name + " " + self.vendor_category


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
    child_id = models.ForeignKey(Child, on_delete=models.CASCADE)
    completion_status = models.BooleanField()

    def __str__(self):
        return self.module_id + " " + self.completion_status


class CourseProgress(models.Model):
    child_id = models.ForeignKey(Child, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    modules_completed = models.IntegerField()

    def __str__(self):
        return self.child_id + " " + self.course_id


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
    child_id = models.ForeignKey(Child, on_delete=models.CASCADE)
    investment_id = models.ForeignKey(Investment, on_delete=models.CASCADE)
    investment_amount = models.IntegerField()

    def __str__(self):
        return self.child_id + " " + self.investment_id + " " + self.investment_amount
