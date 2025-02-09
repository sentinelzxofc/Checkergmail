import requests
import os
from colorama import Fore, init

init(autoreset=True)

def upgrade_script():
    url = "https://raw.githubusercontent.com/sentinelzxofc/Checkergmail/main/gmail_checker.py"
    local_path = "gmail_checker.py"

    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(response.text)

        print(Fore.GREEN + "Atualização concluída com sucesso!")
    except Exception as e:
        print(Fore.RED + f"Erro ao atualizar o script: {e}")

if __name__ == "__main__":
    upgrade_script()