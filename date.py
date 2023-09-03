#!/usr/bin/env python3


def format_date(value: str) -> str:
    '''Formatting date from database to print it for user

    Parameters
    ----------
    value: str - date from a database

    **e. g.** '2023-09-03'

    Returns
    -------
    str
    **e. g.** 'Date: 03.09.2023'
    '''
    vals = value.split('-')
    return f'Date: {vals[2]}.{vals[1]}.{vals[0]}'
