# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hdus/dev/qgis/qgis-cloud-plugin/qgiscloud/ui_qgiscloudplugin.ui'
#
# Created: Wed Sep  3 14:40:08 2014
#      by: PyQt4 UI code generator 4.10.4
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
        QgisCloudPlugin.resize(429, 602)
        QgisCloudPlugin.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_6 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.services = QtGui.QWidget()
        self.services.setObjectName(_fromUtf8("services"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.services)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.logo = QtGui.QLabel(self.services)
        self.logo.setAutoFillBackground(False)
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/qgiscloud/logo.png")))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.verticalLayout_7.addWidget(self.logo)
        self.btnPublishMap = QtGui.QPushButton(self.services)
        self.btnPublishMap.setObjectName(_fromUtf8("btnPublishMap"))
        self.verticalLayout_7.addWidget(self.btnPublishMap)
        self.serviceLinks = QtGui.QStackedWidget(self.services)
        self.serviceLinks.setMaximumSize(QtCore.QSize(16777215, 140))
        self.serviceLinks.setObjectName(_fromUtf8("serviceLinks"))
        self.pageStart = QtGui.QWidget()
        self.pageStart.setObjectName(_fromUtf8("pageStart"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.pageStart)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_7 = QtGui.QLabel(self.pageStart)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_9.addWidget(self.label_7)
        self.label_6 = QtGui.QLabel(self.pageStart)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_9.addWidget(self.label_6)
        self.label_9 = QtGui.QLabel(self.pageStart)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setOpenExternalLinks(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_9.addWidget(self.label_9)
        spacerItem = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.serviceLinks.addWidget(self.pageStart)
        self.pageVersions = QtGui.QWidget()
        self.pageVersions.setObjectName(_fromUtf8("pageVersions"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.pageVersions)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_13 = QtGui.QLabel(self.pageVersions)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_3.addWidget(self.label_13)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lblVersionQGIS = QtGui.QLabel(self.pageVersions)
        self.lblVersionQGIS.setText(_fromUtf8(""))
        self.lblVersionQGIS.setObjectName(_fromUtf8("lblVersionQGIS"))
        self.gridLayout_3.addWidget(self.lblVersionQGIS, 3, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.pageVersions)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 3, 1, 1, 1)
        self.lblVersionPlugin = QtGui.QLabel(self.pageVersions)
        self.lblVersionPlugin.setText(_fromUtf8(""))
        self.lblVersionPlugin.setObjectName(_fromUtf8("lblVersionPlugin"))
        self.gridLayout_3.addWidget(self.lblVersionPlugin, 4, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.pageVersions)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 5, 1, 1, 1)
        self.lblVersionPython = QtGui.QLabel(self.pageVersions)
        self.lblVersionPython.setText(_fromUtf8(""))
        self.lblVersionPython.setObjectName(_fromUtf8("lblVersionPython"))
        self.gridLayout_3.addWidget(self.lblVersionPython, 6, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.pageVersions)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 4, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.pageVersions)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 6, 1, 1, 1)
        self.lblVersionOGR = QtGui.QLabel(self.pageVersions)
        self.lblVersionOGR.setText(_fromUtf8(""))
        self.lblVersionOGR.setObjectName(_fromUtf8("lblVersionOGR"))
        self.gridLayout_3.addWidget(self.lblVersionOGR, 5, 2, 1, 1)
        self.lblVersionOS = QtGui.QLabel(self.pageVersions)
        self.lblVersionOS.setText(_fromUtf8(""))
        self.lblVersionOS.setObjectName(_fromUtf8("lblVersionOS"))
        self.gridLayout_3.addWidget(self.lblVersionOS, 7, 2, 1, 1)
        self.label_16 = QtGui.QLabel(self.pageVersions)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 7, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.serviceLinks.addWidget(self.pageVersions)
        self.pageLinks = QtGui.QWidget()
        self.pageLinks.setObjectName(_fromUtf8("pageLinks"))
        self.gridLayout_2 = QtGui.QGridLayout(self.pageLinks)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.pageLinks)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lblWebmap = QtGui.QLabel(self.pageLinks)
        self.lblWebmap.setOpenExternalLinks(True)
        self.lblWebmap.setObjectName(_fromUtf8("lblWebmap"))
        self.gridLayout.addWidget(self.lblWebmap, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.pageLinks)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lblMobileMap = QtGui.QLabel(self.pageLinks)
        self.lblMobileMap.setEnabled(True)
        self.lblMobileMap.setOpenExternalLinks(True)
        self.lblMobileMap.setObjectName(_fromUtf8("lblMobileMap"))
        self.gridLayout.addWidget(self.lblMobileMap, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.pageLinks)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.lblWMS = QtGui.QLabel(self.pageLinks)
        self.lblWMS.setOpenExternalLinks(True)
        self.lblWMS.setObjectName(_fromUtf8("lblWMS"))
        self.gridLayout.addWidget(self.lblWMS, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.pageLinks)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.lblMaps = QtGui.QLabel(self.pageLinks)
        self.lblMaps.setOpenExternalLinks(True)
        self.lblMaps.setObjectName(_fromUtf8("lblMaps"))
        self.gridLayout.addWidget(self.lblMaps, 3, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.pageLinks)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.lblMobileMap_2 = QtGui.QLabel(self.pageLinks)
        self.lblMobileMap_2.setEnabled(True)
        self.lblMobileMap_2.setOpenExternalLinks(True)
        self.lblMobileMap_2.setObjectName(_fromUtf8("lblMobileMap_2"))
        self.gridLayout.addWidget(self.lblMobileMap_2, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 31, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.serviceLinks.addWidget(self.pageLinks)
        self.verticalLayout_7.addWidget(self.serviceLinks)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.tabWidget.addTab(self.services, _fromUtf8(""))
        self.upload = QtGui.QWidget()
        self.upload.setEnabled(True)
        self.upload.setObjectName(_fromUtf8("upload"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.upload)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_10 = QtGui.QLabel(self.upload)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.cbUploadDatabase = QtGui.QComboBox(self.upload)
        self.cbUploadDatabase.setObjectName(_fromUtf8("cbUploadDatabase"))
        self.horizontalLayout_3.addWidget(self.cbUploadDatabase)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.lblDbSizeUpload = QtGui.QLabel(self.upload)
        self.lblDbSizeUpload.setText(_fromUtf8(""))
        self.lblDbSizeUpload.setObjectName(_fromUtf8("lblDbSizeUpload"))
        self.verticalLayout_10.addWidget(self.lblDbSizeUpload)
        self.tblLocalLayers = QtGui.QTableWidget(self.upload)
        self.tblLocalLayers.setObjectName(_fromUtf8("tblLocalLayers"))
        self.tblLocalLayers.setColumnCount(0)
        self.tblLocalLayers.setRowCount(0)
        self.tblLocalLayers.verticalHeader().setVisible(False)
        self.verticalLayout_10.addWidget(self.tblLocalLayers)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.btnRefreshLocalLayers = QtGui.QPushButton(self.upload)
        self.btnRefreshLocalLayers.setObjectName(_fromUtf8("btnRefreshLocalLayers"))
        self.horizontalLayout_7.addWidget(self.btnRefreshLocalLayers)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.cbReplaceLocalLayers = QtGui.QCheckBox(self.upload)
        self.cbReplaceLocalLayers.setChecked(True)
        self.cbReplaceLocalLayers.setObjectName(_fromUtf8("cbReplaceLocalLayers"))
        self.verticalLayout_10.addWidget(self.cbReplaceLocalLayers)
        self.btnUploadData = QtGui.QPushButton(self.upload)
        self.btnUploadData.setObjectName(_fromUtf8("btnUploadData"))
        self.verticalLayout_10.addWidget(self.btnUploadData)
        self.uploadProgressBar = QtGui.QProgressBar(self.upload)
        self.uploadProgressBar.setProperty("value", 24)
        self.uploadProgressBar.setObjectName(_fromUtf8("uploadProgressBar"))
        self.verticalLayout_10.addWidget(self.uploadProgressBar)
        self.btnPublishMapUpload = QtGui.QPushButton(self.upload)
        self.btnPublishMapUpload.setObjectName(_fromUtf8("btnPublishMapUpload"))
        self.verticalLayout_10.addWidget(self.btnPublishMapUpload)
        self.tabWidget.addTab(self.upload, _fromUtf8(""))
        self.account = QtGui.QWidget()
        self.account.setObjectName(_fromUtf8("account"))
        self.gridLayout_5 = QtGui.QGridLayout(self.account)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(self.account)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.editServer = QtGui.QLineEdit(self.account)
        self.editServer.setEnabled(True)
        self.editServer.setObjectName(_fromUtf8("editServer"))
        self.horizontalLayout_4.addWidget(self.editServer)
        self.resetUrlBtn = QtGui.QToolButton(self.account)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/qgiscloud/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetUrlBtn.setIcon(icon)
        self.resetUrlBtn.setObjectName(_fromUtf8("resetUrlBtn"))
        self.horizontalLayout_4.addWidget(self.resetUrlBtn)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btnLogin = QtGui.QPushButton(self.account)
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.horizontalLayout_5.addWidget(self.btnLogin)
        self.lblSignup = QtGui.QLabel(self.account)
        self.lblSignup.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSignup.setOpenExternalLinks(True)
        self.lblSignup.setObjectName(_fromUtf8("lblSignup"))
        self.horizontalLayout_5.addWidget(self.lblSignup)
        self.lblLoginStatus = QtGui.QLabel(self.account)
        self.lblLoginStatus.setObjectName(_fromUtf8("lblLoginStatus"))
        self.horizontalLayout_5.addWidget(self.lblLoginStatus)
        self.btnLogout = QtGui.QPushButton(self.account)
        self.btnLogout.setObjectName(_fromUtf8("btnLogout"))
        self.horizontalLayout_5.addWidget(self.btnLogout)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.groupBoxDatabases = QtGui.QGroupBox(self.account)
        self.groupBoxDatabases.setObjectName(_fromUtf8("groupBoxDatabases"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBoxDatabases)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tabDatabases = QtGui.QListWidget(self.groupBoxDatabases)
        self.tabDatabases.setObjectName(_fromUtf8("tabDatabases"))
        self.verticalLayout_4.addWidget(self.tabDatabases)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnDbRefresh = QtGui.QPushButton(self.groupBoxDatabases)
        self.btnDbRefresh.setObjectName(_fromUtf8("btnDbRefresh"))
        self.horizontalLayout.addWidget(self.btnDbRefresh)
        spacerItem5 = QtGui.QSpacerItem(37, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnDbCreate = QtGui.QPushButton(self.groupBoxDatabases)
        self.btnDbCreate.setObjectName(_fromUtf8("btnDbCreate"))
        self.horizontalLayout_2.addWidget(self.btnDbCreate)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.btnDbDelete = QtGui.QPushButton(self.groupBoxDatabases)
        self.btnDbDelete.setEnabled(False)
        self.btnDbDelete.setObjectName(_fromUtf8("btnDbDelete"))
        self.horizontalLayout_6.addWidget(self.btnDbDelete)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.gridLayout_5.addWidget(self.groupBoxDatabases, 4, 0, 1, 1)
        self.lblDbSize = QtGui.QLabel(self.account)
        self.lblDbSize.setText(_fromUtf8(""))
        self.lblDbSize.setObjectName(_fromUtf8("lblDbSize"))
        self.gridLayout_5.addWidget(self.lblDbSize, 3, 0, 1, 1)
        self.tabWidget.addTab(self.account, _fromUtf8(""))
        self.about = QtGui.QWidget()
        self.about.setObjectName(_fromUtf8("about"))
        self.gridLayout_4 = QtGui.QGridLayout(self.about)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.aboutText = QtGui.QTextEdit(self.about)
        self.aboutText.setObjectName(_fromUtf8("aboutText"))
        self.gridLayout_4.addWidget(self.aboutText, 0, 0, 1, 1)
        self.tabWidget.addTab(self.about, _fromUtf8(""))
        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)
        QgisCloudPlugin.setWidget(self.dockWidgetContents)
        self.label_2.setBuddy(self.editServer)

        self.retranslateUi(QgisCloudPlugin)
        self.tabWidget.setCurrentIndex(2)
        self.serviceLinks.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(QgisCloudPlugin)

    def retranslateUi(self, QgisCloudPlugin):
        QgisCloudPlugin.setWindowTitle(_translate("QgisCloudPlugin", "QGIS Cloud", None))
        self.btnPublishMap.setText(_translate("QgisCloudPlugin", "Publish Map", None))
        self.label_7.setText(_translate("QgisCloudPlugin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">QGIS Cloud Hosting</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://qgiscloud.com/\"><span style=\" text-decoration: underline; color:#0057ae;\">qgiscloud.com</span></a></p></body></html>", None))
        self.label_6.setText(_translate("QgisCloudPlugin", "Publish your own maps directly from the desktop!\n"
"\n"
"It\'s free to get started and sign up is instant. Publish your first map within minutes.", None))
        self.label_9.setText(_translate("QgisCloudPlugin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://qgiscloud.com/account/sign_up\"><span style=\" text-decoration: underline; color:#0057ae;\">Signup</span></a></p></body></html>", None))
        self.label_13.setText(_translate("QgisCloudPlugin", "Versions", None))
        self.label_11.setText(_translate("QgisCloudPlugin", "QGIS:", None))
        self.label_14.setText(_translate("QgisCloudPlugin", "OGR/GDAL:", None))
        self.label_12.setText(_translate("QgisCloudPlugin", "Plugin:", None))
        self.label_15.setText(_translate("QgisCloudPlugin", "Python:", None))
        self.label_16.setText(_translate("QgisCloudPlugin", "OS:", None))
        self.label_3.setText(_translate("QgisCloudPlugin", "Webmap", None))
        self.lblWebmap.setText(_translate("QgisCloudPlugin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://qgiscloud.com/user/map\"><span style=\" font-family:\'Ubuntu\'; text-decoration: underline; color:#0057ae;\">http://qgiscloud.com/user/map</span></a></p></body></html>", None))
        self.label_4.setText(_translate("QgisCloudPlugin", "Mobile map", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.services), _translate("QgisCloudPlugin", "Services", None))
        self.label_10.setText(_translate("QgisCloudPlugin", "Database", None))
        self.btnRefreshLocalLayers.setText(_translate("QgisCloudPlugin", "Refresh layers", None))
        self.cbReplaceLocalLayers.setText(_translate("QgisCloudPlugin", "Replace local layers in project", None))
        self.btnUploadData.setText(_translate("QgisCloudPlugin", "Upload data", None))
        self.btnPublishMapUpload.setText(_translate("QgisCloudPlugin", "Publish Map", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.upload), _translate("QgisCloudPlugin", "Upload Data", None))
        self.label_2.setText(_translate("QgisCloudPlugin", "Server:", None))
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
        self.groupBoxDatabases.setTitle(_translate("QgisCloudPlugin", "Databases", None))
        self.btnDbRefresh.setText(_translate("QgisCloudPlugin", "Refresh", None))
        self.btnDbCreate.setText(_translate("QgisCloudPlugin", "Create new database", None))
        self.btnDbDelete.setText(_translate("QgisCloudPlugin", "Delete database", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.account), _translate("QgisCloudPlugin", "Account", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), _translate("QgisCloudPlugin", "About", None))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    QgisCloudPlugin = QtGui.QDockWidget()
    ui = Ui_QgisCloudPlugin()
    ui.setupUi(QgisCloudPlugin)
    QgisCloudPlugin.show()
    sys.exit(app.exec_())

