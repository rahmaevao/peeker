format:
	@echo Format 💆
	isort .
	black .

up:
	@echo Start of 💄 🤭
	python peeker.py --path=tests/images/ninja_turtles.jpeg
