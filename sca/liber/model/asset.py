from pymongo import MongoClient
from marrow.mongo import Index, Field
from marrow.mongo.field import String, Array, Mapping, Embed
from marrow.mongo.trait import Queryable, Identified


class Asset(Queryable):
	__collection__ = 'assets'
	
	class Metadata(Identified):
		id = String()
		value = Field()
	
	class Location(Identified):
		name = String()
	
	metadata = Mapping('.Metadata', key='id', default=lambda: [], assign=True, repr=False, positional=False)
	
	location = Array(Embed('.Location'), default=lambda: [], assign=True, repr=False, positional=False)
	
	metadata_ = Index('metadata.value')


db = MongoClient('mongodb://localhost/library').library
Item.bind(db)

