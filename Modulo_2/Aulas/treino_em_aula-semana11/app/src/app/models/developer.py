from src.app import DB, MA
from src.app.models.user import User


developer_technologies = DB.Table('developer_technologies',
                    DB.Column('developer_id', DB.Integer, DB.ForeignKey('developers.id')),
                    DB.Column('technology_id', DB.Integer, DB.ForeignKey('technologies.id'))
                    )


class Developer(DB.Model):
  __tablename__ = "developers"
  id = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
  months_experience = DB.Column(DB.Integer, nullable = True)
  accepted_remote_work = DB.Column(DB.Boolean, nullable = False, default = True)
  user_id = DB.Column(DB.Integer, DB.ForeignKey(User.id), nullable = False)
  technologies = DB.relationship('Technology', secondary=developer_technologies, backref='developers')

  def __init__(self, months_experience, accepted_remote_work, user_id, technologies):
    self.months_experience = months_experience
    self.accepted_remote_work = accepted_remote_work
    self.user_id = user_id
    self.technologies = technologies

  @classmethod
  def seed(cls, months_experience, accepted_remote_work, user_id, technologies):
    developer = Developer(
      months_experience = months_experience,
      accepted_remote_work = accepted_remote_work, 
      user_id = user_id,
      technologies = technologies)

    developer.save()

  def save(self): 
    DB.session.add(self)
    DB.session.commit()

class DeveloperSchema(MA.Schema):
  class Meta:
    fields = ('id', 'months_experience', 'accepted_remote_work', 'user_id', 'technologies')

developer_share_schema = DeveloperSchema()
developers_share_schema = DeveloperSchema(many = True)