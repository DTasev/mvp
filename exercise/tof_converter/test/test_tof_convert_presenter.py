from __future__ import absolute_import
import unittest
from unittest import TestCase
from mock import Mock
from view import TofConverterView
from presenter import TofConverterPresenter


class TofConverterPresenterTest(TestCase):
    def setUp(self):
        self.view = Mock()
        self.presenter = TofConverterPresenter(view=self.view)

    def test_convert(self):
        # Mock Setup
        self.view.InputVal.return_value = '123'
        self.view.inputUnits.return_value = 'Energy (meV)'
        self.view.outputUnits.return_value = 'Wavelength (Angstroms)'

        # Do the presenter action
        self.presenter.action_convert()

        # Assert Results
        self.view.convertedVal.assert_called_once_with('0.815435441558')


if __name__ == '__main__':
    unittest.main()
