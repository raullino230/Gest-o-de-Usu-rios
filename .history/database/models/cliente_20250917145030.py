from peewee import CharField, Model, DateField
class Cliente(Model):
    name = CharField()
    email = CharField()
    data_c= DateField()

    class Meta:
        database = db