import socket

# Endereço IP e porta do servidor
host = '10.113.60.230'  # Endereço IP do servidor
porta = 12345  # Porta do servidor

# Cria um objeto socket UDP
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Função para receber mensagens do servidor
def receber_mensagens():
    while True:
        mensagem, endereco = cliente_socket.recvfrom(1024)
        print(f"Recebido de {endereco[0]}: {mensagem.decode('utf-8')}")

# Inicializa uma thread para receber mensagens do servidor
import threading
thread_recebimento = threading.Thread(target=receber_mensagens)
thread_recebimento.daemon = True
thread_recebimento.start()

# Loop principal do cliente
while True:
    mensagem = input("Digite a mensagem a ser enviada: ")
    
    if mensagem == ".parar":
        print("Encerrando o programa...")
        break
    
    if mensagem.startswith(".destino "):
        host = mensagem[9:]
        print(f"Mudou o destino para {host}")
        continue

    cliente_socket.sendto(mensagem.encode('utf-8'), (host, porta))

# Feche o socket do cliente
cliente_socket.close()
