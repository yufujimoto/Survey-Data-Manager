# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yufujimoto/GitHub/tetheredShooting/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 695)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tab_control = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_control.setMinimumSize(QtCore.QSize(420, 0))
        self.tab_control.setMaximumSize(QtCore.QSize(420, 16777215))
        self.tab_control.setIconSize(QtCore.QSize(24, 24))
        self.tab_control.setObjectName("tab_control")
        self.tab_prj_item = QtWidgets.QWidget()
        self.tab_prj_item.setObjectName("tab_prj_item")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_prj_item)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lay_h_dir_root = QtWidgets.QHBoxLayout()
        self.lay_h_dir_root.setContentsMargins(-1, 0, -1, -1)
        self.lay_h_dir_root.setObjectName("lay_h_dir_root")
        self.lbl_prjDir = QtWidgets.QLabel(self.tab_prj_item)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_prjDir.sizePolicy().hasHeightForWidth())
        self.lbl_prjDir.setSizePolicy(sizePolicy)
        self.lbl_prjDir.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_prjDir.setObjectName("lbl_prjDir")
        self.lay_h_dir_root.addWidget(self.lbl_prjDir)
        self.lbl_prj_path = QtWidgets.QLabel(self.tab_prj_item)
        self.lbl_prj_path.setText("")
        self.lbl_prj_path.setObjectName("lbl_prj_path")
        self.lay_h_dir_root.addWidget(self.lbl_prj_path)
        self.verticalLayout_7.addLayout(self.lay_h_dir_root)
        self.tre_prj_item = QtWidgets.QTreeWidget(self.tab_prj_item)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tre_prj_item.sizePolicy().hasHeightForWidth())
        self.tre_prj_item.setSizePolicy(sizePolicy)
        self.tre_prj_item.setMinimumSize(QtCore.QSize(0, 0))
        self.tre_prj_item.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tre_prj_item.setLineWidth(1)
        self.tre_prj_item.setColumnCount(3)
        self.tre_prj_item.setObjectName("tre_prj_item")
        self.tre_prj_item.header().setDefaultSectionSize(150)
        self.tre_prj_item.header().setHighlightSections(False)
        self.verticalLayout_7.addWidget(self.tre_prj_item)
        self.tab_control.addTab(self.tab_prj_item, "")
        self.tab_prj_cam = QtWidgets.QWidget()
        self.tab_prj_cam.setObjectName("tab_prj_cam")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_prj_cam)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lay_h_cam_detect = QtWidgets.QHBoxLayout()
        self.lay_h_cam_detect.setObjectName("lay_h_cam_detect")
        self.lbl_cam_detected = QtWidgets.QLabel(self.tab_prj_cam)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_cam_detected.sizePolicy().hasHeightForWidth())
        self.lbl_cam_detected.setSizePolicy(sizePolicy)
        self.lbl_cam_detected.setMinimumSize(QtCore.QSize(200, 0))
        self.lbl_cam_detected.setMaximumSize(QtCore.QSize(16777215, 200))
        self.lbl_cam_detected.setObjectName("lbl_cam_detected")
        self.lay_h_cam_detect.addWidget(self.lbl_cam_detected)
        self.btn_cam_detect = QtWidgets.QPushButton(self.tab_prj_cam)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cam_detect.sizePolicy().hasHeightForWidth())
        self.btn_cam_detect.setSizePolicy(sizePolicy)
        self.btn_cam_detect.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btn_cam_detect.setObjectName("btn_cam_detect")
        self.lay_h_cam_detect.addWidget(self.btn_cam_detect)
        self.verticalLayout_2.addLayout(self.lay_h_cam_detect)
        self.grp_cam = QtWidgets.QGroupBox(self.tab_prj_cam)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grp_cam.sizePolicy().hasHeightForWidth())
        self.grp_cam.setSizePolicy(sizePolicy)
        self.grp_cam.setMinimumSize(QtCore.QSize(0, 400))
        self.grp_cam.setMaximumSize(QtCore.QSize(400, 16777215))
        self.grp_cam.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.grp_cam.setObjectName("grp_cam")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.grp_cam)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lbl_cam_qoi = QtWidgets.QLabel(self.grp_cam)
        self.lbl_cam_qoi.setObjectName("lbl_cam_qoi")
        self.gridLayout_4.addWidget(self.lbl_cam_qoi, 7, 0, 1, 1)
        self.cbx_cam_epg = QtWidgets.QComboBox(self.grp_cam)
        self.cbx_cam_epg.setObjectName("cbx_cam_epg")
        self.gridLayout_4.addWidget(self.cbx_cam_epg, 9, 1, 1, 1)
        self.cbx_cam_size = QtWidgets.QComboBox(self.grp_cam)
        self.cbx_cam_size.setObjectName("cbx_cam_size")
        self.gridLayout_4.addWidget(self.cbx_cam_size, 1, 1, 1, 1)
        self.lbl_cam_fmod = QtWidgets.QLabel(self.grp_cam)
        self.lbl_cam_fmod.setObjectName("lbl_cam_fmod")
        self.gridLayout_4.addWidget(self.lbl_cam_fmod, 8, 0, 1, 1)
        self.lbl_cam_epg = QtWidgets.QLabel(self.grp_cam)
        self.lbl_cam_epg.setObjectName("lbl_cam_epg")
        self.gridLayout_4.addWidget(self.lbl_cam_epg, 9, 0, 1, 1)
        self.lbl_cam_size = QtWidgets.QLabel(self.grp_cam)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_cam_size.sizePolicy().hasHeightForWidth())
        self.lbl_cam_size.setSizePolicy(sizePolicy)
        self.lbl_cam_size.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lbl_cam_size.setObjectName("lbl_cam_size")
        self.gridLayout_4.addWidget(self.lbl_cam_size, 1, 0, 1, 1)
        self.cbx_cam_fmod = QtWidgets.QComboBox(self.grp_cam)
        self.cbx_cam_fmod.setObjectName("cbx_cam_fmod")
        self.gridLayout_4.addWidget(self.cbx_cam_fmod, 8, 1, 1, 1)
        self.lbl_cam_iso = QtWidgets.QLabel(self.grp_cam)
        self.lbl_cam_iso.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lbl_cam_iso.setObjectName("lbl_cam_iso")
        self.gridLayout_4.addWidget(self.lbl_cam_iso, 3, 0, 1, 1)
        self.cbx_cam_iso = QtWidgets.QComboBox(self.grp_cam)
        self.cbx_cam_iso.setObjectName("cbx_cam_iso")
        self.gridLayout_4.addWidget(self.cbx_cam_iso, 3, 1, 1, 1)
        self.lbl_cam_cpt = QtWidgets.QLabel(self.grp_cam)
        self.lbl_cam_cpt.setObjectName("lbl_cam_cpt")
        self.gridLayout_4.addWidget(self.lbl_cam_cpt, 10, 0, 1, 1)
        self.lbl_cam_fval = QtWidgets.QLabel(self.grp_cam)
        self.lbl_cam_fval.setObjectName("lbl_cam_fval")
        self.gridLayout_4.addWidget(self.lbl_cam_fval, 6, 0, 1, 1)
        self.lbl_cam_wht = QtWidgets.QLabel(self.grp_cam)
        self.lbl_cam_wht.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lbl_cam_wht.setObjectName("lbl_cam_wht")
        self.gridLayout_4.addWidget(self.lbl_cam_wht, 4, 0, 1, 1)
        self.cbx_cam_cpt = QtWidgets.QComboBox(self.grp_cam)
        self.cbx_cam_cpt.setObjectName("cbx_cam_cpt")
        self.gridLayout_4.addWidget(self.cbx_cam_cpt, 10, 1, 1, 1)
        self.cbx_cam_wht = QtWidgets.QComboBox(self.grp_cam)
        self.cbx_cam_wht.setObjectName("cbx_cam_wht")
        self.gridLayout_4.addWidget(self.cbx_cam_wht, 4, 1, 1, 1)
        self.lbl_cam_exp = QtWidgets.QLabel(self.grp_cam)
        self.lbl_cam_exp.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lbl_cam_exp.setObjectName("lbl_cam_exp")
        self.gridLayout_4.addWidget(self.lbl_cam_exp, 5, 0, 1, 1)
        self.cbx_cam_exp = QtWidgets.QComboBox(self.grp_cam)
        self.cbx_cam_exp.setObjectName("cbx_cam_exp")
        self.gridLayout_4.addWidget(self.cbx_cam_exp, 5, 1, 1, 1)
        self.lbl_cam_met = QtWidgets.QLabel(self.grp_cam)
        self.lbl_cam_met.setObjectName("lbl_cam_met")
        self.gridLayout_4.addWidget(self.lbl_cam_met, 11, 0, 1, 1)
        self.cbx_cam_met = QtWidgets.QComboBox(self.grp_cam)
        self.cbx_cam_met.setObjectName("cbx_cam_met")
        self.gridLayout_4.addWidget(self.cbx_cam_met, 11, 1, 1, 1)
        self.cbx_cam_fval = QtWidgets.QComboBox(self.grp_cam)
        self.cbx_cam_fval.setObjectName("cbx_cam_fval")
        self.gridLayout_4.addWidget(self.cbx_cam_fval, 6, 1, 1, 1)
        self.cbx_cam_qoi = QtWidgets.QComboBox(self.grp_cam)
        self.cbx_cam_qoi.setObjectName("cbx_cam_qoi")
        self.gridLayout_4.addWidget(self.cbx_cam_qoi, 7, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.grp_cam)
        self.tab_control.addTab(self.tab_prj_cam, "")
        self.horizontalLayout.addWidget(self.tab_control)
        self.lay_v_item_info = QtWidgets.QVBoxLayout()
        self.lay_v_item_info.setContentsMargins(-1, 0, -1, -1)
        self.lay_v_item_info.setObjectName("lay_v_item_info")
        self.tab_target = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_target.sizePolicy().hasHeightForWidth())
        self.tab_target.setSizePolicy(sizePolicy)
        self.tab_target.setMinimumSize(QtCore.QSize(0, 0))
        self.tab_target.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tab_target.setAutoFillBackground(False)
        self.tab_target.setIconSize(QtCore.QSize(24, 24))
        self.tab_target.setTabsClosable(False)
        self.tab_target.setObjectName("tab_target")
        self.tab_con = QtWidgets.QWidget()
        self.tab_con.setObjectName("tab_con")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_con)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lay_h_con_ope = QtWidgets.QHBoxLayout()
        self.lay_h_con_ope.setContentsMargins(-1, 0, -1, -1)
        self.lay_h_con_ope.setObjectName("lay_h_con_ope")
        self.rad_con_new = QtWidgets.QRadioButton(self.tab_con)
        self.rad_con_new.setMinimumSize(QtCore.QSize(200, 0))
        self.rad_con_new.setMaximumSize(QtCore.QSize(200, 16777215))
        self.rad_con_new.setObjectName("rad_con_new")
        self.lay_h_con_ope.addWidget(self.rad_con_new)
        self.rad_con_mod = QtWidgets.QRadioButton(self.tab_con)
        self.rad_con_mod.setObjectName("rad_con_mod")
        self.lay_h_con_ope.addWidget(self.rad_con_mod)
        self.verticalLayout.addLayout(self.lay_h_con_ope)
        self.lay_h_con_nam = QtWidgets.QHBoxLayout()
        self.lay_h_con_nam.setContentsMargins(-1, 0, -1, -1)
        self.lay_h_con_nam.setObjectName("lay_h_con_nam")
        self.lbl_con_name = QtWidgets.QLabel(self.tab_con)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_con_name.sizePolicy().hasHeightForWidth())
        self.lbl_con_name.setSizePolicy(sizePolicy)
        self.lbl_con_name.setMinimumSize(QtCore.QSize(100, 0))
        self.lbl_con_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_con_name.setObjectName("lbl_con_name")
        self.lay_h_con_nam.addWidget(self.lbl_con_name)
        self.tbx_con_name = QtWidgets.QLineEdit(self.tab_con)
        self.tbx_con_name.setEnabled(False)
        self.tbx_con_name.setObjectName("tbx_con_name")
        self.lay_h_con_nam.addWidget(self.tbx_con_name)
        self.verticalLayout.addLayout(self.lay_h_con_nam)
        self.lay_h_con_geo = QtWidgets.QHBoxLayout()
        self.lay_h_con_geo.setContentsMargins(-1, 0, -1, -1)
        self.lay_h_con_geo.setObjectName("lay_h_con_geo")
        self.lbl_con_geoname = QtWidgets.QLabel(self.tab_con)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_con_geoname.sizePolicy().hasHeightForWidth())
        self.lbl_con_geoname.setSizePolicy(sizePolicy)
        self.lbl_con_geoname.setMinimumSize(QtCore.QSize(100, 0))
        self.lbl_con_geoname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_con_geoname.setObjectName("lbl_con_geoname")
        self.lay_h_con_geo.addWidget(self.lbl_con_geoname)
        self.tbx_con_geoname = QtWidgets.QLineEdit(self.tab_con)
        self.tbx_con_geoname.setEnabled(False)
        self.tbx_con_geoname.setObjectName("tbx_con_geoname")
        self.lay_h_con_geo.addWidget(self.tbx_con_geoname)
        self.verticalLayout.addLayout(self.lay_h_con_geo)
        self.lay_h_con_tmp = QtWidgets.QHBoxLayout()
        self.lay_h_con_tmp.setContentsMargins(-1, 0, -1, -1)
        self.lay_h_con_tmp.setObjectName("lay_h_con_tmp")
        self.lbl_con_tempral = QtWidgets.QLabel(self.tab_con)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_con_tempral.sizePolicy().hasHeightForWidth())
        self.lbl_con_tempral.setSizePolicy(sizePolicy)
        self.lbl_con_tempral.setMinimumSize(QtCore.QSize(100, 0))
        self.lbl_con_tempral.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_con_tempral.setObjectName("lbl_con_tempral")
        self.lay_h_con_tmp.addWidget(self.lbl_con_tempral)
        self.tbx_con_temporal = QtWidgets.QLineEdit(self.tab_con)
        self.tbx_con_temporal.setEnabled(False)
        self.tbx_con_temporal.setObjectName("tbx_con_temporal")
        self.lay_h_con_tmp.addWidget(self.tbx_con_temporal)
        self.verticalLayout.addLayout(self.lay_h_con_tmp)
        self.lay_h_con_dsc = QtWidgets.QHBoxLayout()
        self.lay_h_con_dsc.setContentsMargins(-1, 0, -1, -1)
        self.lay_h_con_dsc.setObjectName("lay_h_con_dsc")
        self.lbl_con_description = QtWidgets.QLabel(self.tab_con)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_con_description.sizePolicy().hasHeightForWidth())
        self.lbl_con_description.setSizePolicy(sizePolicy)
        self.lbl_con_description.setMinimumSize(QtCore.QSize(100, 0))
        self.lbl_con_description.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_con_description.setObjectName("lbl_con_description")
        self.lay_h_con_dsc.addWidget(self.lbl_con_description)
        self.tbx_con_description = QtWidgets.QLineEdit(self.tab_con)
        self.tbx_con_description.setEnabled(False)
        self.tbx_con_description.setObjectName("tbx_con_description")
        self.lay_h_con_dsc.addWidget(self.tbx_con_description)
        self.verticalLayout.addLayout(self.lay_h_con_dsc)
        self.lay_h_con_ctrl = QtWidgets.QHBoxLayout()
        self.lay_h_con_ctrl.setContentsMargins(-1, 0, -1, -1)
        self.lay_h_con_ctrl.setObjectName("lay_h_con_ctrl")
        self.btn_con_add = QtWidgets.QPushButton(self.tab_con)
        self.btn_con_add.setObjectName("btn_con_add")
        self.lay_h_con_ctrl.addWidget(self.btn_con_add)
        self.btn_con_update = QtWidgets.QPushButton(self.tab_con)
        self.btn_con_update.setObjectName("btn_con_update")
        self.lay_h_con_ctrl.addWidget(self.btn_con_update)
        self.btn_con_take = QtWidgets.QPushButton(self.tab_con)
        self.btn_con_take.setObjectName("btn_con_take")
        self.lay_h_con_ctrl.addWidget(self.btn_con_take)
        self.btn_con_rec = QtWidgets.QPushButton(self.tab_con)
        self.btn_con_rec.setObjectName("btn_con_rec")
        self.lay_h_con_ctrl.addWidget(self.btn_con_rec)
        self.btn_con_del = QtWidgets.QPushButton(self.tab_con)
        self.btn_con_del.setObjectName("btn_con_del")
        self.lay_h_con_ctrl.addWidget(self.btn_con_del)
        self.verticalLayout.addLayout(self.lay_h_con_ctrl)
        self.lay_h_con_fls = QtWidgets.QHBoxLayout()
        self.lay_h_con_fls.setContentsMargins(-1, 0, -1, -1)
        self.lay_h_con_fls.setObjectName("lay_h_con_fls")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lst_con_fls = QtWidgets.QListWidget(self.tab_con)
        self.lst_con_fls.setObjectName("lst_con_fls")
        self.verticalLayout_5.addWidget(self.lst_con_fls)
        self.lay_h_con_fls.addLayout(self.verticalLayout_5)
        self.tabWidget = QtWidgets.QTabWidget(self.tab_con)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_mat_img_properties = QtWidgets.QWidget()
        self.tab_mat_img_properties.setObjectName("tab_mat_img_properties")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_mat_img_properties)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tre_con_fl = QtWidgets.QTreeWidget(self.tab_mat_img_properties)
        self.tre_con_fl.setObjectName("tre_con_fl")
        self.tre_con_fl.header().setDefaultSectionSize(100)
        self.verticalLayout_8.addWidget(self.tre_con_fl)
        self.tabWidget.addTab(self.tab_mat_img_properties, "")
        self.tab_con_img_preview = QtWidgets.QWidget()
        self.tab_con_img_preview.setObjectName("tab_con_img_preview")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_con_img_preview)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_con_img_preview = QtWidgets.QLabel(self.tab_con_img_preview)
        self.lbl_con_img_preview.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_con_img_preview.setObjectName("lbl_con_img_preview")
        self.horizontalLayout_4.addWidget(self.lbl_con_img_preview)
        self.tabWidget.addTab(self.tab_con_img_preview, "")
        self.lay_h_con_fls.addWidget(self.tabWidget)
        self.verticalLayout.addLayout(self.lay_h_con_fls)
        self.tab_target.addTab(self.tab_con, "")
        self.tab_mat = QtWidgets.QWidget()
        self.tab_mat.setObjectName("tab_mat")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_mat)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.rad_mat_new = QtWidgets.QRadioButton(self.tab_mat)
        self.rad_mat_new.setMinimumSize(QtCore.QSize(200, 0))
        self.rad_mat_new.setMaximumSize(QtCore.QSize(200, 16777215))
        self.rad_mat_new.setObjectName("rad_mat_new")
        self.horizontalLayout_5.addWidget(self.rad_mat_new)
        self.rad_mat_mod = QtWidgets.QRadioButton(self.tab_mat)
        self.rad_mat_mod.setObjectName("rad_mat_mod")
        self.horizontalLayout_5.addWidget(self.rad_mat_mod)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.lay_h_con_nam_3 = QtWidgets.QHBoxLayout()
        self.lay_h_con_nam_3.setContentsMargins(-1, 0, -1, -1)
        self.lay_h_con_nam_3.setObjectName("lay_h_con_nam_3")
        self.lbl_mat_name = QtWidgets.QLabel(self.tab_mat)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_mat_name.sizePolicy().hasHeightForWidth())
        self.lbl_mat_name.setSizePolicy(sizePolicy)
        self.lbl_mat_name.setMinimumSize(QtCore.QSize(100, 0))
        self.lbl_mat_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_mat_name.setObjectName("lbl_mat_name")
        self.lay_h_con_nam_3.addWidget(self.lbl_mat_name)
        self.tbx_mat_name = QtWidgets.QLineEdit(self.tab_mat)
        self.tbx_mat_name.setEnabled(False)
        self.tbx_mat_name.setObjectName("tbx_mat_name")
        self.lay_h_con_nam_3.addWidget(self.tbx_mat_name)
        self.verticalLayout_3.addLayout(self.lay_h_con_nam_3)
        self.lay_h_mat_geo = QtWidgets.QHBoxLayout()
        self.lay_h_mat_geo.setContentsMargins(-1, 0, -1, -1)
        self.lay_h_mat_geo.setObjectName("lay_h_mat_geo")
        self.lbl_mat_geoname = QtWidgets.QLabel(self.tab_mat)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_mat_geoname.sizePolicy().hasHeightForWidth())
        self.lbl_mat_geoname.setSizePolicy(sizePolicy)
        self.lbl_mat_geoname.setMinimumSize(QtCore.QSize(100, 0))
        self.lbl_mat_geoname.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lbl_mat_geoname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_mat_geoname.setObjectName("lbl_mat_geoname")
        self.lay_h_mat_geo.addWidget(self.lbl_mat_geoname)
        self.tbx_mat_geo_lat = QtWidgets.QLineEdit(self.tab_mat)
        self.tbx_mat_geo_lat.setEnabled(False)
        self.tbx_mat_geo_lat.setObjectName("tbx_mat_geo_lat")
        self.lay_h_mat_geo.addWidget(self.tbx_mat_geo_lat)
        self.label = QtWidgets.QLabel(self.tab_mat)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lay_h_mat_geo.addWidget(self.label)
        self.tbx_mat_geo_lon = QtWidgets.QLineEdit(self.tab_mat)
        self.tbx_mat_geo_lon.setEnabled(False)
        self.tbx_mat_geo_lon.setObjectName("tbx_mat_geo_lon")
        self.lay_h_mat_geo.addWidget(self.tbx_mat_geo_lon)
        self.label_2 = QtWidgets.QLabel(self.tab_mat)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lay_h_mat_geo.addWidget(self.label_2)
        self.tbx_mat_geo_alt = QtWidgets.QLineEdit(self.tab_mat)
        self.tbx_mat_geo_alt.setEnabled(False)
        self.tbx_mat_geo_alt.setObjectName("tbx_mat_geo_alt")
        self.lay_h_mat_geo.addWidget(self.tbx_mat_geo_alt)
        self.verticalLayout_3.addLayout(self.lay_h_mat_geo)
        self.lay_h_mat_tmp = QtWidgets.QHBoxLayout()
        self.lay_h_mat_tmp.setContentsMargins(-1, 0, -1, -1)
        self.lay_h_mat_tmp.setObjectName("lay_h_mat_tmp")
        self.lbl_mat_tmp_bgn = QtWidgets.QLabel(self.tab_mat)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_mat_tmp_bgn.sizePolicy().hasHeightForWidth())
        self.lbl_mat_tmp_bgn.setSizePolicy(sizePolicy)
        self.lbl_mat_tmp_bgn.setMinimumSize(QtCore.QSize(100, 0))
        self.lbl_mat_tmp_bgn.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_mat_tmp_bgn.setObjectName("lbl_mat_tmp_bgn")
        self.lay_h_mat_tmp.addWidget(self.lbl_mat_tmp_bgn)
        self.tbx_mat_tmp_bgn = QtWidgets.QLineEdit(self.tab_mat)
        self.tbx_mat_tmp_bgn.setEnabled(False)
        self.tbx_mat_tmp_bgn.setObjectName("tbx_mat_tmp_bgn")
        self.lay_h_mat_tmp.addWidget(self.tbx_mat_tmp_bgn)
        self.lbl_mat_tmp_end = QtWidgets.QLabel(self.tab_mat)
        self.lbl_mat_tmp_end.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_mat_tmp_end.setObjectName("lbl_mat_tmp_end")
        self.lay_h_mat_tmp.addWidget(self.lbl_mat_tmp_end)
        self.tbx_mat_tmp_end = QtWidgets.QLineEdit(self.tab_mat)
        self.tbx_mat_tmp_end.setEnabled(False)
        self.tbx_mat_tmp_end.setObjectName("tbx_mat_tmp_end")
        self.lay_h_mat_tmp.addWidget(self.tbx_mat_tmp_end)
        self.verticalLayout_3.addLayout(self.lay_h_mat_tmp)
        self.lay_h_mat_dsc = QtWidgets.QHBoxLayout()
        self.lay_h_mat_dsc.setContentsMargins(-1, 0, -1, -1)
        self.lay_h_mat_dsc.setObjectName("lay_h_mat_dsc")
        self.lbl_mat_description = QtWidgets.QLabel(self.tab_mat)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_mat_description.sizePolicy().hasHeightForWidth())
        self.lbl_mat_description.setSizePolicy(sizePolicy)
        self.lbl_mat_description.setMinimumSize(QtCore.QSize(100, 0))
        self.lbl_mat_description.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_mat_description.setObjectName("lbl_mat_description")
        self.lay_h_mat_dsc.addWidget(self.lbl_mat_description)
        self.tbx_mat_description = QtWidgets.QLineEdit(self.tab_mat)
        self.tbx_mat_description.setEnabled(False)
        self.tbx_mat_description.setObjectName("tbx_mat_description")
        self.lay_h_mat_dsc.addWidget(self.tbx_mat_description)
        self.verticalLayout_3.addLayout(self.lay_h_mat_dsc)
        self.lay_h_mat_ctrl = QtWidgets.QHBoxLayout()
        self.lay_h_mat_ctrl.setContentsMargins(-1, 0, -1, -1)
        self.lay_h_mat_ctrl.setObjectName("lay_h_mat_ctrl")
        self.btn_mat_add = QtWidgets.QPushButton(self.tab_mat)
        self.btn_mat_add.setObjectName("btn_mat_add")
        self.lay_h_mat_ctrl.addWidget(self.btn_mat_add)
        self.btn_mat_update = QtWidgets.QPushButton(self.tab_mat)
        self.btn_mat_update.setObjectName("btn_mat_update")
        self.lay_h_mat_ctrl.addWidget(self.btn_mat_update)
        self.btn_mat_take = QtWidgets.QPushButton(self.tab_mat)
        self.btn_mat_take.setObjectName("btn_mat_take")
        self.lay_h_mat_ctrl.addWidget(self.btn_mat_take)
        self.btn_mat_rec = QtWidgets.QPushButton(self.tab_mat)
        self.btn_mat_rec.setObjectName("btn_mat_rec")
        self.lay_h_mat_ctrl.addWidget(self.btn_mat_rec)
        self.btn_mat_del = QtWidgets.QPushButton(self.tab_mat)
        self.btn_mat_del.setObjectName("btn_mat_del")
        self.lay_h_mat_ctrl.addWidget(self.btn_mat_del)
        self.verticalLayout_3.addLayout(self.lay_h_mat_ctrl)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lst_mat_fls = QtWidgets.QListWidget(self.tab_mat)
        self.lst_mat_fls.setObjectName("lst_mat_fls")
        self.verticalLayout_4.addWidget(self.lst_mat_fls)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.tab_img_info = QtWidgets.QTabWidget(self.tab_mat)
        self.tab_img_info.setObjectName("tab_img_info")
        self.tab_mat_img_properties1 = QtWidgets.QWidget()
        self.tab_mat_img_properties1.setObjectName("tab_mat_img_properties1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_mat_img_properties1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tre_mat_fl = QtWidgets.QTreeWidget(self.tab_mat_img_properties1)
        self.tre_mat_fl.setObjectName("tre_mat_fl")
        self.tre_mat_fl.header().setDefaultSectionSize(100)
        self.horizontalLayout_3.addWidget(self.tre_mat_fl)
        self.tab_img_info.addTab(self.tab_mat_img_properties1, "")
        self.tab_mat_img_preview = QtWidgets.QWidget()
        self.tab_mat_img_preview.setObjectName("tab_mat_img_preview")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_mat_img_preview)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbl_mat_img_preview = QtWidgets.QLabel(self.tab_mat_img_preview)
        self.lbl_mat_img_preview.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_mat_img_preview.setObjectName("lbl_mat_img_preview")
        self.verticalLayout_6.addWidget(self.lbl_mat_img_preview)
        self.tab_img_info.addTab(self.tab_mat_img_preview, "")
        self.horizontalLayout_2.addWidget(self.tab_img_info)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tab_target.addTab(self.tab_mat, "")
        self.lay_v_item_info.addWidget(self.tab_target)
        self.horizontalLayout.addLayout(self.lay_v_item_info)
        MainWindow.setCentralWidget(self.centralwidget)
        self.bar_menu = QtWidgets.QMenuBar(MainWindow)
        self.bar_menu.setGeometry(QtCore.QRect(0, 0, 1124, 28))
        self.bar_menu.setObjectName("bar_menu")
        self.men_prj = QtWidgets.QMenu(self.bar_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.men_prj.sizePolicy().hasHeightForWidth())
        self.men_prj.setSizePolicy(sizePolicy)
        self.men_prj.setMinimumSize(QtCore.QSize(0, 0))
        self.men_prj.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.men_prj.setObjectName("men_prj")
        MainWindow.setMenuBar(self.bar_menu)
        self.actionCreate_New_Project = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_Project.setObjectName("actionCreate_New_Project")
        self.actionOpen_Project = QtWidgets.QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.act_prj_open = QtWidgets.QAction(MainWindow)
        self.act_prj_open.setIconVisibleInMenu(True)
        self.act_prj_open.setObjectName("act_prj_open")
        self.men_prj.addAction(self.act_prj_open)
        self.bar_menu.addAction(self.men_prj.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_control.setCurrentIndex(0)
        self.tab_target.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.tab_img_info.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "メイン画面"))
        self.lbl_prjDir.setText(_translate("MainWindow", "プロジェクト : "))
        self.tre_prj_item.headerItem().setText(0, _translate("MainWindow", "統合体ID"))
        self.tre_prj_item.headerItem().setText(1, _translate("MainWindow", "統合体名"))
        self.tre_prj_item.headerItem().setText(2, _translate("MainWindow", "備考"))
        self.tab_control.setTabText(self.tab_control.indexOf(self.tab_prj_item), _translate("MainWindow", "アイテム"))
        self.lbl_cam_detected.setText(_translate("MainWindow", "接続中のカメラ: No Camera detected"))
        self.btn_cam_detect.setText(_translate("MainWindow", "カメラの認識"))
        self.grp_cam.setTitle(_translate("MainWindow", "撮影モード"))
        self.lbl_cam_qoi.setText(_translate("MainWindow", "Image Quality"))
        self.lbl_cam_fmod.setText(_translate("MainWindow", "Focus Mode"))
        self.lbl_cam_epg.setText(_translate("MainWindow", "Exposure Program"))
        self.lbl_cam_size.setText(_translate("MainWindow", "Image Size"))
        self.lbl_cam_iso.setText(_translate("MainWindow", "ISO Speed Rating"))
        self.lbl_cam_cpt.setText(_translate("MainWindow", "Capture Mode"))
        self.lbl_cam_fval.setText(_translate("MainWindow", "F-Number"))
        self.lbl_cam_wht.setText(_translate("MainWindow", "White Balance"))
        self.lbl_cam_exp.setText(_translate("MainWindow", "Exposure Compensation"))
        self.lbl_cam_met.setText(_translate("MainWindow", "Metering Mode"))
        self.tab_control.setTabText(self.tab_control.indexOf(self.tab_prj_cam), _translate("MainWindow", "カメラ"))
        self.rad_con_new.setText(_translate("MainWindow", "新規作成"))
        self.rad_con_mod.setText(_translate("MainWindow", "情報更新"))
        self.lbl_con_name.setText(_translate("MainWindow", "統合体の名称"))
        self.lbl_con_geoname.setText(_translate("MainWindow", "地理識別子"))
        self.lbl_con_tempral.setText(_translate("MainWindow", "時間識別子"))
        self.lbl_con_description.setText(_translate("MainWindow", "統合体の備考"))
        self.btn_con_add.setText(_translate("MainWindow", "統合体の追加"))
        self.btn_con_update.setText(_translate("MainWindow", "統合体の更新"))
        self.btn_con_take.setText(_translate("MainWindow", "撮影する"))
        self.btn_con_rec.setText(_translate("MainWindow", "録音する"))
        self.btn_con_del.setText(_translate("MainWindow", "統合体の削除"))
        self.lst_con_fls.setSortingEnabled(True)
        self.tre_con_fl.headerItem().setText(0, _translate("MainWindow", "プロパティ"))
        self.tre_con_fl.headerItem().setText(1, _translate("MainWindow", "値"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mat_img_properties), _translate("MainWindow", "プロパティ"))
        self.lbl_con_img_preview.setText(_translate("MainWindow", "プレビュー"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_con_img_preview), _translate("MainWindow", "プレビュー"))
        self.tab_target.setTabText(self.tab_target.indexOf(self.tab_con), _translate("MainWindow", "統合体情報"))
        self.rad_mat_new.setText(_translate("MainWindow", "新規作成"))
        self.rad_mat_mod.setText(_translate("MainWindow", "情報更新"))
        self.lbl_mat_name.setText(_translate("MainWindow", "資料の名称"))
        self.lbl_mat_geoname.setText(_translate("MainWindow", "緯度"))
        self.label.setText(_translate("MainWindow", "経度"))
        self.label_2.setText(_translate("MainWindow", "標高"))
        self.lbl_mat_tmp_bgn.setText(_translate("MainWindow", "開始時期"))
        self.lbl_mat_tmp_end.setText(_translate("MainWindow", "終了時期"))
        self.lbl_mat_description.setText(_translate("MainWindow", "資料の備考"))
        self.btn_mat_add.setText(_translate("MainWindow", "資料の追加"))
        self.btn_mat_update.setText(_translate("MainWindow", "資料の更新"))
        self.btn_mat_take.setText(_translate("MainWindow", "撮影する"))
        self.btn_mat_rec.setText(_translate("MainWindow", "録音する"))
        self.btn_mat_del.setText(_translate("MainWindow", "資料の削除"))
        self.lst_mat_fls.setSortingEnabled(True)
        self.tre_mat_fl.headerItem().setText(0, _translate("MainWindow", "プロパティ"))
        self.tre_mat_fl.headerItem().setText(1, _translate("MainWindow", "値"))
        self.tab_img_info.setTabText(self.tab_img_info.indexOf(self.tab_mat_img_properties1), _translate("MainWindow", "プロパティ"))
        self.lbl_mat_img_preview.setText(_translate("MainWindow", "preview"))
        self.tab_img_info.setTabText(self.tab_img_info.indexOf(self.tab_mat_img_preview), _translate("MainWindow", "プレビュー"))
        self.tab_target.setTabText(self.tab_target.indexOf(self.tab_mat), _translate("MainWindow", "資料情報"))
        self.men_prj.setTitle(_translate("MainWindow", "プロジェクト"))
        self.actionCreate_New_Project.setText(_translate("MainWindow", "Create New Project"))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project"))
        self.act_prj_open.setText(_translate("MainWindow", "開く"))
        self.act_prj_open.setShortcut(_translate("MainWindow", "Ctrl+O"))

