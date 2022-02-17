import json

import pytest
import eq_jsons


def test_equal():
    tests = (
        ({}, {}),
        ({'x': 1}, {'x': 1}),
        ({'x': 1, 'y': 52.45678910}, {'x': 1, 'y': 52.45678910}),
        ({
            'name': 'test',
            'latlng': [56.456789, 39.654325],
            'children': [
                {'name': 'test1', 'latlng': [45.678908, 56.765456]},
                {'name': 'test2', 'latlng': [23.567898, 12.345435]}
            ]
         }, {
            'name': 'test',
            'latlng': [56.456789, 39.654325],
            'children': [
                {'name': 'test1', 'latlng': [45.678908, 56.765456]},
                {'name': 'test2', 'latlng': [23.567898, 12.345435]}
            ]
        })
    )
    for case in tests:
        assert eq_jsons.is_equal(json.dumps(case[0]), json.dumps(case[1]))


def test_not_equal():
    tests = (
        ({'x': 1, 'y': 2}, {'x': 1}),
        ({'x': 1}, {'x': 1, 'y': 2}),
        ({'x': 1, 'y': 52.45678}, {'x': 1, 'y': 52.45678910}),
    )
    for case in tests:
        assert eq_jsons.is_equal(json.dumps(case[0]), json.dumps(case[1])) is False
