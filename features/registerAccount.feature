# Created by Dass at 21.01.2018
Feature: Регистрация аккаунта на сайте https://ru.investing.com/
  # Enter feature description here

#  Scenario: Успешная регистрация на сайте
#    Given Зайти на сайт "https://ru.investing.com/"
#    #Then Нажать на кнопку "Бесплатная регистрация"
#    Then Появилось окно Входа/Регистрации
#    When Нажать на кнопку "Зарегистрироваться"
#    Then Появилось окно ввода регистрационных данных
#    And Ввести "Иван" в поле "Имя:"
#    And Ввести "Иванов" в поле "Фамилия:"
#    And Ввести "example@mail.com" в поле "Email"
#    And Ввести "pass12word" в поле "Пароль"
#    And Выбрать страну "Россия" в выпадающем меню "Выбрать страну"
#    And Ввести "900-111-22-11" в поле "Номер телефона"
#    And Приянть правилами использования и политику конфиденциальности
#    And Сделать скриншот

  Scenario: Регистрация с незаполнеными полями
    Given Зайти на сайт "https://ru.investing.com/"
    Then Появилось окно Входа/Регистрации
    When Нажать на кнопку "Зарегистрироваться"
    Then Появилось окно ввода регистрационных данных
    When дави сюда
    #When Нажать на кнопку "Зарегистрироваться"