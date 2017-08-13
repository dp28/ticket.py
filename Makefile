.virtualenv:
	virtualenv -p python3 .virtualenv

run:
	.virtualenv/bin/python src/ticket.py

test:
	.virtualenv/bin/pytest .
