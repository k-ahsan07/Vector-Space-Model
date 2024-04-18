import sys
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)

import Assign2

########################   MAIN WINDOW    ########################################

class PersonalInfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle('Personal Information')
        self.setGeometry(300, 300, 900, 500)

        # Set background color
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(128, 128, 128))
        palette.setColor(QPalette.Button, QColor(128, 128, 128))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        self.setPalette(palette)

        # Create a widget to hold the labels and line edits
        widget = QWidget()
        self.setCentralWidget(widget)

        # Create a vertical layout for the widget
        layout = QVBoxLayout()
        widget.setLayout(layout)

        info_label = QLabel('K213328 Khuzaima Ahsan')
        info_label.setStyleSheet('color: black; font-size: 25px;')
        layout.addWidget(info_label)

        info_label = QLabel('Information Reterival')
        info_label.setStyleSheet('color: black; font-size: 25px; ')
        layout.addWidget(info_label)

        info_label = QLabel('Assignment: 02')
        info_label.setStyleSheet('color: black; font-size: 25px; ')
        layout.addWidget(info_label)

        # Create a button to proceed to the query page
        proceed_button = QPushButton('Proceed to Query')
        proceed_button.setStyleSheet('color: black')
        proceed_button.clicked.connect(self.show_query_window)
        layout.addWidget(proceed_button)

    def show_query_window(self):
        self.query_window = QueryWindow()
        self.query_window.show()
        self.hide()


########################   QUERY WINDOW    ########################################

class QueryWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle('Query Page')
        self.setGeometry(300, 300, 900, 500)

        # Set background color
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(128, 128, 128))
        palette.setColor(QPalette.Button, QColor(128, 128, 128))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        self.setPalette(palette)

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout()
        widget.setLayout(layout)


        query_layout = QHBoxLayout()
        layout.addLayout(query_layout)

        self.query_label = QLabel('Enter a query:')
        self.query_label.setStyleSheet('color: white')
        query_layout.addWidget(self.query_label)

        self.query_edit = QLineEdit()
        self.query_edit.setStyleSheet('background-color: white')
        query_layout.addWidget(self.query_edit)

        # Create a button to process the query
        self.query_button = QPushButton('Process Query')
        self.query_button.setStyleSheet('color: black')
        self.query_button.clicked.connect(self.push_button)
        layout.addWidget(self.query_button)

        # Create a label to display result
        self.result_label = QLabel()
        self.result_label.setStyleSheet('color: white')
        self.result_label.setWordWrap(True)
        layout.addWidget(self.result_label)

    def push_button(self):
        query = self.query_edit.text()
        result, time_taken = Assign2.processQuery(query)
        time_taken = str(time_taken*1000)

        if len(result) == 0:
            self.result_label.setText("Result: No results found\nTime taken: "+time_taken+" ms")
        else:
            self.result_label.setText("Result: "+str(result)+"\nTime taken: "+time_taken+" ms")


if __name__ == '__main__':
    # Process docs at the start of application
    Assign2.processDocs()

    # Create instances of both windows
    app = QApplication(sys.argv)
    personal_info_window = PersonalInfoWindow()

    # Show the personal info window
    personal_info_window.show()

    sys.exit(app.exec_())
