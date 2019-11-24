# python-wordpuzzle

This is an Python implementation of the 9 letter word puzzle.

## Quick Start

The following applies to Linux where the base installation contains both Python
2 & 3.

### Virtual Environment

To initialise the virtual environment, `venv`:

```bash
pip3 install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
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
pip3 install -r requirements.txt
pip3 list
pip3 freeze
```

### Format Code

To format code to the [Google Python Code
Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md) run the
[YAPF](https://github.com/google/yapf) utility:

```bash
yapf --style google --parallel -i wordpuzzle.py tests/testwordpuzzle.py tests/__init__.py utils/__init__.py utils/filters.py
```

Where:

  - using Google style 
  - in place changes

### Lint Code

[Lint](https://www.pylint.org/) source:

```bash
pylint wordpuzzle.py tests/testwordpuzzle.py tests/__init__.py utils/__init__.py utils/filters.py
```

Run application with:

```bash
python3 wordpuzzle.py -m c -l adevcrsoi
```

### Test application.

Testing using PyTest:

```bash
pytest -v tests/test*.py
```

## Tools Used

These tools require Python 3.

* [hypothesis](https://hypothesis.readthedocs.io/) - quickcheck style testing framework
* [pylint](https://www.pylint.org/) - checks source files
* [pytest](https://docs.pytest.org/) - unit tests
* [venv](https://docs.python.org/library/venv.html) - manage this projects environment
* [yapf](https://github.com/google/yapf) - format source files

## References

* [Hypothesis](https://hypothesis.works/)
* [PyTest](https://docs.pytest.org/)
* [Python 3 Tutorial](https://docs.python.org/3/tutorial/)
* [Python Code Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
* [Virtual Environment Tutorial](https://realpython.com/python-virtual-environments-a-primer/)

## LICENSE

[GNU GPLv3 LICENSE](./LICENSE)
