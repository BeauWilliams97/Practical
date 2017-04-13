usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

password= str(input("password: "))
if password not in usernames:
    print("invalid password")
    user_name = str(input("password: "))
elif password in usernames:
    print("password accepted")
