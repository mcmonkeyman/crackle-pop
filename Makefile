pip=./venv/bin/pip3
python=./venv/bin/python3

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv -p python3 venv
	. venv/bin/activate; $(pip) install -Ur requirements.txt
	touch venv/bin/activate

clean:
	rm -rf venv
	find -iname "*.pyc" -delete

freeze:
	$(pip) freeze > requirements.txt

run: venv
	python ./cracklepop.py

test: venv
	python ./cracklepoptest.py
