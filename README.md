# python-blueprint
A simple blueprint for python projects with pre configured YAML config and logging support.

## Setup

1. Clone the repo
```zsh
git clone git@github.com:ezrarieben/python-blueprint.git
```

2. Set your project directory as a env variable
```zsh
export PY_PROJECT_DIR="/ABSOLUTE/PATH/TO/YOUR/PROJECT"
```

3. Copy the blueprint files into your project directory
```zsh
cp python-blueprint/* ${PY_PROJECT_DIR}
```

4. Initialize a new python virtual environment in your project directory
```zsh
python3 -m venv ${PY_PROJECT_DIR}/.venv
```

5. Install requirements via pip
> [!NOTE]
> You will want to keep your `requirements.txt` up to date during development so you can re-create the environment at any time.
> See: [requirements.txt](#requirementstxt)
```zsh
${PY_PROJECT_DIR}/.venv/bin/pip install -r ${PY_PROJECT_DIR}/requirements.txt
```

## requirements.txt
During development you may import different modules that need to be installed via pip. To keep track of the installed modules the `requirements.txt` file is used.

You can update the requirements.txt file after installing new modules using `pip freeze`.

Run the `pip freeze` command (see below) in your projects root folder (or wherever you have the `requirements.txt` file placed) using the pip binary in your virtual environment.
```zsh
${PY_PROJECT_DIR}/.venv/bin/pip freeze > requirements.txt
```
