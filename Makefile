all: install_requirements

install_requirements:
	pip install --no-cache-dir -r requirements.txt

run_sever: install_requirements
	python3 secretnote/manage.py runserver

run_tests:
	python manage.py test

build_image:
	docker build --tag=buildme-secretnote:v5.0 --target=base .

run_container:
	docker compose up

