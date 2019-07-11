#!/usr/bin/env python3

'''
test_launchlibrary.py

Main testing module for the launchlibrary module.
'''


from datetime import datetime
from unittest import TestCase

from requests import Response

from launchlibrary import launchlibrary


def datetime_from_datestring(date_str):
    '''
    Utility function to get a datetime object from the datetime string
    used in/provided by the Launch Library API.

    args:
        date_str (str): Date string in the format 'yyyy-mm-dd hh:mm:ss'

    returns:
        datetime.datetime
    '''
    return datetime.fromisoformat(date_str)


class TestLaunchLibraryAgency(TestCase):

    def test_agency(self):
        resp = launchlibrary.agency()
        self.assertEqual(200, resp.status_code)
        self.assertIsInstance(resp, Response)

    def test_agency_json(self):
        resp_json = launchlibrary.agency().json()
        self.assertIsInstance(resp_json, dict)
        self.assertIn('agencies', resp_json)
        self.assertIsInstance(resp_json['agencies'], list)
        self.assertIn('total', resp_json)
        self.assertIsInstance(resp_json['total'], int)
        self.assertIn('count', resp_json)
        self.assertIsInstance(resp_json['count'], int)
        self.assertIn('offset', resp_json)
        self.assertIsInstance(resp_json['offset'], int)

    def test_agency_id(self):
        resp_json = launchlibrary.agency(id=44).json()
        agencies = resp_json['agencies']
        nasa = agencies[0]
        self.assertEqual(resp_json['count'], 1)
        self.assertIsInstance(agencies, list)
        self.assertIsInstance(nasa, dict)
        self.assertEqual(nasa['id'], 44)

    def test_agency_name(self):
        resp_json = launchlibrary.agency(
            name='National Aeronautics and Space Administration'
        ).json()
        agencies = resp_json['agencies']
        nasa = agencies[0]
        self.assertEqual(resp_json['count'], 1)
        self.assertIsInstance(agencies, list)
        self.assertIsInstance(nasa, dict)
        self.assertEqual(nasa['name'],
                        'National Aeronautics and Space Administration')

    def test_agency_abbrev(self):
        resp_json = launchlibrary.agency(abbrev='NASA').json()
        agencies = resp_json['agencies']
        nasa = agencies[0]
        self.assertEqual(resp_json['count'], 1)
        self.assertIsInstance(agencies, list)
        self.assertIsInstance(nasa, dict)
        self.assertEqual(nasa['abbrev'], 'NASA')

    def test_agency_type(self):
        resp_json = launchlibrary.agency(type=1).json()
        agencies = resp_json['agencies']
        agency = agencies[0]
        self.assertIsInstance(agencies, list)
        self.assertIsInstance(agency, dict)
        self.assertEqual(agency['type'], 1)

    def test_agency_country_code(self):
        resp_json = launchlibrary.agency(countryCode='USA').json()
        agencies = resp_json['agencies']
        agency = agencies[0]
        self.assertIsInstance(agencies, list)
        self.assertIsInstance(agency, dict)
        self.assertEqual(agency['countryCode'], 'USA')

    def test_agency_is_lsp(self):
        resp_json = launchlibrary.agency(islsp=1).json()
        agencies = resp_json['agencies']
        agency = agencies[0]
        self.assertIsInstance(agencies, list)
        self.assertIsInstance(agency, dict)
        self.assertEqual(agency['islsp'], 1)

    def test_agency_changed(self):
        resp = launchlibrary.agency(changed='2012-09-05 00:00:00')
        resp_json = resp.json()
        agencies = resp_json['agencies']
        agency = agencies[0]
        self.assertIsInstance(agencies, list)
        self.assertIsInstance(agency, dict)
        # changed will show agencies that have changed since the
        # date provided so we check that resulting date is 
        # greater or equal than the date provided
        self.assertGreaterEqual(
            datetime_from_datestring(agency['changed']),
            datetime_from_datestring('2012-09-05 00:00:00')
        )


