# Qt5 version 5.15.2
# PyQt5 version 5.15.2
# python version 3.8

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui


class OwnFrame:
    def __init__(self, parent, width=None, height=None):
        self.__frame = QFrame(parent)
        if width is not None:
            self.__frame.setFixedWidth(width)
        if height is not None:
            self.__frame.setFixedHeight(height)

        self._setup()

    def getFrame(self):
        return self.__frame

    def _setup(self):
        self._setupTextInputRestrict()
        self._setupDataInWidgets()

    @classmethod
    def _setupTextInputRestrict(cls):
        ncRegx = QtCore.QRegExp(r"[a-zA-Z\d]+")  # 匹配数字和字母的组合
        cls.ncRegxValidator = QtGui.QRegExpValidator(ncRegx)

        intRegx = QtCore.QRegExp(r"(^(?!0)\-?\d+)|0")  # 不以0开头除非是0，包含负数
        cls.intRegxValidator = QtGui.QRegExpValidator(intRegx)

        npRegx = QtCore.QRegExp(r"(^(?!0)\d+)|0")  # 不以0开头除非是0，不包含负数
        cls.npRegxValidator = QtGui.QRegExpValidator(npRegx)

        # .123或123.或123.123或0.123或0，其实0可以不单独写出来，但如果要在别的地方用还是要的
        # 有一种特殊情况要排除，就是只有一个'.'，这样是不能转换为浮点数的，要么默认这个为0，要么为非法输入
        # 单个'.'就认为是0了
        floatRegx = QtCore.QRegExp(r"(^(?!0)\-?\d*\.?\d*)|(^\-?(0\.)\d*)|0")
        cls.floatRegxValidator = QtGui.QRegExpValidator(floatRegx)
        # float;float;...
        # 是基于floatRegx改过来的，也有单个'.'的情况
        floatListRegx = QtCore.QRegExp(
            r"^(?!;)((((?!0)\-?\d*\.?\d*)|(\-?(0\.)\d*)|0);(?!;))*(((?!0)\-?\d*\.?\d*)|(\-?(0\.)\d*)|0)")
        cls.floatListRegxValidator = QtGui.QRegExpValidator(floatListRegx)

        # 两个浮点数，float-float
        twoFloatRegx = QtCore.QRegExp(
            r"^(?!;)((((?!0)\-?\d*\.?\d*)|(\-?(0\.)\d*)|0);(?!;))?(((?!0)\-?\d*\.?\d*)|(\-?(0\.)\d*)|0)")
        cls.twoFloatRegxValidator = QtGui.QRegExpValidator(twoFloatRegx)

    @classmethod
    def _toSimpleStrFromText(cls, text: str or QLineEdit) -> str or None:
        if type(text) is not str:
            text = text.text()
        return None if len(text) == 0 else text

    @classmethod
    def _toIntFromText(cls, text: str or QLineEdit) -> int or None:
        if type(text) is not str:
            text = text.text()
        try:
            res = None if len(text) == 0 else int(text)
        except ValueError:
            cls.informMsg("数据格式有错误:on to int")
            res = None
        return res

    @classmethod
    def _toFloatFromText(cls, text: str or QLineEdit) -> float or None:
        if type(text) is not str:
            text = text.text()
        try:
            res = None if len(text) == 0 else (0.0 if text == "." else float(text))
        except ValueError:
            cls.informMsg("数据格式有错误:on to float")
            res = None
        return res

    @classmethod
    def _toFloatListByStrFromText(cls, text: str or QLineEdit) -> list or None:
        if type(text) is not str:
            text = text.text()
        if len(text) > 0:
            str_list = text.split(";")
            res = []
            for ele in str_list:
                if len(ele) > 0:
                    temp = cls._toFloatFromText(ele)
                    if temp is None:
                        res = None
                        break
                    res.append(temp)
        else:
            res = None
        return res

    @classmethod
    def _toFloatListByWidgets_1DFromText(cls, widgets: list) -> list or None:
        if len(widgets) == 0:
            return None
        res = []
        for ele in widgets:
            res.append(cls._toFloatFromText(ele.text()))  # 可能得到None的元素，代表这个框没有输入，一些情况下没有输入默认为0，一些情况下有其他默认值
        return res

    @classmethod
    def _toFloatListByWidgets_2DFromText(cls, widgets: [[]]) -> [[]] or None:
        if len(widgets) == 0:
            return None
        res = []
        allNone = True
        for ele in widgets:
            temp = cls._toFloatListByWidgets_1DFromText(ele)
            if temp is not None:
                allNone = False
            res.append(temp)
        return None if allNone else res

    def _setupDataInWidgets(self):
        # 在各个页面都设置好之后调用这个
        # 把各个需要获取输入的控件(或其上数据)加入字典中，同时指定解析方式
        # 方便之后从界面获取输入
        self.widgetsWithData = {}  # key是代表名字的str，value是一个元组(widget, method to parse)

    def _bindDataWithWidgets(self, name: str, widget, parser):
        self.widgetsWithData[name] = (widget, parser)

    def _getDataFromInupt(self, dataName: str):
        # 根据数据名从界面相应组件获取数据
        # 用个字典来存下各个组件吧
        if dataName not in self.widgetsWithData.keys():
            self.informMsg(f"从widgetsWithData中获取数据时出错，错误的数据名:{dataName}")
            return None
        data_with_processor = self.widgetsWithData[dataName]
        return data_with_processor[1](data_with_processor[0])

    @classmethod
    def informMsg(cls, msg: str):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("inform")
        msgBox.setText(msg)
        msgBox.exec_()  # 模态

