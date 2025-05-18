up:
	docker-compose up -d

down:
	docker-compose down

down_volume:
	docker-compose down -v

venv:
	python3 -m venv .venv
	grep -v 'mysql' requirements.txt | xargs -n 1 .venv/bin/pip install
