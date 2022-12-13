import pytest
from flask import Flask
from decouple import config as env


@pytest.fixture()
def setup():
    """Setup the app for testing."""
    app = Flask(__name__)

    app.config["MONGO_DBNAME"] = env("MONGO_DB_URI_TEST")
    app.config["MONGO_COLLECTION"] = env("MONGO_COL_TEST")

    with app.app_context():
        yield app


@pytest.fixture()
def client(setup):
    """Setup the app for testing."""
    return setup.test_client()


@pytest.fixture()
def runner(setup):
    """Setup the app for testing."""
    return setup.test_cli_runner()
