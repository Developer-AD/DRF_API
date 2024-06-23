# from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Student


# class StudentSerializer(serializers.Serializer):
#     '''By defaul you will not see id in json response to
#         see it, you have to add explicitly here'''

#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance

# ------------------- Model Serializer Start -----------------------
class StudentSerializer(serializers.ModelSerializer):
    """
    You have to user Either 'fields' or 'exclude'.

    You can use normal Serializer or Model Serializer both are good,
    but using Model serializer is good choice because we have to code less 
    and many built in things are present.
    """

    # --------------------- Customer Validation ----------------------------
    """The Django Rest Framework does not have Meta attribute. Don't user this 

       read_only_fields = ('name', 'roll') # Not Working.
       extra_kwargs = {
           'name': {'read_only': True},
           'roll': {'read_only': True},
        }
    """
    

    # If we update all fields then also our 'name' field will not update.
    # name = serializers.CharField(read_only=True) # Working.
    # roll = serializers.IntegerField(read_only=True) # Working.
    class Meta:
        model = Student

        # fields = ['id', 'name', 'roll', 'city']
        fields = '__all__'

        # exclude = ['roll']

        # ------------ Validations --------------
        # 1. Field Level Validation:-
        # def validate_roll(self, value):
        #     if value>20:
        #         raise serializers.ValidationError('Seat Full')
        #     return value
        # ------------ Validations --------------
# ------------------- Model Serializer End -----------------------