:: cd .../python_consoleapp


echo '--- before'; ./.venv/Scripts/pip freeze

./.venv/Scripts/python -m pip install --upgrade pip

echo '::install :requests'
./.venv/Scripts/pip install requests

echo '--- after' ; ./.venv/Scripts/pip freeze