from peewee import CharField, Model
class Cliente(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db