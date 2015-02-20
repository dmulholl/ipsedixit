
Ipse Dixit
==========

Lorem ipsum on steroids.

This Python package runs a Markov chain algorithm over the surviving works of the Roman historian Tacitus to generate naturalistic-looking pseudo-Latin gibberish. Useful when you need to generate dummy text as a placeholder in templates, etc.

Sample output:

> Brigantes femina duce exurere coloniam, expugnare castra, ac nisi felicitas in tali casu effugium subveniebat in aperta et solida. Neque is miseriarum finis. Struendum vallum, petendus agger, amissa magna ex parte luxus egestatis scelerum sibi conscios nisi pollutum obstrictumque meritis suis principem passuros.


Usage
-----

#### Library Module ####

Import `ipsedixit` and initialize a `Generator` object:

    >>> import ipsedixit
    >>> generator = ipsedixit.Generator()

The generator's `paragraphs()` method returns a list of `n` generated paragraphs. You can optionally specify the minimum and maximum number of sentences per paragraph. Once initialized, a generator object can continue generating fresh paragraphs indefinitely.

    >>> paragraphs = generator.paragraphs(n, min=2, max=4)

You can substitute a custom source text by supplying it as a string to the initializer:

    >>> generator = ipsedixit.Generator("source text")

Note that passing the string `"caesar"` will swap in a bundled copy of Julius Caesar's *De Bello Gallico* in place of Tacitus:

    >>> generator = ipsedixit.Generator("caesar")


#### Command Line ####

Should the need arise, you can also generate mellifluous pseudo-Latin prose directly from the comfort of the command line:

    $ ipsedixit --help

    usage: ipsedixit [-h] [-v] [--min MIN] [--max MAX] [num]

    positional arguments:
      num            number of paragraphs to generate (default: 4)

    optional arguments:
      -h, --help     show this help message and exit
      -v, --version  show program's version number and exit
      --min MIN      min number of sentences per paragraph (default: 2)
      --max MAX      max number of sentences per paragraph (default: 4)

Output is printed to `stdout`.


Installation
------------

Install directly from the Python Package Index using `pip`:

    $ pip install ipsedixit

Requires Python 3.


License
-------

This work has been placed in the public domain.
