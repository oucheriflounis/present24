PROJECT_NAME = oucherif-talata
PYTHON = python3
ZIP_FILE = $(PROJECT_NAME)


# define phony targets
.PHONY: run clean zip


# define default target
attaque:
	python3 attaque.py


# define target for executing encryption
chiffrement:
	python3 chifrement.py


# define target for executing decryption
dechiffrement:
	python3 dechifferement.py


# define target for cleaning up
clean:
	rm -rf __pycache__


# define target to create a .zip
zip:
	rm -rf $(ZIP_FILE)
	mkdir $(ZIP_FILE)
	cp Makefile $(ZIP_FILE)
	cp attaque.py $(ZIP_FILE)
	cp chifrement.py $(ZIP_FILE)
	cp dechifferement.py $(ZIP_FILE)
	cp genere_liste.py $(ZIP_FILE)
	cp cadencement.py $(ZIP_FILE)
	cp README.md $(ZIP_FILE)
	cp rapport.txt $(ZIP_FILE)
	rm -f $(ZIP_FILE).zip
	zip -r $(ZIP_FILE).zip $(ZIP_FILE)
	rm -rf $(ZIP_FILE)
