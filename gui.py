"""
Interface for Daily Eamil list
"""

import sys
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication,QLabel,
                             QHBoxLayout, QVBoxLayout, QGridLayout,QTextEdit,QLineEdit,QTimeEdit,QCheckBox)
 
class PyQtLayout(QWidget):
 
    def __init__(self):
        super().__init__()
        self.UI()
 
    def UI(self):

        #add the title
        lbl_name = QLabel() 
        lbl_name.setText("Daily Emails")
        lbl_name.adjustSize()
        lbl_name.move(250,10)

        #text  to add emails
        txt_recepient = QLineEdit()
        
        #add recepient button
        btn_email = QPushButton('Add Email')
        btn_email.resize(60,40)
        btn_email.move(40,40)

        #vbox to add text and the button
        vbox_recepient = QVBoxLayout()
        vbox_recepient.addWidget(txt_recepient)
        vbox_recepient.addWidget(btn_email)

        #text  area to edit added emails
        txt_recepient = QTextEdit()
        txt_recepient.setFixedSize(250,200)
        txt_recepient.move(60,60)

        #edit  recepient button
        btn_email = QPushButton('Delete Email')
        btn_email.resize(60,40)
        btn_email.move(40,40)


        hbox_receipients= QHBoxLayout()
        hbox_receipients.addLayout(vbox_recepient)
        hbox_receipients.addWidget(txt_recepient)
        hbox_receipients.addWidget(btn_email)

        #add the timer
        lbl_timer = QLabel() 
        lbl_timer.setText("Schedule timer")
        lbl_timer.adjustSize()
    
        #edit time
        timer = QTimeEdit()

        #hbox for the timer
        hbox_timer= QHBoxLayout()
        hbox_timer.addWidget(lbl_timer)
        hbox_timer.addWidget(timer)

        #content
        lbl_timer = QLabel() 
        lbl_timer.setText("Select Content")
        lbl_timer.adjustSize()

        check_1 = QCheckBox()
        check_1.setText("Option1")

        check_2 = QCheckBox()
        check_2.setText("Option2")

        check_3 = QCheckBox()
        check_3.setText("Option3")

        check_4 = QCheckBox()
        check_4.setText("Option4")


        #vbox to add text and the button
        vbox_checkbox1 = QVBoxLayout()
        vbox_checkbox1.addWidget(check_1)
        vbox_checkbox1.addWidget(check_2)

        #vbox to add text and the button
        vbox_checkbox2 = QVBoxLayout()
        vbox_checkbox2.addWidget(check_3)
        vbox_checkbox2.addWidget(check_4)

        #hbox for the timer
        hbox_checkbox= QHBoxLayout()
        hbox_checkbox.addWidget(lbl_timer)
        hbox_checkbox.addLayout(vbox_checkbox1)
        hbox_checkbox.addLayout(vbox_checkbox2)


        #sender
        lbl_sender = QLabel() 
        lbl_sender.setText("Sender")
        lbl_sender.adjustSize()

        #username
        txt_senderemail = QLineEdit()

        #password
        txt_password = QLineEdit()
        txt_password.setEchoMode(QLineEdit.Password)        
       

        #sender
        hbox_sender= QHBoxLayout()
        hbox_sender.addWidget(lbl_sender)
        hbox_sender.addWidget(txt_senderemail)
        hbox_sender.addWidget(txt_password)

        #buttons to update details
        btn_settings = QPushButton('Update settings')
    
        btn_manual = QPushButton('Send Manually')

        hbox_update_details= QHBoxLayout()
        hbox_update_details.addWidget(btn_settings)
        hbox_update_details.addWidget(btn_manual)

    

        vbox_main = QVBoxLayout()
        vbox_main.addWidget(lbl_name)
        vbox_main.addLayout(hbox_receipients)
        vbox_main.addLayout(hbox_timer)
        vbox_main.addLayout(hbox_checkbox)
        vbox_main.addLayout(hbox_sender)
        vbox_main.addLayout(hbox_update_details)   
        
        self.setLayout(vbox_main)
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Daily Emails')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = PyQtLayout()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()