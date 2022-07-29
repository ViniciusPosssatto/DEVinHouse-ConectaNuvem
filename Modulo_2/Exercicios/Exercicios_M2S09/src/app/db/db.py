from tinydb import TinyDB, Query


db_user = TinyDB('src/app/db/users_db.json')

User = Query()


def insert_user_db(user):
    db_user.insert(user)


def search_user_db(key, param):
    return db_user.search(User[key] == param)


def delete_user_db(key, value):
    return db_user.remove(User[key] == value)



def search_all():
    return db_user.all()


def update_user_db(key: str, value, user):
    db_user.update(user, User[key] == value)


# search_user_db("nome", "joao")
# print(db_user.all())
# print('-------------------------')
# delete_user_db("id", 1)
# print(db_user.all())
