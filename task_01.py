#! usr/bin/env pythong
# -*- coding: utf-8 -*-
"""Task 1 week 7"""


def get_matches(players):
    """A list of player names.
    Args:
        players(list, str): A list of strings with player names.
    Returns:
        A list of player names matched with no duplicates (half-cartesian).
    Examples:
        >>> get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]
        """

    mylist = []
    for idx1, name in enumerate(players):
        for idx2, name in enumerate(players):
            if idx1 < idx2:
                mylist.append((players[idx1], name))
    return mylist
