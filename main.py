from flask import *

app = Flask(__name__)

buildings = [
    {
        "id": 1,
        "name": "Building 1",
        "address": "Address 1",
        "manager": "Manager 1",
        "description": "Description 1",
        "image": "../static/images/apartment1.jpg",
        "Parking": 1,
    },
    {
        "id": 2,
        "name": "Building 2",
        "address": "Address 2",
        "manager": "Manager 2",
        "description": "Description 2",
        "image": "Image 2",
        "Parking": 2,
    },
    {
        "id": 3,
        "name": "Building 3",
        "address": "Address 3",
        "manager": "Manager 3",
        "description": "Description 3",
        "image": "Image 3",
        "Parking": 3,
    },
    {
        "id": 4,
        "name": "Building 4",
        "address": "Address 4",
        "manager": "Manager 4",
        "description": "Description 4",
        "image": "Image 4",
        "Parking": 4,
    },
    {
        "id": 5,
        "name": "Building 5",
        "address": "Address 5",
        "manager": "Manager 5",
        "description": "Description 5",
        "image": "Image 5",
        "Parking": 5,
    },
    {
        "id": 5,
        "name": "Building 5",
        "address": "Address 5",
        "manager": "Manager 5",
        "description": "Description 5",
        "image": "Image 5",
        "Parking": 5,
    },
    {
        "id": 5,
        "name": "Building 5",
        "address": "Address 5",
        "manager": "Manager 5",
        "description": "Description 5",
        "image": "Image 5",
        "Parking": 5,
    },
    {
        "id": 5,
        "name": "Building 5",
        "address": "Address 5",
        "manager": "Manager 5",
        "description": "Description 5",
        "image": "Image 5",
        "Parking": 5,
    },
    {
        "id": 5,
        "name": "Building 5",
        "address": "Address 5",
        "manager": "Manager 5",
        "description": "Description 5",
        "image": "Image 5",
        "Parking": 5,
    },
    {
        "id": 5,
        "name": "Building 5",
        "address": "Address 5",
        "manager": "Manager 5",
        "description": "Description 5",
        "image": "Image 5",
        "Parking": 5,
    },
    {
        "id": 5,
        "name": "Building 5",
        "address": "Address 5",
        "manager": "Manager 5",
        "description": "Description 5",
        "image": "Image 5",
        "Parking": 5,
    },
    {
        "id": 5,
        "name": "Building 5",
        "address": "Address 5",
        "manager": "Manager 5",
        "description": "Description 5",
        "image": "Image 5",
        "Parking": 5,
    },
    {
        "id": 5,
        "name": "Building 5",
        "address": "Address 5",
        "manager": "Manager 5",
        "description": "Description 5",
        "image": "Image 5",
        "Parking": 5,
    },
    {
        "id": 5,
        "name": "Building 5",
        "address": "Address 5",
        "manager": "Manager 5",
        "description": "Description 5",
        "image": "Image 5",
        "Parking": 5,
    },
    {
        "id": 5,
        "name": "Building 5",
        "address": "Address 5",
        "manager": "Manager 5",
        "description": "Description 5",
        "image": "Image 5",
        "Parking": 5,
    },
    {
        "id": 5,
        "name": "Building 5",
        "address": "Address 5",
        "manager": "Manager 5",
        "description": "Description 5",
        "image": "Image 5",
        "Parking": 5,
    },
    {
        "id": 5,
        "name": "Building 5",
        "address": "Address 5",
        "manager": "Manager 5",
        "description": "Description 5",
        "image": "Image 5",
        "Parking": 5,
    },
    {
        "id": 5,
        "name": "Building 5",
        "address": "Address 5",
        "manager": "Manager 5",
        "description": "Description 5",
        "image": "Image 5",
        "Parking": 5,
    }]


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/test")
def test():
    return "Test"


if __name__ == "__main__":
    app.run(debug=True)
