# Files explained

<br>
<br>
<br>

# Table of contents:

- [.editorconfig](#editorconfig)
- [.gitignore](#gitignore)
- [.prettierignore](#prettierignore)
- [.prettierrc.js](#prettierrcjs)
- [.pylintrc](#pylintrc)
- [.python-version](#python-version)
- [.style-yapf](#style-yapf)
- [.yapfignore](#yapfignore)
- [example.env](#exampleenv)
- [manage.py](#managepy)
- [Pipfile / Pipfile.lock](#pipfile--pipfilelock)
- [Procfile](#procfile)
- [`pytest.ini`](#pytestini)
- [runtime.txt](#runtimetxt)
<hr>

<br>
<br>
<br>

## .editorconfig

File recognised by `editorconfig`.
Ensures some style on filetypes.
Need to install extension in IDE.

<details open>
<summary>Useful links</summary>

- [official] [Editorconfig homepage](https://editorconfig.org/)
- [/docs/dependencies/linters.md](/docs/dependencies/linters.md)

</details>

<br>
<br>

## .gitignore

File recognised by `git`.
Used to prevent git from applying version control on files matching certain patterns.

<details open>
<summary>Useful links</summary>

- [official] [gitignore documentation](https://git-scm.com/docs/gitignore)

</details>

<br>
<br>

## .prettierignore

File recognised by `prettier`.
Used to prevent prettier from applying formatting on files matching certain patterns.

<details open>
<summary>Useful links</summary>

- [official] [prettierignore documentation](https://prettier.io/docs/en/ignore.html#ignoring-files-prettierignore)
- [official] [prettier documentation](https://prettier.io/docs/en/index.html)

</details>

<br>
<br>

## .prettierrc.js

File recognised by `prettier`.
Used to configure formatting rules.

<details open>
<summary>Useful links</summary>

- [official] [prettier configuration](https://prettier.io/docs/en/configuration.html)
- [official] [prettier documentation](https://prettier.io/docs/en/index.html)

</details>

<br>
<br>

## .pylintrc

File recognised by `pylint`.
Used to configure linting rules.

<details open>
<summary>Useful links</summary>

- [official] [pylint documentation](https://pylint.pycqa.org/en/latest/)
- [github] [pylintrc example](https://github.com/PyCQA/pylint/blob/main/pylintrc)

</details>

<br>
<br>

## .python-version

File recognised by `pyenv`.
Workspace setting for which python version `pyenv` should run. Useful in conjunction with `pipenv` because correct python version is a prerequisite for running `pipenv`.

<details open>
<summary>Useful links</summary>

- [official] [pylint documentation](https://pylint.pycqa.org/en/latest/)
- [github] [pylintrc example](https://github.com/PyCQA/pylint/blob/main/pylintrc)

</details>

## .style-yapf

Config file recognised by `yapf`.
Style conforms to PEP8 guidelines, but with minor tweaks.
We define `based_on_style = facebook` to use some other rules.
Read more [here]()

See yapf docs here.
See VSCode setup for more yapf setup.

## .yapfignore

File recognised by `yapf`.
Similar to .gitignore where a glob pattern can lighten the workload on yapf by excluding certain filres or directories.

## example.env

Example file of environment variables that should be set in the project. Copy this file and rename to `.env` which is automatically recognised by the project.

## manage.py

Root of Django project. Run this file to see possible commands.

## Pipfile / Pipfile.lock

Python dependencies for the project recognised by `pipenv`. Similar to `requirements.txt`.

## Procfile

File recognised by `heroku`.

Read more here.

## `pytest.ini`

Config file recognised by `pytest`.

Read more pytest docs here.

## runtime.txt

File recognised by `heroku`.
Defines python version to use.

Read more here.
