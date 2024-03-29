# Word Puzzle Python Solver

This is a Python implementation of the 9-letter word puzzle:

- [Nine Letter Word](http://nineletterword.tompaton.com/adevcrsoi/)
- [Your Word Life](http://www.yourwiselife.com.au/games/9-letter-word/)

![nineletterword.tompaton.com](nineletterword.png)

Here we are using a subset of the British dictionary from the
[wbritish](https://packages.debian.org/sid/text/wbritish) package.

## Quick Start

To show program options call the program with the `-h` option:

```bash
./wordpuzzle.py -h
```

Find all dictionary words of length 8 or more using the letters `cadevrsoi`:

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

## Tools Used

The tools [required](requirements.txt) to build and test this project are:

- [black](https://github.com/psf/black) - format source files
- [flake8](https://github.com/pycqa/flake8) - checks source files
- [hypothesis](https://hypothesis.readthedocs.io/) - [QuickCheck](https://en.wikipedia.org/wiki/QuickCheck) style testing framework
- [isort](https://pycqa.github.io/isort/) - sort imports
- [pylint](https://www.pylint.org/) - lint source files
- [pytest](https://docs.pytest.org/) - unit tests including [test coverage](https://pytest-cov.readthedocs.io/en/latest/)
- [venv](https://docs.python.org/library/venv.html) - manage this projects environment

## Dictionary

This project requires a dictionary of valid words.
By default the project uses a subset of the British dictionary from
[wbritish-huge](http://wordlist.sourceforge.net/). Since this is a large file,
and we need at most 9-letter words, we can create a smaller dictionary using:

```bash
egrep '^[[:lower:]]{1,9}$' /usr/share/dict/british-english-huge > dictionary
```

## Virtual Environment

To initialise the virtual environment, `.venv`:

```bash
pip3 install -U virtualenv
python3 -m virtualenv .venv
source .venv/bin/activate
pip3 install -Ur requirements.txt
```

To start the virtual environment:

```bash
source .venv/bin/activate
```

To end virtual environment session:

```bash
deactivate
```

## Dependent Packages

Install and list packages:

```bash
pip3 install -Ur requirements.txt
pip3 list
pip3 freeze
```

## Format

To format code formatter using [Google Python Code
Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md) using
[black](https://github.com/psf/black):

```bash
black *.py library/*.py tests/*.py
```

## Lint

Lint source files using both [flake8](https://github.com/pycqa/flake8) and
[Pylint](https://www.pylint.org/):

```bash
flake8 *.py library/*.py tests/*.py
pylint *.py library/*.py tests/*.py
```

## Test

Test using [PyTest](https://docs.pytest.org/):

```bash
pytest -v --cov-report term-missing --cov=library tests
```

## Run

Run application with:

```bash
python3 wordpuzzle.py -s 7 -l cadevrsoi
```

Or:

```bash
./wordpuzzle.py -s 7 -l cadevrsoi
```

## Documentation

Get [pydoc](https://docs.python.org/3/library/pydoc.html) using:

```bash
pydoc wordpuzzle
pydoc library.filters
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

## Partial functions

In an older commit,
[4c3e0acf](https://gitlab.com/frankhjung1/python-wordpuzzle/-/tree/4c3e0acff3dd603737fc0b6914d98824b1e11a4e),
[wordpuzzle](./wordpuzzle.py) used a partial function to validate the letters
argument. There is an easier, more direct way to do this.

```python
from functools import partial

def arg_test(arg_test_func, param):
    '''Test if valid argument.

    Args:
        arg_test_func (func): Function to test argument
        param : Argument to test

    Returns:
        param : the validated argument

    Raises:
        ArgumentTypeError : if argument invalid
    '''
    if not arg_test_func(param):
        raise argparse.ArgumentTypeError(f"{param} invalid value")

    return param

#: Validate letters argument
arg_letters = partial(arg_test, is_valid_letters)

# Used by argparse argument declaration:
PARSER.add_argument(
    '-l',
    '--letters',
    help='letters to create words from (mandatory is first letter)',
    type=arg_letters,
    required=True,
)
```

## Updating Packages

Use `pip list --outdated` to show updates to packages.

To update outdated packages, use:

```bash
pip3 list -o | cut -f1 -d' ' | tr " " "\n" | awk '{if(NR>=3)print}' | cut -d' ' -f1 | xargs -n1 pip3 install -U
```

## References

- [Hypothesis](https://hypothesis.works/)
- [Pytest](https://docs.pytest.org/)
- [Python 3 Tutorial](https://docs.python.org/3/tutorial/)
- [Python Code Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
- [Virtual Environment Tutorial](https://realpython.com/python-virtual-environments-a-primer/)

## Other Implementations

- [Clojure](https://gitlab.com/frankhjung1/clojure-wordpuzzle)
- [Haskell](https://gitlab.com/frankhjung1/haskell-wordpuzzle)
- [Java](https://gitlab.com/frankhjung1/java-wordpuzzle)
- [Kotlin](https://gitlab.com/frankhjung1/kotlin-wordpuzzle)
- [Go](https://gitlab.com/frankhjung1/go-wordpuzzle)
- [Python](https://gitlab.com/frankhjung1/python-wordpuzzle)

## LICENSE

[GNU GPLv3 LICENSE](./LICENSE)
