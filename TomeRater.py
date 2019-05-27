import re


class User:
    """
        User class

        Args:
            name (str):  user's name
            email (str):  user's email

        Attributes:
            books (dict): empty dict - will contain books titles as keys and the ratings given
                by the user as values

    """

    def __init__(self, name, email):

        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        return f'<User {self.name}, email: {self.email}, books read: {len(self.books)}>'

    def __eq__(self, other_user):
        """
        Two User objects are considered equal if they have the same name and email

        Args:
            other_user(User):  another user object

        Returns:
            bool: True if the two users are equals, False otherwise.

        """
        return (self.name == other_user.name and self.email == other_user.email)

    def get_email(self):
        """
        Get the User email

        Returns:
            str: the User's email

        """
        return self.email

    @staticmethod
    def check_email_is_valid(email):
        """
        Check if the email syntax is valid

        Args:
            email (str):  the email address to check

        Returns:
            bool: True if valid email syntax, False otherwise

        """
        valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                               email)

        return valid_email

    def change_email(self, new_address):
        """
        Change the existing User's email with a new one if the email address has a valid format

        Args:
            new_address (str):  new User's email address

        Raises:
            ValueError: if the email syntax is not valid
        """

        if self.check_email_is_valid(new_address):
            self.email = new_address
            print('User email has been updated')
        else:
            raise ValueError('Bad email syntax')

    def read_book(self, book, rating=None):
        """
        If the rating is valid or equal to None: add a book to the User's 'books'
        dictionary along with the book's rating.

        Add the rating to the book object passed as a parameter if the rating is valid
        but not equal to None.

        Args:
            book (Book):  book object read
            rating (int): optional, default to None

        """
        if isinstance(book, Book):
            try:
                Book.check_rating_is_valid(rating)
            except ValueError:
                if rating is not None:
                    print('The rating must be either None or an integer from 0 to 4')
                    raise

            self.books[book] = rating
            if rating:
                book.add_rating(rating)
        else:
            raise TypeError('The book must be a Book object')

    @property
    def get_average_rating(self):
        """
        Calculate the average rating given by a User.
        Ratings equals to None are not taken into account.
        The average rating is accessible as a property.

        Returns:
            float: average rating

        """
        nb_of_ratings = 0
        sum_ratings = 0
        for book, rating in self.books.items():
            if rating is None:
                continue
            nb_of_ratings += 1
            sum_ratings += rating

        if not nb_of_ratings:
            return 0
        return sum_ratings / nb_of_ratings

    def get_books_collection(self):
        """
        Get the list of books read by the User

        Returns:
            list: the books read by the user
        """
        return list(self.books.keys())


class Book:
    """
    Book class

        Args:
            title (str):  the book title
            isbn (int):  the book ISBN
            price(int): the book price, optional, default to 0

        Attributes:
            ratings (list): empty list - will contain the ratings given by the users.
    """

    def __init__(self, title, isbn, price=0):

        self.title = title
        self.isbn = isbn
        self.price = price
        self.ratings = []

    def __repr__(self):
        return f'<Book {self.title}, with isbn {self.isbn}>'

    def __hash__(self):
        """Returns a consistent hash for an instance of a book object"""
        return hash((self.title, self.isbn))

    def __eq__(self, other_book):
        """
        Two Book objects are considered equal if they have the same title and isbn

            Args:
                other_book (Book): another book object

            Returns:
                bool: True if the two books are equals, False otherwise.
        """

        return (self.title == other_book.title and self.isbn == other_book.isbn)

    def get_isbn(self):
        """
            Returns:
                str: the book isbn

        """
        return self.isbn

    def get_title(self):
        """
            Returns:
                str: the book title
        """
        return self.title

    def set_isbn(self, new_isbn):
        """
            Change the book isbn

            Args:
                new_isbn (int): the new isbn for the book
        """
        if type(new_isbn) is int:
            self.isbn = new_isbn
            print('the isbn has been updated')
        else:
            raise TypeError('the new isbn must be an integer')

    @staticmethod
    def check_rating_is_valid(rating):
        """
        Check if a book rating is in the valid range (from 0 to 4)

            Args:
                rating (int): the book rating

            Raises:
                ValueError: if the rating is not in the valid range
        """
        if rating not in range(0, 5):
            raise ValueError('Invalid rating')

    def add_rating(self, rating):
        """
        Add a rating to the book if the rating is valid

            Args:
                rating (int): the Book rating
        """

        try:
            self.check_rating_is_valid(rating)
            self.ratings.append(rating)
        except ValueError:
            print('Invalid rating. Please enter a rating from 0 to 4')
            raise

    @property
    def average_rating(self):
        """
        Calculate the average rating for a Book

            Returns:
                float: the average rating

        """
        if len(self.ratings):
            return sum(self.ratings) / len(self.ratings)
        return 0


