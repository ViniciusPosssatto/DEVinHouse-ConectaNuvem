from src.app import DB, MA
from src.app.models.country import Country

class State(DB.Model): 
  __tablename__ = "states"
  id = DB.Column(DB.Integer, autoincrement = True, primary_key = True)
  country_id = DB.Column(DB.Integer, DB.ForeignKey(Country.id), nullable = False)
  name = DB.Column(DB.String(84), nullable = False)
  initials = DB.Column(DB.String(2), nullable = False)

  def __init__(self, country_id, name, initials):
    self.country_id = country_id
    self.name = name
    self.initials = initials
  
  @classmethod
  def seed(cls, country_id, name, initials):
    state = State(
      country_id = country_id,
      name = name,
      initials = initials
    )
    state.save()

  def save(self): 
    DB.session.add(self)
    DB.session.commit()

class StateSchema(MA.Schema):
  class Meta:
    fields = ('id', 'country_id', 'name', 'initials')

state_share_schema = StateSchema()
states_share_schema = StateSchema(many = True)