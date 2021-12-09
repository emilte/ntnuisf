# VSCode à la @emilte

## Table of contents

- [Table of contents](#table-of-contents)
- [What is this?](#what-is-this)
- [Files explained](#files-explained)
- [Local setup](#local-setup)
- [Extensions explained](#extensions-explained)
  - [Default](#default)
  - [Recommended](#recommended)

<hr>
<br>
<br>

## What is this?

The current README is designed for development directly inside a running container. This causes issues when the codebase is introduced with lines of code that the running container is unable to compile. You will be stuck in a loop of wanting to fix some code to get the project to compile, whilst being dependent on a working container to develop.

Instead, I propose a local development environment independent from Docker.

> Attaching directly to the container is still useful when you want to utilise the debug server.

<br><br>

## Files explained

Which folders and files are relevant to VScode, what do they mean, and which ones are recognised by VSCode.

- `.vscode/`  
  Folder recognized by VSCode. Contains configurations for workspace.

- `extensions.json`  
  Contains common extensions needed for this project.
  This file is recognised by VSCode, so hopefully it prompts you to install these automatically.

- `extensions.json.recommended`  
  Contains recommended optional extensions for this project.

- `launch.json`  
  Contains configurations for debugging.

- `settings.json`  
  Contains workspace settings for VSCode and extensions. Note that workspace settings takes precedens over user-settings.
  This file is recognised by VSCode and is to be configured to your liking. That's why this file is intentionally excluded from git.

- `settings.json.default`  
  Contains common project-specific settings shared between developers. These settings are project specific and intended to be used ba all team-members. Copy these settings into `settings.json`.

- `settings.json.suggestions`  
  Contains suggestions for useful settings, but not neccessary ones. Copy into `settings.json` if desired.

<br><br>

## Local setup

> Make sure you have downloaded a version of VSCode compatible with your device.  
> MAC: universal or M1.  
> Windows: ...  
> Linux: ...

- Install dependencies locally in a virtual environment. Use e.g. virtualenv or pipenv.
- Select this environment as interpreter for workspace.
- Install extensions from `extensions.json`.
- Install desired extensions from `extensions.json.recommended`.
- Create file `/.vscode/settings.json`.
- Copy settings from `settings.json.default` into `settings.json`.
- Copy desired settings from `settings.json.suggestions` into `settings.json`.

<br><br>

## Extensions explained

This section motivates the multiple extensions relevant for this project.

<br>

### Default

List of extensions you should have in this project. Found in [`extensions.json`](/.vscode/extensions.json).

- `batisteo.vscode-django`
  [link](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)  
  Supports Django syntax in templates (.html) and useful snippets.

- `editorconfig.editorconfig`
  [link](https://marketplace.visualstudio.com/items?itemName=editorconfig.editorconfig)  
  [EditorConfig](https://editorconfig.org/) configures consistent coding styles across various editors and filetypes.

- `ms-python.python` [link](https://marketplace.visualstudio.com/items?itemName=ms-python.python)  
  This project uses Django as framework, which is python based. This extension includes neccessary python language support. It also includes `ms-python.vscode-pylance` [(link)](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) which is the default language server for VSCode. A language server is able to lint in realtime unlike pylint. It also enables helper/suggestion pallette when developing. `visualstudioexptteam.vscodeintellicode` [(link)](https://marketplace.visualstudio.com/items?itemName=visualstudioexptteam.vscodeintellicode).

- `dbaeumer.vscode-eslint` [link](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)  
  Code quality in frontend.

- `fnando.linter` [link](https://marketplace.visualstudio.com/items?itemName=fnando.linter)  
  idk

- `orta.vscode-jest` [link](https://marketplace.visualstudio.com/items?itemName=orta.vscode-jest)  
  idk

- `esbenp.prettier-vscode` [link](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)  
  Prettier is a formatting tool for frontend configured in this project (see [`prettierrc.js`](/.prettierrc.js)). This extension

<br>

### Recommended

Documented optional (nice-to-have) extensions for development. They can be found in [`extensions.json.recommended`](/.vscode/extensions.json.recommended).

- `mikestead.dotenv` [link](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv)  
  Environment-files (.env) have no highlighting by default. This extension fixes that.

- `mrorz.language-gettext` [link](https://marketplace.visualstudio.com/items?itemName=mrorz.language-gettext)  
  Django supports localization which generates .po files with translations. This extension provides syntax highlight for these files.

- `eamodio.gitlens` [link](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)  
  Powerful extension to integrate git version control into VSCode. Highly customizable.

- `yzhang.markdown-all-in-one` [link](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)  
  Extension which enables preview while writing markdown (.md). It also has a lot of useful commands, snippets and shortcuts.
  For example enables this extensions auto-generated table of contents used in these docs.

- `ms-vscode-remote.remote-containers` [link](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)  
  Enables VSCode to attach to a running container. Useful for debugging and developing without having to install any dependencies locally.

- `ms-azuretools.vscode-docker` [link](https://marketplace.visualstudio.com/items?itemName=xxx)  
  This project is setup with container-technology with Docker. This extensions integrates Docker functionality.
