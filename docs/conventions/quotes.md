# Conventions

This documents contains conventions when developing `feide-kp`.
This list is scoped by subject, eg. `models`, `quotes`, `imports`.
Each section can be further divided into `frontend` or `backend`


## How to add new convention entry
1. Provide a subject as sub-title (two hashtags `##`)
2. If neccessary; scope into `frontend` or `backend`
3. Write:
    - Convention
    - [optional] Usage
    - [optional] Exceptions and their conventions
    - [optional] Why?


## Quotes:

### Backend (Python)

#### Convention
Use single-quote `'` when working with strings. Eg. when defining variables/constants or writing json/config.
I.e. when working with string internally in the project.

Exceptions: 
- The string utilises both quotes to format something.
    - Example: 
    ```python
    return "Click 'enter' to access"
    ```
- The string is an obvious message supposed to be presented to eg. end-user or log. Use double-quote `"`.
    - Example: 
    ```python
    f"{user.name} tried to access admin-tools"
    ```
- Doc-strings for classes and methods. Use double-quote, eg. `""" Doc-string """`


#### Why
Refactoring and cross-project searching is way easier when a standard is universally implemented.
