def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    falsey = [0, 0.0, False, [], {}, "", None, ()]
    lst_copy = []
    for entry in lst:
        if entry not in falsey:
            lst_copy.append(entry)
    return lst_copy
