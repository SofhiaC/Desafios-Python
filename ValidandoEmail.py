import re

def funcao(s):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    #Padrão regex simples e mais eficaz do e-mail.
    return re.search(padrao, s) != None

def filtro(emails):
    return list(filter(funcao, emails))

if __name__ == '__main__':
    n = int(input("Insira a quantidade de email que você deseja verificar:"))
    emails = []
    for _ in range(n):
        emails.append(input("Email:"))

emails_filtrados = filtro(emails)
emails_filtrados.sort()
print(f"Email válidos: {emails_filtrados}") 