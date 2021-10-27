# python-wordpuzzle

This is an Python implementation of the 9 letter word puzzle.

## Quick Start

The following applies to Linux where the base installation contains both Python
2 & 3.

To get program help call:

```bash
./wordpuzzle.py -h
```

Example call using parameters:

```bash
$ ./wordpuzzle.py -s 8 -l cadevrsoi
codrives
covaried
covaries
discover
divorces
idocrase
varicose
varicosed
```

## Dictionary

To build a English dictionary of valid words, use words from
[wbritish-huge](http://wordlist.sourceforge.net/):

```bash
egrep '^[[:lower:]]+$' /usr/share/dict/british-english-huge > dictionary
```

### Virtual Environment

To initialise the virtual environment, `venv`:

```bash
pip3 install -U virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip3 install -U -r requirements.txt
```

To start the virtual environment:

```bash
source venv/bin/activate
```

To end virtual environment session:

```bash
deactivate
```

### Dependent Packages

Install and list packages:

```bash
pip3 install -U -r requirements.txt
pip3 list
pip3 freeze
```

### Format Code

Use [black](https://github.com/psf/black) to format code:

```bash
black wordpuzzle.py **/*.py
```

An alternative code formatter using [Google Python Code
Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md) is the
[YAPF](https://github.com/google/yapf) utility:

```bash
yapf --style google -rpi wordpuzzle.py test lib
```

Where:

- using Google style
- in place changes

### Lint Code

[Lint](https://www.pylint.org/) source:

```bash
pylint wordpuzzle.py **/*.py
```

### Test application

Test using [PyTest](https://docs.pytest.org/):

```bash
pytest -v tests
```

### Run

Run application with:

```bash
python3 ./wordpuzzle.py -s 8 -l cadevrsoi
```

## Build and run from Docker

To run using my Docker image first install the default dictionary:

```bash
curl https://raw.githubusercontent.com/dwyl/english-words/master/words.txt -o dictionary
```

Then call the application using GNU make:

```bash
docker run --rm -t -v $PWD:/opt/workspace -u $(id -u):$(id -g) frankhjung/python:latest make exec
```

This will call the `exec` goal, which executes the application using the default
dictionary.

## Tools Used

These tools require Python 3.

- [hypothesis](https://hypothesis.readthedocs.io/) - [QuickCheck](https://en.wikipedia.org/wiki/QuickCheck) style testing framework
- [pylint](https://www.pylint.org/) - checks source files
- [pytest](https://docs.pytest.org/) - unit tests
- [venv](https://docs.python.org/library/venv.html) - manage this projects environment
- [yapf](https://github.com/google/yapf) - format source files

## LICENSE

[GNU GPLv3 LICENSE](./LICENSE)

## References

- [Hypothesis](https://hypothesis.works/)
- [PyTest](https://docs.pytest.org/)
- [Python 3 Tutorial](https://docs.python.org/3/tutorial/)
- [Python Code Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
- [Virtual Environment Tutorial](https://realpython.com/python-virtual-environments-a-primer/)

## Other Implementations

- [Haskell](https://gitlab.com/frankhjung1/haskell-wordpuzzle)
- [Java](https://gitlab.com/frankhjung1/java-wordpuzzle)
- [Kotlin](https://gitlab.com/frankhjung1/kotlin-wordpuzzle)
- [Go](https://gitlab.com/frankhjung1/go-wordpuzzle)
- [Python](https://gitlab.com/frankhjung1/python-wordpuzzle)
