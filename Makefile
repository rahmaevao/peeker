format:
	@echo Format 💆
	isort .
	black .

up:
	@echo Start of 💄 🤭
	python peeker.py tests/images/ninja_turtles.jpeg
