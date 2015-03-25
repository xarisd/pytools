# Code Style

## PEP8: Style Guide for Python Code

https://www.python.org/dev/peps/pep-0008/

* PEP: Python Enhancement Proposal.
  * Provide information to the Python community, or
  * Describe a new feature for Python

* PEP8: Style Guide for Python Code
  * Code Lay-out
  * Whitespace
  * Comments
  * Naming Conventions

## Layout

* It's about readability
* Indentation: 4 spaces per level
* Line length max. 79 characters
* Blank lines:
  * 2 lines between top-level functions and classes
  * 1 line between methods inside a class
* Imports
* Use of spaces in expressions
* If you don't know the rules, your tools will tell you (mostly)

## Documentation and Naming

* Docstrings for all public modules, functions, classes and methods

* Naming:
  * Modules: short, lowercase names
  * Classes: CapitalizedNaming
  * Functions and methods: lowercase_with_underscores
  * Constants: ALL_CAPS
  * Non-public names start with underscore

* Programming Recommendations
  * ...and more

## Pylint

http://www.pylint.org/

* Static code checker
* PEP8
* Error detection (code smells)
* Code duplication
* Very configurable
* Integration with many IDE's

### Running `pylint`

* Run against a package or module
  * With full reporting

  ```
  pylint <package_or_module>
  ```

  * Only messages (use `-r n`)

  ```
  pylint -r n <package_or_module>
  ```

* Get help

  ```
  pylint --help
  ```

* Run with GUI

  ```
  pylint-gui
  ```

  **IMPORTANT**: You have to quit and rerun it in order to take into account code changes

* Disable messages in you code

  ```
  # pylint: disable=message-name
  ```

  You can do this on module or function/method level

* Generate a configuration file for pylint : `pylintrc`

  ```
  pylint --generate-rcfile > pylint
  ```

  * You can configure reporting, which messages to ignore...and more
  * Pylint searches `pylintrc` in
    * Current working directory
    * Home directory (for global settings for all your projects)
    * or **per package**

## Resources

* **PEP8**
  * https://www.python.org/dev/peps/pep-0008/
* **All PEPs**
  * https://www.python.org/dev/peps/
* **Pylint & documentation**
  * http://www.pylint.org/
