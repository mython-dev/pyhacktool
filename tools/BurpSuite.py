description_tool_burpsuite = f'''
Burp Suite — это интегрированная платформа для тестирования безопасности веб-приложений. 
Его различные инструменты без проблем работают вместе, 
чтобы поддерживать весь процесс тестирования, 
от первоначального отображения и анализа поверхности атаки приложения до поиска и использования уязвимостей безопасности.

Burp дает вам полный контроль, 
позволяя сочетать передовые ручные методы с современной автоматизацией, 
чтобы сделать вашу работу быстрее, эффективнее и веселее.
'''

install_burpsuite = ('''curl https://portswigger-cdn.net/burp/releases/download?product=community&version=2022.8.4&type=Linux --output burpsuite_community_linux_v2022_8_4.sh 
&& chmod +x && ./burpsuite_community_linux_v2022_8_4.sh''')


zapusk_burpsuite = print(f'Запуск инстурмента: burpsuite')