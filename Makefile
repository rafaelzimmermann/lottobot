

build:
	docker build . -t duckbot:latest

run:
	docker run -d duckbot:latest