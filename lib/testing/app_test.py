#!/usr/bin/env python3

from os import path
import runpy
import io
import sys
from app import get_hello_world

def test_hello_world():
    result = get_hello_world()
    expected = 'Hello world!Hello Sun!!Hello Sky!!!\n'
    assert result == expected, f"AssertionError: expected {expected}, but got {result}"



class TestAppPy:
    '''
    app.py
    '''
    def test_app_py_exists(self):
        '''
        exists in lib directory
        '''
        assert(path.exists("lib/app.py"))

    def test_app_py_runs(self):
        '''
        is executable
        '''
        runpy.run_path("lib/app.py")

    def test_prints_hello_world(self):
        '''
        prints "Hello World! Pass this test, please."
        '''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        runpy.run_path("lib/app.py")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Hello World! Pass this test, please.\n")
