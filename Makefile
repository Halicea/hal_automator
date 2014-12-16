run:
	(cd src; python hal_automator.py)

debug:
	(cd src; pdb hal_automator.py)	

clean:
	rm -rf $(BUILDDIR)/*

install:
	sudo python setup.py install

install_console:
	sudo python setup_console.py install