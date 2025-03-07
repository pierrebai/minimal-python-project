# Description

This Python repo contains a minimal Python project.

# Setup

You will need the following to use this code:

- Python 3.11+: see [Python official site for an installer](https://www.python.org/)
- pipenv: run `pip install pipenv` in a shell that has Python in its command path.
- Python dependencies: run `pipenv install` in the root of the project.


# Running Tests

## Running unit tests

You can run the tests with this command:

```Running tests
manager tests
```

You can also get code coverage analysis with this command instead:

```Running tests with code coverage
manager coverage tests
```

## Generating the code coverage report

The following command will generate the code coverage report in HTML
format, after you've run the tests with code coverage:

```Generate code coverage report in HTML
manager coverage report --html
```

# Update Package Requirements

If you modify the code and need an additional Python package, you can add it
using pipenv or the manager. To add or update a package, use these commands:

```cmd
manager dependency add *new-package-name*
```

```cmd
manager dependency update
```


# Running Tests in VSCode

To run the integration tests in Visual Studio Code, you need to setup VSCode to
find the necessary packages and use the correct Python virtual environment.
Here is brief overview of what you will have to do:

1. Setup VSCode to use the correct virtual environment.
2. Setup the Python PYTHONPATH environment.
3. Setup VSCode to find the tests.

## 1. Setup VSCode virtual environment

In VSCode, you must select the Python environment created by pipenv. It will
typically be found under a `virtualenv` folder and have a complicated name with
the words `manager in it. For example:

```
C:\Users\Your-User-Name\.virtualenvs\Your-Project-Name-SOME-RANDOM_LETTERS
```

To select the Python environment, type the `Control-Shift-P` keyboard shortcut
and enter `Python select` in the prompt to find the `Python: Select Interpreter`
command. Select it and then select the Python environment as described above.

## 2. Setup the PYTHONPATH environment

The unit test can only import your project Python modules if those modules are
in the Python import path. To allow this, you must create a `.env` file at the
root of the project that points to the location of the source code of your
modules. So create that `.env` file with the following contents:

```.env
PYTHONPATH=src
```

## 3. Setup VSCode unit tests

In VSCode, you must setup the test pane to use unittest. Clicking on the test
pane in the left-hand panel (it looks like a chemistry flask), and then trying
to run tests, VSCode should prompt you to select the test configuration. Select
the following:

* For testing package, select `unittest`
* For testing folder, select `tests`
* For tests pattern, select `test*.py`

