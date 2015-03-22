# Python Packages

## How an installed package is found

* `sys.path`
  * List of directories searched for packages
  * First item : **Current directory** `('')`
  * Last item : `site-packages`
* **site-packages**
  * Third-party pacjages are installed here
  * Location depends on OS, Python version, installation procedure, virtual environments e.t.c.
  * It will be somewhere _inside_ your Python installation or your virtual environment
  * May not even be called `site-packages` (i.e. on Debian : `dist-packages`)

## Packaging: Current State of Affairs

* How to create, distribute and install packages?
* Lots of info on the web is outdated or contradictory
* **Multiple tools**:
  * `distutils`
  * `setuptools`
  * `easy_install`
  * `ez_setup`
  * `pip`
* **Multiple formats**:
  * `egg`
  * `wheel`
  * `source dist`

## Preferred Tools

**Python Packaging Authority** (**PyPA**) recommends

### Creating and distributing packages

* Use `setuptools`
* `distutils`    : **discontinued**, _merged into `setuptools`_
* `easy_install` : is included in `setuptools`


### Installing packages

* [Use `pip`](Pip.md)
* With `virtualenv`

### Where to find packages

* Cheese Shop : [http://pypi.python.org/]


## Resources

* **Python Packaging User Guide**
  * https://packaging.python.org/en/latest/
* **Pip**
  * https://pip.pypa.io
* **Python Package Index (PyPI)**
  * https://pypi.python.org/pypi




