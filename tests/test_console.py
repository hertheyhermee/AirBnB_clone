#!/usr/bin/python3
'''
    Description:
        Test suite for the console
'''


import sys
import models
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec


class test_console(unittest.TestCase):
    '''
        Description:
            Test the console module
    '''
    def setUp(self):
        '''setup for'''
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        ''''''
        sys.stdout = self.backup

    def create(self):
        '''
            Description:
                create an instance of the HBNBCommand class
        '''
        return HBNBCommand()

    def test_quit(self):
        '''
            Description:
                Test quit exists
        '''
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        '''
            Description:
                Test EOF exists
        '''
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_all(self):
        '''
            Description:
                Test all exists
        '''
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))
