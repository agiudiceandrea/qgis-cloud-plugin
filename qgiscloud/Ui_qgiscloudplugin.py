# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hdus/dev/qgis/qgis-cloud-plugin/qgiscloud/qgiscloudplugin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_QgisCloudPlugin(object):
    def setupUi(self, QgisCloudPlugin):
        QgisCloudPlugin.setObjectName(_fromUtf8("QgisCloudPlugin"))
        QgisCloudPlugin.resize(500, 646)
        QgisCloudPlugin.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.mapTab = QtGui.QWidget()
        self.mapTab.setObjectName(_fromUtf8("mapTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.mapTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 7, 1, 1, 1)
        self.line_3 = QtGui.QFrame(self.mapTab)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_4.addWidget(self.line_3, 5, 0, 1, 3)
        self.logo_2 = QtGui.QLabel(self.mapTab)
        self.logo_2.setAutoFillBackground(False)
        self.logo_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/qgiscloud/logo.png")))
        self.logo_2.setScaledContents(False)
        self.logo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_2.setObjectName(_fromUtf8("logo_2"))
        self.gridLayout_4.addWidget(self.logo_2, 0, 0, 1, 2)
        self.line_2 = QtGui.QFrame(self.mapTab)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_4.addWidget(self.line_2, 3, 0, 1, 3)
        self.btnPublishMap = QtGui.QPushButton(self.mapTab)
        self.btnPublishMap.setObjectName(_fromUtf8("btnPublishMap"))
        self.gridLayout_4.addWidget(self.btnPublishMap, 4, 0, 1, 3)
        self.labelOpenLayersPlugin = QtGui.QLabel(self.mapTab)
        self.labelOpenLayersPlugin.setWordWrap(True)
        self.labelOpenLayersPlugin.setObjectName(_fromUtf8("labelOpenLayersPlugin"))
        self.gridLayout_4.addWidget(self.labelOpenLayersPlugin, 2, 0, 1, 3)
        self.btnBackgroundLayer = QtGui.QToolButton(self.mapTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBackgroundLayer.sizePolicy().hasHeightForWidth())
        self.btnBackgroundLayer.setSizePolicy(sizePolicy)
        self.btnBackgroundLayer.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.btnBackgroundLayer.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btnBackgroundLayer.setArrowType(QtCore.Qt.NoArrow)
        self.btnBackgroundLayer.setObjectName(_fromUtf8("btnBackgroundLayer"))
        self.gridLayout_4.addWidget(self.btnBackgroundLayer, 1, 0, 1, 3)
        self.widgetServices = QtGui.QWidget(self.mapTab)
        self.widgetServices.setObjectName(_fromUtf8("widgetServices"))
        self.gridLayout = QtGui.QGridLayout(self.widgetServices)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblMobileMap = QtGui.QLabel(self.widgetServices)
        self.lblMobileMap.setEnabled(True)
        self.lblMobileMap.setOpenExternalLinks(True)
        self.lblMobileMap.setObjectName(_fromUtf8("lblMobileMap"))
        self.gridLayout.addWidget(self.lblMobileMap, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.widgetServices)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.lblWMS = QtGui.QLabel(self.widgetServices)
        self.lblWMS.setOpenExternalLinks(True)
        self.lblWMS.setObjectName(_fromUtf8("lblWMS"))
        self.gridLayout.addWidget(self.lblWMS, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.widgetServices)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lblMaps = QtGui.QLabel(self.widgetServices)
        self.lblMaps.setOpenExternalLinks(True)
        self.lblMaps.setObjectName(_fromUtf8("lblMaps"))
        self.gridLayout.addWidget(self.lblMaps, 4, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.widgetServices)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.lblMobileMap_2 = QtGui.QLabel(self.widgetServices)
        self.lblMobileMap_2.setEnabled(True)
        self.lblMobileMap_2.setOpenExternalLinks(True)
        self.lblMobileMap_2.setObjectName(_fromUtf8("lblMobileMap_2"))
        self.gridLayout.addWidget(self.lblMobileMap_2, 5, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.widgetServices)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.widgetServices)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lblWebmap = QtGui.QLabel(self.widgetServices)
        self.lblWebmap.setOpenExternalLinks(True)
        self.lblWebmap.setObjectName(_fromUtf8("lblWebmap"))
        self.gridLayout.addWidget(self.lblWebmap, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.widgetServices)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.lblQwc1 = QtGui.QLabel(self.widgetServices)
        self.lblQwc1.setOpenExternalLinks(True)
        self.lblQwc1.setObjectName(_fromUtf8("lblQwc1"))
        self.gridLayout.addWidget(self.lblQwc1, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.widgetServices, 6, 0, 1, 3)
        self.tabWidget.addTab(self.mapTab, _fromUtf8(""))
        self.uploadTab = QtGui.QWidget()
        self.uploadTab.setEnabled(True)
        self.uploadTab.setObjectName(_fromUtf8("uploadTab"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.uploadTab)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_10 = QtGui.QLabel(self.uploadTab)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.cbUploadDatabase = QtGui.QComboBox(self.uploadTab)
        self.cbUploadDatabase.setObjectName(_fromUtf8("cbUploadDatabase"))
        self.horizontalLayout_3.addWidget(self.cbUploadDatabase)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.lblDbSizeUpload = QtGui.QLabel(self.uploadTab)
        self.lblDbSizeUpload.setText(_fromUtf8(""))
        self.lblDbSizeUpload.setObjectName(_fromUtf8("lblDbSizeUpload"))
        self.verticalLayout_6.addWidget(self.lblDbSizeUpload)
        self.tblLocalLayers = QtGui.QTableWidget(self.uploadTab)
        self.tblLocalLayers.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblLocalLayers.setObjectName(_fromUtf8("tblLocalLayers"))
        self.tblLocalLayers.setColumnCount(0)
        self.tblLocalLayers.setRowCount(0)
        self.tblLocalLayers.horizontalHeader().setStretchLastSection(True)
        self.tblLocalLayers.verticalHeader().setVisible(False)
        self.verticalLayout_6.addWidget(self.tblLocalLayers)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.btnRefreshLocalLayers = QtGui.QPushButton(self.uploadTab)
        self.btnRefreshLocalLayers.setObjectName(_fromUtf8("btnRefreshLocalLayers"))
        self.horizontalLayout_7.addWidget(self.btnRefreshLocalLayers)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.btnUploadData = QtGui.QPushButton(self.uploadTab)
        self.btnUploadData.setObjectName(_fromUtf8("btnUploadData"))
        self.verticalLayout_6.addWidget(self.btnUploadData)
        self.progressWidget = QtGui.QWidget(self.uploadTab)
        self.progressWidget.setObjectName(_fromUtf8("progressWidget"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.progressWidget)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.spinner = Spinner(self.progressWidget)
        self.spinner.setObjectName(_fromUtf8("spinner"))
        self.horizontalLayout_6.addWidget(self.spinner)
        self.lblProgress = QtGui.QLabel(self.progressWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblProgress.sizePolicy().hasHeightForWidth())
        self.lblProgress.setSizePolicy(sizePolicy)
        self.lblProgress.setText(_fromUtf8(""))
        self.lblProgress.setObjectName(_fromUtf8("lblProgress"))
        self.horizontalLayout_6.addWidget(self.lblProgress)
        self.verticalLayout_6.addWidget(self.progressWidget)
        self.tabWidget.addTab(self.uploadTab, _fromUtf8(""))
        self.accountTab = QtGui.QWidget()
        self.accountTab.setObjectName(_fromUtf8("accountTab"))
        self.gridLayout_5 = QtGui.QGridLayout(self.accountTab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(self.accountTab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.editServer = QtGui.QLineEdit(self.accountTab)
        self.editServer.setEnabled(True)
        self.editServer.setObjectName(_fromUtf8("editServer"))
        self.horizontalLayout_4.addWidget(self.editServer)
        self.resetUrlBtn = QtGui.QToolButton(self.accountTab)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/qgiscloud/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetUrlBtn.setIcon(icon)
        self.resetUrlBtn.setObjectName(_fromUtf8("resetUrlBtn"))
        self.horizontalLayout_4.addWidget(self.resetUrlBtn)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btnLogin = QtGui.QPushButton(self.accountTab)
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.horizontalLayout_5.addWidget(self.btnLogin)
        self.lblSignup = QtGui.QLabel(self.accountTab)
        self.lblSignup.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSignup.setOpenExternalLinks(True)
        self.lblSignup.setObjectName(_fromUtf8("lblSignup"))
        self.horizontalLayout_5.addWidget(self.lblSignup)
        self.lblLoginStatus = QtGui.QLabel(self.accountTab)
        self.lblLoginStatus.setObjectName(_fromUtf8("lblLoginStatus"))
        self.horizontalLayout_5.addWidget(self.lblLoginStatus)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.btnLogout = QtGui.QPushButton(self.accountTab)
        self.btnLogout.setObjectName(_fromUtf8("btnLogout"))
        self.horizontalLayout_5.addWidget(self.btnLogout)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.widgetDatabases = QtGui.QWidget(self.accountTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetDatabases.sizePolicy().hasHeightForWidth())
        self.widgetDatabases.setSizePolicy(sizePolicy)
        self.widgetDatabases.setObjectName(_fromUtf8("widgetDatabases"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widgetDatabases)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.line = QtGui.QFrame(self.widgetDatabases)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_29 = QtGui.QLabel(self.widgetDatabases)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.horizontalLayout_2.addWidget(self.label_29)
        self.lblDbSize = QtGui.QLabel(self.widgetDatabases)
        self.lblDbSize.setText(_fromUtf8(""))
        self.lblDbSize.setObjectName(_fromUtf8("lblDbSize"))
        self.horizontalLayout_2.addWidget(self.lblDbSize)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabDatabases = QtGui.QListWidget(self.widgetDatabases)
        self.tabDatabases.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabDatabases.setObjectName(_fromUtf8("tabDatabases"))
        self.verticalLayout_3.addWidget(self.tabDatabases)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnDbCreate = QtGui.QPushButton(self.widgetDatabases)
        self.btnDbCreate.setObjectName(_fromUtf8("btnDbCreate"))
        self.horizontalLayout.addWidget(self.btnDbCreate)
        self.btnDbDelete = QtGui.QPushButton(self.widgetDatabases)
        self.btnDbDelete.setEnabled(False)
        self.btnDbDelete.setObjectName(_fromUtf8("btnDbDelete"))
        self.horizontalLayout.addWidget(self.btnDbDelete)
        spacerItem3 = QtGui.QSpacerItem(37, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.btnDbRefresh = QtGui.QPushButton(self.widgetDatabases)
        self.btnDbRefresh.setObjectName(_fromUtf8("btnDbRefresh"))
        self.horizontalLayout.addWidget(self.btnDbRefresh)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout_5.addWidget(self.widgetDatabases, 2, 0, 1, 1)
        self.widgetMaps = QtGui.QWidget(self.accountTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetMaps.sizePolicy().hasHeightForWidth())
        self.widgetMaps.setSizePolicy(sizePolicy)
        self.widgetMaps.setObjectName(_fromUtf8("widgetMaps"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widgetMaps)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnMapLoad = QtGui.QPushButton(self.widgetMaps)
        self.btnMapLoad.setObjectName(_fromUtf8("btnMapLoad"))
        self.gridLayout_2.addWidget(self.btnMapLoad, 3, 0, 1, 1)
        self.tabMaps = QtGui.QListWidget(self.widgetMaps)
        self.tabMaps.setObjectName(_fromUtf8("tabMaps"))
        self.gridLayout_2.addWidget(self.tabMaps, 1, 0, 2, 4)
        self.lblMaps_2 = QtGui.QLabel(self.widgetMaps)
        self.lblMaps_2.setObjectName(_fromUtf8("lblMaps_2"))
        self.gridLayout_2.addWidget(self.lblMaps_2, 0, 0, 1, 1)
        self.btnMapDelete = QtGui.QPushButton(self.widgetMaps)
        self.btnMapDelete.setEnabled(False)
        self.btnMapDelete.setObjectName(_fromUtf8("btnMapDelete"))
        self.gridLayout_2.addWidget(self.btnMapDelete, 3, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(145, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 2, 1, 1)
        self.gridLayout_5.addWidget(self.widgetMaps, 4, 0, 1, 1)
        self.line_4 = QtGui.QFrame(self.accountTab)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_5.addWidget(self.line_4, 3, 0, 1, 1)
        self.tabWidget.addTab(self.accountTab, _fromUtf8(""))
        self.aboutTab = QtGui.QWidget()
        self.aboutTab.setObjectName(_fromUtf8("aboutTab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.aboutTab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.logo = QtGui.QLabel(self.aboutTab)
        self.logo.setAutoFillBackground(False)
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/qgiscloud/logo.png")))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.verticalLayout.addWidget(self.logo)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_6 = QtGui.QLabel(self.aboutTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lblVersionPlugin = QtGui.QLabel(self.aboutTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblVersionPlugin.sizePolicy().hasHeightForWidth())
        self.lblVersionPlugin.setSizePolicy(sizePolicy)
        self.lblVersionPlugin.setText(_fromUtf8(""))
        self.lblVersionPlugin.setObjectName(_fromUtf8("lblVersionPlugin"))
        self.horizontalLayout_8.addWidget(self.lblVersionPlugin)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.aboutText = QtGui.QTextEdit(self.aboutTab)
        self.aboutText.setObjectName(_fromUtf8("aboutText"))
        self.verticalLayout.addWidget(self.aboutText)
        self.tabWidget.addTab(self.aboutTab, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        QgisCloudPlugin.setWidget(self.dockWidgetContents)
        self.label_2.setBuddy(self.editServer)

        self.retranslateUi(QgisCloudPlugin)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(QgisCloudPlugin)

    def retranslateUi(self, QgisCloudPlugin):
        QgisCloudPlugin.setWindowTitle(_translate("QgisCloudPlugin", "&QGIS Cloud", None))
        self.btnPublishMap.setText(_translate("QgisCloudPlugin", "Publish Map", None))
        self.labelOpenLayersPlugin.setText(_translate("QgisCloudPlugin", "<i>To add a background layer to the map, install the OpenLayers plugin.</i>", None))
        self.btnBackgroundLayer.setText(_translate("QgisCloudPlugin", "Add background layer", None))
        self.lblMobileMap.setText(_translate("QgisCloudPlugin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://m.qgiscloud.com/user/map\"><span style=\" font-family:\'Ubuntu\'; text-decoration: underline; color:#0057ae;\">http://m.qgiscloud.com/user/map</span></a></p></body></html>", None))
        self.label.setText(_translate("QgisCloudPlugin", "Public WMS", None))
        self.lblWMS.setText(_translate("QgisCloudPlugin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://wms.qgiscloud.com/user/map\"><span style=\" font-family:\'Ubuntu\'; text-decoration: underline; color:#0057ae;\">http://wms.qgiscloud.com/user/map</span></a></p></body></html>", None))
        self.label_5.setText(_translate("QgisCloudPlugin", "Map Admin", None))
        self.lblMaps.setText(_translate("QgisCloudPlugin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://qgiscloud.com/maps\"><span style=\" font-family:\'Ubuntu\'; text-decoration: underline; color:#0057ae;\">http://qgiscloud.com/maps</span></a></p></body></html>", None))
        self.label_8.setText(_translate("QgisCloudPlugin", "Support", None))
        self.lblMobileMap_2.setText(_translate("QgisCloudPlugin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"mailto:support@qgiscloud.com?subject=QGISCloud support\"><span style=\" font-family:\'Ubuntu\'; text-decoration: underline; color:#0057ae;\">support@qgiscloud.com</span></a></p></body></html>", None))
        self.label_4.setText(_translate("QgisCloudPlugin", "Mobile map (old)", None))
        self.label_3.setText(_translate("QgisCloudPlugin", "Webmap", None))
        self.lblWebmap.setText(_translate("QgisCloudPlugin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://qgiscloud.com/user/map\"><span style=\" font-family:\'Ubuntu\'; text-decoration: underline; color:#0057ae;\">http://qgiscloud.com/user/map</span></a></p></body></html>", None))
        self.label_7.setText(_translate("QgisCloudPlugin", "QWC1 Webmap (old)", None))
        self.lblQwc1.setText(_translate("QgisCloudPlugin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://qgiscloud.com/user/map/qwc2/\"><span style=\" font-size:9pt; text-decoration: underline; color:#0057ae;\">http://qgiscloud.com/user/map/qwc1/</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mapTab), _translate("QgisCloudPlugin", "Map", None))
        self.label_10.setText(_translate("QgisCloudPlugin", "Database:", None))
        self.btnRefreshLocalLayers.setText(_translate("QgisCloudPlugin", "Refresh layers", None))
        self.btnUploadData.setText(_translate("QgisCloudPlugin", "Upload data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uploadTab), _translate("QgisCloudPlugin", "Upload Data", None))
        self.label_2.setText(_translate("QgisCloudPlugin", "&Server:", None))
        self.editServer.setText(_translate("QgisCloudPlugin", "https://api.qgiscloud.com", None))
        self.resetUrlBtn.setToolTip(_translate("QgisCloudPlugin", "Reset QGIS Cloud API URL", None))
        self.resetUrlBtn.setText(_translate("QgisCloudPlugin", "...", None))
        self.btnLogin.setText(_translate("QgisCloudPlugin", "Login", None))
        self.lblSignup.setText(_translate("QgisCloudPlugin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://qgiscloud.com/account/sign_up\"><span style=\" text-decoration: underline; color:#0057ae;\">Signup</span></a></p></body></html>", None))
        self.lblLoginStatus.setText(_translate("QgisCloudPlugin", "Logged in as ...", None))
        self.btnLogout.setText(_translate("QgisCloudPlugin", "Logout", None))
        self.label_29.setText(_translate("QgisCloudPlugin", "Databases", None))
        self.btnDbCreate.setText(_translate("QgisCloudPlugin", "Create", None))
        self.btnDbDelete.setText(_translate("QgisCloudPlugin", "Delete", None))
        self.btnDbRefresh.setText(_translate("QgisCloudPlugin", "Refresh", None))
        self.btnMapLoad.setText(_translate("QgisCloudPlugin", "Load", None))
        self.lblMaps_2.setText(_translate("QgisCloudPlugin", "Maps", None))
        self.btnMapDelete.setText(_translate("QgisCloudPlugin", "Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.accountTab), _translate("QgisCloudPlugin", "Account", None))
        self.label_6.setText(_translate("QgisCloudPlugin", "<b>Plugin version:</b>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), _translate("QgisCloudPlugin", "About", None))

from spinner import Spinner
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    QgisCloudPlugin = QtGui.QDockWidget()
    ui = Ui_QgisCloudPlugin()
    ui.setupUi(QgisCloudPlugin)
    QgisCloudPlugin.show()
    sys.exit(app.exec_())
