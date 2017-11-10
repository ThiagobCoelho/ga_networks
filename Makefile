target=pytest

all:
	python -B $(target).py -t 1

clean:
	rm -f *.pyc
