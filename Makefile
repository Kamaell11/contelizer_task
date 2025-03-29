VENV_NAME=venv
PYTHON=python3
PIP=$(VENV_NAME)/bin/pip

run:
	docker build -t contelizer .
	docker run -p 8000:8000 contelizer

install:
	$(PYTHON) -m venv $(VENV_NAME)
	$(PIP) install -r requirements.txt

server:
	$(VENV_NAME)/bin/python manage.py runserver 0.0.0.0:8000

clean:
	rm -rf $(VENV_NAME)


docker-build:
	docker build -t contelizer .

docker-run:
	docker run -p 8000:8000 contelizer


.PHONY: install run test migrate server clean docker-build docker-run
