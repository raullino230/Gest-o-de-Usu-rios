from peewee import CharField, Model, DateTimeField,



class Cliente(Model):
    nome = CharField()
    email = CharField()
    data_registro= DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db