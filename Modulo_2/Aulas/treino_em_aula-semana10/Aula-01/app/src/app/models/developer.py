from src.app import DB, MA


class Developer(DB.Model):
    __tablename__ = "developers"
    id = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
    months_experience = DB.Column(DB.Integer, nullable=True)
    accepted_remote_work = DB.Column(DB.Boolean, nullable=True, default=True)
    # user_id = DB.Column(DB.Integer, DB.ForeignKey(User.id), nullable=True)

    def __init__(self, months, acc_remote, user_id):
        self.months_experience = months
        self.accepted_remote_work = acc_remote
        self.user_id = user_id


class DeveloperSchema(MA.Schema):
    class Meta:
        fields = ('id', 'months_experience', 'accepted_remote_work')


developer_share_schema = DeveloperSchema()
developers_share_schema = DeveloperSchema(many=True)
