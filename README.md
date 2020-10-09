### Product Table

| Product ID    | Product Name         | Price         |
| ------------- | -------------------- | ------------- |
| wf            | Workflow             |               |
| docgen        | Document Generation  |               |
| form          | Form                 |               |

### Promo Code Table

| id  | Second Header | First Header  | Second Header |
| ------------- | ------------- | ------------- | ------------- |
| 0   | Content Cell  |
| Content Cell  | Content Cell  |

### API LIST

    GET  - /api/v1/products
    POST - /api/v1/promo-details
    POST - /api/v1/apply-promo
    POST - /api/v1/checkout
    POST - /api/v1/add-promo
    POST - /api/v1/invalidate-promo
    
    
 #!/bin/bash

echo "Creating tables..."
python manage.py create_db

echo "Initializing tables..."
python manage.py db init

echo "Apply database migrations..."
python manage.py db migrate

echo "Running the server..."
python manage.py runserver