HOST=127.0.0.1
PORT=5000
TEST_PATH=./
ENVIRONMENT=development

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
		FLASK_ENV=development \
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

.PHONY: build clean run lint test
