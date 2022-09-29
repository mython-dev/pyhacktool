
description_tool_owasp = f"""
Кроссплатформенный инструмент с открытым исходным кодом, 
который поддерживается безопасниками со всего мира и имеет много общего с Burp Suite. 
OWASP ZAP удобен в использовании. Интерфейс состоит из нескольких окон. Есть поддержка 13 языков, 
включая английский.
"""

install_owasp = ('''sudo apt update &&
sudo apt install snapd && 
sudo snap install core && 
sudo snap install zaproxy --classic ''')

zapusk_owasp = print('Запуск инструмента: zaproxy')