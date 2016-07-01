project_name = phantomas
coverage_options = --include='$(project_name)/*' --omit='$(project_name)/test/*,*__init__.py'

install:
	npm install --global phantomas

test_requirements:
	pip install -U -e .\[tests\]

test:
	py.test -x

coverage:
	rm -f .coverage*
	rm -rf htmlcov/*
	coverage run -p -m py.test -x
	coverage combine
	coverage html -d htmlcov $(coverage_options)
	coverage xml -i
	coverage report $(coverage_options)

lint:
	pep8 $(project_name)/; pylint $(project_name)/

publish:
	python setup.py sdist upload -r pypi
	./tag.sh

setup: install test_requirements