class Fiction(Book):
    """
    Fiction book class

    Inherit from the Book class - call the parent class constructor for 'title', 'isbn', 'price' arguments

        Args:
            title (str):  the book title
            author (str): the book's author
            isbn (int):  the book isbn
            price(int): the book price, optional, default to 0

    """

    def __init__(self, title, author, isbn, price=0):
        super().__init__(title, isbn, price)
        self.author = author

    def __repr__(self):
        return f'<Fiction {self.title} by {self.author}>'

    def get_author(self):
        """

              Returns:
                  str: the book's author

        """
        return self.author


class NonFiction(Book):
    """
    Non Fiction book class

    Inherit from the Book class - call the parent class constructor for 'title', 'isbn', 'price' arguments

        Args:
            title (str):  the book's title
            subject (str): the book's subject
            level (str): the book's difficulty level
            isbn (int):  the book's isbn
            price(int): the book price, optional, default to 0
    """

    def __init__(self, title, subject, level, isbn, price=0):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def get_subject(self):
        """
              Returns:
                  str: the book's subject
        """
        return self.subject

    def get_level(self):
        """
              Returns:
                  str: the book's difficulty level
        """
        return self.level

    def __repr__(self):
        return f'<NonFiction {self.title}, a {self.level} manual on {self.subject}>'


