# Проект «!toohaK»

## Цель проекта
Создать сайт с онлайн викторинами, на котором пользователи смогут проходить созданные другими пользователями викторины, также добавить на сайт соревновательный аспект с помощью создания таблицы лидеров.

## Реализация
Было создано приложения на python с помощью веб-фреймворка [Flask](https://palletsprojects.com/p/flask/).

Основные формы (логин, регистрация, добавление теста) на сайте созданы с помощью библиотеки [flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/). Для управления авторизацией использована [flask-login](https://flask-login.readthedocs.io/en/latest/) – библиотека, расширяющая Flask. Для защиты от кражи паролей пароли хранятся в базе данных зашифрованными.

В форме добавления теста также используется java-script, для удобства конструирования

Взаимодействие с базой данных реализовано с помощью библиотеки [sqlalchemy](https://www.sqlalchemy.org/). База данных состоит из 3 таблиц – completions (попытки прохождения теста), quizzes (все тесты сайта), users (пользователи). Функции для взаимодействия с базой данных вынесены в специальный файл manage_db.py (например, получение пользователя по id)

Все ORM модели для бд находятся в папке data
Для стилизации веб-страниц в проекте используются css файлы, а также css-фреймворк [bootstrap](https://getbootstrap.com/).
Также в проекте используются шаблоны (работа с шаблонами осуществляется с помощью встроенного во flask шаблонизатора [Jinja2](https://palletsprojects.com/p/jinja/)). Любой шаблон проекта наследуется от base.html – базового шаблона. 

Файл app.py – главный исполняемый файл приложения. Содержит в себе обработчики веб страниц, а также несколько дополнительных функций.

## Для пользователя

Для того, чтобы добавить тест/квиз в общий доступ пользователь должен перейти по адресу (https://toohak-quiz.herokuapp.com/login) для входа на сайт или (https://toohak-quiz.herokuapp.com/register) для регистрации на сайте. После успешного входа под своим логином пользователь будет направлен на основное меню пользователя с его данными. 
Добавление теста  происходит по системе – указать название теста, указать описание теста, указать название вопроса – указать правильный ответ (правильный ответ не надо повторно указывать в вариантах ответа; правильный вариант будет автоматически добавлен в выбор ответа), добавить варианты ответа, добавить вопросы к тесту, добавить тест в общий доступ.
Проходить тест могут все авторизованные пользователи (создатели теста не могут проходить свои тесты) получая баллы за прохождение тестов, которые будут добавляться в общий рейтинг пользователя и отображаться в таблице лидеров по пользователю – тест можно проходить множество раз.
