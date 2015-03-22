# (Isolated) Virtual Environments

## Why we need isolated virtual environments

* Shortcomings of system-wide installs
  * Multiple projects with conflicting dependencies
  * Conflicts with system dependencies
  * Multi-user systems
  * Testing code against different python and library versions


## Best practices

* Use `virtualenv` to create isolated Python environments
  * Isolate project dependencies
* Don't install Python packages globally!
  * Work inside `virtualenv`
* Projects with conflicting dependecies can coexist peacefully
  * If thy live inside their own virtualenv


## Virtualenv

### Preparation/Install virtualenv

* Install `virtualenv`

  ```
  pip install virtualenv
  ```

### Creating and activating a virtual envirinment

* You can keep all your virtual environments in a central place

  ```
  mkdir ~/.virtualenvs
  cd ~/.virtualenvs
  virtualenv myenv
  source ~/.virtualenvs/myenv/bin/activate
  ```

* Or, alternatively, you can have it locally on a per project fashion (and specify a specific Python version (i.e. version 3) with `-p python3`)

  ```
  cd path/to/my/project
  virtualenv -p python3 .venv
  source .venv/bin/activate
  ```

  **IMPORTANT**: If you create your virtualenv _inside_ your projects **make sure you ignore the folder for version control**.
  A good practice is to always name your virtualenv folder with a standard name i.e. `.venv` and ALWAYS put it on your `.gitignore` file.

* After activating a virtual environment the name of the active virtualenv is shown in parentheses in front of your normal shell prompt

  ```
  (.venv)user@computer:currentdir$
  ```


### Deactivating a virtual environment

```
deactivate
```

### Working in a virtual environment

* Activating your virtual environment CHANGES YOUR PATH
  * `<path/to/your/project>/.venv/bin` is added as the first PATH element
* Packages will be installed inside your virtualenv `site-packages` directory
  * `<path/to/your/project>/.venv/lib/pythonX/site-packages`
* `sys.path` changes to include ONLY your virtualenv paths. i.e.
  * `''`
  * `<path/to/your/project>/.venv/lib/python34.zip`
  * `<path/to/your/project>/.venv/lib/python3.4`
  * `<path/to/your/project>/.venv/lib/python3.4/plat-darwin`
  * `<path/to/your/project>/.venv/lib/python3.4/lib-dynload`
  * `/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4`
  * `/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/plat-darwin`
  * `<path/to/your/project>/.venv/lib/python3.4/site-packages`


## Virtualenvwrapper

A user-friendly wrapper around virtualenv.
This should be used along with **central location** for all virtual environments.

### Installing Virtualenvwrapper

* You should install it **system-wide**

* Windows
  * `pip install virtualenvwrapper-win`
  * Default virtualenv location: `%USERPROFILE\Envs`

* Mac / Linux
  * `(sudo) pip install virtualenvwrapper`
  * edit `~/.profile`

    ```
    source /usr/local/bin/virtualenvwrapper.sh
    export PROJECT_HOME="$HOME/dev"
    ```

### Using Virtualenvwrapper

* Create a virtual environment and activate it

  ```
  mkvirtualenv envname
  ```

* Remove a virtual environment

  ```
  rmvirtualenv envname
  ```

* Bind a project to the **active virtual environment**

  ```
  cd myproject
  setvirtualenvproject
  ```

* List all the environments/projects

  ```
  workon
  ```

* Activate environment and switch to project

  ```
  workon envname
  ```

* Deactivate environment

  ```
  deactivate
  ```

* Creating a Python project from scratch by hand

  ```
  cd my/projects/path
  mkdir my_new_project
  mkvirtualenv my_new_project
  cd my_new_project
  setvirtualenvproject
  ```


* Creating a Python project with `mkproject`

  ```
  mkproject my_new_project
  ```

  This command :

  * Creates the folder my_new_project inside the `$PROJECT_HOME` dir (set in your `~/.profile` file)
  * Changes current directory to the project folder
  * Creates a virtual environment with the same name and activates it
  * Binds the project folder to the virtual environment
  * You are ready to work!

**IMPORTANT**: You should name your virtual environments according to your projects

### Virtualenvwrapper for Windows

* The package is called `virtualenvwrapper-win`

* To bind an existing project to the active virtualenv use

  ```
  setprojectdir
  ```

* There is no `mkproject` command

  You must create projects and bind them to virtualenvs yourself

## Resources

* **Virtualenv**
  * https://virtualenv.pypa.io/en/latest/
* **Virtualenvwrapper**
  * https://virtualenvwrapper.readthedocs.org/en/latest/
* **Virtualenvwrapper-win**
  * https://pypi.python.org/pypi/virtualenvwrapper-win

