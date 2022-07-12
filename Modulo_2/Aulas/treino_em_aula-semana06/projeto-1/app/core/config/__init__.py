from os.path import abspath, join, dirname


class Settings:

    ROOT_PATH = dirname(dirname(dirname(abspath(__file__))))
    DATA_PATH = join(ROOT_PATH, "data")

    DATABASE_PATH = join(DATA_PATH, "database.json")
    print(DATABASE_PATH)
