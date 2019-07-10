import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Open browser
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# Push button
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Accept confirm
confirm = browser.switch_to.alert
confirm.accept()

# Получаем значение "Х" из текста, между тегами
x_value = browser.find_element_by_id('input_value')
x = x_value.text
y = calc(x)

# Вводим результат получениы после вычисления формулы
input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()