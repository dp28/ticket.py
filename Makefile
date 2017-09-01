.virtualenv:
	virtualenv -p python3 .virtualenv

run:
	.virtualenv/bin/python src/ticket.py

test:
	.virtualenv/bin/pytest .

test_and_notify:
	@.virtualenv/bin/pytest . --color yes | \
		tee /dev/tty | \
		grep '=========' | \
		tail -n 1 | \
		sed s/=//g  | \
		sed -r "s/\x1B\[([0-9];)?([0-9]{1,2}(;[0-9]{1,2})?)?[mGK]//g" | \
		xargs -I {} notify-send {}

install:
	virtualenv -p python3 install
	install/bin/pip install .
	echo "alias ticket=$(shell pwd)/install/bin/ticket" >> ~/.bashrc
	$(source ~/.bashrc)
	@echo "\n\nAdded an alias to this installation to ~/.bashrc"
	@echo "If this doesn't work, please try adding it to your own shell config file"

update:
	rm -rf install
	make install

test_watch:
	-make test_and_notify
	@echo "Watching current directory for changes ..."
	@while inotifywait . --recursive -e modify >/dev/null 2>&1 ; \
	do \
		make test_and_notify ; \
	done
