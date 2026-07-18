run: build
	cd src && fastapi run ./main.py
build:
	chmod +x ./setup.sh
	./setup.sh