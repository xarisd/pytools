Packaging and distribution
==========================

Preparing your project for packaging
------------------------------------

* Add a file `setup.py` to your projects top folder
  * It is a Python script
  * Call `setup()` function with at least:
    * `name` and
    * `version`
  * Use `setuptools` (not _distutils_)
  * Dependencies: `install_requires`

* `MANIFEST.in`
  * If you need to explicitely exclude or include other files


* `python setup.py sdist`
  * Package as a **source distribution**

* `python setup.py bdist_wheel`
  * You need to install package `wheel`
  * Supports C extensions and platform-specific ditribution
  * Faster installation
  * Towards to be the de-facto distribution format

* `python setup.py register`
  * Registers your project to **PyPI**

* `python setup.py sdist upload`
  * Creates the source distribution (with `sdist`)
  * Uploads the distribution file to PyPI (with `upload`)
  * You can upload multiple distribution files in different formats for the same version of your project


Distributing executables
------------------------

* Automatic script creation
  * Use `entry_points` in `setup.py`

* **Py2exe**
  * Creates a Windows executable (includes Python interpreter)
  * http://www.py2exe.org

* **Py2app**
  * Creates a Mac OS X application (includes Python interpreter)
  * http://www.pythonhosted.org/py2app/

* **PyInstaller**
  * Supports multiple platforms
  * http://www.pyinstaller.org


Resources
---------

* **Setuptools Documentation**
  * https://pythonhosted.org/setuptools/
* **PyPA sample project**
  * https://github.com/pypa/sampleproject
* **Python Packaging User Guide**
  * https://packaging.python.org/en/latest/

