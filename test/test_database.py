from test.fixtures import setup
from pymongo import MongoClient
from datetime import datetime
from decouple import config as env

client = MongoClient(env("MONGO_DB_URI_TEST"))
db = client[env("MONGO_DB_NAME_TEST")]
collection = db[env("MONGO_COL_TEST")]


# Test Database Connection.
def test_database_name():
    assert db.name == "todo-test"


def test_database_collection():
    assert collection.name == "todo-collection"


def test_database_collection_count(setup):
    assert collection.count_documents({}) == 0


# Test CRUD Operations.
def test_create_todo():
    todo = {
        "slug": "test-slug",
        "title": "test-title",
        "description": "test-description",
        "completed": False,
        "image": [],
        "date_created": datetime.now(),
        "date_modified": datetime.now(),
    }
    collection.insert_one(todo)
    assert collection.count_documents({}) == 1


def test_read_todo():
    todo = collection.find_one({"slug": "test-slug"})
    assert todo["slug"] == "test-slug"
    assert todo["title"] == "test-title"
    assert todo["description"] == "test-description"
    assert todo["completed"] == False
    assert todo["image"] == []
    assert todo["date_created"] == todo["date_modified"]


def test_update_todo():
    collection.update_one(
        {"slug": "test-slug"},
        {
            "$set": {
                "title": "test-title-updated",
                "description": "test-description-updated",
                "completed": True,
                "image": ["test-image"],
                "date_modified": datetime.now(),
            }
        },
    )
    todo = collection.find_one({"slug": "test-slug"})
    assert todo["slug"] == "test-slug"
    assert todo["title"] == "test-title-updated"
    assert todo["description"] == "test-description-updated"
    assert todo["completed"] == True
    assert todo["image"] == ["test-image"]
    assert todo["date_created"] != todo["date_modified"]


def test_delete_todo():
    collection.delete_one({"slug": "test-slug"})
    assert collection.count_documents({}) == 0
