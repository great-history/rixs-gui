# Qt5 version 5.15.2
# PyQt5 version 5.15.2
# python version 3.8

from OwnFrame import *
from DataManager import *
import sys


class FirstFrame(OwnFrame):
    def __init__(self, parent, width=None, height=None):
        OwnFrame.__init__(self, parent, width, height)
        self.frame = super().getFrame()
        self.dataManager = DataManager()

        self._arrangeUI()
        self._retranslateAll()

        self._textInputRestrict()
        self._arrangeDataInWidgets()

    def getFrame(self):
        return self.scrollForFirstFrame

    def _arrangeUI(self):
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        # self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.frame.setMinimumHeight(self.frame.parent().height()-20)
        self.frame.setMinimumWidth(self.frame.parent().width()-36)

        boxBasicPara = QGroupBox(self.frame)
        needToSaveStyleSheet = 'color:rgb(160,60,60)'
        self.v_name_label = QLabel(boxBasicPara)
        self.v_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.v_name_label.setStyleSheet(needToSaveStyleSheet)
        self.v_name_label.setFixedHeight(32)

        self.v_name_text = QLineEdit(boxBasicPara)  # str
        self.v_name_text.setStyleSheet(needToSaveStyleSheet)
        self.v_name_text.setFixedHeight(32)

        self.v_noccu_label = QLabel(boxBasicPara)
        self.v_noccu_label.setAlignment(QtCore.Qt.AlignCenter)
        self.v_noccu_label.setStyleSheet(needToSaveStyleSheet)
        self.v_noccu_label.setFixedHeight(32)

        self.v_noccu_text = QLineEdit(boxBasicPara)  # int
        self.v_noccu_text.setStyleSheet(needToSaveStyleSheet)
        self.v_noccu_text.setFixedHeight(32)

        self.c_name_label = QLabel(boxBasicPara)
        self.c_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.c_name_label.setStyleSheet(needToSaveStyleSheet)
        self.c_name_label.setFixedHeight(32)

        self.c_name_text = QLineEdit(boxBasicPara)  # str
        self.c_name_text.setStyleSheet(needToSaveStyleSheet)
        self.c_name_text.setFixedHeight(32)

        self.c_noccu_label = QLabel(boxBasicPara)
        self.c_noccu_label.setAlignment(QtCore.Qt.AlignCenter)
        self.c_noccu_label.setStyleSheet(needToSaveStyleSheet)
        self.c_noccu_label.setFixedHeight(32)

        self.c_noccu_text = QLineEdit(boxBasicPara)  # int
        self.c_noccu_text.setStyleSheet(needToSaveStyleSheet)
        self.c_noccu_text.setFixedHeight(32)

        self.v_soc_label = QLabel(boxBasicPara)
        self.v_soc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.v_soc_label.setStyleSheet(needToSaveStyleSheet)
        self.v_soc_label.setFixedHeight(32)

        self.v_soc_text = QLineEdit(boxBasicPara)  # float-float
        self.v_soc_text.setStyleSheet(needToSaveStyleSheet)
        self.v_soc_text.setFixedHeight(32)

        self.c_soc_label = QLabel(boxBasicPara)
        self.c_soc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.c_soc_label.setStyleSheet(needToSaveStyleSheet)
        self.c_soc_label.setFixedHeight(32)

        self.c_soc_text = QLineEdit(boxBasicPara)  # float
        self.c_soc_text.setStyleSheet(needToSaveStyleSheet)
        self.c_soc_text.setFixedHeight(32)

        self.shell_level_v_label = QLabel(boxBasicPara)
        self.shell_level_v_label.setAlignment(QtCore.Qt.AlignCenter)
        self.shell_level_v_label.setFixedHeight(32)

        self.shell_level_v_text = QLineEdit(boxBasicPara)  # float
        self.shell_level_v_text.setFixedHeight(32)

        self.shell_level_c_label = QLabel(boxBasicPara)
        self.shell_level_c_label.setAlignment(QtCore.Qt.AlignCenter)
        self.shell_level_c_label.setFixedHeight(32)

        self.shell_level_c_text = QLineEdit(boxBasicPara)  # float
        self.shell_level_c_text.setFixedHeight(32)

        self.slater_initial_box = QGroupBox(boxBasicPara)
        self.slater_initial_box.setStyleSheet(needToSaveStyleSheet)

        self.slater_initial_Fx_vv_label = QLabel(self.slater_initial_box)
        self.slater_initial_Fx_vv_label.setAlignment(QtCore.Qt.AlignCenter)
        self.slater_initial_Fx_vv_label.setFixedHeight(32)

        self.slater_initial_Fx_vv_text = QLineEdit(self.slater_initial_box)
        self.slater_initial_Fx_vv_text.setFixedHeight(32)

        self.slater_initial_Fx_vc_label = QLabel(self.slater_initial_box)
        self.slater_initial_Fx_vc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.slater_initial_Fx_vc_label.setFixedHeight(32)

        self.slater_initial_Fx_vc_text = QLineEdit(self.slater_initial_box)
        self.slater_initial_Fx_vc_text.setFixedHeight(32)

        self.slater_initial_Gx_vc_label = QLabel(self.slater_initial_box)
        self.slater_initial_Gx_vc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.slater_initial_Gx_vc_label.setFixedHeight(32)

        self.slater_initial_Gx_vc_text = QLineEdit(self.slater_initial_box)
        self.slater_initial_Gx_vc_text.setFixedHeight(32)

        self.slater_initial_Fx_cc_label = QLabel(self.slater_initial_box)
        self.slater_initial_Fx_cc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.slater_initial_Fx_cc_label.setFixedHeight(32)

        self.slater_initial_Fx_cc_text = QLineEdit(self.slater_initial_box)
        self.slater_initial_Fx_cc_text.setFixedHeight(32)

        slaterInitialBoxLayout = QGridLayout(self.slater_initial_box)
        slaterInitialBoxLayout.setAlignment(QtCore.Qt.AlignTop)
        slaterInitialBoxLayout.addWidget(self.slater_initial_Fx_vv_label, 0, 0, QtCore.Qt.AlignTop)
        slaterInitialBoxLayout.addWidget(self.slater_initial_Fx_vv_text, 0, 1, 1, 3, QtCore.Qt.AlignTop)
        slaterInitialBoxLayout.addWidget(self.slater_initial_Fx_vc_label, 1, 0, QtCore.Qt.AlignTop)
        slaterInitialBoxLayout.addWidget(self.slater_initial_Fx_vc_text, 1, 1, 1, 3, QtCore.Qt.AlignTop)
        slaterInitialBoxLayout.addWidget(self.slater_initial_Gx_vc_label, 2, 0, QtCore.Qt.AlignTop)
        slaterInitialBoxLayout.addWidget(self.slater_initial_Gx_vc_text, 2, 1, 1, 3, QtCore.Qt.AlignTop)
        slaterInitialBoxLayout.addWidget(self.slater_initial_Fx_cc_label, 3, 0, QtCore.Qt.AlignTop)
        slaterInitialBoxLayout.addWidget(self.slater_initial_Fx_cc_text, 3, 1, 1, 3, QtCore.Qt.AlignTop)

        self.slater_initial_box.setLayout(slaterInitialBoxLayout)

        self.slater_intermediate_box = QGroupBox(boxBasicPara)

        self.slater_intermediate_Fx_vv_label = QLabel(self.slater_intermediate_box)
        self.slater_intermediate_Fx_vv_label.setAlignment(QtCore.Qt.AlignCenter)
        self.slater_intermediate_Fx_vv_label.setFixedHeight(32)

        self.slater_intermediate_Fx_vv_text = QLineEdit(self.slater_intermediate_box)
        self.slater_intermediate_Fx_vv_text.setFixedHeight(32)

        self.slater_intermediate_Fx_vc_label = QLabel(self.slater_intermediate_box)
        self.slater_intermediate_Fx_vc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.slater_intermediate_Fx_vc_label.setFixedHeight(32)

        self.slater_intermediate_Fx_vc_text = QLineEdit(self.slater_intermediate_box)
        self.slater_intermediate_Fx_vc_text.setFixedHeight(32)

        self.slater_intermediate_Gx_vc_label = QLabel(self.slater_intermediate_box)
        self.slater_intermediate_Gx_vc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.slater_intermediate_Gx_vc_label.setFixedHeight(32)

        self.slater_intermediate_Gx_vc_text = QLineEdit(self.slater_intermediate_box)
        self.slater_intermediate_Gx_vc_text.setFixedHeight(32)

        self.slater_intermediate_Fx_cc_label = QLabel(self.slater_intermediate_box)
        self.slater_intermediate_Fx_cc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.slater_intermediate_Fx_cc_label.setFixedHeight(32)

        self.slater_intermediate_Fx_cc_text = QLineEdit(self.slater_intermediate_box)
        self.slater_intermediate_Fx_cc_text.setFixedHeight(32)

        slaterIntermediateBoxLayout = QGridLayout(self.slater_intermediate_box)
        slaterIntermediateBoxLayout.setAlignment(QtCore.Qt.AlignTop)
        slaterIntermediateBoxLayout.addWidget(self.slater_intermediate_Fx_vv_label, 0, 0, QtCore.Qt.AlignTop)
        slaterIntermediateBoxLayout.addWidget(self.slater_intermediate_Fx_vv_text, 0, 1, 1, 3, QtCore.Qt.AlignTop)
        slaterIntermediateBoxLayout.addWidget(self.slater_intermediate_Fx_vc_label, 1, 0, QtCore.Qt.AlignTop)
        slaterIntermediateBoxLayout.addWidget(self.slater_intermediate_Fx_vc_text, 1, 1, 1, 3, QtCore.Qt.AlignTop)
        slaterIntermediateBoxLayout.addWidget(self.slater_intermediate_Gx_vc_label, 2, 0, QtCore.Qt.AlignTop)
        slaterIntermediateBoxLayout.addWidget(self.slater_intermediate_Gx_vc_text, 2, 1, 1, 3, QtCore.Qt.AlignTop)
        slaterIntermediateBoxLayout.addWidget(self.slater_intermediate_Fx_cc_label, 3, 0, QtCore.Qt.AlignTop)
        slaterIntermediateBoxLayout.addWidget(self.slater_intermediate_Fx_cc_text, 3, 1, 1, 3, QtCore.Qt.AlignTop)

        self.slater_intermediate_box.setLayout(slaterIntermediateBoxLayout)

        self.buttonAddToAtomList = QPushButton(boxBasicPara)
        self.buttonAddToAtomList.setStyleSheet(needToSaveStyleSheet)
        self.buttonAddToAtomList.setFixedHeight(32)
        self.buttonAddToAtomList.clicked.connect(self._handleOnAddToAtomList)

        boxBasicParaLayout = QGridLayout(boxBasicPara)
        boxBasicParaLayout.setAlignment(QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.v_name_label, 0, 0, QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.v_name_text, 0, 1, QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.v_noccu_label, 0, 2, QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.v_noccu_text, 0, 3, QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.c_name_label, 0, 4, QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.c_name_text, 0, 5, QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.c_noccu_label, 0, 6, QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.c_noccu_text, 0, 7, QtCore.Qt.AlignTop)

        boxBasicParaLayout.addWidget(self.v_soc_label, 1, 0, QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.v_soc_text, 1, 1, QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.shell_level_v_label, 1, 2, QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.shell_level_v_text, 1, 3, QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.c_soc_label, 1, 4, QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.c_soc_text, 1, 5, QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.shell_level_c_label, 1, 6, QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.shell_level_c_text, 1, 7, QtCore.Qt.AlignTop)

        boxBasicParaLayout.addWidget(self.slater_initial_box, 2, 0, 6, 4, QtCore.Qt.AlignTop)
        boxBasicParaLayout.addWidget(self.slater_intermediate_box, 2, 4, 6, 4, QtCore.Qt.AlignTop)

        boxBasicParaLayout.addWidget(self.buttonAddToAtomList, 8, 7, QtCore.Qt.AlignTop)

        boxBasicPara.setLayout(boxBasicParaLayout)

        boxAtomList = QGroupBox(self.frame)
        self.atom_name_label = QLabel(boxAtomList)
        self.atom_name_label.setFixedHeight(32)
        self.atom_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.atom_name_text = QLineEdit(boxAtomList)
        self.atom_name_text.setFixedHeight(32)
        self.atom_list = QListWidget(boxAtomList)  # 一个列表，包含各个电子的情况
        # 给list设置一个右键菜单，可以右键删除
        # 然后双击事件的话是打开进行修改
        atom_list_menu = QMenu(self.atom_list)
        self.atom_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.atom_list_menu_import_action = QAction(atom_list_menu)

        def atom_list_import_action():  # 这个action不能直接接handleOnImport，这个Import是带参数item的
            # 如果能打开menu的话肯定是选中item了的
            self._handleOnImportAtomFromList(self.atom_list.currentItem())
        self.atom_list_menu_import_action.triggered.connect(atom_list_import_action)
        self.atom_list_menu_delete_action = QAction(atom_list_menu)
        self.atom_list_menu_delete_action.triggered.connect(self._handleOnDeleteFromAtomList)

        atom_list_menu.addAction(self.atom_list_menu_import_action)
        atom_list_menu.addAction(self.atom_list_menu_delete_action)

        def atom_list_menu_show(pos):
            # 还要判断一下是否选中item
            if self.atom_list.currentItem() is None:
                return
            atom_list_menu.exec_(QtGui.QCursor.pos())

        self.atom_list.customContextMenuRequested.connect(atom_list_menu_show)
        self.atom_list.itemDoubleClicked.connect(self._handleOnImportAtomFromList)

        self.atom_list_save_button = QPushButton(self.atom_list)
        self.atom_list_save_button.setFixedHeight(32)
        self.atom_list_save_button.clicked.connect(self._handleOnSaveAtomList)

        self.atom_list_load_button = QPushButton(self.atom_list)
        self.atom_list_load_button.setFixedHeight(32)
        self.atom_list_load_button.clicked.connect(self._handleOnLoadAtomList)

        boxAtomListLayout = QGridLayout(boxAtomList)
        boxAtomListLayout.setAlignment(QtCore.Qt.AlignTop)
        boxAtomListLayout.addWidget(self.atom_name_label, 0, 1, QtCore.Qt.AlignTop)
        boxAtomListLayout.addWidget(self.atom_name_text, 0, 2, 1, 2, QtCore.Qt.AlignTop)
        boxAtomListLayout.addWidget(self.atom_list, 1, 0, 2, 5, QtCore.Qt.AlignTop)
        boxAtomListLayout.addWidget(self.atom_list_save_button, 3, 0, 1, 2, QtCore.Qt.AlignTop)
        boxAtomListLayout.addWidget(self.atom_list_load_button, 3, 3, 1, 2, QtCore.Qt.AlignTop)

        boxAtomList.setLayout(boxAtomListLayout)

        self.v1_ext_B_label = QLabel(self.frame)
        self.v1_ext_B_label.setAlignment(QtCore.Qt.AlignCenter)
        self.v1_ext_B_label.setFixedHeight(32)

        self.v1_ext_B_texts = [QLineEdit(self.frame), QLineEdit(self.frame), QLineEdit(self.frame)]
        for text in self.v1_ext_B_texts:
            text.setFixedHeight(32)

        self.v1_on_which_label = QLabel(self.frame)
        self.v1_on_which_label.setAlignment(QtCore.Qt.AlignCenter)
        self.v1_on_which_label.setFixedHeight(32)

        self.v1_on_which_text = QLineEdit(self.frame)
        self.v1_on_which_text.setFixedHeight(32)

        self.v1_cfmt_box = QGroupBox(self.frame)
        # 最大7*7的一个数组，默认就7*7吧，然后加一个update按钮来根据参数更新
        self.v1_cfmt_para_texts = [[QLineEdit(self.v1_cfmt_box) for col in range(7)] for row in range(7)]

        v1_cfmt_box_layout = QGridLayout(self.v1_cfmt_box)
        v1_cfmt_box_layout.setAlignment(QtCore.Qt.AlignTop)

        def arrange_matrix_on_box(grid_layout, widgets):
            for row_i in range(len(widgets)):
                one_row = widgets[row_i]
                for col_j in range(len(one_row)):
                    grid_layout.addWidget(one_row[col_j], row_i, col_j, QtCore.Qt.AlignTop)

        arrange_matrix_on_box(v1_cfmt_box_layout, self.v1_cfmt_para_texts)
        self.v1_cfmt_box.setLayout(v1_cfmt_box_layout)
        # 添加更新按钮
        v1_cfmt_menu = QMenu(self.v1_cfmt_box)
        self.v1_cfmt_box.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        def cfmt_and_othermat_update_action():
            # TODO:update dimension of matrix
            self.informMsg("not implemented yet")

        self.v1_cfmt_menu_update_action = QAction(v1_cfmt_menu)
        self.v1_cfmt_menu_update_action.triggered.connect(cfmt_and_othermat_update_action)
        v1_cfmt_menu.addAction(self.v1_cfmt_menu_update_action)
        self.v1_cfmt_box.customContextMenuRequested.connect(lambda: v1_cfmt_menu.exec_(QtGui.QCursor.pos()))

        # othermat在格式上和cfmt保持一致
        self.v1_othermat_box = QGroupBox(self.frame)
        # 最大7*7的一个数组，默认就7*7吧，然后加一个update按钮来根据参数更新
        self.v1_othermat_para_texts = [[QLineEdit(self.v1_cfmt_box) for _ in range(7)] for _ in range(7)]

        v1_othermat_box_layout = QGridLayout(self.v1_othermat_box)
        v1_othermat_box_layout.setAlignment(QtCore.Qt.AlignTop)

        arrange_matrix_on_box(v1_othermat_box_layout, self.v1_othermat_para_texts)
        self.v1_othermat_box.setLayout(v1_othermat_box_layout)
        # 添加更新按钮
        v1_othermat_menu = QMenu(self.v1_othermat_box)
        self.v1_othermat_box.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.v1_othermat_menu_update_action = QAction(v1_othermat_menu)
        self.v1_othermat_menu_update_action.triggered.connect(cfmt_and_othermat_update_action)  # 这个可以复用，其实这两个矩阵应该同步更新
        v1_othermat_menu.addAction(self.v1_othermat_menu_update_action)
        self.v1_othermat_box.customContextMenuRequested.connect(lambda: v1_othermat_menu.exec_(QtGui.QCursor.pos()))

        self.local_axis_box = QGroupBox(self.frame)
        # 3*3的矩阵
        self.local_axis_texts = [[QLineEdit(self.local_axis_box) for _ in range(3)] for _ in range(3)]

        local_axis_box_layout = QGridLayout(self.local_axis_box)
        local_axis_box_layout.setAlignment(QtCore.Qt.AlignTop)

        arrange_matrix_on_box(local_axis_box_layout, self.local_axis_texts)
        self.local_axis_box.setLayout(local_axis_box_layout)

        self.verbose_label = QLabel(self.frame)
        self.verbose_label.setAlignment(QtCore.Qt.AlignCenter)
        self.verbose_label.setFixedHeight(32)

        self.verbose_text = QLineEdit(self.frame)
        self.verbose_text.setFixedHeight(32)

        self.diagonalize_box = QGroupBox(self.frame)  # 对角化计算，用python或fortan

        self.diagonalize_by_python_button = QPushButton(self.diagonalize_box)
        self.diagonalize_by_python_button.setFixedHeight(32)
        self.diagonalize_by_python_button.clicked.connect(self._handleOnDiagonalizeAndComputeByPython)

        self.diagonalize_by_fortan_button = QPushButton(self.diagonalize_box)
        self.diagonalize_by_fortan_button.setFixedHeight(32)
        self.diagonalize_by_fortan_button.clicked.connect(self._handleOnDiagonalizeAndComputeByFortan)

        diagonalize_box_layout = QHBoxLayout(self.diagonalize_box)
        diagonalize_box_layout.addWidget(self.diagonalize_by_python_button)
        diagonalize_box_layout.addWidget(self.diagonalize_by_fortan_button)
        diagonalize_box_layout.setAlignment(QtCore.Qt.AlignTop)

        self.diagonalize_box.setLayout(diagonalize_box_layout)

        self.firstPageOutputBox = QGroupBox(self.frame)
        # TODO:add output widgets
        firstPageOutputBoxLayout = QGridLayout(self.firstPageOutputBox)
        firstPageOutputBoxLayout.setAlignment(QtCore.Qt.AlignTop)

        self.firstPageOutputBox.setLayout(firstPageOutputBoxLayout)
        # TODO:here to continue
        # 底下一些具体参数最后再设置，要注意最后的比例会影响最终能否填满窗口
        mainLayout = QGridLayout(self.frame)  # 主要的布局
        mainLayout.setAlignment(QtCore.Qt.AlignTop)
        mainLayout.addWidget(boxBasicPara, 0, 0, 1, 4, QtCore.Qt.AlignTop)
        mainLayout.addWidget(boxAtomList, 0, 4, 1, 2, QtCore.Qt.AlignTop)  # 列表
        mainLayout.addWidget(self.v1_ext_B_label, 1, 0, QtCore.Qt.AlignTop)
        for i in range(3):
            mainLayout.addWidget(self.v1_ext_B_texts[i], 1, i+1, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.v1_on_which_label, 1, 4, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.v1_on_which_text, 1, 5, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.v1_cfmt_box, 2, 0, 1, 3, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.v1_othermat_box, 2, 3, 1, 3, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.local_axis_box, 3, 0, 3, 2, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.verbose_label, 3, 2, 1, 1, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.verbose_text, 3, 3, 1, 1, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.diagonalize_box, 4, 2, 2, 2, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.firstPageOutputBox, 6, 0, 3, 6, QtCore.Qt.AlignTop)
        for t in range(mainLayout.columnCount()):
            mainLayout.setColumnStretch(t, 1)
        for t in range(mainLayout.rowCount()):
            mainLayout.setRowStretch(t, 1)
        mainLayout.setRowStretch(0, 6)
        mainLayout.setRowStretch(2, 5)
        boxBasicParaLayout.setSizeConstraint(QLayout.SetMaximumSize)

        self.frame.setLayout(mainLayout)

        self.scrollForFirstFrame = QScrollArea(self.frame.parent())
        # self.scrollForFirstFrame.setWidgetResizable(True)
        # self.scrollForFirstFrame.setMinimumSize(1060, 700)
        self.scrollForFirstFrame.setWidget(self.frame)
        # tempLayout = QGridLayout()
        # tempLayout.addWidget(self.frame)
        # self.scrollForFirstFrame.setLayout(tempLayout)  # 为了让FirstFrame里的也能缩放
        # self.scrollForFirstFrame.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def _retranslateAll(self):
        self._retranslateTips()
        self._retranslateNames()

    def _retranslateTips(self):
        _translate = QtCore.QCoreApplication.translate
        self.atom_name_text.setToolTip(
            _translate("FirstFrame_atom_name_text_tip", "atom name"))
        self.atom_name_text.setPlaceholderText(
            _translate("FirstFrame_atom_name_text_sample", "例:Cu"))
        self.v_name_text.setToolTip(
            _translate("FirstFrame_v_name_text_tip", ""))
        self.v_name_text.setPlaceholderText(
            _translate("FirstFrame_v_name_text_sample", "例:3d"))
        self.v_noccu_text.setToolTip(
            _translate("FirstFrame_v_noccu_text_tip", ""))
        self.v_noccu_text.setPlaceholderText(
            _translate("FirstFrame_v_noccu_text_sample", "例:10"))
        self.c_name_text.setToolTip(
            _translate("FirstFrame_c_name_text_tip", ""))
        self.c_name_text.setPlaceholderText(
            _translate("FirstFrame_c_name_text_sample", "例:1s"))
        self.c_noccu_text.setToolTip(
            _translate("FirstFrame_c_noccu_text_tip", ""))
        self.c_noccu_text.setPlaceholderText(
            _translate("FirstFrame_c_noccu_text_sample", "例:1"))
        self.v_soc_text.setToolTip(
            _translate("FirstFrame_v_soc_text_tip", "(initial, intermediate)"))
        self.v_soc_text.setPlaceholderText(
            _translate("FirstFrame_v_soc_text_sample", "例:0.1;0.1"))
        self.c_soc_text.setToolTip(
            _translate("FirstFrame_c_soc_text_tip", ""))
        self.c_soc_text.setPlaceholderText(
            _translate("FirstFrame_c_soc_text_sample", "例:0.0"))

        self.shell_level_v_text.setToolTip(
            _translate("FirstFrame_shell_level_v_text_tip", ""))
        self.shell_level_v_text.setPlaceholderText(
            _translate("FirstFrame_shell_level_v_text_sample", "例:0.1"))
        self.shell_level_c_text.setToolTip(
            _translate("FirstFrame_shell_level_c_text_tip", ""))
        self.shell_level_c_text.setPlaceholderText(
            _translate("FirstFrame_shell_level_c_text_sample", "例:0.1"))

        self.slater_initial_Fx_vv_text.setToolTip(
            _translate("FirstFrame_slater_initial_Fx_vv_text_tip", ""))
        self.slater_initial_Fx_vv_text.setPlaceholderText(
            _translate("FirstFrame_slater_initial_Fx_vv_text_sample", "例:1.2;1.2;..."))
        self.slater_initial_Fx_vc_text.setToolTip(
            _translate("FirstFrame_slater_initial_Fx_vc_text_tip", ""))
        self.slater_initial_Fx_vc_text.setPlaceholderText(
            _translate("FirstFrame_slater_initial_Fx_vc_text_sample", "例:1.2;1.2;..."))
        self.slater_initial_Gx_vc_text.setToolTip(
            _translate("FirstFrame_slater_initial_Gx_vc_text_tip", ""))
        self.slater_initial_Gx_vc_text.setPlaceholderText(
            _translate("FirstFrame_slater_initial_Gx_vc_text_sample", "例:1.2;1.2;..."))
        self.slater_initial_Fx_cc_text.setToolTip(
            _translate("FirstFrame_slater_initial_Fx_cc_text_tip", ""))
        self.slater_initial_Fx_cc_text.setPlaceholderText(
            _translate("FirstFrame_slater_initial_Fx_cc_text_sample", "例:1.2;1.2-..."))

        self.slater_intermediate_Fx_vv_text.setToolTip(
            _translate("FirstFrame_slater_intermediate_Fx_vv_text_tip", ""))
        self.slater_intermediate_Fx_vv_text.setPlaceholderText(
            _translate("FirstFrame_slater_intermediate_Fx_vv_text_sample", "例:1.2;1.2-..."))
        self.slater_intermediate_Fx_vc_text.setToolTip(
            _translate("FirstFrame_slater_intermediate_Fx_vc_text_tip", ""))
        self.slater_intermediate_Fx_vc_text.setPlaceholderText(
            _translate("FirstFrame_slater_intermediate_Fx_vc_text_sample", "例:1.2;1.2-..."))
        self.slater_intermediate_Gx_vc_text.setToolTip(
            _translate("FirstFrame_slater_intermediate_Gx_vc_text_tip", ""))
        self.slater_intermediate_Gx_vc_text.setPlaceholderText(
            _translate("FirstFrame_slater_intermediate_Gx_vc_text_sample", "例:1.2;1.2-..."))
        self.slater_intermediate_Fx_cc_text.setToolTip(
            _translate("FirstFrame_slater_intermediate_Fx_cc_text_tip", ""))
        self.slater_intermediate_Fx_cc_text.setPlaceholderText(
            _translate("FirstFrame_slater_intermediate_Fx_cc_text_sample", "例:1.2;1.2;..."))

        self.buttonAddToAtomList.setToolTip(
            _translate("FirstFrame_add_to_atom_list_button_tip", "添加到列表中"))

        self.atom_list_menu_import_action.setToolTip(  # 这个好像没用
            _translate("FirstFrame_atom_list_menu_import_action_tip", "导入选中元素"))
        self.atom_list_menu_delete_action.setToolTip(  # 这个好像没用
            _translate("FirstFrame_atom_list_menu_delete_action_tip", "删除选中元素"))

        self.atom_list_save_button.setToolTip(
            _translate("FirstFrame_atom_list_save_button_tip", "保存列表"))
        self.atom_list_load_button.setToolTip(
            _translate("FirstFrame_atom_list_load_button_tip", "加载列表"))

        for text in self.v1_ext_B_texts:
            text.setToolTip(
                _translate("FirstFrame_v1_ext_B_texts_tip", ""))
            text.setPlaceholderText(
                _translate("FirstFrame_v1_ext_B_texts_sample", "例:1.0"))

        self.v1_on_which_text.setToolTip(
            _translate("FirstFrame_v1_on_which_text_tip", ""))
        self.v1_on_which_text.setPlaceholderText(
            _translate("FirstFrame_v1_on_which_text_sample", "例:spin"))

        self.v1_cfmt_menu_update_action.setToolTip(
            _translate("FirstFrame_v1_cfmt_update_action_tip", "更新矩阵维度"))

        for row in self.v1_cfmt_para_texts:  # 这只是初始化，后续如果更新矩阵的话要重新设置一遍
            for lineEdit in row:
                lineEdit.setToolTip(
                    _translate("FirstFrame_v1_cfmt_para_texts_tip", ""))
                lineEdit.setPlaceholderText(
                    _translate("FirstFrame_v1_cfmt_para_texts_sample", "例:1.0"))

        for row in self.v1_othermat_para_texts:  # 这只是初始化，后续如果更新矩阵的话要重新设置一遍
            for lineEdit in row:
                lineEdit.setToolTip(
                    _translate("FirstFrame_v1_othermat_para_texts_tip", ""))
                lineEdit.setPlaceholderText(
                    _translate("FirstFrame_v1_othermat_para_texts_sample", "例:1.0"))

        for row in self.local_axis_texts:
            for lineEdit in row:
                lineEdit.setToolTip(
                    _translate("FirstFrame_local_axis_texts_tip", ""))
                lineEdit.setPlaceholderText(
                    _translate("FirstFrame_local_axis_texts_sample", "例:1.0"))

        self.verbose_text.setToolTip(
            _translate("FirstFrame_verbose_text_tip", ""))
        self.verbose_text.setPlaceholderText(
            _translate("FirstFrame_verbose_text_sample", "例:0"))

        self.diagonalize_by_python_button.setToolTip(
            _translate("FirstFrame_diagonalize_by_python_button_tip", "by python"))
        self.diagonalize_by_fortan_button.setToolTip(
            _translate("FirstFrame_diagonalize_by_fortan_button_tip", "by fortan"))

    def _retranslateNames(self):
        _translate = QtCore.QCoreApplication.translate

        self.atom_name_label.setText(
            _translate("FirstFrame_atom_name_label", "atom_name"))
        self.v_name_label.setText(
            _translate("FirstFrame_v_name_label", "v_name"))
        self.v_noccu_label.setText(
            _translate("FirstFrame_v_noccu_label", "v_noccu"))
        self.c_name_label.setText(
            _translate("FirstFrame_c_name_label", "c_name"))
        self.c_noccu_label.setText(
            _translate("FirstFrame_c_noccu_label", "c_noccu"))
        self.v_soc_label.setText(
            _translate("FirstFrame_v_soc_label", "v_soc"))
        self.c_soc_label.setText(
            _translate("FirstFrame_c_soc_label", "c_soc"))
        self.shell_level_v_label.setText(
            _translate("FirstFrame_shell_level_v_label", "shell_level_v"))
        self.shell_level_c_label.setText(
            _translate("FirstFrame_shell_level_c_label", "shell_level_c"))

        self.slater_initial_box.setTitle(
            _translate("FirstFrame_slater_initial_box_title", "vc_slater_integrals_initial"))
        self.slater_initial_Fx_vv_label.setText(
            _translate("FirstFrame_slater_initial_Fx_vv_label", "Fx_vv"))
        self.slater_initial_Fx_vc_label.setText(
            _translate("FirstFrame_slater_initial_Fx_vc_label", "Fx_vc"))
        self.slater_initial_Gx_vc_label.setText(
            _translate("FirstFrame_slater_initial_Gx_vc_label", "Gx_vc"))
        self.slater_initial_Fx_cc_label.setText(
            _translate("FirstFrame_slater_initial_Fx_cc_label", "Fx_cc"))

        self.slater_intermediate_box.setTitle(
            _translate("FirstFrame_slater_intermediate_box_title", "vc_slater_integrals_intermediate"))
        self.slater_intermediate_Fx_vv_label.setText(
            _translate("FirstFrame_slater_intermediate_Fx_vv_label", "Fx_vv"))
        self.slater_intermediate_Fx_vc_label.setText(
            _translate("FirstFrame_slater_intermediate_Fx_vc_label", "Fx_vc"))
        self.slater_intermediate_Gx_vc_label.setText(
            _translate("FirstFrame_slater_intermediate_Gx_vc_label", "Gx_vc"))
        self.slater_intermediate_Fx_cc_label.setText(
            _translate("FirstFrame_slater_intermediate_Fx_cc_label", "Fx_cc"))

        self.buttonAddToAtomList.setText(
            _translate("FirstFrame_add_to_atom_list_button_label", "add to ->"))

        self.atom_list_menu_import_action.setText(
            _translate("FirstFrame_atom_list_menu_import_action_name", "import"))
        self.atom_list_menu_delete_action.setText(
            _translate("FirstFrame_atom_list_menu_delete_action_name", "delete"))
        self.atom_list_save_button.setText(
            _translate("FirstFrame_atom_list_save_button_label", "save"))
        self.atom_list_load_button.setText(
            _translate("FirstFrame_atom_list_load_button_label", "load"))

        self.v1_ext_B_label.setText(
            _translate("FirstFrame_v1_ext_B_label", "v1_ext_B"))

        self.v1_on_which_label.setText(
            _translate("FirstFrame_v1_on_which_label", "v1_on_which"))

        self.v1_cfmt_box.setTitle(
            _translate("FirstFrame_v1_cfmt_box_title", "v_cfmt"))
        self.v1_cfmt_menu_update_action.setText(
            _translate("FirstFrame_v1_cfmt_update_action_name", "update"))
        self.v1_othermat_box.setTitle(
            _translate("FirstFrame_v1_othermat_box_title", "v_othermat"))
        self.v1_othermat_menu_update_action.setText(
            _translate("FirstFrame_v1_othermat_update_action_name", "update"))

        self.local_axis_box.setTitle(
            _translate("FirstFrame_local_axis_box_title", "local_axis"))

        self.verbose_label.setText(
            _translate("FirstFrame_verbose_label", "verbose"))

        self.diagonalize_box.setTitle(
            _translate("FirstFrame_diagonalize_box_title", "diagonalize and compute"))

        self.diagonalize_by_python_button.setText(
            _translate("FirstFrame_diagonalize_by_python_button_label", "python"))
        self.diagonalize_by_fortan_button.setText(
            _translate("FirstFrame_diagonalize_by_fortan_button_label", "fortan"))

        self.firstPageOutputBox.setTitle(
            _translate("FirstFrame_firstPageOutputBox_title", "output"))

    def _retranslateDynamicly(self):
        # 这个不在初始化时调用了，在后续动态更新中被调用
        _translate = QtCore.QCoreApplication.translate
        for row in self.v1_cfmt_para_texts:  # 后续如果更新矩阵的话要重新设置一遍
            for lineEdit in row:
                lineEdit.setToolTip(
                    _translate("FirstFrame_v1_cfmt_para_texts_tip", ""))
                lineEdit.setPlaceholderText(
                    _translate("FirstFrame_v1_cfmt_para_texts_sample", "例:1.0"))

        for row in self.v1_othermat_para_texts:  # 后续如果更新矩阵的话要重新设置一遍
            for lineEdit in row:
                lineEdit.setToolTip(
                    _translate("FirstFrame_v1_othermat_para_texts_tip", ""))
                lineEdit.setPlaceholderText(
                    _translate("FirstFrame_v1_othermat_para_texts_sample", "例:1.0"))

    def _textInputRestrict(self):
        forOnWhichRegx = QtCore.QRegExp(r"spin|orbital|both")
        forOnWhichRegxValidator = QtGui.QRegExpValidator(forOnWhichRegx, self.frame)

        self.atom_name_text.setValidator(self.ncRegxValidator)  # 元素名也用这个吧

        self.v_name_text.setValidator(self.ncRegxValidator)
        self.c_name_text.setValidator(self.ncRegxValidator)

        self.v_noccu_text.setValidator(self.npRegxValidator)
        self.c_noccu_text.setValidator(self.npRegxValidator)

        self.v_soc_text.setValidator(self.twoFloatRegxValidator)
        self.c_soc_text.setValidator(self.floatRegxValidator)
        self.shell_level_v_text.setValidator(self.floatRegxValidator)
        self.shell_level_c_text.setValidator(self.floatRegxValidator)

        self.slater_initial_Fx_vv_text.setValidator(self.floatListRegxValidator)
        self.slater_initial_Fx_vc_text.setValidator(self.floatListRegxValidator)
        self.slater_initial_Gx_vc_text.setValidator(self.floatListRegxValidator)
        self.slater_initial_Fx_cc_text.setValidator(self.floatListRegxValidator)
        self.slater_intermediate_Fx_vv_text.setValidator(self.floatListRegxValidator)
        self.slater_intermediate_Fx_vc_text.setValidator(self.floatListRegxValidator)
        self.slater_intermediate_Gx_vc_text.setValidator(self.floatListRegxValidator)
        self.slater_intermediate_Fx_cc_text.setValidator(self.floatListRegxValidator)

        for text in self.v1_ext_B_texts:
            text.setValidator(self.floatRegxValidator)

        self.v1_on_which_text.setValidator(forOnWhichRegxValidator)

        for row in self.v1_cfmt_para_texts:  # 这里只是初始化，后续如果更新矩阵的话要重新设置一遍
            for lineEdit in row:
                lineEdit.setValidator(self.floatRegxValidator)
        for row in self.v1_othermat_para_texts:  # 这里只是初始化，后续如果更新矩阵的话要重新设置一遍
            for lineEdit in row:
                lineEdit.setValidator(self.floatRegxValidator)

        for row in self.local_axis_texts:
            for lineEdit in row:
                lineEdit.setValidator(self.floatRegxValidator)

        self.verbose_text.setValidator(self.intRegxValidator)

    def _textInputRestrictDyanmicly(self):
        for row in self.v1_cfmt_para_texts:  # 后续如果更新矩阵的话要重新设置一遍
            for lineEdit in row:
                lineEdit.setValidator(self.floatRegxValidator)
        for row in self.v1_othermat_para_texts:  # 后续如果更新矩阵的话要重新设置一遍
            for lineEdit in row:
                lineEdit.setValidator(self.floatRegxValidator)

    def _arrangeDataInWidgets(self):
        # 在各个页面都设置好之后调用这个
        # 把各个需要获取输入的控件(或其上数据)加入字典中，同时指定解析方式
        # 方便之后从界面获取输入
        super()._bindDataWithWidgets("v_name", self.v_name_text, self._toSimpleStrFromText)
        super()._bindDataWithWidgets("v_noccu", self.v_noccu_text, self._toIntFromText)
        super()._bindDataWithWidgets("c_name", self.c_name_text, self._toSimpleStrFromText)
        super()._bindDataWithWidgets("c_noccu", self.c_noccu_text, self._toIntFromText)
        super()._bindDataWithWidgets("v_soc", self.v_soc_text, self._toFloatListByStrFromText)  # float-float, (initial, optional[imtermediate])
        super()._bindDataWithWidgets("c_soc", self.c_soc_text, self._toFloatFromText)
        super()._bindDataWithWidgets("shell_level_v", self.shell_level_v_text, self._toFloatFromText)
        super()._bindDataWithWidgets("shell_level_c", self.shell_level_c_text, self._toFloatFromText)
        super()._bindDataWithWidgets("atom_name", self.atom_name_text, self._toSimpleStrFromText)

        super()._bindDataWithWidgets("slater_Fx_vv_initial", self.slater_initial_Fx_vv_text, self._toFloatListByStrFromText)
        super()._bindDataWithWidgets("slater_Fx_vc_initial", self.slater_initial_Fx_vc_text, self._toFloatListByStrFromText)
        super()._bindDataWithWidgets("slater_Gx_vc_initial", self.slater_initial_Gx_vc_text, self._toFloatListByStrFromText)
        super()._bindDataWithWidgets("slater_Fx_cc_initial", self.slater_initial_Fx_cc_text, self._toFloatListByStrFromText)
        super()._bindDataWithWidgets("slater_Fx_vv_intermediate", self.slater_intermediate_Fx_vv_text, self._toFloatListByStrFromText)
        super()._bindDataWithWidgets("slater_Fx_vc_intermediate", self.slater_intermediate_Fx_vc_text, self._toFloatListByStrFromText)
        super()._bindDataWithWidgets("slater_Gx_vc_intermediate", self.slater_intermediate_Gx_vc_text, self._toFloatListByStrFromText)
        super()._bindDataWithWidgets("slater_Fx_cc_intermediate", self.slater_intermediate_Fx_cc_text, self._toFloatListByStrFromText)

        super()._bindDataWithWidgets("v1_ext_B", self.v1_ext_B_texts, self._toFloatListByWidgets_1DFromText)
        super()._bindDataWithWidgets("v1_on_which", self.v1_on_which_text, self._toSimpleStrFromText)

        super()._bindDataWithWidgets("v1_cfmt", self.v1_cfmt_para_texts, self._toFloatListByWidgets_2DFromText)
        super()._bindDataWithWidgets("v1_othermat", self.v1_othermat_para_texts, self._toFloatListByWidgets_2DFromText)
        super()._bindDataWithWidgets("local_axis", self.local_axis_texts, self._toFloatListByWidgets_2DFromText)

    def _verifyValidAtomData(self):
        # 如果验证通过，可以加入到列表中
        verified = True

        v_name = super()._getDataFromInupt("v_name")
        v_noccu = super()._getDataFromInupt("v_noccu")  # int
        v_soc = super()._getDataFromInupt("v_soc")  # float-[float], first one not empty

        if v_name is None or v_noccu is None or v_soc is None:
            verified = False

        return verified

    def _getAtomDataFromInput(self) -> AtomBasicData or None:
        # 这个获取的不是用来计算的，是用来保存的，所以一些参数只取initial
        if not self._verifyValidAtomData():
            self.informMsg("信息不完整，请检查")
            return None
        # 如果信息完整，进行保存，可能还要查重，默认同名就是直接修改了，就不查重了
        v_name = super()._getDataFromInupt("v_name")
        v_noccu = super()._getDataFromInupt("v_noccu")  # int
        c_name = super()._getDataFromInupt("c_name")
        c_noccu = super()._getDataFromInupt("c_noccu")  # int
        v_soc = super()._getDataFromInupt("v_soc")  # float-float, take the first
        c_soc = super()._getDataFromInupt("c_soc")  # float
        slater_Fx_vv = super()._getDataFromInupt("slater_Fx_vv_initial")  # float-float-...
        slater_Fx_vc = super()._getDataFromInupt("slater_Fx_vc_initial")  # float-float-...
        slater_Gx_vc = super()._getDataFromInupt("slater_Gx_vc_initial")  # float-float-...
        slater_Fx_cc = super()._getDataFromInupt("slater_Fx_cc_initial")  # float-float-...

        atomData = AtomBasicData(
            v_name=v_name,
            v_noccu=v_noccu,
            c_name=c_name,
            c_noccu=c_noccu,
            slater_Fx_vv=slater_Fx_vv,
            slater_Fx_vc=slater_Fx_vc,
            slater_Gx_vc=slater_Gx_vc,
            slater_Fx_cc=slater_Fx_cc,
            v_soc=v_soc[0],  # 只取第一个initial
            c_soc=c_soc
        )
        return atomData

    def _getItemFromAtomData(self, parent, atomData: AtomBasicData) -> QListWidgetItem:
        item = QListWidgetItem(parent)
        itemName = DataManager.getNameFromAtomData(atomData)
        item.setText(itemName)  # 默认这个name非空，需要在获取item前自行检查
        # 之后就根据这个name去数据中找相应的数据
        return item

    def _setInterfaceByAtomData(self, data: AtomBasicData):
        if data is None:
            return
        self.v_name_text.setText("" if data.v_name is None else data.v_name)
        self.v_noccu_text.setText("" if data.v_noccu is None else str(data.v_noccu))
        self.c_name_text.setText("" if data.c_name is None else data.c_name)
        self.c_noccu_text.setText("" if data.c_noccu is None else str(data.c_noccu))
        self.v_soc_text.setText("" if data.v_soc is None else str(data.v_soc))
        self.c_soc_text.setText("" if data.c_soc is None else str(data.c_soc))

        temp = ""
        if data.slater_Fx_vv is not None:
            for i in range(len(data.slater_Fx_vv)):
                if i > 0:
                    temp += ";"
                temp += str(data.slater_Fx_vv[i])
        self.slater_initial_Fx_vv_text.setText(temp)
        temp = ""
        if data.slater_Fx_vc is not None:
            for i in range(len(data.slater_Fx_vc)):
                if i > 0:
                    temp += ";"
                temp += str(data.slater_Fx_vc[i])
        self.slater_initial_Fx_vc_text.setText(temp)
        temp = ""
        if data.slater_Gx_vc is not None:
            for i in range(len(data.slater_Gx_vc)):
                if i > 0:
                    temp += ";"
                temp += str(data.slater_Gx_vc[i])
        self.slater_initial_Gx_vc_text.setText(temp)
        temp = ""
        if data.slater_Fx_cc is not None:
            for i in range(len(data.slater_Fx_cc)):
                if i > 0:
                    temp += ";"
                temp += str(data.slater_Fx_cc[i])
        self.slater_initial_Fx_cc_text.setText(temp)
        # intermediate 的数据应该不用加载

    def _handleOnAddToAtomList(self):
        atomData = self._getAtomDataFromInput()
        if atomData is None:  # 获取失败
            return
        if self.dataManager.addAtomData(atomData) is False:
            self.informMsg("信息不完整或有误，请检查")
            return
        item = self._getItemFromAtomData(self.atom_list, atomData)
        # 遍历atom_list看有没有同名的，有的话先删除
        row = 0
        while row < self.atom_list.count():
            if self.atom_list.item(row).text() == item.text():
                break
            row += 1
        if row != self.atom_list.count():
            # 已经存在同名的，先删除旧的
            self.atom_list.takeItem(row)
        self.atom_list.addItem(item)
        self.atom_list.sortItems()
        self.atom_list.setCurrentItem(item)  # 排过序之后可能不是原先的位置了，重新设置一下

    def _handleOnDeleteFromAtomList(self) -> bool:
        item = self.atom_list.currentItem()
        if item is None:
            return False
        row = self.atom_list.row(item)
        self.atom_list.takeItem(row)
        # 把dataManager中的也删了吧
        self.dataManager.atomBasicDataList[item.text()] = None
        # print(item.text())
        return True

    def _handleOnImportAtomFromList(self, item: QListWidgetItem):
        data = self.dataManager.getAtomDataByName(item.text())
        if data is None:  # 应该不会到这里，加入列表的时候存在，这个选择又只能选择列表中的，应该不会不存在
            self.informMsg(f"导入数据失败，未找到:{item.text()}")
            return
        # 根据数据设置界面
        self._setInterfaceByAtomData(data)

    def _handleOnSaveAtomList(self):
        self.informMsg("not implemented yet")
        # TODO:to implement

    def _handleOnLoadAtomList(self):
        self.informMsg("not implemented yet")
        # TODO:to implement

    def _handleOnDiagonalizeAndComputeByPython(self):
        self.informMsg("not implemented yet")
        # TODO:to implement

    def _handleOnDiagonalizeAndComputeByFortan(self):
        self.informMsg("not implemented yet")
        # TODO:to implement
