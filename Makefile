format:
	@echo Format 💆
	isort .
	black .

up:
	@echo Start of 💄 🤭
	streamlit run main.py
