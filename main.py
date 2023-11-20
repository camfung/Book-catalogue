from Project1 import BookCatalogue
from login_class import LoginScreen

j = LoginScreen()

if j.allow_login:
    x = BookCatalogue
    x.user = j.user
    x()

