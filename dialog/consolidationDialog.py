# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yufujimoto/GitHub/SurveyDataCollector/ui/consolidation.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConsolidationDialog(object):
    def setupUi(self, ConsolidationDialog):
        ConsolidationDialog.setObjectName("ConsolidationDialog")
        ConsolidationDialog.resize(761, 476)
        self.gridLayout = QtWidgets.QGridLayout(ConsolidationDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(ConsolidationDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_con_uuid = QtWidgets.QLabel(self.frame)
        self.lbl_con_uuid.setMinimumSize(QtCore.QSize(125, 0))
        self.lbl_con_uuid.setMaximumSize(QtCore.QSize(125, 16777215))
        self.lbl_con_uuid.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_con_uuid.setObjectName("lbl_con_uuid")
        self.horizontalLayout.addWidget(self.lbl_con_uuid)
        self.tbx_con_uuid = QtWidgets.QLineEdit(self.frame)
        self.tbx_con_uuid.setMinimumSize(QtCore.QSize(0, 25))
        self.tbx_con_uuid.setBaseSize(QtCore.QSize(0, 0))
        self.tbx_con_uuid.setFrame(True)
        self.tbx_con_uuid.setReadOnly(True)
        self.tbx_con_uuid.setObjectName("tbx_con_uuid")
        self.horizontalLayout.addWidget(self.tbx_con_uuid)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_con_name = QtWidgets.QLabel(self.frame)
        self.lbl_con_name.setMinimumSize(QtCore.QSize(125, 0))
        self.lbl_con_name.setMaximumSize(QtCore.QSize(125, 16777215))
        self.lbl_con_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_con_name.setObjectName("lbl_con_name")
        self.horizontalLayout_2.addWidget(self.lbl_con_name)
        self.tbx_con_name = QtWidgets.QLineEdit(self.frame)
        self.tbx_con_name.setMinimumSize(QtCore.QSize(0, 25))
        self.tbx_con_name.setBaseSize(QtCore.QSize(0, 0))
        self.tbx_con_name.setFrame(True)
        self.tbx_con_name.setObjectName("tbx_con_name")
        self.horizontalLayout_2.addWidget(self.tbx_con_name)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_con_geoname = QtWidgets.QLabel(self.frame)
        self.lbl_con_geoname.setMinimumSize(QtCore.QSize(125, 0))
        self.lbl_con_geoname.setMaximumSize(QtCore.QSize(125, 16777215))
        self.lbl_con_geoname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_con_geoname.setObjectName("lbl_con_geoname")
        self.horizontalLayout_3.addWidget(self.lbl_con_geoname)
        self.tbx_con_geoname = QtWidgets.QLineEdit(self.frame)
        self.tbx_con_geoname.setMinimumSize(QtCore.QSize(0, 25))
        self.tbx_con_geoname.setBaseSize(QtCore.QSize(0, 0))
        self.tbx_con_geoname.setFrame(True)
        self.tbx_con_geoname.setObjectName("tbx_con_geoname")
        self.horizontalLayout_3.addWidget(self.tbx_con_geoname)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_con_tempral = QtWidgets.QLabel(self.frame)
        self.lbl_con_tempral.setMinimumSize(QtCore.QSize(125, 0))
        self.lbl_con_tempral.setMaximumSize(QtCore.QSize(125, 16777215))
        self.lbl_con_tempral.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_con_tempral.setObjectName("lbl_con_tempral")
        self.horizontalLayout_4.addWidget(self.lbl_con_tempral)
        self.tbx_con_temporal = QtWidgets.QLineEdit(self.frame)
        self.tbx_con_temporal.setMinimumSize(QtCore.QSize(0, 25))
        self.tbx_con_temporal.setBaseSize(QtCore.QSize(0, 0))
        self.tbx_con_temporal.setFrame(True)
        self.tbx_con_temporal.setObjectName("tbx_con_temporal")
        self.horizontalLayout_4.addWidget(self.tbx_con_temporal)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_con_description = QtWidgets.QLabel(self.frame)
        self.lbl_con_description.setMinimumSize(QtCore.QSize(125, 0))
        self.lbl_con_description.setMaximumSize(QtCore.QSize(125, 16777215))
        self.lbl_con_description.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_con_description.setObjectName("lbl_con_description")
        self.horizontalLayout_5.addWidget(self.lbl_con_description)
        self.tbx_con_description = QtWidgets.QLineEdit(self.frame)
        self.tbx_con_description.setMinimumSize(QtCore.QSize(0, 25))
        self.tbx_con_description.setBaseSize(QtCore.QSize(0, 0))
        self.tbx_con_description.setFrame(True)
        self.tbx_con_description.setObjectName("tbx_con_description")
        self.horizontalLayout_5.addWidget(self.tbx_con_description)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.bbx_con_res = QtWidgets.QDialogButtonBox(self.frame)
        self.bbx_con_res.setOrientation(QtCore.Qt.Horizontal)
        self.bbx_con_res.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.bbx_con_res.setObjectName("bbx_con_res")
        self.verticalLayout_6.addWidget(self.bbx_con_res)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(ConsolidationDialog)
        self.bbx_con_res.accepted.connect(ConsolidationDialog.accept)
        self.bbx_con_res.rejected.connect(ConsolidationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConsolidationDialog)
        ConsolidationDialog.setTabOrder(self.tbx_con_uuid, self.tbx_con_name)
        ConsolidationDialog.setTabOrder(self.tbx_con_name, self.tbx_con_geoname)
        ConsolidationDialog.setTabOrder(self.tbx_con_geoname, self.tbx_con_temporal)
        ConsolidationDialog.setTabOrder(self.tbx_con_temporal, self.tbx_con_description)

    def retranslateUi(self, ConsolidationDialog):
        _translate = QtCore.QCoreApplication.translate
        ConsolidationDialog.setWindowTitle(_translate("ConsolidationDialog", "Dialog"))
        self.lbl_con_uuid.setText(_translate("ConsolidationDialog", "UUID : "))
        self.lbl_con_name.setText(_translate("ConsolidationDialog", "統合体の名称 : "))
        self.lbl_con_geoname.setText(_translate("ConsolidationDialog", "地理識別子 : "))
        self.lbl_con_tempral.setText(_translate("ConsolidationDialog", "時間識別子 : "))
        self.lbl_con_description.setText(_translate("ConsolidationDialog", "備考 : "))