class TestLaunchLibraryAgencyType(TestCase):

    def test_agencytype(self):
        resp = launchlibrary.agency_type()
        self.assertEqual(200, resp.status_code)
        self.assertIsInstance(resp, Response)

    def test_agencytype_json(self):
        resp_json = launchlibrary.agency_type().json()
        self.assertIsInstance(resp_json, dict)
        self.assertIn('types', resp_json)
        self.assertIsInstance(resp_json['types'], list)
        self.assertIn('total', resp_json)
        self.assertIsInstance(resp_json['total'], int)
        self.assertIn('count', resp_json)
        self.assertIsInstance(resp_json['count'], int)
        self.assertIn('offset', resp_json)
        self.assertIsInstance(resp_json['offset'], int)

    def test_agencytype_name(self):
        resp_json = launchlibrary.agency_type(
            name='Government'
        ).json()
        types = resp_json['types']
        government = types[0]
        self.assertEqual(resp_json['count'], 1)
        self.assertIsInstance(types, list)
        self.assertIsInstance(government, dict)
        self.assertEqual(government['name'], 'Government')

    def test_agencytype_id(self):
        resp_json = launchlibrary.agency_type(id=1).json()
        types = resp_json['types']
        government = types[0]
        self.assertEqual(resp_json['count'], 1)
        self.assertIsInstance(types, list)
        self.assertIsInstance(government, dict)
        self.assertEqual(government['id'], 1)

    def test_agencytype_changed(self):
        resp = launchlibrary.agency_type(changed='2012-09-05 00:00:00')
        resp_json = resp.json()
        types = resp_json['types']
        t = types[0]
        self.assertIsInstance(types, list)
        self.assertIsInstance(t, dict)
        # changed will show agencies that have changed since the
        # date provided so we check that resulting date is 
        # greater or equal than the date provided
        self.assertGreaterEqual(
            datetime_from_datestring(t['changed']),
            datetime_from_datestring('2012-09-05 00:00:00')
        )


class TestLaunchLibraryCalendar(TestCase):
    '''
    Because this request returns a response object that has ICS data
    in its content, this test is very minimal.  Since the calendar()
    API call is an equivalent to the launch() call with format set to
    'ics', the launch test will be "good enough".

    A .ics file is a universal calendar format used by several email
    and calendar programs.
    To parse an ICS file in Python, check out the icalendar package.
    https://pypi.org/project/icalendar/
    '''

    def test_calendar(self):
        resp = launchlibrary.calendar()
        self.assertEqual(200, resp.status_code)
        self.assertIsInstance(resp, Response)


class TestLaunchLibraryLaunch(TestCase):

    def test_launch(self):
        resp = launchlibrary.launch()
        self.assertEqual(200, resp.status_code)
        self.assertIsInstance(resp, Response)

    def test_launch_json(self):
        resp_json = launchlibrary.launch().json()
        self.assertIsInstance(resp_json, dict)
        self.assertIn('launches', resp_json)
        self.assertIsInstance(resp_json['launches'], list)
        self.assertIn('total', resp_json)
        self.assertIsInstance(resp_json['total'], int)
        self.assertIn('count', resp_json)
        self.assertIsInstance(resp_json['count'], int)
        self.assertIn('offset', resp_json)
        self.assertIsInstance(resp_json['offset'], int)

    def test_launch_mode_list(self):
        resp_json = launchlibrary.launch(mode='list').json()
        launches = resp_json['launches']
        launch = launches[0]
        keys = ['id', 'name', 'windowstart', 'windowend', 'net',
                'status', 'hashtag', 'vidURLs', 'vidURL', 'tbdtime',
                'tbddate', 'probability', 'changed', 'lsp']
        keys = sorted(keys)
        resp_keys = sorted(launch.keys())
        self.assertListEqual(resp_keys, keys)

    def test_launch_mode_summary(self):
        resp_json = launchlibrary.launch(mode='summary').json()
        launches = resp_json['launches']
        launch = launches[0]
        keys = ['id', 'name', 'windowstart', 'windowend', 'net',
                'status', 'inhold', 'tbdtime', 'tbddate', 'probability',
                'changed', 'lsp', 'hashtag', 'vidURL', 'vidURLs']
        keys = sorted(keys)
        resp_keys = sorted(launch.keys())
        self.assertListEqual(resp_keys, keys)

    def test_launch_mode_verbose(self):
        resp_json = launchlibrary.launch(mode='verbose').json()
        launches = resp_json['launches']
        launch = launches[0]
        keys = ['id', 'name', 'windowstart', 'windowend', 'net',
                'wsstamp', 'westamp', 'netstamp', 'isostart', 'isoend',
                'isonet', 'status', 'inhold', 'tbdtime', 'vidURLs',
                'vidURL', 'infoURLs', 'infoURL', 'holdreason',
                'failreason', 'tbddate', 'probability', 'hashtag',
                'changed', 'location', 'rocket', 'missions', 'lsp']
        keys = sorted(keys)
        resp_keys = sorted(launch.keys())
        self.assertListEqual(resp_keys, keys)

    def test_launch_sort(self):
        # default order is ascending, so we will only check that
        # descending (sort='desc') works
        # 
        # upon further inspection, sort doesn't seem to work in the 
        # website's API, so this really does nothing until they fix that
        resp_json = launchlibrary.launch(sort='desc').json()
        launches = resp_json['launches']
        launch0 = launches[0]
        launch1 = launches[1]
        date_format = '%B %d, %Y %H:%M:%S' # format of NET without the UTC
        net0 = launch0['net'][:-4] # strip off the 'UTC' at the end
        net1 = launch1['net'][:-4] # strip off the 'UTC' at the end
        dt0 = datetime.strptime(net0, date_format)
        dt1 = datetime.strptime(net1, date_format)
        self.assertLess(dt0, dt1)


