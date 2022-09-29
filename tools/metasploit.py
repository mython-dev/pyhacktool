description_tool_msf = f'''
Metasploit Framework — это фреймворк, 
который включает в себя набор инструментов для пентеста и этичного хакерства. 
Им пользуются, чтобы взламывать системы и сети, 
запускать в них вредоносный код или получать доступ к нужной информации.
'''

install_msf = ('curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall')

zapusk_msf = print('Запуск инструмента: msfconsole')