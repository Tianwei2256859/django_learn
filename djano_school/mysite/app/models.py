# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime

class School(models.Model):
    number = models.CharField(u'学校id',max_length=30)
    name = models.CharField(u'学校名称',max_length=50)
    principal=models.CharField(u'校长',max_length=30)
    
    class Meta:
    	verbose_name_plural=u"学校"
    def __unicode__(self):
        return self.name
    
    @classmethod
    def create_sch(cls, number,name,principal):
        sch= cls.objects.get_or_create(number=number,name=name,principal=principal)
        return sch

    def sch_stu(self):
        return self.student_set.all()

    def sch_teacher(self):
        return Teacher.objects.get(teacher__id=self.pk)

class Class(models.Model):
    number = models.CharField(u'班级编号',max_length=30)
    name = models.CharField(u"学段",max_length=50)
    grade = models.DateField(u'学年')
    headmaster=models.CharField(u'班主任',max_length=10)
    class_school=models.ForeignKey(School,null=True,blank=True,verbose_name=u"班级所在学校")

    @classmethod
    def create_cla(cls, number,name,grade,headmaster):
        cla= cls.objects.get_or_create(number=number,name=name,grade=grade,headmaster=headmaster)
        return cla

    class Meta:
    	verbose_name_plural=u"班级"
    def __unicode__(self):
        return self.number
    
class Teacher(models.Model):
    number=models.CharField(u'教师id',max_length=30)    
    name = models.CharField(u'教师名字',max_length=50)
    class_teacher=models.ManyToManyField(Class,null=True,blank=True,verbose_name=u'教师所在班级')
    school_teacher=models.ForeignKey(School,null=True,blank=True,verbose_name=u"教师所在学校")
    teach=models.CharField(u'任教课程',max_length=50)

    class Meta:
    	verbose_name_plural=u"教师" 
    def __unicode__(self):
        return self.name

    @classmethod
    def create_tea(cls, number,name,teach):
        tea= cls.objects.get_or_create(number=number,name=name,teach=teach)
        return tea  

class Student(models.Model):
    number = models.CharField(u'学生id',max_length=30) 
    name = models.CharField(u'学生名字',max_length=50)
    class_student=models.ForeignKey(Class,verbose_name=u"学生所在班级",null=True,blank=True)
    teacher=models.ForeignKey(Teacher,verbose_name=u"任教教师",null=True,blank=True)
    student_school=models.ForeignKey(School,verbose_name=u"学生所在学校",null=True,blank=True)

    class Meta:
    	verbose_name_plural=u"学生"
    def __unicode__(self):
        return self.name

    @classmethod
    def create_stu(cls, number,name):
        stu= cls.objects.get_or_create(number=number,name=name)
        return stu

       

  
