import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QRadioButton, QTableWidget, QTableWidgetItem, QTextEdit, QHBoxLayout, QMessageBox
from utility import create_database, read_all_books, add_book, update_book, delete_book

class BookTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Book Tracker")
        self.setGeometry(100, 100, 800, 400)
        self.initUI()
        create_database()
        self.load_data()

    def initUI(self):
        # Form fields
        self.title_input = QLineEdit()
        # self.title_input.setPlaceholderText("Type a Book Title")

        self.author_input = QLineEdit()
        # self.author_input.setPlaceholderText("Type in the Author")

        self.isbn_input = QLineEdit()
        # self.isbn_input.setPlaceholderText("ISBN")

        self.read_yes = QRadioButton("Read")
        self.read_no = QRadioButton("Not Read")
        self.read_yes.setChecked(True)

        self.comment_input = QTextEdit()
        # self.comment_input.setPlaceholderText("Comment")

        # Table for displaying books
        self.data_table = QTableWidget()
        self.data_table.setColumnCount(5)
        self.data_table.setHorizontalHeaderLabels(["ID", "Title", "Author", "ISBN", "Read", "Comment"])
        self.data_table.itemSelectionChanged.connect(self.load_selected_book)

        # Buttons
        self.add_button = QPushButton("Add Book")
        self.add_button.clicked.connect(self.add_book)

        self.update_button = QPushButton("Update Book")
        self.update_button.clicked.connect(self.update_book)
        self.update_button.setEnabled(False)

        self.delete_button = QPushButton("Delete Book")
        self.delete_button.clicked.connect(self.delete_book)
        self.delete_button.setEnabled(False)

        # Layout
        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Title"))
        form_layout.addWidget(self.title_input)
        form_layout.addWidget(QLabel("Author"))
        form_layout.addWidget(self.author_input)
        form_layout.addWidget(QLabel("ISBN"))
        form_layout.addWidget(self.isbn_input)
        form_layout.addWidget(QLabel("Read Status"))
        form_layout.addWidget(self.read_yes)
        form_layout.addWidget(self.read_no)
        form_layout.addWidget(QLabel("Comment"))
        form_layout.addWidget(self.comment_input)
        form_layout.addWidget(self.add_button)
        form_layout.addWidget(self.update_button)
        form_layout.addWidget(self.delete_button)

        main_layout = QHBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.data_table)

        self.setLayout(main_layout)

    def load_data(self):
        books = read_all_books()
        self.data_table.setRowCount(len(books))
        for row_index, row_data in enumerate(books):
            for column_index, data in enumerate(row_data):
                self.data_table.setItem(row_index, column_index, QTableWidgetItem(str(data)))

    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        isbn = self.isbn_input.text()
        read_book = self.read_yes.isChecked()
        comment = self.comment_input.toPlainText()

        if title and author:
            add_book(title, author, isbn, read_book, comment)
            self.load_data()
            self.clear_form()
        else:
            QMessageBox.warning(self, "Input Error", "Title and Author are required.")

    def load_selected_book(self):
        selected = self.data_table.currentRow()
        if selected >= 0:
            self.update_button.setEnabled(True)
            self.delete_button.setEnabled(True)

            # Use try-except to prevent 'NoneType' error
            try:
                book_id_item = self.data_table.item(selected, 0)
                title_item = self.data_table.item(selected, 1)
                author_item = self.data_table.item(selected, 2)
                isbn_item = self.data_table.item(selected, 3)
                read_item = self.data_table.item(selected, 4)
                comment_item = self.data_table.item(selected, 5)

                # Ensure items are not None before accessing text
                self.current_book_id = int(book_id_item.text()) if book_id_item else None
                self.title_input.setText(title_item.text() if title_item else "")
                self.author_input.setText(author_item.text() if author_item else "")
                self.isbn_input.setText(isbn_item.text() if isbn_item else "")
                self.read_yes.setChecked(read_item.text() == "True" if read_item else False)
                self.comment_input.setPlainText(comment_item.text() if comment_item else "")
            except AttributeError:
                QMessageBox.warning(self, "Selection Error", "Unable to load selected book. Please try again.")
                self.clear_form()

    def update_book(self):
        update_book(
            self.current_book_id,
            self.title_input.text(),
            self.author_input.text(),
            self.isbn_input.text(),
            self.read_yes.isChecked(),
            self.comment_input.toPlainText()
        )
        self.load_data()
        self.clear_form()

    def delete_book(self):
        delete_book(self.current_book_id)
        self.load_data()
        self.clear_form()

    def clear_form(self):
        self.title_input.clear()
        self.author_input.clear()
        self.isbn_input.clear()
        self.read_yes.setChecked(True)
        self.comment_input.clear()
        self.update_button.setEnabled(False)
        self.delete_button.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BookTracker()
    window.show()
    sys.exit(app.exec())