class TomeRater:
    """
    TomeRater application class

    Provides methods to manage users, rate the books and some analytics methods

        Attributes:
            users (dict): map a user’s email to the corresponding User object
            books (dict): map a Book object to the number of Users that have read it
    """

    def __init__(self):

        self.users = {}
        self.books = {}

    def catalog_generator(self):
        """
        Generator that yield each book from the book catalog

              Yields:
                  Book: a book object from the collection

        """
        for book in self.books.keys():
            yield book

    def check_isbn_in_catalog(self, isbn):
        """
        Check if the book is already in the book catalog by comparing the book's isbn with the other books' isbn

            Args:
                isbn (int): the book's isbn that is searched in the catalog

            Returns:
                bool: True if the book already exists, False otherwise.

        """

        catalog = self.catalog_generator()
        for book in catalog:
            if book.isbn == isbn:
                print('Book already exist')
                return True
        return False

    def check_book_in_catalog(self, book):
        """
        Check if the book is already in the book catalog by checking if the Book object is in the catalog

              Returns:
                bool: True if the book already exists, False otherwise.

        """
        if not isinstance(book, Book):
            raise TypeError('The argument must be a Book object')

        if book in self.books.keys():
            return True
        else:
            return False

    def create_book(self, title, isbn, price=0):
        """
        Create a new book if the book is not in the catalog (check if the isbn already exist)

            Args:
                title (str): the book's title
                isbn (int): the book's isbn
                price (int): the book's price, optional, default to 0

            Returns:
                Book: a Book object with above title, isbn and price
        """
        if not self.check_isbn_in_catalog(isbn):
            return Book(title, isbn, price)

    def create_novel(self, title, author, isbn, price=0):
        """
        Create a new novel if the novel is not in the catalog (check if the isbn already exist)

            Args:
                title (str): the book's title
                author (str): the book's author
                isbn (int): the book's isbn
                price (int): the book's price, optional, default to 0

            Returns:
                Fiction: a Fiction object with above title, author, isbn and price

        """

        if not self.check_isbn_in_catalog(isbn):
            return Fiction(title, author, isbn, price)

    def create_non_fiction(self, title, subject, level, isbn, price=0):
        """
        Create a new non fiction book if the book is not in the catalog (check if the isbn already exist)

            Args:
                title (str):  the book's title
                subject (str): the book's subject
                level (str): the book's difficulty level
                isbn (int):  the book's isbn
                price (int): the book's price, optional, default to 0

            Returns:
                Fiction: a Fiction object with above title, author, isbn and price

        """
        if not self.check_isbn_in_catalog(isbn):
            return NonFiction(title, subject, level, isbn, price)

    def is_existing_user(self, email):
        """
        Check if the user already exist by comparing its email with the existing ones

            Args:
                email (str): the user's email

            Returns:
                bool: True if the user already exists, False otherwise.
        """

        if not User.check_email_is_valid(email):
            raise ValueError('Please enter a valid email')

        if email in self.users.keys():
            return True
        else:
            return False

    def add_user(self, name, email, user_books=None):
        """
        Add a user to the user dictionary if the email is valid and the user
        is not an existing user
        If a book list is provided, add it to the user's books collection

        Args:
            name (str): user's name
            email (str): user's email
            user_books (list): list of Book objects belonging to the user, optional, default to None

        """

        if not User.check_email_is_valid(email):
            raise ValueError('Please enter a valid email')

        if not self.is_existing_user(email):
            user = User(name, email)
            self.users[email] = user
            if type(user_books) is list:
                for book in user_books:
                    if isinstance(book, Book):
                        self.add_book_to_user(book, email)
                    else:
                        print(f"{book} is not a Book, it was not added to {name} book list")
        else:
            print('User already exists')

    def add_book_to_user(self, book, email, rating=None):
        """
        Add a book to the user collection and read the book.

            Args:
                book (Book): a book object to add to the user
                email (str): the user's email
                rating (int): the book rating, from 0 to 4, optional, default to None
        """

        if self.is_existing_user(email):
            user = self.users.get(email)
            user.read_book(book, rating)

            if self.check_book_in_catalog(book):
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print(f'No user with email {email}!')

    def print_catalog(self):
        """ Print the application's book catalog """
        print('Book catalog:')
        for book in self.books.keys():
            print(book)

    def print_users(self):
        """ Print all the users of the application"""
        print("Tome rater's users: ")
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        """
        Get the most read book from the catalog

            Returns:
                Book: the most read book
        """
        return max(self.books.keys(), key=(lambda k: self.books[k]))

    def highest_rated_book(self):
        """
        Get the highest rated book from the catalog

            Returns:
                Book: the highest rated book
        """
        highest_rated_book = Book('reference_book', 1000002)
        for book in self.books.keys():
            if book.average_rating > highest_rated_book.average_rating:
                highest_rated_book = book
        return highest_rated_book

    def most_positive_user(self):
        """
        Get the user that gives the highest average ratings for his books

            Returns:
                User: the most positive user
        """
        most_positive_user = User('reference_user', 'mail@domain.com')
        for user in self.users.values():
            if user.get_average_rating > most_positive_user.get_average_rating:
                most_positive_user = user
        return most_positive_user

    def get_n_most_read_books(self, n):
        """
        Get the specified number of most read books from the catalog.

            Args:
                n (int): the number of books to get

            Returns:
                list: the list of the specified number of most read books
                    order -> most read book first.
        """
        book_list = list(self.books.items())
        book_list.sort(key=lambda tup: tup[1], reverse=True)
        return book_list[:n]

    def get_n_most_prolific_readers(self, n):
        """
        Get the specified number of users that have read the most books

            Args:
                n (int): the number of users to get

            Returns:
                list: the list of the specified number of users that have
                    read the most books.
                    order -> most prolific reader first.
        """
        user_list = list(self.users.values())
        user_list.sort(key=lambda user: len(user.books), reverse=True)
        return user_list[:n]

    def get_n_most_expensive_books(self, n):
        """
        Get the specified number of the most expensive books from the catalog

            Args
                n (int): the number of books to get

            Returns:
                list: a list of tuples ("book's title" : price) with the specified number
                    of most expensive books.
                    order -> most expensive book first.
        """
        books_price_list = list()

        for book in self.books.keys():
            title = book.title
            price = book.price
            books_price_list.append((title, price))

        books_price_list.sort(key=lambda tup: tup[1], reverse=True)
        return books_price_list[:n]

    def get_worth_of_user(self, user_email):
        """
        Calculate the total value of the user's book collection

            Args:
                user_email (str): the user's email

            Returns:
                int: the price of the user's book collection
        """
        if user_email in self.users:
            user = self.users.get(user_email)
            user_books = user.get_books_collection()
            worth_of_user = 0
            for book in user_books:
                worth_of_user += book.price
            return worth_of_user
        else:
            print(f"{user_email} is not an existing user email")
