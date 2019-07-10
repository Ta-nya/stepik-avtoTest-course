from selenium import webdriver
from selenium.webdriver.support.ui import Select


# Открываем браузер
link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

# Получаем значение "a" и "b" из текста, между тегами и складываем
a_value = browser.find_element_by_id('num1')
a = a_value.text

b_value = browser.find_element_by_id('num2')
b = b_value.text

x = str(int(a) + int(b))

#Находим список и выбираем значение равное "X"
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(x) # ищем элемент

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()
