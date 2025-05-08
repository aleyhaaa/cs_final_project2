import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QRadioButton, QButtonGroup, QTextEdit, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt
from utility import read_all_books  # Make sure this is correctly defined

"""
GUI (Graphical User Interface)
"""

# CONSTANTS
APPLICATION_TITLE = "Book Tracking"

class HorizontalView(QWidget):
    """
    This class will create the horizontal view of our application.
    """
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle(APPLICATION_TITLE)

        # Load data from table
        self.load_data()

    def load_data(self):
        """
        This function will load all of the data within the database to show within QTableWidget
        """
        rows = read_all_books()  # Loads all data within database

        # Ensure rows are not empty
        if rows:
            column_count = len(rows[0])  # Correct column count
        else:
            column_count = 5  # Default column count if no data

        # Create table that shows the data
        self.data_table = QTableWidget()
        self.data_table.setColumnCount(column_count)
        self.data_table.setRowCount(len(rows))
        self.data_table.setHorizontalHeaderLabels(["Book Title", "Author", "ISBN", "Read Book", "Comment"][:column_count])

        # Populate table with data
        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                self.data_table.setItem(row_index, column_index, QTableWidgetItem(str(data)))

        # Set Geometry of the window (Increased height)
        self.setGeometry(100, 100, 600, 400)

        # Create widgets
        self.book_title = QLabel('Book Title')
        self.book_title_line = QLineEdit()

        # Author 
        self.author_title = QLabel('Author')
        self.author_title_line = QLineEdit()

        # ISBN
        self.isbn_title = QLabel('ISBN')
        self.isbn_title_line = QLineEdit()

        # Have you read the book?
        self.read_book_title = QLabel('Have you read the book?')
        self.radio_read_yes = QRadioButton("Yes")
        self.radio_read_no = QRadioButton("No")

        # Group the radio buttons (optional for logic)
        self.gender_group = QButtonGroup()
        self.gender_group.addButton(self.radio_read_yes)
        self.gender_group.addButton(self.radio_read_no)

        # Comment
        self.comment_title = QLabel('Comments')
        self.comment_title_line = QTextEdit()
        self.button = QPushButton("Submit")

        # Create vertical layout and add widgets
        h_layout = QVBoxLayout()
        h_layout.addWidget(self.book_title)
        h_layout.addWidget(self.book_title_line)
        h_layout.addWidget(self.author_title)
        h_layout.addWidget(self.author_title_line)
        h_layout.addWidget(self.isbn_title)
        h_layout.addWidget(self.isbn_title_line)
        h_layout.addWidget(self.read_book_title)
        h_layout.addWidget(self.radio_read_yes)
        h_layout.addWidget(self.radio_read_no)
        h_layout.addWidget(self.comment_title)
        h_layout.addWidget(self.comment_title_line)
        h_layout.addWidget(self.button)
        h_layout.addWidget(self.data_table)

        # Set main layout to the main window
        self.setLayout(h_layout)

    def show_text(self):
        """
        Show the text within the textbox
        """
        name = self.textbox.text()
        self.label.setText("Text Placeholder")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HorizontalView()
    window.show()
    sys.exit(app.exec())