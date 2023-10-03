--- prepare .venv/
python -V
python -m pip install --upgrade pip
python -m pip install --upgrade virtualenv
python -m virtualenv .venv

--- install Flask package
./.venv/bin/pip install Flask
./.venv/bin/pip freeze