class TestLaunchLibraryLaunchProviders(TestCase):

    def test_launch_providers(self):
        resp = launchlibrary.launch_providers()
        self.assertEqual(200, resp.status_code)
        self.assertIsInstance(resp, Response)

    def test_launch_providers_json(self):
        resp_json = launchlibrary.launch_providers().json()
        self.assertIsInstance(resp_json, dict)
        self.assertIn('agencies', resp_json)
        self.assertIsInstance(resp_json['agencies'], list)
        self.assertIn('total', resp_json)
        self.assertIsInstance(resp_json['total'], int)
        self.assertIn('count', resp_json)
        self.assertIsInstance(resp_json['count'], int)
        self.assertIn('offset', resp_json)
        self.assertIsInstance(resp_json['offset'], int)

    def test_launch_providers_id(self):
        resp_json = launchlibrary.launch_providers(id=44).json()
        agencies = resp_json['agencies']
        nasa = agencies[0]
        self.assertEqual(resp_json['count'], 1)
        self.assertIsInstance(agencies, list)
        self.assertIsInstance(nasa, dict)
        self.assertEqual(nasa['id'], 44)

    def test_launch_providers_name(self):
        resp_json = launchlibrary.launch_providers(
            name='National Aeronautics and Space Administration'
        ).json()
        agencies = resp_json['agencies']
        nasa = agencies[0]
        self.assertEqual(resp_json['count'], 1)
        self.assertIsInstance(agencies, list)
        self.assertIsInstance(nasa, dict)
        self.assertEqual(nasa['name'],
                        'National Aeronautics and Space Administration')

    def test_launch_providers_abbrev(self):
        resp_json = launchlibrary.launch_providers(abbrev='NASA').json()
        agencies = resp_json['agencies']
        nasa = agencies[0]
        self.assertEqual(resp_json['count'], 1)
        self.assertIsInstance(agencies, list)
        self.assertIsInstance(nasa, dict)
        self.assertEqual(nasa['abbrev'], 'NASA')

    def test_launch_providers_type(self):
        resp_json = launchlibrary.launch_providers(type=1).json()
        agencies = resp_json['agencies']
        agency = agencies[0]
        self.assertIsInstance(agencies, list)
        self.assertIsInstance(agency, dict)
        self.assertEqual(agency['type'], 1)

    def test_launch_providers_country_code(self):
        resp_json = launchlibrary.launch_providers(countryCode='USA').json()
        agencies = resp_json['agencies']
        agency = agencies[0]
        self.assertIsInstance(agencies, list)
        self.assertIsInstance(agency, dict)
        self.assertEqual(agency['countryCode'], 'USA')

    def test_launch_providers_changed(self):
        resp = launchlibrary.launch_providers(changed='2012-09-05 00:00:00')
        resp_json = resp.json()
        agencies = resp_json['agencies']
        agency = agencies[0]
        self.assertIsInstance(agencies, list)
        self.assertIsInstance(agency, dict)
        # changed will show agencies that have changed since the
        # date provided so we check that resulting date is 
        # greater or equal than the date provided
        self.assertGreaterEqual(
            datetime_from_datestring(agency['changed']),
            datetime_from_datestring('2012-09-05 00:00:00')
        )


class TestLaunchLibraryLaunchStatus(TestCase):

    def test_launch_status(self):
        resp = launchlibrary.launch_status()
        self.assertEqual(200, resp.status_code)
        self.assertIsInstance(resp, Response)

    def test_status_json(self):
        resp_json = launchlibrary.launch_status().json()
        self.assertIsInstance(resp_json, dict)
        self.assertIn('types', resp_json)
        self.assertIsInstance(resp_json['types'], list)
        self.assertIn('total', resp_json)
        self.assertIsInstance(resp_json['total'], int)
        self.assertIn('count', resp_json)
        self.assertIsInstance(resp_json['count'], int)
        self.assertIn('offset', resp_json)
        self.assertIsInstance(resp_json['offset'], int)
