--- prepare .venv/
python -V
python -m pip install --upgrade pip
python -m pip install --upgrade virtualenv
python -m virtualenv .venv

--- install Flask package
./.venv/bin/pip install Flask
./.venv/bin/pip freeze

--- api endpoint / and /hi
FLASK_APP=src.app  ./.venv/bin/flask run

curl localhost:5000
> hi @ index /

curl localhost:5000/hi
> hi @ /hi
