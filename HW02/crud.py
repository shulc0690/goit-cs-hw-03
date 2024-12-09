from pymongo import MongoClient, errors
from bson.objectid import ObjectId
from pymongo.server_api import ServerApi

# Підключення до MongoDB
uri = "mongodb+srv://shulc0690:IWJ1ftVT5RThS35D@cluster0.ytrpt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi("1"))
db = client["cat_database"]
collection = db["cats"]


def add_cat(name, age, features):
    """
    Функція для додавання кота (Create)
    """
    cat = {"name": name, "age": age, "features": features}
    try:
        collection.insert_one(cat)
        print(f"Кота '{name}' додано до бази даних.")
    except errors.PyMongoError as e:
        print(f"Помилка при додаванні кота: {e}")


def get_all_cats():
    """
    Функція для виведення всіх записів (Read)
    """
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except errors.PyMongoError as e:
        print(f"Помилка при отриманні котів: {e}")


def get_cat_by_name(name):
    """
    Функція для виведення інформації про кота за ім'ям (Read)
    """
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кота з ім'ям '{name}' не знайдено.")
    except errors.PyMongoError as e:
        print(f"Помилка при отриманні кота: {e}")


def update_cat_age(name, age):
    """
    Функція для оновлення віку кота за ім'ям (Update)
    """
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": age}})
        if result.modified_count > 0:
            print(f"Вік кота '{name}' оновлено до {age}.")
        else:
            print(f"Кота з ім'ям '{name}' не знайдено.")
    except errors.PyMongoError as e:
        print(f"Помилка при оновленні віку кота: {e}")


def add_feature_to_cat(name, feature):
    """
    Функція для додавання нової характеристики до списку features (Update)
    """
    try:
        result = collection.update_one(
            {"name": name}, {"$addToSet": {"features": feature}}
        )
        if result.modified_count > 0:
            print(f"Характеристику '{feature}' додано до кота '{name}'.")
        else:
            print(f"Кота з ім'ям '{name}' не знайдено.")
    except errors.PyMongoError as e:
        print(f"Помилка при додаванні характеристики коту: {e}")


def delete_cat_by_name(name):
    """
    Функція для видалення кота за ім'ям (Delete)
    """
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кота з ім'ям '{name}' видалено.")
        else:
            print(f"Кота з ім'ям '{name}' не знайдено.")
    except errors.PyMongoError as e:
        print(f"Помилка при видаленні кота: {e}")


def delete_all_cats():
    """
    Функція для видалення всіх записів (Delete)
    """
    try:
        result = collection.delete_many({})
        print(f"Видалено {result.deleted_count} записів.")
    except errors.PyMongoError as e:
        print(f"Помилка при видаленні всіх котів: {e}")


# Приклади викликів функцій
if __name__ == "__main__":
    add_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    get_all_cats()
    get_cat_by_name("barsik")
    update_cat_age("barsik", 4)
    add_feature_to_cat("barsik", "любить рибу")
    delete_cat_by_name("barsik")
    delete_all_cats()
