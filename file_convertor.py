#!/usr/bin/env python3
# -*- coding:utf8 -*-

######################################################
# Module    :                                        #
# Author    : su.ch                                  #
# Date      : 2020-11-27                             #
# Coding    : utf8                                   #
# -------------------------------------------------- #
# Overview  : set the attributes of GUI              #
# -------------------------------------------------- #
# Copyright : @Copyright by Su.ch                    #
# -------------------------------------------------- #
# Records   :                                        #
######################################################

""" import """
import sys

from PyQt5 import QtWidgets

import Template_File_Convertor.UI.file_convert_1 as FC_1


""" class """
class mainWin(QtWidgets.QMainWindow, FC_1.Ui_MainWindow):
    """ Summary of class here.

    The attributes of GUI.

    Attributes:

    """

    def __init__(self, parent=None):
        """ Python构造方法，同时解决多重继承问题 """

        super(mainWin, self).__init__(parent)
        self.setupUi(self)
        self.addUi()

    def addUi(self):
        """ add attributes of GUI """

        # fixed size of windows
        self.setFixedSize(500, 327)

        # title
        self.setWindowTitle('File Convertor Module')

        # 输入文件部分
        self.lineEdit.setPlaceholderText('*.bit')
        self.pushButton.clicked.connect(self.inputFile)

        # 输出文件部分
        self.lineEdit_3.setPlaceholderText('*.bin')
        self.pushButton_3.clicked.connect(self.outputFile)

    def inputFile(self):
        """ import file """

        get_data = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File', '', 'Bit file(*.bit)')
        bit_file = get_data[0]

        # check file -- add here

        # fill file path
        self.lineEdit.clear()
        self.lineEdit.insert(bit_file)

    def outputFile(self):
        """ output file """

        get_data = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File', '', 'Bit file(*.bin)')
        bin_file = get_data[0]

        # check file -- add here

        # fill file path
        self.lineEdit_3.clear()
        self.lineEdit_3.insert(bin_file)


""" Function """


######################################################
# Name     : main                                    #
# Author   : su.ch                                   #
# Date     : 2020-11-27                              #
# Coding   : utf8                                    #
# -------------------------------------------------- #
# Overview : main function                           #
# Input    : None                                    #
# Return   : None                                    #
# -------------------------------------------------- #
# Note     :                                         #
######################################################
if __name__ == '__main__':

    ######################################
    # Step1 : Application object
    ######################################
    app = QtWidgets.QApplication(sys.argv)

    ######################################
    # Step2 : Window instantiation
    ######################################
    mainWin = mainWin()
    mainWin.show()

    ######################################
    # Step3 : Application exit
    ######################################
    sys.exit(app.exec_())
