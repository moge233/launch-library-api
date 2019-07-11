#!/usr/bin/env python3

'''
utils.py

This module contains utility functions used for various reasons in the
launchlibrary API wrapper.

functions:
    parse_ics_calendar_format
'''


def parse_ics_calendar_format(ics_response_string):
    '''
    Parses an ICS string returned by the calendar(format='ics') call.

    args:
        ics_response_string (str): the string returned in the content
                                   of the call to callendar(format='ics')
    returns:
        dictionary with the key:value pairs given in the content string
    '''
    ret = dict()
    lines = ics_response_string.splitlines()
    first_four = lines[:4]
    rest = lines[4:]
    for item in first_four:
        key, value = item.split(b':', maxsplit=1)
        ret[key] = value
    ret['launches'] = __parse_ics_launches(rest)
    return ret


def __parse_ics_launches(launches_list):
    '''
    Function for internal use only.
    Used by parse_ics_calendar_format() to parse the list of launches
    provided by the call to calendar(format='ics')

    args:
        launches_list (list): list of launches in ics format

    returns:
        list of launches
    '''
    ret = [] # list of launches to return
    __d = dict() # used for storing the intermediate dictionary
    for item in launches_list:
        key, value = item.split(b':', maxsplit=1)
        if key == b'BEGIN':
            __d.clear() # clear intermediate dictionary at the start
        __d[key] = value
        if key == b'END':
            ret.append(__d) # append intermediate dictionary at the end
    return ret


__all__ = ['parse_ics_calendar_format',]
