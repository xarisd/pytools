# Documentation

## PEP257

* Semantics and conventions associated with Python docstrings
  * If you violate these conventions, the worst you'll get is some dirty looks

* Docstring
  * String as first statement of a module, function, class, or method
  * Becomes the `__doc__` special attribute of that object

* Main conventions
  * Always use `"""`triple double quotes`"""`
  * A phrase ending in a period
  * For methods: specify the return value

## Docstrings

  ```python
  def function(a, b):
    """Do X and return a list."""
  ```

  ```python
  def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part
    """
  ```

## Sphinx

* Sphinx is the **Python Documentation Generator**
* It is the **De-facto standard**
* It is used to generate official Python docs
* Input: `reStructuredText`
* Output:
  * HTML
  * PDF
  * ePub
  * man pages
  * Texinfo
  *...etc.
* It has many features and extensions

### Installing Sphinx

```
pip install sphinx
```


### Running Sphinx

* Run `sphinx-quickstart` from `docs/` folder
  * Don't forget to enable `autodocs`

* Edit the `index.rst` file

* Run `make html` to built the html

* Configuration is in `conf.py` file
  * You can edit it to change settings (html theme, etc)


## reStructuredText

* Plain-text based markup

* Paragraphs are separated by a single line
  * Identation matters

* Emphasis:
  * \**italic*\*
  * \*\***bold**\*\*
  * \`\``code`\`\`

* Links:
  * \`Link text <http://example.com>\`_
  * A plain URL (http://...) will be recognized as well

## References

* **.. _target:**
  * A plain link target
  * Mark a section

* **:ref:\`target\`**
  * Will use the section's title as link's description

* **\`target\`_**
  * Will simply use "target" as description

### Documenting you code

* Literal code blocks:
  * End a paragraph with `::`
  * Following block will be layed out as code
  * Must be indented and surrounded by blank lines

* Documenting Python structures
  * Adds them to index as well

  | Structure | Target                  | References
  |-----------|-------------------------|---------------------
  | module    | **.. module:: name**    | **:module:\`name\`**
  | function  | **.. function:: name**  | **:func:\`name\`**
  | class     | **.. class:: name**     | **:class:\`name\`**
  | method    | **.. method:: name**    | **:meth:\`name\`**

## Autodoc

* `.. autofunction:: name`
* `.. automethod:: name`
* `.. autoclass:: name`
  * `:members:` (all public methods with docstrings)
  * `:members: width, height`
* `.. automodule:: name`
  * Also has `:members:` option

* Make sure to activate the `autodoc` extension in `conf.py`!

  ```
  extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
  ]
  ```

* And fix the path in `conf.py`

  ```python
  sys.path.insert(0, os.path.abspath('..'))
  ```

## Resources

* **Sphinx Documentation**
  * http://sphinx-doc.org/
* **reStructredText Home page**
  * http://docutils.sourceforge.net/rst.html
* **reStructredText Primer**
  * http://sphinx-doc.org/rest.html
* **Autodoc Extension**
  * http://sphinx-doc.org/ext/autodoc.html
