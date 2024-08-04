# To run, paste this code in a folder with a other folder called "bin" and in folder "bin", put the chromedriver
# this file  -> C:\Users\User\project\main.py
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'bin' / 'chromedriver.exe'
DIR_FILES = ROOT_FOLDER / 'info'
DIR_FILES.mkdir(exist_ok=True)


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    options = ('--headless',)
    browser = make_chrome_browser(*options)

    try:
        browser.get('https://www.wikipedia.org')

        find_input = browser.find_element(By.ID, 'searchInput')

        user_input = input('Digite o que quer pesquisar na wikipedia: ')

        find_input.click()
        find_input.send_keys(user_input)
        find_input.send_keys(Keys.ENTER)

        sleep(2)

        results = WebDriverWait(browser, 2).until(
            EC.presence_of_element_located(
                (By.ID, 'firstHeading')  # Get the title of search in wikipedia
            )
        )
        if results.text != 'Resultados da pesquisa':
            print(f'Resultado: {results.text}')

        page = WebDriverWait(browser, 3).until(
            EC.presence_of_element_located(
                (By.ID, 'mw-content-text')
            )
        )
        if results.text == 'Resultados da pesquisa':
            print('Sem resultados, cheque o arquivo salvo.')

            with open(DIR_FILES / 'Resultados_pesquisa.txt',
                      'w', encoding='utf8') as file:

                file.write(f'{results.text}\n')
                file.write(page.text)

            print(F'Salvo em {DIR_FILES}')

        else:
            with open(DIR_FILES / f'{results.text}.txt',
                      'w', encoding='utf8') as file:

                file.write(f'{results.text}\n')
                file.write(page.text)

                print(F'Salvo em {DIR_FILES}')

    except Exception as e:
        print(f'An error ocurred: {e}')

    finally:
        browser.quit()
