# Coderators

A Django web application to keep track of multi-user code snippets with pretty code formatting. Enjoy!

## How to run the project on a local machine?

Please, follow these instructions:

```
# navigate to some directory
cd ~/Desktop

# clone github repository
git clone git@github.com:zavanton123/coderators.git
cd coderators

# create virtual environment
python3 -m venv venv
source venv/bin/activate


# install the dependencies
pip install -r requirements.txt

# add private data to env/.env
DEBUG=on
SECRET_KEY=some-key
DATABASE_URL=some-db-url
SQLITE_URL=some-db-url
CACHE_URL=some-cache-url
REDIS_URL=some-redis-url


# migrate DB
python manage.py makemigrations
python manage.py migrate


# collect the static files
python manage.py collectstatic


# create translations
python manage.py makemessages -l ru
python manage.py compilemessages


# create admin user
python manage.py createsuperuser

# run the project on the server
python manage.py runserver 9999


```


## Check out the real life deployed project

* [Coderators](http://coderators2.herokuapp.com/) - Demo coderators website

## Contributing

You are welcome to contribute

## Versioning

You can check out the version history  [here](https://github.com/zavanton123/coderators/tags). 

## License

This project is licensed under the MIT License.
