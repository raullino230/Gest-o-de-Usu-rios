from peewee import CharField, Model, DateField
class Cliente(Model):
    name = CharField()
     data= DateField()

    class Meta:
        database = db