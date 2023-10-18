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

        """
        Getting the email from the user and appending the input email to the textedit area

        """

        #add the title
        self.lbl_name = QLabel() 
        self.lbl_name.setText("Daily Emails")
        self.lbl_name.adjustSize()
        self.lbl_name.move(250,10)
        entered_email = self.lbl_name.text()

        #text  to add emails
        self.txt_recepient = QLineEdit()
        
        #add recepient button
        self.btn_add_email = QPushButton('Add Email')
        self.btn_add_email.resize(60,40)
        self.btn_add_email.move(40,40)
        self.btn_add_email.clicked.connect(self.add_email_clicked)

        #vbox to add text and the button
        self.vbox_recepient = QVBoxLayout()
        self.vbox_recepient.addWidget(self.txt_recepient)
        self.vbox_recepient.addWidget(self.btn_add_email)

        #text  area to edit added emails
        self.txt_email_list = QTextEdit()
        self.txt_email_list.setFixedSize(250,200)
        self.txt_email_list.move(60,60)

        #edit  recepient button
        self.btn_delete_email = QPushButton('Delete Email')
        self.btn_delete_email.resize(60,40)
        self.btn_delete_email.move(40,40)
        self.btn_delete_email.clicked.connect(self.delete_selected_email)


        self.hbox_receipients= QHBoxLayout()
        self.hbox_receipients.addLayout(self.vbox_recepient)
        self.hbox_receipients.addWidget(self.txt_email_list)
        self.hbox_receipients.addWidget(self.btn_delete_email)

        #add the timer
        self.lbl_timer = QLabel() 
        self.lbl_timer.setText("Schedule timer")
        self.lbl_timer.adjustSize()
    
        #edit time
        self.timer = QTimeEdit()

        #hbox for the timer
        self.hbox_timer= QHBoxLayout()
        self.hbox_timer.addWidget(self.lbl_timer)
        self.hbox_timer.addWidget(self.timer)

        #content
        self.lbl_timer = QLabel() 
        self.lbl_timer.setText("Select Content")
        self.lbl_timer.adjustSize()

        self.check_1 = QCheckBox()
        self.check_1.setText("Option1")

        self.check_2 = QCheckBox()
        self.check_2.setText("Option2")

        self.check_3 = QCheckBox()
        self.check_3.setText("Option3")

        self.check_4 = QCheckBox()
        self.check_4.setText("Option4")


        #vbox to add text and the button
        self.vbox_checkbox1 = QVBoxLayout()
        self.vbox_checkbox1.addWidget(self.check_1)
        self.vbox_checkbox1.addWidget(self.check_2)

        #vbox to add text and the button
        self.vbox_checkbox2 = QVBoxLayout()
        self.vbox_checkbox2.addWidget(self.check_3)
        self.vbox_checkbox2.addWidget(self.check_4)

        #hbox for the timer
        self.hbox_checkbox= QHBoxLayout()
        self.hbox_checkbox.addWidget(self.lbl_timer)
        self.hbox_checkbox.addLayout(self.vbox_checkbox1)
        self.hbox_checkbox.addLayout(self.vbox_checkbox2)


        #sender
        self.lbl_sender = QLabel() 
        self.lbl_sender.setText("Sender")
        self.lbl_sender.adjustSize()

        #username
        self.txt_senderemail = QLineEdit()

        #password
        self.txt_password = QLineEdit()
        self.txt_password.setEchoMode(QLineEdit.Password)        
       

        #sender
        self.hbox_sender= QHBoxLayout()
        self.hbox_sender.addWidget(self.lbl_sender)
        self.hbox_sender.addWidget(self.txt_senderemail)
        self.hbox_sender.addWidget(self.txt_password)

        #buttons to update details
        self.btn_settings = QPushButton('Update settings')
    
        self.btn_manual = QPushButton('Send Manually')

        self.hbox_update_details= QHBoxLayout()
        self.hbox_update_details.addWidget(self.btn_settings)
        self.hbox_update_details.addWidget(self.btn_manual)

    

        self.vbox_main = QVBoxLayout()
        self.vbox_main.addWidget(self.lbl_name)
        self.vbox_main.addLayout(self.hbox_receipients)
        self.vbox_main.addLayout(self.hbox_timer)
        self.vbox_main.addLayout(self.hbox_checkbox)
        self.vbox_main.addLayout(self.hbox_sender)
        self.vbox_main.addLayout(self.hbox_update_details)   
        
        self.setLayout(self.vbox_main)
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Daily Emails')
        self.show()

    """
    Update the email list using the new email added by the user
    """
    def add_email_clicked(self):
        input_email = self.txt_recepient.text()
        #get the current email list
        current_emails=self.txt_email_list.toPlainText()
        #append the new email
        updated_emails = current_emails +'\n'+input_email
        #set the updated text
        self.txt_email_list.setPlainText(updated_emails)
    """
    Select a text from QTextEdit and delete the selected text when 
    a button is clicked
    """
    def delete_selected_email(self):
        selected_text = self.txt_email_list.textCursor()
        selected_text.removeSelectedText()

        
    def delete_selected_text(self):
        cursor = self.text_edit.textCursor()
        selected_text = cursor.selectedText()
        current_text = self.text_edit.toPlainText()

        if selected_text:
            updated_text = current_text.replace(selected_text, "")
            self.text_edit.setPlainText(updated_text)

def main():
    app = QApplication(sys.argv)
    ex = PyQtLayout()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()