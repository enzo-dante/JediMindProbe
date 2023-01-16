#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 13:31:31 2023

@author: enzo_dante
"""

import unittest
from jedi_mind_probe_script import filterForKeyword, getSentiment, readData, removeColumn
from jedi_mind_probe_strings import *

class JediMindProbeTests(unittest.TestCase):
        
    def setUp(self):
        self.file = FILE_NAME
        self.data = readData(self.file)
        self.data_length = 10437
        
    def test_readData(self):
        """should return dataframe of articles.xlsl excel file"""
        actual = readData(self.file)
        expected = self.data_length

        self.assertEquals(expected, len(actual))

    def test_removeColumn(self):
        """should return dataframe with without COLUMN_ENGAGEMENT_REACTION_COUNT"""
        actual = removeColumn(self.data, COLUMN_ENGAGEMENT_COMMENT_PLUGIN_COUNT)
        expected = 14

        self.assertEquals(expected, len(actual.columns))
        
    def test_filterForKeyword(self):
        """should return list of 0 or 1 flags if keyword was in the article title"""
        actual = filterForKeyword(TEST_KEYWORD)
        expected = self.data_length
        
        self.assertEquals(expected, len(actual))

    def test_getSentiment(self):
        """should return 3 populated series of sentiment analysis"""
        a, b, c = getSentiment(self.data)
        actual = [a, b, c]
        expected = 3
        
        self.assertEqual(expected, len(actual))
        
        expected = self.data_length
        
        self.assertEqual(expected, len(a))
        self.assertEqual(expected, len(b))
        self.assertEqual(expected, len(c))
        
if __name__ == "__main__":
    unittest.main()
