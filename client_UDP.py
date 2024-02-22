#!bin/python3

# Importando a biblioteca socket
import socket

# Variável que armazena o host do alvo
target_host = "127.0.0.1"

# Variável que armazena a porta do alvo
target_port = 9997

# Criando objeto socket
# 'AF_INET' significa que a comunicação será em IPv4 ou nome de host
# 'SOCK_DGRAM' significa que o protocolo utilizado será UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviando alguns dados
# OBS: O protocolo UDP não necessita de uma conexão
# 'b' significa que os dados serão enviados em bytes
client.sendto(b'AAABBBCCC', (target_host, target_port))

# Recebendo alguns dados
# 'recvfrom()' é utilizado para receber dados
# 4096 é o número máximo de bytes a serem recebidos em uma única chamada
data, addr = client.recvfrom(4096)

# Exibindo os dados
# 'print()' é usado para exibir o resultado na saída padrão (normalmente, a console)
# 'decode()  Este é um método utilizado para converter dados binários (bytes) em uma string. 
print(data.decode())

# 'close()' é para fechar o socket
client.close()







