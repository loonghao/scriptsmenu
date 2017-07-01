# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
import os
import sys

from Qt import QtWidgets, QtGui
from scriptsmenu import ScriptsMenu
from scriptsmenu.scriptsmenu import load_from_configuration


# set the example evironment variable
os.environ["SCRIPTMENU"] = os.path.dirname(__file__)

config = os.path.expandvars(r"$SCRIPTMENU/menu.yaml")
app = QtWidgets.QApplication(sys.argv)

menu = ScriptsMenu(title="Scripts", parent=None)

# populate the menu using the configuration JSON file.
load_from_configuration(menu, config)

menu.exec_(QtGui.QCursor.pos())

app.exec_()
