import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Открываем браузер
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# Получаем значение "Х" из текста, между тегами
x_value = browser.find_element_by_id('treasure')
x = x_value.get_attribute("valuex")
y = calc(x)

# Вводим результат получениы после вычисления формулы
input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

# Подтверждаем что мы роботы
option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

#Роботы рулят! Держитесь кожанные ублюдки!!!
option1 = browser.find_element_by_id('robotsRule')
option1.click()

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()