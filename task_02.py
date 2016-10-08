#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 2 for week 7"""

import authentication
import getpass


def login(username, maxattempts=1):
    """str, int(optional). Prompt for password and tests if correct or not.
    Args:
        username(str): Arg of username as a string.
        maxattempts(int, optional): attmepts to enter correct password as int.
    Returns:
        Something.
    Example:
        >>> import task_02
        task_02.login('mike', 4)
    Please enter your password:
    Incorrect username or password. You have 3 attempts left.
    Please enter your password:
    Incorrect username or password. You have 2 attempts left.
    Please enter your password:
    Incorrect username or password. You have 1 attempts left.
    Please enter your password:
    Incorrect username or password. You have 0 attempts left.
    False>>>
    """
    authenticated = False
    attleft = 'Incorrect username or password. You have {} attempts left.'

    while not authenticated and maxattempts != 0:
        passinput = getpass.getpass()
        print passinput
        authenticated = authentication.authenticate(username, passinput)
        if authenticated is True:
            return authenticated
        elif not authenticated and maxattempts != 0:
            maxattempts -= 1
            print attleft.format(maxattempts)
    return authenticated
