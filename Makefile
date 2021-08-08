HOST=127.0.0.1
PORT=5000
ENVIRONMENT=development

all: help

build:
	python3 -m venv venv
	. venv/bin/activate
	./venv/bin/pip3 install -r requirements.txt

clean:
	rm -rf venv
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	rm -rf .pytest_cache/

run: 
	. venv/bin/activate
	FLASK_APP=main.py \
		FLASK_ENV=${ENVIRONMENT} \
		./venv/bin/flask run --host=${HOST} --port=${PORT}

lint:
	. venv/bin/activate
	./venv/bin/flake8 --ignore D203 \
		 --exclude .git,__pycache__,venv \
		 --max-complexity 10

test:
	. venv/bin/activate
	./venv/bin/pytest --cache-clear

# docker-run:
#     docker build \
#       --file=./Dockerfile \
#       --tag=sms-comms ./
#     docker run \
#       --detach=false \
#       --name=sms-comms \
#       --publish=$(HOST):8080 \
#       sms-comms

help:
	@echo "    build"
	@echo "        Build virtual env and install packages"
	@echo "    clean"
	@echo "        Remove python artifacts."
	@echo '    run'
	@echo '        Run the `sms-comms' service on localhost, OPTIONAL: specify the port --PORT=5000 and/or --HOST=0.0.0.0 
	@echo "    lint"
	@echo "        Check style with flake8."
	@echo "    test"
	@echo "        Run all unit tests in the test directory"
	@echo '    docker-run'
	@echo '        Build and run the `sms-comms` service in a Docker container.'

.PHONY: build clean run lint test
