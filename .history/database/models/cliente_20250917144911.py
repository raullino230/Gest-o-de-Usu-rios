from peewee import CharField, Model, DateField
class Cliente(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db