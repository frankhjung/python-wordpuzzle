# Word Puzzle Python Solver

This is a Python implementation of the 9-letter word puzzle:

- [Nine Letter Word][nine-letter-word]
- [Your Word Life][your-word-life]

![nineletterword.tompaton.com](nineletterword.png)

Here we are using a subset of the British dictionary from the
[wbritish][wbritish] package.

## Quick Start

To show program options, call the program with the `-h` option:

```bash
uv run python wordpuzzle.py -h
```

Find all dictionary words of length 8 or more using the letters
`cadevrsoi`:

```bash
uv run python wordpuzzle.py -s 8 -l cadevrsoi
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

- [bandit][bandit-docs] - static analysis security testing (SAST)
- [hypothesis][hypothesis-docs] -
  [QuickCheck][quickcheck-wiki] style property-based testing
- [pdoc][pdoc-docs] - API documentation generator
- [pytest][pytest-docs] - unit tests including
  [test coverage][pytest-cov-docs]
- [ruff][ruff-repo] - format and lint source files
- [uv][uv-docs] - manage this project's environment

## Dictionary

This project requires a dictionary of valid words. By default the
project uses a subset of the British dictionary from
[wbritish-huge][wbritish-huge-site]. Since this is a large file, and
we need at most 9-letter words, we can create a smaller dictionary
using:

```bash
grep -E '^[[:lower:]]{1,9}$' /usr/share/dict/british-english-huge \
  > dictionary
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
uv run ruff format
```

## Lint

Lint source files using [ruff][ruff-repo]:

```bash
uv run ruff check
```

## Security

Run a security scan using [bandit][bandit-docs]:

```bash
uv run bandit --recursive library
```

## Test

Test using [pytest][pytest-docs]:

```bash
uv run pytest -v --cov-report term-missing --cov=library tests
```

## Run

Run application with:

```bash
uv run python wordpuzzle.py -s 7 -l cadevrsoi
```

## Documentation

Generate HTML API documentation using [pdoc][pdoc-docs]:

```bash
uv run pdoc library
```

Or view inline module documentation using
[pydoc][pydoc-docs]:

```bash
uv run python -m pydoc wordpuzzle
uv run python -m pydoc library.domain
uv run python -m pydoc library.filters
```

## Architecture

This project follows a **pure core, effectful shell** architecture:

- **library/domain.py**: Contains the `Puzzle` domain object and the
  `solve` function. This is the pure core where all solving logic
  resides.
- **wordpuzzle.py**: The effectful shell that handles command-line
  arguments, file I/O (streaming the dictionary via `pathlib.Path`),
  and printing results.
- **library/filters.py**: A backward-compatible wrapper around the
  domain logic.

## Build and Run From Docker

To run using the Docker image, ensure a dictionary is present (a
default dictionary is already included in the workspace). If you need
to download a custom dictionary, you can run:

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

This will call the `run` goal, which executes the application using
the default dictionary.

## Upgrading Outdated Packages

List outdated packages using:

```bash
uv pip list --outdated
```

To upgrade all packages to their latest versions:

```bash
uv sync --upgrade
```

Alternatively, edit [pyproject.toml](./pyproject.toml) and run
`uv sync`.

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

## Licence

[GNU GPLv3 LICENSE](./LICENSE)

[nine-letter-word]: http://nineletterword.tompaton.com/adevcrsoi/
[your-word-life]: http://www.yourwiselife.com.au/games/9-letter-word/
[wbritish]: https://packages.debian.org/sid/text/wbritish
[uv-docs]: https://docs.astral.sh/uv/
[bandit-docs]: https://bandit.readthedocs.io/
[hypothesis-docs]: https://hypothesis.readthedocs.io/
[quickcheck-wiki]: https://en.wikipedia.org/wiki/QuickCheck
[pdoc-docs]: https://pdoc.dev/
[pytest-docs]: https://docs.pytest.org/
[pytest-cov-docs]: https://pytest-cov.readthedocs.io/en/latest/
[ruff-repo]: https://github.com/astral-sh/ruff
[wbritish-huge-site]: http://wordlist.sourceforge.net/
[pydoc-docs]: https://docs.python.org/3/library/pydoc.html
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
