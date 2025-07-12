from selene import be, have
from selene.support.shared import browser


def test_google_search_negative(window_size):
    browser.open('https://google.com/ncr')
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.no.text('Blah-blah-blah'))


def test_conflict_git(yandex_config):
    browser.open('https://ya.ru/memes')