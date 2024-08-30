import reflex as rx
from guessyou.pages.results import results
from guessyou.pages.index import index







app = rx.App()
app.add_page(index)
app.add_page(results)
