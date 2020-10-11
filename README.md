

### API LIST

    GET  - /api/v1/products/getall 
    POST - /api/v1/promo-details
    POST - /api/v1/apply-promo
    POST - /api/v1/add-promo
    
    
    
 #!/bin/bash

echo "Creating tables..."
python manage.py create_db

echo "Initializing tables..."
python manage.py db init

echo "Apply database migrations..."
python manage.py db migrate

echo "Running the server..."
python manage.py runserver


## product :

    {
        "product_id": "wf",
        "product_name": "Workflow",
        "price": 199.99
    }
    
     {
        "product_id": "docgen",
        "product_name": "Document Generation",
        "price": 9.99
     }
     
      {
        "product_id": "form",
        "product_name": "Form",
        "price": 99.99
     }
    
### Promo Code

##### Add Promo Code

    POST - http://localhost:8000/api/v1/add-promo

##### Flat Category

    {
        "promo_code": "RRD4D32",
        "is_flat": true,
        "discount_type": true,
        "amount": 10 ,
        "least_amount": 1000
    }
    
    {
        "promo_code": "44F4T11",
        "is_flat": true,
        "discount_type": true,
        "amount": 15 ,
        "least_amount": 1500
    }


#####  Conditional Category


    {
        "promo_code": "FF9543D1",
        "is_flat": false,
        "discount_type": false,
        "amount": 8.99 ,
        "quantity": 10,
        "product_id": 15,
        "target_product_id: 14
    }
    
    {
        "promo_code": "YYGWKJD",
        "is_flat": false,
        "discount_type": false,
        "amount": 89.99 ,
        "quantity": 1,
        "product_id": 13,
        "target_product_id":15
    }
   
   * discount_type - Dollar(False)
   * amount - Discount Amount (Can be in percentage or dollar)
   * quantity - Least amount (Can be quantity )
   * least_amount - Minimum amount(dollar) to avail flat discount
   
### Apply Promo

#### Flat Promo

    {
    "cart":[
        {
            "product_id": 1,
            "unit_price": 9.99,
            "quantity": 10  
        }
        ],
    "subtotal": 234,
    "promo_code": "44F4T11"
    }
    
    ----------------------------------------------------
    
    {
    "cart":[
        {
            "product_id": 1,
            "unit_price": 9.99,
            "quantity": 10  
        }
        ],
    "subtotal": 2000,
    "promo_code": "44F4T11"
    }
    
    ----------------------------------------------------
    
    {
    "cart":[
        {
            "product_id": 1,
            "unit_price": 9.99,
            "quantity": 10  
        }
        ],
    "subtotal": 2000,
    "promo_code": "RRD4D32"
    }
    
    ----------------------------------------------------
    {
    "cart":[
        {
            "product_id": 1,
            "unit_price": 9.99,
            "quantity": 10  
        }
        ],
    "subtotal": 2000,
    "promo_code": "FF9543D1"
    }
    
    
####  Conditional Promo


    {
    "cart":[
   
        {
            "product_id": 11,
            "unit_price": 9.99,
            "quantity": 11
        }
        ],
    "subtotal": 99.9,
    "promo_code": "FF9543D1"
    }
    
   Answer: subtotal
   
   
   
   
       {
                "product_id": 12,
                "unit_price": 99.99,
                "quantity": 10  
            },
             {
                "product_id": 13,
                "unit_price": 8.99,
                "quantity": 1  
            }
            
            
* Which product price we have to reduce