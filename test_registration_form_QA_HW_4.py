import os
import time
from time import sleep

from selene import browser, be, have



def test_registration_form(browser_settings):
    #Открытие страницы
    browser.open('https://demoqa.com/automation-practice-form')
    #Заполнение формы
    browser.element('[id="firstName"]').should(be.blank).type('Evgenii')
    browser.element('[id="lastName"]').should(be.blank).type('Peters')
    browser.element('[id="userEmail"]').should(be.blank).type('example@mail.ru')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('[id = "userNumber"]').should(be.blank).type('88005553535')
    browser.element('[id = "dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__month-select"]').element('option[value="5"]').click()
    browser.element('[class="react-datepicker__year-select"]').element('option[value="1999"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--022"]').click()
    browser.element('[id="subjectsInput"]').type('Geometry')
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('[id="uploadPicture"]').set_value(os.path.abspath('example.png'))
    #browser.element('[id="uploadPicture"]').set_value('C:/Users/evgen/PycharmProjects/QAGURUR_HW_22')
    browser.element('[id = "currentAddress"]').should(be.blank).type('exemple street')
    browser.element('[id = "state"]').click()
    browser.element('[id="react-select-3-input"]').type('Haryana').press_enter()
    browser.element('[id = "city"]').click()
    browser.element('[id="react-select-4-input"]').type('Panipat').press_enter()
    browser.element('[id = "submit"]').click()
    #Проверка что форма заполнена
    browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))
    #не уверен насчет этой части проверки поэтому добавил выше проверку просто  что сабмит прошел успешно
    browser.all('td').should(have.text([
        'Student Name', 'Evgenii Peters',
        'Student Email', 'example@mail.ru',
        'Gender', 'Male',
        'Mobile', '8800555353',
        'Date of Birth', '22 June,1999',
        'Subjects', 'Geometry',
        'Hobbies', 'Reading',
        'Picture', 'example.png',
        'Address', 'exemple street',
    ]))


















