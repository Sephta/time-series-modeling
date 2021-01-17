# time-series-modeling

This repo holds all of the project files for class project 1 of CIS 422 (Software Methodology), at the University of Oregon

## Development Setup

Create the virtual env

```
pip install virtualenv
virtualenv env
```

If using VSCode, you may get prompted to use the virtual environment for the current workspace. Say yes, and add the following to the generated .vscode/settings.json to enable linting/formatting on save:

```
{
  ...
  "python.linting.pep8Enabled": true,
  "python.linting.pylintEnabled": true,
  "editor.formatOnSave": true,
}
```

Start the virtual env (for Windows):

```
. env/scripts/activate
```

or for Linux/MacOS:

```
. env/bin/activate (MacOS/Linux)
```

After starting the virtual environment, install the linter and pep8:

```
pip install pep8
pip install pylint
pip install autopep8
```
