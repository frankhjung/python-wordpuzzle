# Word Puzzle Python Solver

This is a Python implementation of the 9-letter word puzzle:

- [Nine Letter Word][nine-letter-word]
- [Your Word Life][your-word-life]

![nineletterword.tompaton.com](nineletterword.png)

Here we are using a subset of the British dictionary from the
[wbritish][wbritish] package.

## Quick Start

To show program options call the program with the `-h` option:

```bash
uv run python wordpuzzle.py -h
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

The tools required to build and test this project are managed via
[uv][uv-docs] and defined in [pyproject.toml](./pyproject.toml):

- [hypothesis][hypothesis-docs] -
  [QuickCheck][quickcheck-wiki] style testing framework
- [pytest][pytest-docs] - unit tests including
  [test coverage][pytest-cov-docs]
- [ruff][ruff-repo] - format and lint source files
- [uv][uv-docs] - manage this project's environment

## Dictionary

This project requires a dictionary of valid words. By default the project uses a
subset of the British dictionary from [wbritish-huge][wbritish-huge-site]. Since
this is a large file, and we need at most 9-letter words, we can create a
smaller dictionary using:

```bash
egrep '^[[:lower:]]{1,9}$' /usr/share/dict/british-english-huge > dictionary
```

## Environment Setup

To initialise the development environment:

```bash
uv sync
```

This creates a virtual environment and installs all dependencies from
[pyproject.toml](./pyproject.toml).

## Dependent Packages

List installed packages:

```bash
uv pip list
```

## Format

To format code using [ruff][ruff-repo]:

```bash
uv run ruff format *.py library/*.py tests/*.py
```

## Lint

Lint source files using [ruff][ruff-repo]:

```bash
uv run ruff check *.py library/*.py tests/*.py
```

## Test

Test using [PyTest][pytest-docs]:

```bash
uv run pytest -v --cov-report term-missing --cov=library tests
```

## Run

Run application with:

```bash
uv run python wordpuzzle.py -s 7 -l cadevrsoi
```

## Documentation

Get [pydoc][pydoc-docs] using:

```bash
uv run python -m pydoc wordpuzzle
uv run python -m pydoc library.domain
uv run python -m pydoc library.filters
```

## Architecture

This project follows a **pure core, effectful shell** architecture:

- **library/domain.py**: Contains the `Puzzle` domain object and the `solve`
  function. This is the pure core where all solving logic resides.
- **wordpuzzle.py**: The effectful shell that handles command-line arguments,
  file I/O (streaming the dictionary), and printing results.
- **library/filters.py**: A backward-compatible wrapper around the domain
  logic.

## Build and run from Docker

To run using the Docker image, ensure a dictionary is present (a default
dictionary is already included in the workspace). If you need to download a
custom dictionary, you can run:

```bash
curl -L \
  https://raw.githubusercontent.com/dwyl/english-words/master/words.txt \
  -o dictionary
```

Then run the application using GNU Make:

```bash
docker run --rm -t -v "$PWD":/opt/workspace -u "$(id -u):$(id -g)" \
  frankhjung/python:latest make run
```

This will call the `run` goal, which executes the application using the default
dictionary.

## Partial functions

In an older commit, [4c3e0acf][commit-4c3e0acf], [wordpuzzle.py][wordpuzzle-py]
used a partial function to validate the letters argument. There is an easier,
more direct way to do this.

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

## Upgrading Outdated Packages

List outdated packages using:

```bash
uv pip list --outdated
```

To upgrade all packages to their latest versions:

```bash
uv sync --upgrade
```

Alternatively, edit [pyproject.toml](./pyproject.toml) and run `uv sync`.

## References

- [Glossary][glossary-md]
- [Hypothesis][hypothesis-works]
- [Pytest][pytest-docs]
- [Python 3 Tutorial][python-3-tutorial]
- [Python Code Style][python-code-style]
- [uv][uv-docs]

## Other Implementations

- [Clojure][clojure-puzzle]
- [Haskell][haskell-puzzle]
- [Java][java-puzzle]
- [Kotlin][kotlin-puzzle]
- [Go][go-puzzle]
- [Python][python-puzzle]

## LICENSE

[GNU GPLv3 LICENSE](./LICENSE)

[nine-letter-word]: http://nineletterword.tompaton.com/adevcrsoi/
[your-word-life]: http://www.yourwiselife.com.au/games/9-letter-word/
[wbritish]: https://packages.debian.org/sid/text/wbritish
[uv-docs]: https://docs.astral.sh/uv/
[hypothesis-docs]: https://hypothesis.readthedocs.io/
[quickcheck-wiki]: https://en.wikipedia.org/wiki/QuickCheck
[pytest-docs]: https://docs.pytest.org/
[pytest-cov-docs]: https://pytest-cov.readthedocs.io/en/latest/
[ruff-repo]: https://github.com/astral-sh/ruff
[wbritish-huge-site]: http://wordlist.sourceforge.net/
[pydoc-docs]: https://docs.python.org/3/library/pydoc.html
[commit-4c3e0acf]:
  https://gitlab.com/frankhjung1/python-wordpuzzle/-/tree/4c3e0acff3dd603737fc0b6914d98824b1e11a4e
[wordpuzzle-py]: ./wordpuzzle.py
[glossary-md]: ./GLOSSARY.md
[hypothesis-works]: https://hypothesis.works/
[python-3-tutorial]: https://docs.python.org/3/tutorial/
[python-code-style]:
  https://github.com/google/styleguide/blob/gh-pages/pyguide.md
[clojure-puzzle]: https://gitlab.com/frankhjung1/clojure-wordpuzzle
[haskell-puzzle]: https://gitlab.com/frankhjung1/haskell-wordpuzzle
[java-puzzle]: https://gitlab.com/frankhjung1/java-wordpuzzle
[kotlin-puzzle]: https://gitlab.com/frankhjung1/kotlin-wordpuzzle
[go-puzzle]: https://gitlab.com/frankhjung1/go-wordpuzzle
[python-puzzle]: https://gitlab.com/frankhjung1/python-wordpuzzle
