import smtplib
import socket
import os
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_ascii_art(file):
    try:
        with open(file, 'r') as f:
            ascii_art = f.read()
            print(Fore.MAGENTA + ascii_art)
    except Exception as e:
        print(f"Erro ao carregar o ASCII art: {e}")

def display_credits():
    border = Fore.CYAN + "═" * 50
    credits = [
        Fore.YELLOW + "By https://github.com/sentinelzxofc",
        Fore.YELLOW + "Script GitHub: https://github.com/sentinelzxofc/Checkergmail"
    ]
    print(border)
    for line in credits:
        print(Fore.CYAN + "║" + Fore.YELLOW + line.center(48) + Fore.CYAN + "║")
    print(border)

def get_mx_record(domain):
    try:
        records = socket.gethostbyname_ex(f"alt1.gmail-smtp-in.l.google.com")
        mx_record = records[2][0]
        return mx_record
    except Exception as e:
        print(f"Erro ao obter o registro MX: {e}")
        return None

def check_gmail(email):
    if not email or "@" not in email:
        return False

    domain = email.split('@')[1]
    mx_record = get_mx_record(domain)
    if not mx_record:
        return False

    try:
        server = smtplib.SMTP(mx_record, timeout=10)
        server.set_debuglevel(0)

        server.ehlo()
        server.mail('meuemail@gmail.com')
        code, message = server.rcpt(email)
        server.quit()

        if code == 250:
            return True
        else:
            return False
    except Exception as e:
        print(f"Erro ao verificar o e-mail {email}: {e}")
        return False

def check_bulk_emails():
    input_file = input(Fore.GREEN + "Digite o local do arquivo gmail.txt (ex: /sdcard/gmail.txt): ")
    output_valid = input(Fore.GREEN + "Digite o local para salvar gmail_valido.txt (ex: /sdcard/download): ")
    output_invalid = input(Fore.GREEN + "Digite o local para salvar gmail_invalido.txt (ex: /sdcard/download): ")

    try:
        if not os.path.exists(input_file):
            print(Fore.RED + "Arquivo de entrada não encontrado!")
            return

        with open(input_file, 'r') as f:
            emails = [line.strip() for line in f if line.strip()]

        if not emails:
            print(Fore.RED + "Nenhum e-mail válido encontrado no arquivo!")
            return

        valid_emails = []
        invalid_emails = []

        clear_screen()
        display_ascii_art('v.txt')
        display_file_locations(input_file, output_valid, output_invalid)

        print(Fore.CYAN + "═" * 50)
        print(Fore.GREEN + "Válidos".ljust(25) + Fore.CYAN + "║" + Fore.RED + "Inválidos".rjust(25))
        print(Fore.CYAN + "═" * 50)

        for email in emails:
            if check_gmail(email):
                valid_emails.append(email)
                print(Fore.GREEN + email.ljust(25) + Fore.CYAN + "║" + " " * 25)
            else:
                invalid_emails.append(email)
                print(" " * 25 + Fore.CYAN + "║" + Fore.RED + email.rjust(25))

        if valid_emails:
            with open(os.path.join(output_valid, 'gmail_valido.txt'), 'w') as f:
                f.write("\n".join(valid_emails))

        if invalid_emails:
            with open(os.path.join(output_invalid, 'gmail_invalido.txt'), 'w') as f:
                f.write("\n".join(invalid_emails))

        print(Fore.CYAN + "═" * 50)
        print(Fore.GREEN + f"Verificação concluída! Verifique os arquivos em {output_valid} e {output_invalid}.")

    except Exception as e:
        print(Fore.RED + f"Erro ao processar os e-mails: {e}")

def display_file_locations(input_file, output_valid, output_invalid):
    print(Fore.CYAN + "═" * 50)
    print(Fore.YELLOW + f"Arquivo de entrada: {input_file}")
    print(Fore.YELLOW + f"Arquivo de válidos: {output_valid}/gmail_valido.txt")
    print(Fore.YELLOW + f"Arquivo de inválidos: {output_invalid}/gmail_invalido.txt")
    print(Fore.CYAN + "═" * 50)

def generate_and_check_emails():
    input_file = "290kGmail.txt"
    output_valid = input(Fore.GREEN + "Digite o local para salvar gmail_valido.txt (ex: /sdcard/download): ")
    output_invalid = input(Fore.GREEN + "Digite o local para salvar gmail_invalido.txt (ex: /sdcard/download): ")

    try:
        if not os.path.exists(input_file):
            print(Fore.RED + "Arquivo de entrada não encontrado!")
            return

        with open(input_file, 'r') as f:
            emails = [line.strip().split(":")[0] for line in f if line.strip()]

        if not emails:
            print(Fore.RED + "Nenhum e-mail válido encontrado no arquivo!")
            return

        valid_emails = []
        invalid_emails = []

        clear_screen()
        display_ascii_art('v.txt')

        print(Fore.CYAN + "═" * 50)
        print(Fore.GREEN + "Válidos".ljust(25) + Fore.CYAN + "║" + Fore.RED + "Inválidos".rjust(25))
        print(Fore.CYAN + "═" * 50)

        for email in emails:
            if check_gmail(email):
                valid_emails.append(email)
                print(Fore.GREEN + email.ljust(25) + Fore.CYAN + "║" + " " * 25)
            else:
                invalid_emails.append(email)
                print(" " * 25 + Fore.CYAN + "║" + Fore.RED + email.rjust(25))

        if valid_emails:
            with open(os.path.join(output_valid, 'gmail_valido.txt'), 'w') as f:
                f.write("\n".join(valid_emails))

        if invalid_emails:
            with open(os.path.join(output_invalid, 'gmail_invalido.txt'), 'w') as f:
                f.write("\n".join(invalid_emails))

        print(Fore.CYAN + "═" * 50)
        print(Fore.GREEN + f"Verificação concluída! Verifique os arquivos em {output_valid} e {output_invalid}.")

    except Exception as e:
        print(Fore.RED + f"Erro ao processar os e-mails: {e}")

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

def main_menu():
    clear_screen()
    display_ascii_art('s.txt')
    display_credits()
    print(Fore.CYAN + "\n" + "═" * 50)
    print(Fore.MAGENTA + "1. Verificar Gmail em ")
    print(Fore.MAGENTA + "2. Gerar Gmail e verificar em massa")
    print(Fore.MAGENTA + "3. Verificar Gmail com senha")
    print(Fore.MAGENTA + "4. Upgrade")
    print(Fore.RED + "X. Sair")
    print(Fore.CYAN + "═" * 50)

    choice = input(Fore.YELLOW + "Escolha uma opção: ").strip().lower()

    if choice == '1':
        check_bulk_emails()
    elif choice == '2':
        generate_and_check_emails()
    elif choice == '3':
        print(Fore.YELLOW + "Nova atualização!")
    elif choice == '4':
        upgrade_script()
    elif choice == 'x':
        print(Fore.RED + "Saindo...")
        exit()
    else:
        print(Fore.RED + "Opção inválida. Tente novamente.")

if __name__ == "__main__":
    while True:
        main_menu()
        input(Fore.CYAN + "\nPressione Enter para continuar...")