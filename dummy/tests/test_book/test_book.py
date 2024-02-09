import json
import pytest
from dummy.models import Book, Author


@pytest.mark.django_db(databases=["dummy"])
@pytest.mark.author
class TestBook:
    def test_book_model(self, client):
        """
        Test the Book model.

        Ensures that a Book object can be created with the correct attributes,
        and that the attributes can be retrieved from the object.
        """
        author = Author.objects.create(name="Albin", age=27)
        book = Book.objects.create(
            title="Some Title", author=author, price=50, pages=500
        )

        # Assert that the book has the correct attributes
        assert str(book) == "Some Title"
        assert book.title == "Some Title"
        assert book.price == 50
        assert book.author.name == "Albin"

    def test_book_list_create_view(self, client):
        """
        Test the list and create views of the Book model.

        Ensures that the list view returns a list of all books,
        that the create view creates a new book with the correct data,
        that the create view returns an error when invalid data is provided,
        and that the create view returns an error when duplicate data is provided.
        """
        # Get a list of all books
        response = client.get("/dummy/books/")
        assert response.status_code == 200
        assert len(response.json()["results"]) == 0

        # Create new books with valid data
        author1 = Author.objects.create(name="Albin", age=27)
        author2 = Author.objects.create(name="Ibhax", age=30)
        data = {"title": "Some Book", "price": 50, "pages": 500, "author": author1.id}
        response = client.post("/dummy/books/", data=data)
        assert response.status_code == 201

        data = {"title": "Some Book 2", "price": 60, "pages": 600, "author": author2.id}
        response = client.post("/dummy/books/", data=data)
        assert response.status_code == 201

        # Get a list of all books again
        response = client.get("/dummy/books/")
        assert response.status_code == 200
        assert len(response.json()["results"]) == 2
        assert response.json()["results"][0]["title"] == "Some Book"
        assert response.json()["results"][0]["price"] == 50
        assert response.json()["results"][0]["pages"] == 500

        # Get a sorted list of all books
        response = client.get("/dummy/books/?sort=-title")
        assert response.status_code == 200
        assert response.json()["results"][0]["title"] == "Some Book 2"

        # Try to create an book with duplicate data
        response = client.post("/dummy/books/", data=data)
        assert response.status_code == 400

        # Try to create an book with invalid data
        data = {"title": 555}
        response = client.post("/dummy/books/", data=data)
        assert response.status_code == 400

        # Try to create an book with invalid data type
        data = {"title": 77, "price": "99"}
        response = client.post("/dummy/books/", data=data)
        assert response.status_code == 400

    def test_book_retrieve_view(self, client):
        """
        Test the retrieve view of the Book model.

        Ensures that the retrieve view returns the correct book
        when given the correct ID.
        """
        author = Author.objects.create(name="Albin", age=27)
        book = Book.objects.create(
            title="Some Title", author=author, price=50, pages=500
        )

        response = client.get(f"/dummy/books/{book.id}/")
        assert response.status_code == 200
        assert response.json()["title"] == "Some Title"

    def test_book_update_view(self, client):
        """
        Test the update view of the Book model.

        Ensures that the update view updates the correct book
        when given the correct ID and data.
        """
        author = Author.objects.create(name="Albin", age=27)
        book = Book.objects.create(
            title="Some Title", author=author, price=50, pages=500
        )

        # Test the retrieve view
        response = client.get(f"/dummy/books/{book.id}/")
        assert response.status_code == 200
        assert response.json()["title"] == "Some Title"

        # Update the data
        data = {"title": "Some Book 2", "price": 60, "pages": 600, "author": author.id}
        update = client.patch(
            f"/dummy/books/{book.id}/",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        assert update.status_code == 200

        # Test the update view
        response = client.get(f"/dummy/books/{book.id}/")
        assert response.status_code == 200
        assert response.json()["pages"] == 600

    def test_book_patch_view(self, client):
        """
        Test the patch view of the Book model.

        Ensures that the patch view updates the correct book
        when given the correct ID and data.
        """
        author = Author.objects.create(name="Albin", age=27)
        book = Book.objects.create(
            title="Some Title", author=author, price=50, pages=500
        )

        # Test the retrieve view
        response = client.get(f"/dummy/books/{book.id}/")
        assert response.status_code == 200
        assert response.json()["price"] == 50

        # Update the data
        data = json.dumps({"pages": 800})
        update = client.patch(
            f"/dummy/books/{book.id}/",
            data=data,
            headers={"Content-Type": "application/json"},
        )
        assert update.status_code == 200

        # Test the update view
        response = client.get(f"/dummy/books/{book.id}/")
        assert response.status_code == 200
        assert response.json()["pages"] == 800

    def test_book_delete_view(self, client):
        """
        Test the delete view of the Book model.

        Ensures that the delete view deletes the correct book
        when given the correct ID.
        """
        author = Author.objects.create(name="Albin", age=27)
        book = Book.objects.create(
            title="Some Title", author=author, price=50, pages=500
        )

        # Test the retrieve view
        response = client.get(f"/dummy/books/{book.id}/")
        assert response.status_code == 200
        assert response.json()["price"] == 50

        # Delete the data
        update = client.delete(f"/dummy/books/{book.id}/")
        assert update.status_code == 204

        # Test the delete operation
        response = client.get(f"/dummy/books/{book.id}/")
        assert response.status_code == 404
