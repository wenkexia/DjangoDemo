from rest_framework import serializers
from . import models

# 序列化器
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('stu_id','stu_name','stu_gender','stu_class')

class ClassModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Class
        fields = ('cls_id','cls_name')


class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('tea_id','tea_name','tea_class')