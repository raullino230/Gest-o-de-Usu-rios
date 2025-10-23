
class (Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db