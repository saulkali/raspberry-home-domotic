import unittest
from unittest import defaultTestLoader

from test.common.utils.test_patter_design import PatterDesignTest
from test.modules.moduleLogin.test_login import LoginTest
from test.modules.moduleHome.test_home import HomeTest

suite = defaultTestLoader.discover("test")

suite.addTest(unittest.makeSuite((PatterDesignTest)))
suite.addTest(unittest.makeSuite(LoginTest))
suite.addTest(unittest.makeSuite(HomeTest))