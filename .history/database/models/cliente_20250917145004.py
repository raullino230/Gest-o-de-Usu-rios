from peewee import CharField, Model, DateField
class Cliente(Model):
    name = CharField()
     = CharField()
    data_criaçõa= DateField()

    class Meta:
        database = db