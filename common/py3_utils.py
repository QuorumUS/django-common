# Standard Library
import itertools

try:
    dict.iteritems  # noqa
except AttributeError:
    # Python 3
    def listvalues(d):
        return list(d.values())

    def listitems(d):
        return list(d.items())

    def itervalues(d):
        return iter(d.values())

    def iteritems(d):
        return iter(d.items())

    def filterfalse(predicate, iterable):
        # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
        return itertools.filterfalse(predicate, iterable)

    def zip_longest(fillvalue=None, *args):
        # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
        return itertools.zip_longest(*args, fillvalue=fillvalue)

    def itertools_zip(*iterables):
        # This is just normal zip in Python 3
        return zip(*iterables)

    def list_zip(*iterables):
        return list(zip(*iterables))

    def input_util(prompt=None):
        return input(prompt=prompt)
else:
    # Python 2
    def listvalues(d):
        return d.values()

    def listitems(d):
        return d.items()

    def itervalues(d):
        return d.itervalues()

    def iteritems(d):
        return d.iteritems()

    def filterfalse(predicate, iterable):
        # ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
        return itertools.ifilterfalse(predicate, iterable)

    def zip_longest(*args, **kwds):
        # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
        return itertools.izip_longest(*args, **kwds)

    def itertools_zip(*iterables):
        # izip('ABCD', 'xy') --> Ax By
        return itertools.izip(*iterables)

    def list_zip(*iterables):
        return zip(*iterables)

    def input_util(prompt=''):
        return raw_input(prompt)
