from selenium.webdriver.common.by import By

import FormBase
import NBAPOSN
import NOAEPAF
import NTRPCLS
import PAACDES


def dispatch_for(driver):
    form_code = FormBase.get_form_name(driver)
    print(form_code)

    if (form_code is not None) and ('NOAEPAF' in form_code):
        NOAEPAF.handle(driver)
    if (form_code is not None) and ('NTRPCLS' in form_code):
        NTRPCLS.handle(driver)
    if (form_code is not None) and ('PAACDES' in form_code):
        PAACDES.handle(driver)
    if (form_code is not None) and ('NBAPOSN' in form_code):
        NBAPOSN.handle(driver)


