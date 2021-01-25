### скачать https://www.python.org/downloads/ (ставим галочку: install launchar for all users, add python 3.7 to PATH)
Заходим Панель управления\Система и безопасность\Система ,нажимаем на дополнительные параметры системы-переменные среды-системные переменные(ищем там Path (переменная) и в значении через ; добавляем : C:\Users\User\AppData\Local\Programs\Python\Python38\python.exe;)

###скачать jdk1.8.0_281

Заходим Панель управления\Система и безопасность\Система ,нажимаем на дополнительные параметры системы-переменные среды-системные переменные(ищем там Path (переменная) и в значении через ; добавляем :C:\ProgramFiles\Java\jdk1.8.0_281;)

Скачать jenkins.war





Открываем командную строку 
Заходим в папку где находится наш jenkins.war
Пишем команду: java -jar jenkins.war
Если нужно поставить на другой порт , то пишем:  java -jar jenkins.war --httpPort=8086
Важно не закрывать командную строку и ждать
Если появилась в конце строчка,то все хорошо : Jenkins is fully up and running
Находим строчку с : 
Jenkins initial setup is required. An admin user has been created and a password
 generated.
Please use the following password to proceed to installation:
c5302513456c471db8a1958e36b15f00
Ниже этой строчки стоит пароль , который нужен для входа в jenkins
Открывает бразуер с Url      http://localhost:8080/
Он будет запрашивать пароль, пароль из командной строки , вводим его
C:\Users\User\.jenkins\secrets\initialAdminPassword
Нажимаем установить рекомендуемые плагины
В основном тут пропускаем все найстроки
Вы пропустили настройку администратора . 

Для входа используйте имя пользователя: «admin» и пароль администратора, который вы использовали для доступа к мастеру установки. 
Нажимаем сохранить и продолжить 

Заходим в нсаройки Jenkins
Глобальные инструменты конфигурации
Add jdk
Name пишем:JAVA_HOME
Убираем галочку автоматической установки
В JAV_HOME пишем: C:\Program Files\Java\jdk1.8.0_281
Apply and save
Add git
Name пишем:Default
Убираем галочку автоматической установки
В Path to Git executable пишем: C:/Program Files/Git/bin/git.exe
Apply and save
Заходим в конфигурация системы
Глобальные настройки и нажать на галочку в Environment variables
В name : Python_Home
Значение: C:\Users\User\AppData\Local\Programs\Python\Python38;C:\Users\User\AppData\Local\Programs\Python\Python38\Scripts
В name : Python_Script
Значение: C:\Users\User\AppData\Local\Programs\Python\Python38\Scripts
Apply and save
В папку C:\Users\User\AppData\Local\Programs\Python\Python38\Scripts положить
Chromedriver
Geckodriver
Заходим в настройки jenkins
Manage plugins->available пишем в поисковой строке allure ,нажимаем рядом с ним гаолчку и install without restart

Скачиваем powershell 7 https://github.com/PowerShell/PowerShell/releases
открываем powershell 7. и пишем в нем Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
скачать allure https://github.com/allure-framework/allure2/releases и распаковать в C:\allure-2.9.0 (сами файлы должны быть в этой папке, если в zip архиве есть уже название этой папки ,то просто перекидываем на диск C:)
Заходим Панель управления\Система и безопасность\Система ,нажимаем на дополнительные параметры системы-переменные среды-системные переменные(ищем там Path (переменная) и в значении через ; добавляем : C:\allure-2.9.0\bin;)
Закрыть powershell 7 и снова открыть и ввести allure , если не появилось много красного текста а белы ,то все нормально
Заходим в нсаройки Jenkins
Глобальные инструменты конфигурации
Add allure commandline
Name пишем:Allure
Убираем галочку автоматической установки
В Установочная директория пишем: C:\allure-2.9.0
Apply and save
Нажимаем на Домой
Создать Item
Пишем имя YandexPage_test и выбираем тип проекта (создать задачу со свободной конфигурацией)Нажать ок
В области description, можно что-то написать (если хотите)
Нажимаем рядом с управлением исходным кодом Git
И пишем в repositories url ссылку на выш репозиторий https://github.com/NIk119/Yandex/
Apply and save
Нажимаем build now
Под build history появиться наш запущенные код из репозитория, нажимаем на него
Нажимаем на вывод на консоль
Если в самом низу стоит Finished: SUCCESS,то все хорошо.Данные получены и тест скорее всего пройдет
Заходим в наш проект и в Сборке устанавливаем запуск команды в windows
И пишем в ней текст :
pip install pytest
pip install selenium

Потом
Apply and save
Запускаем сборку
И должно быть установлено 
pip install pytest
pip install selenium
 
Если в самом низу стоит Finished: SUCCESS
(Заходим в наш проект и в Сборке устанавливаем запуск команды в windows
И пишем в ней текст :

pytest -s Tests.py

Потом

Apply and save)
Либо с allure ниже код нужно ввести

(Заходим в наш проект и в Сборке устанавливаем запуск команды в windows

И пишем в ней текст :

pytest --alluredir=./Reports Tests.py
Потом
Apply and save)
Заходим в наш проект и в Post-build Actions allure report
И пишем в ней текст :
Reports
Потом
Apply and save)
Запускаем наш проект
После прохождения, нажимаем на allure reports
Если нужно ,чтобы был еще отедльный репорт, который можно запустить без jenkins
То нужно вместо
pip install pytest
pip install selenium
Написать ниже
rmdir /s /q Reports
rmdir /s /q allure-report
pip install pytest
pip install selenium


В папке будет allure-report находится html нашего отчета
Если нужно узнать где репорты, то в консоли проекта написан путь куда все скидывается
Там должен быть Reports в строке написан, и перед ним через слеш путь к этой папке на диске С: