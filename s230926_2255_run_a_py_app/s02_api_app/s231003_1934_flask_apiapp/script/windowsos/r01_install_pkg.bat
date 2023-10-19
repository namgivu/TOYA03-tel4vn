:: cd .../flask_apiapp


echo '--- before'; ./.venv/Scripts/pip freeze

# install :requests
./.venv/Scripts/pip flask

echo '--- after' ; ./.venv/Scripts/pip freeze
