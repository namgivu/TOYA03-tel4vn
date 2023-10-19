:: cd .../python_consoleapp


echo '--- before'; ./.venv/Scripts/pip freeze

# install :requests
./.venv/Scripts/pip install requests

echo '--- after' ; ./.venv/Scripts/pip freeze
