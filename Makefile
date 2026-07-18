run: build
	cd src && source ./venv/bin/activate && fastapi run ./main.py
build:
	chmod +x ./setup.sh
	./setup.sh