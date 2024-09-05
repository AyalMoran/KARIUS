import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QPushButton,
                             QFormLayout, QWidget, QTableWidget, QTableWidgetItem, QCheckBox,
                             QHBoxLayout, QVBoxLayout, QStatusBar, QTextEdit)


class Karius(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle('Karius Dental App')
        self.setGeometry(100, 100, 3000, 700)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Create menu bar
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.edit_menu = self.menu_bar.addMenu("Edit")

        # Create actions for menu bar
        self.open_action = QtWidgets.QAction("Open", self)
        self.save_action = QtWidgets.QAction("Save", self)
        self.exit_action = QtWidgets.QAction("Exit", self)
        self.cut_action = QtWidgets.QAction("Cut", self)
        self.copy_action = QtWidgets.QAction("Copy", self)
        self.paste_action = QtWidgets.QAction("Paste", self)

        # Add actions to menu
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.exit_action)
        self.edit_menu.addAction(self.cut_action)
        self.edit_menu.addAction(self.copy_action)
        self.edit_menu.addAction(self.paste_action)

        # Create status bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Ready")

        ############################
        # Create table
        self.table = QTableWidget(2, 16, self.centralwidget)
        self.table.setGeometry(5, 5, 2450, 327)
        self.table.setHorizontalHeaderLabels(['1', '2', '3', '4', '5', '6', '7', '8',
                                              '9', '10', '11', '12', '13', '14', '15', '16'])
        self.table.setVerticalHeaderLabels(['Upper', 'Lower'])
        self.teeth_names = ['Third Molar', 'Second Molar', 'First Molar', 'Second Premolar',
                            'First Premolar', 'Canine', 'Lateral Incisor', 'Central Incisor',
                            'Central Incisor', 'Lateral Incisor', 'Canine', 'First Premolar',
                            'Second Premolar', 'First Molar', 'Second Molar', 'Third Molar',
                            'Third Molar', 'Second Molar', 'First Molar', 'Second Premolar',
                            'First Premolar', 'Canine', 'Lateral Incisor', 'Central Incisor',
                            'Central Incisor', 'Lateral Incisor', 'Canine', 'First Premolar',
                            'Second Premolar', 'First Molar', 'Second Molar', 'Third Molar']

        for i in range(32):
            tooth_item = QTableWidgetItem(self.teeth_names[i])
            if i // 16 == 0:
                tooth_item.setTextAlignment(Qt.AlignTop)
            else:
                tooth_item.setTextAlignment(Qt.AlignBottom)
            self.table.setItem(i // 16, i % 16, tooth_item)

            cell_widget = QWidget()
            cell_layout = QVBoxLayout(cell_widget)

            checkbox_item = QWidget()
            checkbox_layout = QVBoxLayout(checkbox_item)

            checkbox1 = QCheckBox()
            checkbox2 = QCheckBox()
            checkbox3 = QCheckBox()
            text_line = QLineEdit('.....')
            text_line.setFixedSize(100,20)
            checkbox1.setStyleSheet('QCheckBox::indicator:checked { background-color: red; }')
            checkbox2.setStyleSheet('QCheckBox::indicator:checked { background-color: yellow; }')
            checkbox3.setStyleSheet('QCheckBox::indicator:checked { background-color: green; }')
            if i // 16 == 0:
                checkbox_layout.addWidget(checkbox1, alignment=Qt.AlignTop)
                checkbox_layout.addWidget(checkbox2, alignment=Qt.AlignTop)
                checkbox_layout.addWidget(checkbox3, alignment=Qt.AlignTop)
                checkbox_layout.addWidget(text_line, alignment=Qt.AlignTop)
            else:
                checkbox_layout.addWidget(checkbox1, alignment=Qt.AlignBottom)
                checkbox_layout.addWidget(checkbox2, alignment=Qt.AlignBottom)
                checkbox_layout.addWidget(checkbox3, alignment=Qt.AlignBottom)
                checkbox_layout.addWidget(text_line, alignment=Qt.AlignTop)

            checkbox_layout.setAlignment(Qt.AlignCenter)
            checkbox_layout.setContentsMargins(0, 0, 0, 0)

            self.table.setCellWidget(i // 16, i % 16, checkbox_item)

            # Set table height
            self.table.setRowHeight(i // 16, 150)
            self.table.setColumnWidth(i % 16, 150)

        # Create text box
        self.textbox = QLineEdit(self.centralwidget)
        self.textbox.setGeometry(2475, 15, 500, 140)
        self.textbox.setPlaceholderText("Enter notes here")
        #
        # # Create status indicator
        # self.status = QLabel(self.centralwidget)
        # self.status.setGeometry(2475, 150, 500, 140)
        # self.status.setText("אני כאן!")
        # self.status.setStyleSheet("QLabel { font: 40pt Arial bold;  }")



        # Create form layout
        self.form_layout = QFormLayout()

        # Create labels and line edits
        self.name_label = QLabel("שם:", self.centralwidget)
        self.name_line_edit = QLineEdit(self.centralwidget)
        self.age_label = QLabel("גיל:", self.centralwidget)
        self.age_line_edit = QLineEdit(self.centralwidget)
        self.patient_id_label = QLabel("תעודת זהות:", self.centralwidget)
        self.patient_id_line_edit = QLineEdit(self.centralwidget)

        self.form_layout.addRow(self.name_label, self.name_line_edit)
        self.form_layout.addRow(self.age_label, self.age_line_edit)
        self.form_layout.addRow(self.patient_id_label, self.patient_id_line_edit)

        # Create logo and pixmap
        self.logo = QLabel(self.centralwidget)
        self.image_pixmap = QPixmap(('chrome_wCbLhEp59f.png'))
        self.logo.setPixmap(self.image_pixmap)

        image_layout = QHBoxLayout()
        image_layout.addWidget(self.logo)

        # Create push buttons
        self.browse_button = QPushButton("עיין...", self.centralwidget)
        self.submit_button = QPushButton("שלח", self.centralwidget)
        self.form_layout.addRow(self.browse_button, self.submit_button)

        # Create vertical layout
        self.vertical_layout = QVBoxLayout(self.centralwidget)
        self.vertical_layout.addWidget(self.table)
        self.vertical_layout.addLayout(self.form_layout)
        self.vertical_layout.addLayout(image_layout)
        self.setCentralWidget(self.centralwidget)

        # Connect signals to slots
        self.browse_button.clicked.connect(self.browse)
        self.submit_button.clicked.connect(self.submit)

    def update_line_edits(self, data_list):
        self.name_line_edit.setText(data_list[0])
        self.age_line_edit.setText(data_list[1])
        self.patient_id_line_edit.setText(data_list[2])

    def browse(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                             "Images (*.png *.xpm *.jpg *.bmp);;All Files (*)",
                                                             options=options)
        if file_name:
            self.image_line_edit.setText(file_name)
            self.image_pixmap = QPixmap(file_name)
            self.logo.setPixmap(self.image_pixmap)

    def submit(self):
        name = self.name_line_edit.text()
        age = self.age_line_edit.text()
        patient_id = self.patient_id_line_edit.text()

        print(f"שם: {name}")
        print(f"גיל: {age}")
        print(f"תעודת זהות: {patient_id}")


    def click_checkbox(self, tooth_number, color):
        row = 0 if tooth_number <= 16 else 1
        if row == 1:
            tooth_number = 33 - tooth_number
        column = tooth_number - 1
        checkbox_item = self.table.cellWidget(row, column)
        checkbox_layout = checkbox_item.layout()
        checkbox = None
        if color == "red":
            checkbox = checkbox_layout.itemAt(0).widget()
        elif color == "yellow":
            checkbox = checkbox_layout.itemAt(1).widget()
        elif color == "green":
            checkbox = checkbox_layout.itemAt(2).widget()
        elif color == 'black':
            print("no checkboxes.")
        if checkbox:
            checkbox.setChecked(True)

    def change_textbox_text(self, text):
        self.textbox.setText(text)

    def enter_tooth_text(self, tooth_number, text):
        row = 0 if tooth_number <= 16 else 1
        if row == 1:
            tooth_number = 33 - tooth_number
        column = tooth_number - 1
        textbox_item = self.table.cellWidget(row, column)
        textbox_layout = textbox_item.layout()
        textbox = textbox_layout.itemAt(3).widget()
        textbox.setText(text)

