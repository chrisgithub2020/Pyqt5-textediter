from PyQt5.QtWidgets import QApplication, QColorDialog, QFileDialog, QMainWindow, QStyleFactory
from PyQt5.QtGui import QFont, QTextBlock, QTextBlockFormat, QTextCharFormat, QTextTableFormat,QTextLength,QTextFrameFormat
from PyQt5.QtCore import Qt
from main_win import Ui_MainWindow
import utils
from insert_table import mainDialog

QApplication.setStyle(QStyleFactory.create('Fusion'))


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_widget_to_action()

    def connect_widget_to_action(self):
        ## CONNECT WIDGET TO ACTIONS
        self.ui.tabWidget.currentChanged.connect(self.switch_stacked_page)
        self.ui.textcolour_button.clicked.connect(self.textColour)
        self.ui.Bold_button.clicked.connect(self.bold)
        self.ui.subscript_button.clicked.connect(self.subscript)
        self.ui.superscript_button.clicked.connect(self.superscript)
        self.ui.italic_button.clicked.connect(self.italic_func)
        self.ui.strikeout_button.clicked.connect(self.strike_through)
        self.ui.underline_button.clicked.connect(self.underline_func)
        self.ui.back_button.clicked.connect(self.reset_screen)
        self.ui.insert_image_button.clicked.connect(self.insert_img)
        self.ui.save_button.clicked.connect(self.save_file)
        self.ui.insert_table_button.clicked.connect(self.insert_table)

        # Sets alignment buttons to function
        self.ui.align_center_button.clicked.connect(lambda: self.ui.textEdit.setAlignment(Qt.AlignCenter))
        self.ui.align_justify_button.clicked.connect(lambda: self.ui.textEdit.setAlignment(Qt.AlignJustify))
        self.ui.align_left_button.clicked.connect(lambda: self.ui.textEdit.setAlignment(Qt.AlignLeft))
        self.ui.align_right_button.clicked.connect(lambda: self.ui.textEdit.setAlignment(Qt.AlignRight))

    def bold(self):
        ## FUNCTION FOR BOLD BUTTON
        if self.ui.textEdit.fontWeight() == 50:
            self.ui.textEdit.setFontWeight(75)
        elif self.ui.textEdit.fontWeight() == 75:
            self.ui.textEdit.setFontWeight(50)

    def switch_stacked_page(self):
        ## FUNCTION TO SWITCH STACKED WIDGET WHEN USER CLICKS ON THE 'FILE' TAB
        if self.ui.tabWidget.currentIndex() == 0:
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            pass

    def textColour(self):
        ## FUNCTION TO CHANGE TEXT COLOUR
        colour_palette = QColorDialog.getColor()
        self.ui.textEdit.setTextColor(colour_palette)

    def subscript(self):
        ## FUNCTION TO ALLOW USER TO TOGGLE BETWEEN SUBSCRIPT AND NORMAL TEXT
        fxt = self.ui.textEdit.currentCharFormat()
        align = fxt.verticalAlignment()
        if align == QTextCharFormat.AlignNormal:
            fxt.setVerticalAlignment(QTextCharFormat.AlignSubScript)
        else:
            fxt.setVerticalAlignment(QTextCharFormat.AlignNormal)
        self.ui.textEdit.setCurrentCharFormat(fxt)

    def superscript(self):
        ## FUNCTION TO ALLOW USER TO TOGGLE BETWEEN SUPERSCRIPT AND NORMAL TEXT
        fxt = self.ui.textEdit.currentCharFormat()
        align = fxt.verticalAlignment()
        if align == QTextCharFormat.AlignNormal:
            fxt.setVerticalAlignment(QTextCharFormat.AlignSuperScript)
        else:
            fxt.setVerticalAlignment(QTextCharFormat.AlignNormal)
        self.ui.textEdit.setCurrentCharFormat(fxt)

    def italic_func(self):
        ## FUNCTION THAT ALLOWS USER TO ITALICISE TEXT
        italic_format = self.ui.textEdit.fontItalic()
        if italic_format == False:
            self.ui.textEdit.setFontItalic(True)
        else:
            self.ui.textEdit.setFontItalic(False)

    def strike_through(self):
        fmt = self.ui.textEdit.currentCharFormat()
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        self.ui.textEdit.setCurrentCharFormat(fmt)

    def underline_func(self):
        """
        This function checks if the fontUnderline property. If fontUnderline is True the sets it to False and vise versa.
        """
        ## FUNCTION THAT ALLOWS USERS TO UNDERLINE TEXT
        underline_format = self.ui.textEdit.fontUnderline()
        if underline_format == False:
            self.ui.textEdit.setFontUnderline(True)
        else:
            self.ui.textEdit.setFontUnderline(False)


    def reset_screen(self):
        self.ui.tabWidget.setCurrentIndex(1)
        self.ui.stackedWidget.setCurrentIndex(0)

    def insert_img(self):
        try:
            img_path = QFileDialog.getOpenFileName(self, 'Select Image',"",'Images(*.png)')
            kof = utils.pil_image_to_base64(img_path[0])
            self.ui.textEdit.insertHtml('<img src="data:image/png;base64,'+''+ kof+' ,alt=Red Dot'+'/>')
        except FileNotFoundError:
            print('File Not Found')

    def save_file(self):
        file_path = QFileDialog.getSaveFileName(self, 'Save As')

    def insert_table(self):
        self.param = mainDialog()
        table_format = QTextTableFormat()
        table_format.setWidth(QTextLength(QTextLength.PercentageLength,50))
        table_format.setAlignment(Qt.AlignCenter)
        table_format.setCellPadding(5)
        table_format.setCellSpacing(0)
        ret = self.param.exec_()

        if ret == 1:
            if self.param.border_style == 'Dotted':
                table_format.setBorderStyle(QTextFrameFormat.BorderStyle_Dotted)
            elif self.param.border_style == 'Groove':
                table_format.setBorderStyle(QTextFrameFormat.BorderStyle_Groove)
            elif self.param.border_style == 'Dashed':
                table_format.setBorderStyle(QTextFrameFormat.BorderStyle_Dashed)
            elif self.param.border_style == 'DotDotDash':
                table_format.setBorderStyle(QTextFrameFormat.BorderStyle_DotDotDash)
            elif self.param.border_style == 'DotDash':
                table_format.setBorderStyle(QTextFrameFormat.BorderStyle_DotDash)
            elif self.param.border_style == 'Double':
                table_format.setBorderStyle(QTextFrameFormat.BorderStyle_Double)
            elif self.param.border_style == 'Inset':
                table_format.setBorderStyle(QTextFrameFormat.BorderStyle_Inset)
            elif self.param.border_style == 'None':
                table_format.setBorderStyle(QTextFrameFormat.BorderStyle_Inset)
            elif self.param.border_style == 'Outset':
                table_format.setBorderStyle(QTextFrameFormat.BorderStyle_Outset)
            elif self.param.border_style == 'Ridge':
                table_format.setBorderStyle(QTextFrameFormat.BorderStyle_Ridge)
            elif self.param.border_style == 'Solid':
                table_format.setBorderStyle(QTextFrameFormat.BorderStyle_Solid)

            if self.param.layout_Direction == 'Left To Right':
                table_format.setLayoutDirection(Qt.LeftToRight)
            elif self.param.layout_Direction == 'Right To Left':
                table_format.setLayoutDirection(Qt.RightToLeft)

            cursor = self.ui.textEdit.textCursor()
            cursor.insertTable(self.param.number_of_rows,self.param.number_of_columns,table_format)
            self.param.close()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainWin()
    main_window.show()
    sys.exit(app.exec_())