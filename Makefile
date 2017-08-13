.virtualenv:
	virtualenv -p python3 .virtualenv

run:
	.virtualenv/bin/python src/ticket.py

test:
	.virtualenv/bin/pytest .

install:
	virtualenv -p python3 install
	install/bin/pip install .
	echo "alias ticket=$(shell pwd)/install/bin/ticket" >> ~/.bashrc
	$(source ~/.bashrc)
	@echo "\n\nAdded an alias to this installation to ~/.bashrc"
	@echo "If this doesn't work, please try adding it to your own shell config file"
