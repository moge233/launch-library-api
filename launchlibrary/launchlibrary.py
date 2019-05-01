#!/usr/bin/env python3

'''
launchlibrary.py

API wrapper for the Launch Library API.

Base URL: https://launchlibrary.net/1.4/

functions:
    agency
    agency_type
    calendar
    event_type
    launch
    launch_event
    launch_providers
    launch_status
    location
    mission
    mission_event
    mission_type
    pad
    payload
    rocket
    rocket_event
    rocket_family
    changelog
'''


import requests


def agency(**kwargs):
    '''
    Get spaces agencies.

    args:
        mode (str): How the data shall be returned. list, summary, verbose
        id (int): ID of a specific agency
        name (str): name of a specific agency
        abbrev (str): abbreviation of a specific agency
        type (int): agency type ID
        countryCode (str): three letter country code for agency's country
                         : of origin
        islsp (int): whether or not this agency is a launch service
                   : provide. 0 for no, 1 for yes
        changed (str): changed on or after the supplied date

    returns:
        requests.Response object
    '''
    resp = requests.get('https://launchlibrary.net/1.4/agency',
                        params=kwargs)
    return resp


def agency_type(**kwargs):
    '''
    Get agency type.

    args:
        name (str): name for the agency type
        id (int): ID for the integer type
        changed (str): changed on or after the supplied date

    returns:
        requests.Response object
    '''
    resp = requests.get('https://launchlibrary.net/1.4/agencytype',
                        params=kwargs)
    return resp


def calendar(**kwargs):
    '''
    An alias for launch() with format='ics'

    kwargs:
        mode (str): list, summary, or verbose
        sort (str): 'asc' for ascending, 'desc' for descending
                  : Defaults to ascending
        seq (int): sequence number to pass in

        ** Search options, if all are omitted, next 10 launches **
        ** are returned by Defaults                             **

        next (int): gets the next N launches
        startdate (str): date/time to start the search at
        enddate (str): date/time to end the search at
        limit (int): limit of responses.  Default is 10
        offset (int): offset for pagination
        id (int): ID of the launch you are searching for
        name (str): name of the launch you are searching for
        locationid (int): locationID you are searching for
        rocketid (int): rocketID you are searching for
        lsp (str): Laucnh Service Provider for the launch
        changed (str): changed on or after the supplied date

    returns:
        requests.Response object
    '''
    resp = requests.get('https://launchlibrary.net/1.4/launch',
                        params=kwargs)
    return resp


__all__ = ['agency', 'agency_type', 'calendar', 'event_type', 'launch',
           'launch_event', 'launch_providers', 'launch_status', 'location',
           'mission', 'mission_event', 'mission_type', 'pad', 'payload',
           'rocket', 'rocket_event', 'rocket_family']


if __name__ == '__main__':
    pass
