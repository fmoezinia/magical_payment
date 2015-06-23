#database functionality. Collection of info comprising: phone number(user), shipping address, credit card token from stripe



from pymongo import MongoClient
client = MongoClient('mongodb://dbmagic:znmagic2@ds036698.mongolab.com:36698/darksidemagic')


data = [{'user': '+17186121018', 
'shipping': ['12 Upper Phillimore Gardens', 'w8 7ha', 'London', 'UK'],
'stripe_token': 'xxxxx'
}]


result = db.user_information.insert_one(data)


#The operation returns an InsertOneResult object, which includes an attribute inserted_id that contains the _id of the inserted document. Access the inserted_id attribute:

result.inserted_id

#>>> db.userinfo.find_one({'x': 1})
#{u'x': 1, u'_id': ObjectId('54f112defba522406c9cc208')}

#In MongoDB, the db.collection.insert() method adds new documents into a collection.

#db.user_information.find()
#will return the data plus a _id section with objectID

#db.user_information.replace_one()
#if user shipping needs to be updated (use user phone number)

