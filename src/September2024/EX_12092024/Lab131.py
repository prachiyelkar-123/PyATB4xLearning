from BroswerPackage.open import start_browser
from BroswerPackage.Close import close_browser


def test_case():
    start_browser()
    print("I am executing a Code TC 1")
    close_browser()

test_case()