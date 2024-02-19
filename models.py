from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

# This code is describing models and create Pydantic models


class Users(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    gender = fields.CharField(max_length=255)
    status = fields.CharField(max_length=255)


Users_Pydantic = pydantic_model_creator(Users, name="User")


class Posts(Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField()
    title = fields.CharField(max_length=255)
    body = fields.CharField(max_length=1000)


Posts_Pydantic = pydantic_model_creator(Posts, name="Post")
