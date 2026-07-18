push:
	cd src && source ./venv/bin/activate && pip freeze > ./requirements.txt
	git commit --amend .
	git push
	
run: build
	cd src && source ./venv/bin/activate && fastapi run ./main.py
build:
	chmod +x ./setup.sh
	./setup.sh
