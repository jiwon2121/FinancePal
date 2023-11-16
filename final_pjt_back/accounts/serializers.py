from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# nickname = models.CharField(max_length=20, unique=True)
# address = models.TextField()
# # deposit_products = models.ManyToManyField()
# # saving_products = models.ManyToManyField()
# birth_date = models.DateField(1998-10-14)
# gender = models.BooleanField() # true: 남자, false: 여자
# profile_img = models.ImageField(blank=True)
# salary = models.IntegerField()
# balance = models.IntegerField()
# # follower = models.ManyToManyField()