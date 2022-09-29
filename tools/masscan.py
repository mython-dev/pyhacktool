descirption_tool_masscan = '''
Masscan - это сканер порта TCP, 
который асинхронно передает пакеты SYN и дает результаты, 
аналогичные NMAP, наиболее известному сканеру порта.
Внутренне он работает больше как Scanrand, Unicornscan и ZMAP, 
используя асинхронную передачу. Это гибкая утилита, 
которая допускает произвольный адрес и портовые диапазоны.
'''

install_masscan = 'sudo apt-get update -y && sudo apt-get install -y masscan'

start_masscan = 'Запуск: masscan'
