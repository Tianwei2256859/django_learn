#!/usr/bin/env python
#encoding: utf-8
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import django,xlrd
from datetime import date
import json

sys.path.append('C:/Python27/Scripts/mysite') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings' 
django.setup()

if __name__=="__main__":

    from app.models import School,Class,Teacher,Student
    workbook = xlrd.open_workbook(r'C:/Python27/Scripts/mysite/school.xlsx')
    school_creat= workbook.sheet_by_index(1)
    classes_creat=workbook.sheet_by_index(0)
    teacher_creat=workbook.sheet_by_index(2)
    student_creat=workbook.sheet_by_index(3)
    
    def schools(school_creat):
        sch_number=[int(sch_number) for sch_number in school_creat.col_values(0)]
        sch_name=[sch_name for sch_name in school_creat.col_values(1)]
        sch_principal=[sch_principal for sch_principal in school_creat.col_values(2)]
        school_list=zip(sch_number,sch_name,sch_principal)
        for school in school_list:
            School.create_sch(*school)

    def classes(classes_creat):
        cla_number=[cla_number for cla_number in classes_creat.col_values(0)]
        cla_name =[cla_name for cla_name in classes_creat.col_values(1)]
        cla_grades =[xlrd.xldate_as_tuple(cla_grades,workbook.datemode) for cla_grades in classes_creat.col_values(2)]
        cla_grade=[date(*cla_grade[:3]).strftime('%Y-%m-%d')for cla_grade in cla_grades]
        cla_headmaster =[cla_headmaster for cla_headmaster in classes_creat.col_values(3)]
        classes_list=zip(cla_number,cla_name,cla_grade,cla_headmaster)
        for clas in classes_list:
            Class.create_cla(*clas)

    def teachers(teacher_creat):
        tea_number=[int(tea_number) for tea_number in teacher_creat.col_values(0)]
        tea_name=[tea_name for tea_name in teacher_creat.col_values(1)]
        tea_tea=[tea_tea for tea_tea in teacher_creat.col_values(2)]
        teacher_list=zip(tea_number,tea_name,tea_tea)
        for teacher in teacher_list:
            Teacher.create_tea(*teacher)

    def students(student_creat):
        stu_number=[int(stu_number) for stu_number in student_creat.col_values(0)]
        stu_name=[stu_name for stu_name in student_creat.col_values(1)]
        student_list=zip(stu_number,stu_name)
        for student in student_list:
            Student.create_stu(*student)

    schools(school_creat)
    classes(classes_creat)
    teachers(teacher_creat)
    students(student_creat)
   





    
   
    
  





    
