#!/usr/bin/env python3


def format_date(year: int, month: int, day: int) -> str:
    '''Formatting date to store it in a database.

    Parameters
    ----------
    year: int  
    month: int  
    day: int  

    **e. g.** year=2023, month=9, day=3

    Returns
    -------
    str

    **e. g.** '2023-09-03'
    '''
    return f'{year}-{str(month).zfill(2)}-{str(day).zfill(2)}'
