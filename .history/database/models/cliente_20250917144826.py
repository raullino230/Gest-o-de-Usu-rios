from peewee
class Cliente(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db