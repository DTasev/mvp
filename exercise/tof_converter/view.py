from __future__ import absolute_import

from utils import load_ui
base, form = load_ui(__file__, "converter.ui")


class TofConverterView(base, form):
    def __init__(self, parent=None, presenter=None):
        super(TofConverterView, self).__init__(parent)
        self.setupUi(self)

        self.presenter = presenter

        # comment or delete the following 2 lines for part 2 of the exercise
        self.historyLabel.setVisible(False)
        self.history.setVisible(False)

        # List of widgets
        # the input value text box
        self.InputVal  # type: QLineEdit
        # self.InputVal.text() for getting the text
        # the `Convert` button
        self.convertButton.clicked.connect(self.presenter.action_convert)
        # the text box for the converted value
        self.convertedVal  # type: QLineEdit
        # the help button
        self.helpButton  # type: QPushButton
        # the input units
        self.inputUnits  # type: QComboBox
        # self.inputUnits.currentText() for the text of the current item
        # the output units
        self.outputUnits  # type: QComboBox
        # the scaterring angle input text box
        self.scatteringAngleInput  # type: QLineEdit
        # the total flight path input text box
        self.totalFlightPathInput  # type: QLineEdit

        self.show()
