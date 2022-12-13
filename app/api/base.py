import os
import itertools
from datetime import datetime
from app.factory import collection
from bson.objectid import ObjectId
from app.utils.slugify import slugify
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
from app.utils.return_url import return_url_file
from flask import request, jsonify, make_response, Blueprint

api_todos = Blueprint("api_todos", __name__)
api = Api(api_todos)


class Todos(Resource):
    """CRUD Operations for Todos. Methods: GET, POST, PUT, DELETE."""

    def get(self):
        """Get all todos and its images."""
        todos_content = collection.find()
        todos = [todo for todo in todos_content]
        return make_response(
            jsonify(
                [
                    {
                        "id": str(todo["_id"]),
                        "slug": todo["slug"],
                        "title": todo["title"],
                        "description": todo["description"],
                        "completed": todo["completed"],
                        "image": [
                            {
                                "url": image,
                            }
                            for image in todo["image"]
                        ],
                        "date_created": todo["date_created"],
                        "date_modified": todo["date_modified"],
                    }
                    for todo in todos
                ]
            ),
            200,
        )

    def post(self):
        """Create a todo and its images."""
        title = request.form.get("title")
        slug = slugify(title)
        description = request.form.get("description")
        completed = request.form.get("completed")
        images = request.files.getlist("image")

        for image in images:
            filename = secure_filename(image.filename)
            image.save(os.path.join(os.getcwd(), "static/images", slugify(filename)))

        collection.insert_one(
            {
                "slug": slug,
                "title": title,
                "description": description,
                "completed": completed,
                "image": [return_url_file(slugify(image.filename)) for image in images],
                "date_created": datetime.now(),
                "date_modified": datetime.now(),
            }
        )
        return make_response(jsonify({"success": "Todo created"}), 200)


class Todo(Resource):
    """CRUD Operations for Todo. Methods: GET, PUT, DELETE."""

    def get(self, id):
        """Get a one todo and its images."""
        todo = collection.find_one({"_id": ObjectId(id)})
        return make_response(
            jsonify(
                {
                    "id": str(todo["_id"]),
                    "slug": todo["slug"],
                    "title": todo["title"],
                    "description": todo["description"],
                    "completed": todo["completed"],
                    "image": [
                        {
                            "url": image,
                        }
                        for image in todo["image"]
                    ],
                    "date_created": todo["date_created"],
                    "date_modified": todo["date_modified"],
                }
            ),
            200,
        )

    def put(self, id):
        """Update a todo and its images."""
        todo = collection.find_one({"_id": ObjectId(id)})
        title = request.form.get("title")
        description = request.form.get("description")
        completed = request.form.get("completed")
        images = request.files.getlist("image")

        if title:
            todo["title"] = title
            todo["slug"] = slugify(title)

        if description:
            todo["description"] = description

        if completed:
            todo["completed"] = completed

        if images:
            todo["image"] = list(
                itertools.chain(
                    todo["image"],
                    [return_url_file(slugify(image.filename)) for image in images],
                )
            )

            for image in images:
                filename = secure_filename(image.filename)
                image.save(
                    os.path.join(os.getcwd(), "static/images", slugify(filename))
                )

        todo["date_modified"] = datetime.now()

        collection.update_one({"_id": ObjectId(id)}, {"$set": todo})
        return make_response(jsonify({"success": "Todo updated"}), 200)

    def delete(self, id):
        """Delete a todo and its images."""
        todo = collection.find_one({"_id": ObjectId(id)})

        for image in todo["image"]:
            try:
                os.remove(
                    os.path.join(os.getcwd(), "static/images", image.split("/")[-1])
                )
            except FileNotFoundError:
                pass

        collection.delete_one({"_id": ObjectId(id)})
        return make_response(jsonify({"success": "Todo deleted"}), 200)


# Routes for Todos
api.add_resource(Todos, "/")
api.add_resource(Todo, "/todo/<id>")
