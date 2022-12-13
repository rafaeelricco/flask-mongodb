from flask import request


def return_url_file(filename):
    """Get the local host url and return the file path"""

    host = request.host_url
    return f"{host}static/images/{filename}"
