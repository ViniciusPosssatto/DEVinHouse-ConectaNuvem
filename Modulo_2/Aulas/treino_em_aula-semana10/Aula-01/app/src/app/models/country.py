from src.app import DB, MA

class Country(DB.Model):
  __tablename__ = 'countries'
  id = DB.Column(DB.Integer, autoincrement = True, primary_key = True)
  name = DB.Column(DB.String(84), nullable = False)
  language = DB.Column(DB.String(84), nullable = False)

  def __init__(self, name, language):
    self.name = name
    self.language = language

class CountrySchema(MA.Schema):
  class Meta:
    fields = ('id', 'name', 'language')

country_share_schema = CountrySchema()
countries_share_schema = CountrySchema(many = True)