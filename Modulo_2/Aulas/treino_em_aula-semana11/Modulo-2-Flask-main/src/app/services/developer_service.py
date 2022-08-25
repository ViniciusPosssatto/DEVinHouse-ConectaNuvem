from sqlalchemy import func
from src.app.models.developer import Developer, developers_share_schema, developer_technologies
from src.app.models.technology import Technology, technologies_share_schema


def list_all_developers_service():

  list_developers = Developer.query.all()
  list_developers_dict = developers_share_schema.dump(list_developers)


  return list_developers_dict


def list_all_developers_techs():

  lista_all = Technology.query.join(Developer, Developer.id == Technology.id).group_by(Technology.id, Developer.id).all()
  
  var = technologies_share_schema.dump(lista_all)

  # lista_all = Developer.query.join(Technology, Developer.id == Technology.id).group_by(Technology.id, Developer.id).all()
  
  # var = developers_share_schema.dump(lista_all)

  return var