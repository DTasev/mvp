from __future__ import absolute_import

from view import TofConverterView


class TofConverterPresenter(object):
    def __init__(self, view=None, model=None):
        self.view = view if view else TofConverterView(parent=None, presenter=self)
