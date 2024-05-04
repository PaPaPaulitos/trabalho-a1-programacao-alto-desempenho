import subprocess
import os
import time

def tests_conections(num_conections):
    username = ""
    for user in range(0,num_conections):
        username = str(user)
        os.chdir("../Client")
        subprocess.Popen(["python", "index_client.py", username], shell=True)
        subprocess.Popen(["cmd", "/c"], creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)

tests=[10,20,100]

for test in tests:
    print(f"Testando com {test} conexões.")
    initial_time = time.time()
    tests_conections(test)
    final_time = time.time()
    total_time = final_time - initial_time
    print(f"O tempo de testagem foi {total_time} segundos.")