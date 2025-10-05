from tortoise import fields
from tortoise.models import Model
from datetime import datetime


class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    price = fields.FloatField()
    reviews: fields.ReverseRelation["Review"]
    summary: fields.ReverseRelation["Summary"]

    class Meta:
        table = "products"


class Review(Model):
    id = fields.IntField(pk=True)
    author = fields.CharField(max_length=255)
    rating = fields.IntField()
    content = fields.TextField()
    created_at = fields.DatetimeField(default=datetime.utcnow)
    product = fields.ForeignKeyField(
        "models.Product", related_name="reviews", on_delete=fields.CASCADE
    )

    class Meta:
        table = "reviews"


class Summary(Model):
    id = fields.IntField(pk=True)
    product = fields.OneToOneField(
        "models.Product", related_name="summary", on_delete=fields.CASCADE
    )
    content = fields.TextField()
    generated_at = fields.DatetimeField(default=datetime.utcnow)
    expires_at = fields.DatetimeField()

    class Meta:
        table = "summaries"
