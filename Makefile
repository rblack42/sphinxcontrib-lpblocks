.PHONY: init
init:
	test -d _venv || \
	python3 -m venv _venv && \
	source _venv/bin/activate && \
	pip install -U pip

.PHONY: reqs
reqs:
	source _venv/bin/activate && \
	pip install -r requirements.txt

.PHONY: docs
docs:
	source _venv/bin/activate && \
	cd rst && \
	sphinx-build -b html -d _build/doctrees . ../docs

