from insert_table_ui import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QApplication, QStyleFactory

QApplication.setStyle(QStyleFactory.create('Fusion'))

class mainDialog(QDialog):
    def __init__(self):
        """
        initiates the maindialog class
        """
        super().__init__()
        self.d_ui = Ui_Dialog()
        self.d_ui.setupUi(self)
        self.add_borderStyle_options()

    def add_borderStyle_options(self):
        """
        This function add border style option so the user can choose from when inserting a table
        """
        borderStyle_list = ['Groove','Dotted','Dashed','DotDotDash','DotDash','Double','Inset','None','Outset','Ridge','Solid']
        layout_direction = ['Left To Right','Right To Left']
        self.d_ui.border_style_comboBox.addItems(borderStyle_list)
        self.d_ui.layout_directio_comboBox.addItems(layout_direction)

    def accept(self):
        """
        This function collects the selected rows and columns as a tuple
        """
        self.number_of_rows = self.d_ui.rows_spinbox.value()
        self.number_of_columns = self.d_ui.columns_spinbox.value()
        self.border_style = self.d_ui.border_style_comboBox.currentText()
        self.layout_Direction = self.d_ui.layout_directio_comboBox.currentText()
        super().accept()




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = mainDialog()
    ui.show()
    sys.exit(app.exec_())