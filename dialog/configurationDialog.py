# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yufujimoto/GitHub/SurveyDataCollector/ui/configuration.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_configurationDialog(object):
    def setupUi(self, configurationDialog):
        configurationDialog.setObjectName("configurationDialog")
        configurationDialog.resize(761, 542)
        configurationDialog.setMaximumSize(QtCore.QSize(16777215, 542))
        self.gridLayout = QtWidgets.QGridLayout(configurationDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.frm_conf_main = QtWidgets.QFrame(configurationDialog)
        self.frm_conf_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_conf_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_conf_main.setObjectName("frm_conf_main")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frm_conf_main)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tab_conf_main = QtWidgets.QTabWidget(self.frm_conf_main)
        self.tab_conf_main.setObjectName("tab_conf_main")
        self.tab_general = QtWidgets.QWidget()
        self.tab_general.setObjectName("tab_general")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_general)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gbx_general = QtWidgets.QGroupBox(self.tab_general)
        self.gbx_general.setObjectName("gbx_general")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.gbx_general)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.hlay_theme_lang = QtWidgets.QHBoxLayout()
        self.hlay_theme_lang.setObjectName("hlay_theme_lang")
        self.lbl_lang = QtWidgets.QLabel(self.gbx_general)
        self.lbl_lang.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_lang.setMaximumSize(QtCore.QSize(150, 30))
        self.lbl_lang.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_lang.setObjectName("lbl_lang")
        self.hlay_theme_lang.addWidget(self.lbl_lang)
        self.cbx_lang = QtWidgets.QComboBox(self.gbx_general)
        self.cbx_lang.setObjectName("cbx_lang")
        self.cbx_lang.addItem("")
        self.cbx_lang.addItem("")
        self.hlay_theme_lang.addWidget(self.cbx_lang)
        self.verticalLayout_5.addLayout(self.hlay_theme_lang)
        self.hlay_theme_skin = QtWidgets.QHBoxLayout()
        self.hlay_theme_skin.setObjectName("hlay_theme_skin")
        self.lbl_skin = QtWidgets.QLabel(self.gbx_general)
        self.lbl_skin.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_skin.setMaximumSize(QtCore.QSize(150, 30))
        self.lbl_skin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_skin.setObjectName("lbl_skin")
        self.hlay_theme_skin.addWidget(self.lbl_skin)
        self.cbx_skin = QtWidgets.QComboBox(self.gbx_general)
        self.cbx_skin.setObjectName("cbx_skin")
        self.cbx_skin.addItem("")
        self.cbx_skin.addItem("")
        self.hlay_theme_skin.addWidget(self.cbx_skin)
        self.verticalLayout_5.addLayout(self.hlay_theme_skin)
        self.verticalLayout.addWidget(self.gbx_general)
        self.gbx_tool = QtWidgets.QGroupBox(self.tab_general)
        self.gbx_tool.setObjectName("gbx_tool")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.gbx_tool)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.hlay_tool_awb = QtWidgets.QHBoxLayout()
        self.hlay_tool_awb.setObjectName("hlay_tool_awb")
        self.lbl_tool_awb = QtWidgets.QLabel(self.gbx_tool)
        self.lbl_tool_awb.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_tool_awb.setMaximumSize(QtCore.QSize(150, 30))
        self.lbl_tool_awb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_tool_awb.setObjectName("lbl_tool_awb")
        self.hlay_tool_awb.addWidget(self.lbl_tool_awb)
        self.cbx_tool_awb = QtWidgets.QComboBox(self.gbx_tool)
        self.cbx_tool_awb.setObjectName("cbx_tool_awb")
        self.cbx_tool_awb.addItem("")
        self.cbx_tool_awb.addItem("")
        self.cbx_tool_awb.addItem("")
        self.cbx_tool_awb.addItem("")
        self.cbx_tool_awb.addItem("")
        self.cbx_tool_awb.addItem("")
        self.cbx_tool_awb.addItem("")
        self.cbx_tool_awb.addItem("")
        self.cbx_tool_awb.addItem("")
        self.hlay_tool_awb.addWidget(self.cbx_tool_awb)
        self.verticalLayout_10.addLayout(self.hlay_tool_awb)
        self.hlay_tool_psp = QtWidgets.QHBoxLayout()
        self.hlay_tool_psp.setObjectName("hlay_tool_psp")
        self.lbl_tool_psp = QtWidgets.QLabel(self.gbx_tool)
        self.lbl_tool_psp.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_tool_psp.setMaximumSize(QtCore.QSize(150, 30))
        self.lbl_tool_psp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_tool_psp.setObjectName("lbl_tool_psp")
        self.hlay_tool_psp.addWidget(self.lbl_tool_psp)
        self.cbx_tool_psp = QtWidgets.QComboBox(self.gbx_tool)
        self.cbx_tool_psp.setObjectName("cbx_tool_psp")
        self.cbx_tool_psp.addItem("")
        self.cbx_tool_psp.addItem("")
        self.cbx_tool_psp.addItem("")
        self.hlay_tool_psp.addWidget(self.cbx_tool_psp)
        self.verticalLayout_10.addLayout(self.hlay_tool_psp)
        self.verticalLayout.addWidget(self.gbx_tool)
        self.gbx_flickr = QtWidgets.QGroupBox(self.tab_general)
        self.gbx_flickr.setObjectName("gbx_flickr")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.gbx_flickr)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.hlay_flc_api = QtWidgets.QHBoxLayout()
        self.hlay_flc_api.setObjectName("hlay_flc_api")
        self.lbl_flc_api = QtWidgets.QLabel(self.gbx_flickr)
        self.lbl_flc_api.setMinimumSize(QtCore.QSize(150, 30))
        self.lbl_flc_api.setMaximumSize(QtCore.QSize(150, 30))
        self.lbl_flc_api.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_flc_api.setObjectName("lbl_flc_api")
        self.hlay_flc_api.addWidget(self.lbl_flc_api)
        self.txt_flc_api = QtWidgets.QLineEdit(self.gbx_flickr)
        self.txt_flc_api.setObjectName("txt_flc_api")
        self.hlay_flc_api.addWidget(self.txt_flc_api)
        self.verticalLayout_4.addLayout(self.hlay_flc_api)
        self.hlay_flc_sec = QtWidgets.QHBoxLayout()
        self.hlay_flc_sec.setObjectName("hlay_flc_sec")
        self.lbl_flc_sec = QtWidgets.QLabel(self.gbx_flickr)
        self.lbl_flc_sec.setMinimumSize(QtCore.QSize(150, 30))
        self.lbl_flc_sec.setMaximumSize(QtCore.QSize(150, 30))
        self.lbl_flc_sec.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_flc_sec.setObjectName("lbl_flc_sec")
        self.hlay_flc_sec.addWidget(self.lbl_flc_sec)
        self.txt_flc_sec = QtWidgets.QLineEdit(self.gbx_flickr)
        self.txt_flc_sec.setObjectName("txt_flc_sec")
        self.hlay_flc_sec.addWidget(self.txt_flc_sec)
        self.verticalLayout_4.addLayout(self.hlay_flc_sec)
        self.verticalLayout.addWidget(self.gbx_flickr)
        self.tab_conf_main.addTab(self.tab_general, "")
        self.tab_geoinfo = QtWidgets.QWidget()
        self.tab_geoinfo.setObjectName("tab_geoinfo")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_geoinfo)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gbx_geospatial = QtWidgets.QGroupBox(self.tab_geoinfo)
        self.gbx_geospatial.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gbx_geospatial.setObjectName("gbx_geospatial")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gbx_geospatial)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_map_tile = QtWidgets.QLabel(self.gbx_geospatial)
        self.lbl_map_tile.setMaximumSize(QtCore.QSize(150, 30))
        self.lbl_map_tile.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_map_tile.setObjectName("lbl_map_tile")
        self.horizontalLayout.addWidget(self.lbl_map_tile)
        self.cbx_map_tile = QtWidgets.QComboBox(self.gbx_geospatial)
        self.cbx_map_tile.setObjectName("cbx_map_tile")
        self.cbx_map_tile.addItem("")
        self.cbx_map_tile.addItem("")
        self.cbx_map_tile.addItem("")
        self.cbx_map_tile.addItem("")
        self.cbx_map_tile.addItem("")
        self.cbx_map_tile.addItem("")
        self.horizontalLayout.addWidget(self.cbx_map_tile)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addWidget(self.gbx_geospatial)
        self.tab_conf_main.addTab(self.tab_geoinfo, "")
        self.tab_network = QtWidgets.QWidget()
        self.tab_network.setObjectName("tab_network")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_network)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.rbtn_no_proxy = QtWidgets.QRadioButton(self.tab_network)
        self.rbtn_no_proxy.setMinimumSize(QtCore.QSize(100, 0))
        self.rbtn_no_proxy.setChecked(True)
        self.rbtn_no_proxy.setObjectName("rbtn_no_proxy")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rbtn_no_proxy)
        self.rbtn_proxy = QtWidgets.QRadioButton(self.tab_network)
        self.rbtn_proxy.setMinimumSize(QtCore.QSize(100, 0))
        self.rbtn_proxy.setObjectName("rbtn_proxy")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rbtn_proxy)
        self.lbl_proxy = QtWidgets.QLabel(self.tab_network)
        self.lbl_proxy.setMinimumSize(QtCore.QSize(100, 30))
        self.lbl_proxy.setMaximumSize(QtCore.QSize(100, 30))
        self.lbl_proxy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_proxy.setObjectName("lbl_proxy")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_proxy)
        self.txt_proxy = QtWidgets.QLineEdit(self.tab_network)
        self.txt_proxy.setObjectName("txt_proxy")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_proxy)
        self.verticalLayout_11.addLayout(self.formLayout_2)
        self.tab_conf_main.addTab(self.tab_network, "")
        self.tab_camera = QtWidgets.QWidget()
        self.tab_camera.setObjectName("tab_camera")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_camera)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frm_cam_list = QtWidgets.QFrame(self.tab_camera)
        self.frm_cam_list.setMinimumSize(QtCore.QSize(300, 0))
        self.frm_cam_list.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frm_cam_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_cam_list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_cam_list.setObjectName("frm_cam_list")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frm_cam_list)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lst_cam = QtWidgets.QListWidget(self.frm_cam_list)
        self.lst_cam.setObjectName("lst_cam")
        self.verticalLayout_9.addWidget(self.lst_cam)
        self.btn_cam_conn = QtWidgets.QPushButton(self.frm_cam_list)
        self.btn_cam_conn.setObjectName("btn_cam_conn")
        self.verticalLayout_9.addWidget(self.btn_cam_conn)
        self.horizontalLayout_8.addWidget(self.frm_cam_list)
        self.frm_cam_param = QtWidgets.QFrame(self.tab_camera)
        self.frm_cam_param.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_cam_param.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_cam_param.setObjectName("frm_cam_param")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frm_cam_param)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.hlay_cam_size = QtWidgets.QHBoxLayout()
        self.hlay_cam_size.setObjectName("hlay_cam_size")
        self.lbl_cam_size = QtWidgets.QLabel(self.frm_cam_param)
        self.lbl_cam_size.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lbl_cam_size.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_cam_size.setObjectName("lbl_cam_size")
        self.hlay_cam_size.addWidget(self.lbl_cam_size)
        self.cbx_cam_size = QtWidgets.QComboBox(self.frm_cam_param)
        self.cbx_cam_size.setObjectName("cbx_cam_size")
        self.hlay_cam_size.addWidget(self.cbx_cam_size)
        self.verticalLayout_8.addLayout(self.hlay_cam_size)
        self.hlay_cam_iso = QtWidgets.QHBoxLayout()
        self.hlay_cam_iso.setObjectName("hlay_cam_iso")
        self.lbl_cam_iso = QtWidgets.QLabel(self.frm_cam_param)
        self.lbl_cam_iso.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lbl_cam_iso.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_cam_iso.setObjectName("lbl_cam_iso")
        self.hlay_cam_iso.addWidget(self.lbl_cam_iso)
        self.cbx_cam_iso = QtWidgets.QComboBox(self.frm_cam_param)
        self.cbx_cam_iso.setObjectName("cbx_cam_iso")
        self.hlay_cam_iso.addWidget(self.cbx_cam_iso)
        self.verticalLayout_8.addLayout(self.hlay_cam_iso)
        self.hlay_cam_wht = QtWidgets.QHBoxLayout()
        self.hlay_cam_wht.setObjectName("hlay_cam_wht")
        self.lbl_cam_wht = QtWidgets.QLabel(self.frm_cam_param)
        self.lbl_cam_wht.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lbl_cam_wht.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_cam_wht.setObjectName("lbl_cam_wht")
        self.hlay_cam_wht.addWidget(self.lbl_cam_wht)
        self.cbx_cam_wht = QtWidgets.QComboBox(self.frm_cam_param)
        self.cbx_cam_wht.setObjectName("cbx_cam_wht")
        self.hlay_cam_wht.addWidget(self.cbx_cam_wht)
        self.verticalLayout_8.addLayout(self.hlay_cam_wht)
        self.hlay_cam_exp = QtWidgets.QHBoxLayout()
        self.hlay_cam_exp.setObjectName("hlay_cam_exp")
        self.lbl_cam_exp = QtWidgets.QLabel(self.frm_cam_param)
        self.lbl_cam_exp.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lbl_cam_exp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_cam_exp.setObjectName("lbl_cam_exp")
        self.hlay_cam_exp.addWidget(self.lbl_cam_exp)
        self.cbx_cam_exp = QtWidgets.QComboBox(self.frm_cam_param)
        self.cbx_cam_exp.setObjectName("cbx_cam_exp")
        self.hlay_cam_exp.addWidget(self.cbx_cam_exp)
        self.verticalLayout_8.addLayout(self.hlay_cam_exp)
        self.hlay_cam_fnum = QtWidgets.QHBoxLayout()
        self.hlay_cam_fnum.setObjectName("hlay_cam_fnum")
        self.lbl_cam_fval = QtWidgets.QLabel(self.frm_cam_param)
        self.lbl_cam_fval.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lbl_cam_fval.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_cam_fval.setObjectName("lbl_cam_fval")
        self.hlay_cam_fnum.addWidget(self.lbl_cam_fval)
        self.cbx_cam_fval = QtWidgets.QComboBox(self.frm_cam_param)
        self.cbx_cam_fval.setObjectName("cbx_cam_fval")
        self.hlay_cam_fnum.addWidget(self.cbx_cam_fval)
        self.verticalLayout_8.addLayout(self.hlay_cam_fnum)
        self.hlay_cam_qoi = QtWidgets.QHBoxLayout()
        self.hlay_cam_qoi.setObjectName("hlay_cam_qoi")
        self.lbl_cam_qoi = QtWidgets.QLabel(self.frm_cam_param)
        self.lbl_cam_qoi.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lbl_cam_qoi.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_cam_qoi.setObjectName("lbl_cam_qoi")
        self.hlay_cam_qoi.addWidget(self.lbl_cam_qoi)
        self.cbx_cam_qoi = QtWidgets.QComboBox(self.frm_cam_param)
        self.cbx_cam_qoi.setObjectName("cbx_cam_qoi")
        self.hlay_cam_qoi.addWidget(self.cbx_cam_qoi)
        self.verticalLayout_8.addLayout(self.hlay_cam_qoi)
        self.hlay_cam_fmod = QtWidgets.QHBoxLayout()
        self.hlay_cam_fmod.setObjectName("hlay_cam_fmod")
        self.lbl_cam_fmod = QtWidgets.QLabel(self.frm_cam_param)
        self.lbl_cam_fmod.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lbl_cam_fmod.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_cam_fmod.setObjectName("lbl_cam_fmod")
        self.hlay_cam_fmod.addWidget(self.lbl_cam_fmod)
        self.cbx_cam_fmod = QtWidgets.QComboBox(self.frm_cam_param)
        self.cbx_cam_fmod.setObjectName("cbx_cam_fmod")
        self.hlay_cam_fmod.addWidget(self.cbx_cam_fmod)
        self.verticalLayout_8.addLayout(self.hlay_cam_fmod)
        self.hlay_cam_epg = QtWidgets.QHBoxLayout()
        self.hlay_cam_epg.setObjectName("hlay_cam_epg")
        self.lbl_cam_epg = QtWidgets.QLabel(self.frm_cam_param)
        self.lbl_cam_epg.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lbl_cam_epg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_cam_epg.setObjectName("lbl_cam_epg")
        self.hlay_cam_epg.addWidget(self.lbl_cam_epg)
        self.cbx_cam_epg = QtWidgets.QComboBox(self.frm_cam_param)
        self.cbx_cam_epg.setObjectName("cbx_cam_epg")
        self.hlay_cam_epg.addWidget(self.cbx_cam_epg)
        self.verticalLayout_8.addLayout(self.hlay_cam_epg)
        self.hlay_cam_cpt = QtWidgets.QHBoxLayout()
        self.hlay_cam_cpt.setObjectName("hlay_cam_cpt")
        self.lbl_cam_cpt = QtWidgets.QLabel(self.frm_cam_param)
        self.lbl_cam_cpt.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lbl_cam_cpt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_cam_cpt.setObjectName("lbl_cam_cpt")
        self.hlay_cam_cpt.addWidget(self.lbl_cam_cpt)
        self.cbx_cam_cpt = QtWidgets.QComboBox(self.frm_cam_param)
        self.cbx_cam_cpt.setObjectName("cbx_cam_cpt")
        self.hlay_cam_cpt.addWidget(self.cbx_cam_cpt)
        self.verticalLayout_8.addLayout(self.hlay_cam_cpt)
        self.hlay_cam_met = QtWidgets.QHBoxLayout()
        self.hlay_cam_met.setObjectName("hlay_cam_met")
        self.lbl_cam_met = QtWidgets.QLabel(self.frm_cam_param)
        self.lbl_cam_met.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lbl_cam_met.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_cam_met.setObjectName("lbl_cam_met")
        self.hlay_cam_met.addWidget(self.lbl_cam_met)
        self.cbx_cam_met = QtWidgets.QComboBox(self.frm_cam_param)
        self.cbx_cam_met.setObjectName("cbx_cam_met")
        self.hlay_cam_met.addWidget(self.cbx_cam_met)
        self.verticalLayout_8.addLayout(self.hlay_cam_met)
        self.horizontalLayout_8.addWidget(self.frm_cam_param)
        self.tab_conf_main.addTab(self.tab_camera, "")
        self.verticalLayout_6.addWidget(self.tab_conf_main)
        self.gridLayout.addWidget(self.frm_conf_main, 0, 1, 1, 1)
        self.frm_conf_btns = QtWidgets.QFrame(configurationDialog)
        self.frm_conf_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_conf_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_conf_btns.setObjectName("frm_conf_btns")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frm_conf_btns)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.bbx_conf_res = QtWidgets.QDialogButtonBox(self.frm_conf_btns)
        self.bbx_conf_res.setOrientation(QtCore.Qt.Horizontal)
        self.bbx_conf_res.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.bbx_conf_res.setObjectName("bbx_conf_res")
        self.verticalLayout_7.addWidget(self.bbx_conf_res)
        self.gridLayout.addWidget(self.frm_conf_btns, 1, 1, 1, 1)

        self.retranslateUi(configurationDialog)
        self.tab_conf_main.setCurrentIndex(0)
        self.bbx_conf_res.accepted.connect(configurationDialog.accept)
        self.bbx_conf_res.rejected.connect(configurationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(configurationDialog)

    def retranslateUi(self, configurationDialog):
        _translate = QtCore.QCoreApplication.translate
        configurationDialog.setWindowTitle(_translate("configurationDialog", "Dialog"))
        self.gbx_general.setTitle(_translate("configurationDialog", "テーマの設定"))
        self.lbl_lang.setText(_translate("configurationDialog", "言語の設定 : "))
        self.cbx_lang.setItemText(0, _translate("configurationDialog", "日本語"))
        self.cbx_lang.setItemText(1, _translate("configurationDialog", "English"))
        self.lbl_skin.setText(_translate("configurationDialog", "色の設定 : "))
        self.cbx_skin.setItemText(0, _translate("configurationDialog", "Grey"))
        self.cbx_skin.setItemText(1, _translate("configurationDialog", "White"))
        self.gbx_tool.setTitle(_translate("configurationDialog", "ツールの設定"))
        self.lbl_tool_awb.setText(_translate("configurationDialog", "ホワイトバランス : "))
        self.cbx_tool_awb.setItemText(0, _translate("configurationDialog", "retinex_adjusted"))
        self.cbx_tool_awb.setItemText(1, _translate("configurationDialog", "stretch"))
        self.cbx_tool_awb.setItemText(2, _translate("configurationDialog", "gray_world"))
        self.cbx_tool_awb.setItemText(3, _translate("configurationDialog", "max_white"))
        self.cbx_tool_awb.setItemText(4, _translate("configurationDialog", "retinex"))
        self.cbx_tool_awb.setItemText(5, _translate("configurationDialog", "stdev_luminance"))
        self.cbx_tool_awb.setItemText(6, _translate("configurationDialog", "stdev_grey_world"))
        self.cbx_tool_awb.setItemText(7, _translate("configurationDialog", "luminance_weighted"))
        self.cbx_tool_awb.setItemText(8, _translate("configurationDialog", "automatic"))
        self.lbl_tool_psp.setText(_translate("configurationDialog", "パンシャープン : "))
        self.cbx_tool_psp.setItemText(0, _translate("configurationDialog", "ihsConvert"))
        self.cbx_tool_psp.setItemText(1, _translate("configurationDialog", "simpleMeanConvert"))
        self.cbx_tool_psp.setItemText(2, _translate("configurationDialog", "broveyConvert"))
        self.gbx_flickr.setTitle(_translate("configurationDialog", "flickrの設定"))
        self.lbl_flc_api.setText(_translate("configurationDialog", "API KEY : "))
        self.lbl_flc_sec.setText(_translate("configurationDialog", "Secret : "))
        self.tab_conf_main.setTabText(self.tab_conf_main.indexOf(self.tab_general), _translate("configurationDialog", "一般"))
        self.gbx_geospatial.setTitle(_translate("configurationDialog", "地理情報"))
        self.lbl_map_tile.setText(_translate("configurationDialog", "マップタイル："))
        self.cbx_map_tile.setItemText(0, _translate("configurationDialog", "OpenStreetMap"))
        self.cbx_map_tile.setItemText(1, _translate("configurationDialog", "Google Streets"))
        self.cbx_map_tile.setItemText(2, _translate("configurationDialog", "Google Hybrid"))
        self.cbx_map_tile.setItemText(3, _translate("configurationDialog", "Google Satellite"))
        self.cbx_map_tile.setItemText(4, _translate("configurationDialog", "Google Terrain"))
        self.cbx_map_tile.setItemText(5, _translate("configurationDialog", "地理院タイル"))
        self.tab_conf_main.setTabText(self.tab_conf_main.indexOf(self.tab_geoinfo), _translate("configurationDialog", "地理情報"))
        self.rbtn_no_proxy.setText(_translate("configurationDialog", "NO PRO&XY"))
        self.rbtn_proxy.setText(_translate("configurationDialog", "HTTP PROX&Y"))
        self.lbl_proxy.setText(_translate("configurationDialog", "Proxy: "))
        self.tab_conf_main.setTabText(self.tab_conf_main.indexOf(self.tab_network), _translate("configurationDialog", "ネットワーク"))
        self.btn_cam_conn.setText(_translate("configurationDialog", "接続"))
        self.lbl_cam_size.setText(_translate("configurationDialog", "<html><head/><body><p>Image Size</p></body></html>"))
        self.lbl_cam_iso.setText(_translate("configurationDialog", "ISO Speed Rating"))
        self.lbl_cam_wht.setText(_translate("configurationDialog", "White Balance"))
        self.lbl_cam_exp.setText(_translate("configurationDialog", "Exposure Compensation"))
        self.lbl_cam_fval.setText(_translate("configurationDialog", "F-Number"))
        self.lbl_cam_qoi.setText(_translate("configurationDialog", "Image Quality"))
        self.lbl_cam_fmod.setText(_translate("configurationDialog", "Focus Mode"))
        self.lbl_cam_epg.setText(_translate("configurationDialog", "Exposure Program"))
        self.lbl_cam_cpt.setText(_translate("configurationDialog", "Capture Mode"))
        self.lbl_cam_met.setText(_translate("configurationDialog", "Metering Mode"))
        self.tab_conf_main.setTabText(self.tab_conf_main.indexOf(self.tab_camera), _translate("configurationDialog", "カメラ接続"))

