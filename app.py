import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QToolButton
from PyQt6.QtCore import Qt


# CONSTANTS
APPLICATION_TITLE = "Book Tracking"

class HorizzontalView(QWidget):
    """
    Class will create the horizontal view for application
    """
    def __init__(self):
        super().__init__()

        # set window title
        self.setWindowTitle(APPLICATION_TITLE)

        # Set geometrics of window
        self.setGeometry(100, 100, 600, 100)

        # create widgets
        # create the book title label and line box 
        self.book_title = QLabel('Book Title')
        self.book_title_line = QLineEdit()
        # author 
        self.author_title = QLabel('Author')
        self.author_title_line = QLineEdit()
        # isbn
        self.isbn_title = QLabel('Isbn')
        self.isbn_title_line = QLineEdit()
        # have you read the book?
        self.read_book_title = QLabel('Have you read the book?')

        # comment
        self.comment_title = QLabel('Comments')
        self.comment_title_line = QLineEdit()
        self.label = QLabel("Book Title")
        self.textbox = QLineEdit()
        self.button = QPushButton("Done")


        # create horizontal layout and add widgets
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.book_title)
        v_layout.addWidget(self.book_title_line)
        v_layout.addWidget(self.author_title)
        v_layout.addWidget(self.author_title_line)
        v_layout.addWidget(self.isbn_title)
        v_layout.addWidget(self.isbn_title_line)
        v_layout.addWidget(self.read_book_title)
        v_layout.addWidget(self.comment_title)
        v_layout.addWidget(self.comment_title_line)

        v_layout.addWidget(self.button)

        # set main layout to the main window
        self.setLayout(v_layout)
    
    def show_text(self):
        """
        show the text within the textbox
        """
        name = self.textbox.text()
        self.label.setText("Text Placeholder")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HorizzontalView()
    window.show()
    sys.exit(app.exec())


