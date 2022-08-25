
# from src.app import DB, MA


# class Developer(DB.Model):
#     __tablename__ = "developers"
#     id = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
#     months_experience = DB.Column(DB.Integer, nullable=True)
#     accepted_remote_work = DB.Column(DB.Boolean, nullable=True, default=True)

#     def __init__(self, months, acc_remote):
#         self.months_experience = months
#         self.accepted_remote_work = acc_remote


# class DeveloperSchema(MA.Schema):
#     class Meta:
#         fields = ('id', 'months_experience', 'accepted_remote_work')


# developer_share_schema = DeveloperSchema()
# developers_share_schema = DeveloperSchema(many=True)


from flask import Blueprint


developers = Blueprint('developers', __name__, url_prefix="/developer")


@developers.route('/', methods=["GET"])
def list_all_developers():
    return jsonify({"data": ["alguém", "outrão", "fulâano"]})


@developers.route('/', methods=["POST"])
def list_new_developers():
    return {"data": ["alguém", "outrão", "fulâano"]}