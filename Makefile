TAG=latest


IMAGE_NAME=simplespacegame:${TAG}


USER ?= $(shell whoami)
CURRENT_UID = $(shell id -u $(USER))
CURRENT_DIR = $(shell pwd)


develop:
	virtualenv env -p python3.5
	env/bin/pip install -Ue ".[develop]"


lint:
	pytest --pylama simplespacegame


gitclean:
	git clean -xfd --exclude env
