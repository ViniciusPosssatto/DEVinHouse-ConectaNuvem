from src.app.models.city import City


def test_new_city():
    city = City.seed(
        20,
        "City test name"
    )

    assert city.state_id == 20
    assert city.name == "City test name"