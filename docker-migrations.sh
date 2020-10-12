docker-compose run pay-checkout-backend python manage.py create_db && python manage.py db init && python manage.py db migrate

# docker-compose run pay-checkout-backend python manage.py db init 
# sleep 2
# docker-compose run pay-checkout-backend python manage.py db migrate