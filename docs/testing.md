# Testing

- How does testing work in this project
- How do we write tests
- Terminology
- How to setup for VSCode and PyCharm

<br>
<br>
<br>

# Table of contents

- [Introduction](#introduction)
  - [What is testing?](#what-is-testing)
  - [How does it work?](#how-does-it-work)
- [pytest](#pytest)
  - [Configuration / customize](#configuration--customize)
  - [Autodiscovery](#autodiscovery)
  - [Skipping](#skipping)
- [Terms](#terms)
  - [Fixtures](#fixtures)
  - [Mock](#mock)
- [How to write tests](#how-to-write-tests)
  - [Create folder/file](#create-folderfile)
- [Setup for IDE's](#setup-for-ides)
  - [VSCode](#vscode)
  - [PyCharm](#pycharm)

<hr>
<br>
<br>

## Introduction

<br>

### What is testing?

Testing is a practice where you write code to make sure the application behave as intended. A better explanation can be read [here](https://docs.pytest.org/en/6.2.x/fixture.html#what-fixtures-are).

<br>

### How does it work?

Run test functions and check if asserted result matches the expected rsult. Depending on what needs to be tested, instances must be created and cleanup up afterwards.

<br>
<br>

## pytest

The [pytest](https://docs.pytest.org/en/6.2.x/) framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

We have selected `pytest` as our primary tool for testing. It's an external library unlike `unittest` (adopted by python and django).

<details open>

<summary>Useful links</summary>

- [official] [pytest documentation](https://docs.pytest.org/en/6.2.x/)
- [official] [pytest configuration](https://docs.pytest.org/en/6.2.x/customize.html)
- [blog] [overview of pytest](https://djangostars.com/blog/django-pytest-testing/)
-

</details>

<br>

### Configuration / customize

Read more about custom configuration using file `pytest.ini` [here](https://docs.pytest.org/en/6.2.x/customize.html).

<br>

### Autodiscovery

Pytest [autodiscovers](https://docs.pytest.org/en/6.2.x/goodpractices.html#test-discovery) tests in the project if we follow a certain naming-convention.

- files with names like: `*_test.py` or `test_*`  
  From those files, collect test items:
  - `test` prefixed test functions or methods outside of class
  - `test` prefixed test functions or methods inside `Test` prefixed test classes (without an **init** method)

<br>

### Skipping

To skip tests, we can mark functions with `@pytest.mark.skip(reason='some custom reason')`. Read more [here](https://docs.pytest.org/en/latest/how-to/skipping.html).

<br>
<br>

## Terms

This section describes the different tools we utilise during testing.

<br>

### Fixtures

See [documentation](https://docs.pytest.org/en/6.2.x/fixture.html#fixture).

Fixtures are the arrange step in testing. Meaning they setup everything a test needs beforehand.

We can define a fixture by decorating with `@pytest.fixture`

Fixtures are often used as arguments in the test method declaration.

If all tests in a file depends on the same fixture. We can enable them [automatically](https://docs.pytest.org/en/6.2.x/fixture.html#autouse-fixtures-fixtures-you-don-t-have-to-request) by setting `@pytest.fixture(autouse=True)`

Printing during tests are captured by pytest and will not show in terminal. Instead all captured prints will be displayed at the end of pytest results.

To cleanup a fixture, we can use [`yield`](https://docs.pytest.org/en/6.2.x/fixture.html#yield-fixtures-recommended) instead of `return`. After the `yield` line, we can tear down what the fixture created. This is recommended practice.  
[StackOverflow: what is yield?](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)

#### Where do fixtures live

Which file/folder?
Above tests they are used in?

<br>

### Mock

<br>
<br>
<br>

## How to write tests

This section will describe how to write tests in this project. We define a set of conventions we want developers to use.

<br>

### Create folder/file

We typically write tests inside a `tests` folder in their respective scoped module. This results in rather small test modules spread across the project where they conseptually belong. E.g. `Feide/api/client/activation/tests/`.

<br>

<br>
<br>

## Setup for IDE's

<br>

### VSCode

<br>

### PyCharm
