from peewee import CharField, Model, DateField
from


class Cliente(Model):
    name = CharField()
    email = CharField()
    data_registro= DateField()

    class Meta:
        database = db