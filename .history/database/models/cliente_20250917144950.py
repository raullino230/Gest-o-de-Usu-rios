from peewee import CharField, Model, DateField
class Cliente(Model):
    name = CharField()
     data_cria= DateField()

    class Meta:
        database = db