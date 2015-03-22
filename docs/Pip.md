# Pip

Installation instructions and Documentation at [https://pip.pypa.io/]

## Installing Pip

* Starting with Python 3.4, `pip` comes pre-installed
  * No need to install anything
* Python 2 or Python 3 < 3.4
  * Follow instructions at [http://www.pip-installer.org]
  * Basically : Download and run `get_pip`.py
  * Linux/Mac users may need to use `sudo`
* Mac users using Homebrew
  * Homebrew installs pip with Python automatically
* Window users
  * pip will be in the `Scripts` directory of the Python installation
  * Add `C:\PythonXX\Scripts\` to your PATH

## Using Pip

### Installing packages with Pip

```
pip install packagename
```

```
pip install packagename==1.0
```

```
pip install 'packagename>=2.1'
```
**IMPORTANT**: Use quotes to prevent redirection with `<` and `>`


### Uninstalling packages with Pip

```
pip uninstall packagename
```

### Inspecting packages with Pip

* List all installed packages

  ```
  pip list
  ```

* Get info on a specific package

  ```
  pip show packagename
  ```

* Search for a package

  ```
  pip search query
  ```

## Requirements Files

You can specify specific packages that you need in a `requirements.txt`

* You can use Pip to create the `requirements.txt`

  ```
  pip freeze > requirements.txt
  ```

  This command will:
  * Save your project's dependencies in `requirements.txt`
  * Including **correct versions**

* You can install your project's dependencies using Pip

  ```
  pip install -r requirements.txt
  ```

  This will:
  * Install all packages listed in `requirements.txt`

