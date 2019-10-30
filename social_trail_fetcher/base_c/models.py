from pymodm import fields, MongoModel, EmbeddedMongoModel


class PersonTrail(MongoModel):
    cpf = fields.CharField(primary_key=True)
    last_query = fields.DateTimeField()
    transactions = fields.EmbeddedDocumentListField('Transaction')
    last_purchase = fields.EmbeddedDocumentField('LastPurchase')


class Transaction(EmbeddedMongoModel):
    date = fields.DateTimeField()
    value = fields.FloatField(min_value=0)


class LastPurchase(EmbeddedMongoModel):
    company = fields.CharField()
    date = fields.DateTimeField()
    value = fields.FloatField(min_value=0)
