from peewee import CharField, Model, DateField
class Cliente(Model):
    name = CharField()
     = DateField()

    class Meta:
        database = db