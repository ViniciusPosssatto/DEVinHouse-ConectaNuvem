from src.app.models.user import User
from src.app.models.role import Role


def test_new_user():
    user = User.seed(
        1,
        "Teste Name",
        23,
        "teste_email@teste.com",
        "123Senha!",
        Role.query.filter_by(description = "OWNER").all()
    )

    assert user.city_id == 1
    assert user.name == "Teste Name"
    assert user.age == 23
    assert user.email == "teste_email@teste.com"
    # assert user.password == "123Senha!"
    assert user.roles[0].description == "OWNER"
  