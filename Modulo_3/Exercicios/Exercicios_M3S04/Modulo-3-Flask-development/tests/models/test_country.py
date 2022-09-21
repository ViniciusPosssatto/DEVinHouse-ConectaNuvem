from src.app.models.country import Country


def test_new_country():
    country = Country.seed(
        "country test name",
        "English"
    )

    assert country.name == "country test name"
    assert country.language == "English"