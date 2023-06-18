# Welcome to the reviewAPI docs
<br></br>

## Docs
#### You can see Swagger type docs in the api url and [``/docs#``](http://127.0.0.1:8000/docs#)

## Get started

### Register and login
You can sign up with POST in ``/register`` with the following json form

        {"username": "YOURUSER",
        "password": "YOURPASS"}


<br></br>
Once registered you can access to the ``/login`` and, POST, with the same form as signing up, you can authorize yourself.

You can see your user info by sending a GET to ``/user``

<br></br>
### Categories

You have a list of the categories and the products thereof on GET ``/category/{id}`` where ``{id}`` is a query for id

If you use a GET without any id it will returns you a list of all categories

The categories JSON format is:

        {
            "id": 1,
            "className": "Laptop"
        }

<br></br>
### Products

By sending a GET to ``/products`` you receive a all products list with the following format:

        {
            "productName": "UltraBook X1",
            "price": 1499,
            "id": 1,
            "from_class": 1
        }

<br></br>

You can also upload a product doing a POST to ``/products`` with:

        {
            "productName": "UltraBook X1",
            "price": 1499,
            "from_class": 1
        }

<br></br>

### Reviews

API allows you to post revies for products in a product or including the product in the json.


        # For upload a general review need to POST:
        {
            "content": "Great product!",
            "for_product": 1
        }

        # And upload a review in /product/{id} is like:
        {
            "content": "Great product!",
        }

<br></br>

You can see as administrator all reviews in ``/revies`` or search for all your reviews in ``/myreviews``. Review object has this schema:

        {
            "content": "Great product!",
            "id": 3,
            "created_by": 1,
            "for_product": 1
        }







    {
        "content": "Great product!",
        "id": 3,
        "created_by": 1,
        "for_product": 1
    }


<br></br>

## Tecnologies included in this proyect
<ul class="contains-task-list">
  <li class="task-list-item"><input type="checkbox" disabled="" checked="checked"> RestAPI</li>
  <li class="task-list-item"><input type="checkbox" disabled="" checked="checked"> SQL ORM</li>
  <li class="task-list-item"><input type="checkbox" disabled="" checked="checked"> Static resources</li>
  <li class="task-list-item"><input type="checkbox" disabled="" checked="checked"> POO</li>
  <li class="task-list-item"><input type="checkbox" disabled=""> GraphQL (Soon)</li>
</ul>

