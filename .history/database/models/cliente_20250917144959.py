from peewee import CharField, Model, DateField
class Cliente(Model):
    name = CharField()
    data_criaçõa= DateField()

    class Meta:
        database = db