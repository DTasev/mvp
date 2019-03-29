from __future__ import absolute_import

from view import TofConverterView
from model import doConversion


class TofConverterPresenter(object):
    def __init__(self, view=None, model=None):
        self.view = view if view else TofConverterView(parent=None, presenter=self)

    def action_convert(self, event):
        input_val = self.view.InputVal.text()
        input_units = self.view.inputUnits.currentText()
        output_units = self.view.outputUnits.currentText()
        theta = self.view.scatteringAngleInput.text()
        flight_path = self.view.totalFlightPathInput.text()
        out = doConversion(input_val, input_units, output_units, theta, flight_path)
        self.view.convertedVal.setText(str(out))
