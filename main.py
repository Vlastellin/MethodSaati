import sys
from PyQt5 import QtWidgets, QtCore
import GUI
import output
import FindSolution_f


class AppStart(QtWidgets.QDialog, GUI.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self._translate = QtCore.QCoreApplication.translate
        self.setupUi(self)
        self.dialogs = list()
        self.index_val = [1, 3, 5, 7, 9, 1/3, 1/5, 1/7, 1/9]
        self.krt_combobox = [self.comboBox, self.comboBox_2, self.comboBox_6, self.comboBox_3, self.comboBox_5, self.comboBox_4]
        self.obj_combobox = [[self.comboBox_9, self.comboBox_10, self.comboBox_12], [self.comboBox_14, self.comboBox_11, self.comboBox_13], [self.comboBox_17, self.comboBox_16, self.comboBox_15], [self.comboBox_20, self.comboBox_19, self.comboBox_18]]
        self.text_edits = [self.textEdit, self.textEdit_2, self.textEdit_3, self.textEdit_4, self.textEdit_7, self.textEdit_6, self.textEdit_5]
        self.labels = [[self.label_5, self.tab_2], [self.label_6, self.tab_3], [self.label_7, self.tab_4], [self.label_8, self.tab_5], [self.label_16, self.label_17, self.label_21, self.label_27, self.label_18, self.label_23, self.label_29], [self.label_12, self.label_10, self.label_22, self.label_28, self.label_13, self.label_24, self.label_30], [self.label_11, self.label_19, self.label_25, self.label_31, self.label_20, self.label_26, self.label_32]]
        self.textEdit.textChanged.connect(self.change_text)
        self.textEdit_2.textChanged.connect(self.change_text)
        self.textEdit_3.textChanged.connect(self.change_text)
        self.textEdit_4.textChanged.connect(self.change_text)
        self.textEdit_5.textChanged.connect(self.change_text)
        self.textEdit_6.textChanged.connect(self.change_text)
        self.textEdit_7.textChanged.connect(self.change_text)
        self.pushButton.clicked.connect(self.output_window)

    def output_window(self):
        criteria_relationship = list()
        objects_relationship = list()
        for item in self.krt_combobox:
            criteria_relationship.append(self.index_val[item.currentIndex()])
        for li in self.obj_combobox:
            objects = list()
            for item in li:
                objects.append(self.index_val[item.currentIndex()])
            objects_relationship.append(objects)
        final_list, final_percent_list, max_id = FindSolution_f.FindSolution(criteria_relationship, objects_relationship)
        window = Output(final_list, final_percent_list, max_id)
        self.dialogs.append(window)
        window.show()

    def change_text(self):
        for i in range(len(self.text_edits)):
            if self.text_edits[i].toPlainText() == "":
                pass
            else:
                for elem in self.labels[i]:
                    if type(elem) == type(self.label):
                        elem.setText(self.text_edits[i].toPlainText())
                    else:
                        self.tabWidget.setTabText(self.tabWidget.indexOf(elem), self._translate("Dialog", self.text_edits[i].toPlainText()))


class Output(QtWidgets.QDialog, output.Ui_Dialog):
    def __init__(self, final_list, final_percent_list, max_id):
        for i in range(len(final_list)):
            final_list[i] = round(final_list[i], 3)
        for i in range(len(final_percent_list)):
            final_percent_list[i] = round(final_percent_list[i], 3)
        super().__init__()
        self.setupUi(self)
        self.label.setText("Конечные веса вариантов выбора:\n {}".format(final_list))
        self.label_2.setText("Конечные веса вариантов выбора в процентах:\n {}".format(final_percent_list))
        self.label_3.setText("Номер самого выгодного варианта:\n {}".format(int(max_id)+1))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AppStart()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
