# time-series-modeling

This repo holds all of the project files for class project 1 of CIS 422 (Software Methodology), at the University of Oregon

## Development Setup

### Auto-format PEP8 and linting

Create the virtual env

```
pip install virtualenv
virtualenv env
```

If using VSCode, create a .vscode/settings.json if not automatically generated. Add the following to the .vscode/settings.json to enable linting/formatting on save:

```
{
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

After starting the virtual environment, install the linter and pep8 (VSCode will sometimes prompt you to do this):

```
pip install pep8
pip install pylint
pip install autopep8
```

To confirm setup was successful, check to see if your files are auto-formatted to pep8 upon saving. If so, the setup worked properly.
