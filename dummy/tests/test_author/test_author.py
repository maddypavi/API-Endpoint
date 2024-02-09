import json
import pytest
from dummy.models import Author


@pytest.mark.django_db(databases=["dummy"])
@pytest.mark.author
class TestAuthor:
    def test_author_model(self, client):
        """
        Test the Author model.

        Ensures that an Author object can be created with the correct attributes,
        and that the attributes can be retrieved from the object.
        """
        author = Author.objects.create(name="Albin", age=27)

        # Assert that the author has the correct attributes
        assert str(author) == "Albin"
        assert author.name == "Albin"
        assert author.age == 27

    def test_author_list_create_view(self, client):
        """
        Test the list and create views of the Author model.

        Ensures that the list view returns a list of all authors,
        that the create view creates a new author with the correct data,
        that the create view returns an error when invalid data is provided,
        and that the create view returns an error when duplicate data is provided.
        """
        # Get a list of all authors
        response = client.get("/dummy/authors/")
        assert response.status_code == 200
        assert len(response.json()["results"]) == 0

        # Create new authors with valid data
        data = {"name": "User", "age": 27}
        response = client.post("/dummy/authors/", data=data)
        assert response.status_code == 201

        data = {"name": "User2", "age": 28}
        response = client.post("/dummy/authors/", data=data)
        assert response.status_code == 201

        # Get a list of all authors again
        response = client.get("/dummy/authors/")
        assert response.status_code == 200
        assert len(response.json()["results"]) == 2
        assert response.json()["results"][0]["name"] == "User"
        assert response.json()["results"][0]["age"] == 27

        # Get a sorted list of all authors
        response = client.get("/dummy/authors/?sort=-name")
        assert response.status_code == 200
        assert response.json()["results"][0]["name"] == "User2"

        # Search for an author
        response = client.get("/dummy/authors/?name=user2")
        assert response.status_code == 200
        assert response.json()["results"][0]["name"] == "User2"

        # Try to create an author with duplicate data
        response = client.post("/dummy/authors/", data=data)
        assert response.status_code == 400

        # Try to create an author with invalid data
        data = {"name": "User"}
        response = client.post("/dummy/authors/", data=data)
        assert response.status_code == 400

        # Try to create an author with invalid data type
        data = {"name": "User", "age": "27"}
        response = client.post("/dummy/authors/", data=data)
        assert response.status_code == 400

    def test_author_retrieve_view(self, client):
        """
        Test the retrieve view of the Author model.

        Ensures that the retrieve view returns the correct author
        when given the correct ID.
        """
        author = Author.objects.create(name="Albin", age=27)

        response = client.get(f"/dummy/authors/{author.id}/")
        assert response.status_code == 200
        assert response.json()["name"] == "Albin"
        assert response.json()["age"] == 27

    def test_author_update_view(self, client):
        """
        Test the update view of the Author model.

        Ensures that the update view updates the correct author
        when given the correct ID and data.
        """
        author = Author.objects.create(name="Albin", age=27)

        # Test the retrieve view
        response = client.get(f"/dummy/authors/{author.id}/")
        assert response.status_code == 200
        assert response.json()["name"] == "Albin"

        # Update the data
        data = json.dumps({"name": "Albin", "age": 28})
        update = client.patch(
            f"/dummy/authors/{author.id}/",
            data=data,
            headers={"Content-Type": "application/json"},
        )
        assert update.status_code == 200

        # Test the update view
        response = client.get(f"/dummy/authors/{author.id}/")
        assert response.status_code == 200
        assert response.json()["age"] == 28

    def test_author_patch_view(self, client):
        """
        Test the patch view of the Author model.

        Ensures that the patch view updates the correct author
        when given the correct ID and data.
        """
        author = Author.objects.create(name="Albin", age=27)

        # Test the retrieve view
        response = client.get(f"/dummy/authors/{author.id}/")
        assert response.status_code == 200
        assert response.json()["name"] == "Albin"

        # Update the data
        data = json.dumps({"age": 28})
        update = client.patch(
            f"/dummy/authors/{author.id}/",
            data=data,
            headers={"Content-Type": "application/json"},
        )
        assert update.status_code == 200

        # Test the update view
        response = client.get(f"/dummy/authors/{author.id}/")
        assert response.status_code == 200
        assert response.json()["age"] == 28

    def test_author_delete_view(self, client):
        """
        Test the delete view of the Author model.

        Ensures that the delete view deletes the correct author
        when given the correct ID.
        """
        author = Author.objects.create(name="Albin", age=27)

        # Test the retrieve view
        response = client.get(f"/dummy/authors/{author.id}/")
        assert response.status_code == 200
        assert response.json()["name"] == "Albin"

        # Delete the data
        update = client.delete(f"/dummy/authors/{author.id}/")
        assert update.status_code == 204

        # Test the delete operation
        response = client.get(f"/dummy/authors/{author.id}/")
        assert response.status_code == 404
