from selene import browser, have, be


def test_results_ok(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Результаты поиска'))


def test_results_not_ok(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('uegiu iuerj iuejrh dfuierjkdb ').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
