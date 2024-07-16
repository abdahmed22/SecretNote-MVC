all: install_requirements

install_requirements:
	pip install --no-cache-dir -r requirements.txt

run_sever: install_requirements
	python3 secretnote/manage.py runserver

build_image:
	docker build --tag=buildme-secretnote:v3.0

run_container:
	docker compose up