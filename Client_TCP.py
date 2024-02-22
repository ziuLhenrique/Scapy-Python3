#!/usr/bin/python3

import socket
import sys

def main():
    # Verifica se o número correto de argumentos foi fornecido
    if len(sys.argv) != 5:
        print(f"Uso {sys.argv[0]} <IP> <PORTA> <METODO> </caminho> <--exemplo> ")
        sys.exit(1)

    # Obtém o IP e a porta a partir dos argumentos de linha de comando
    targuet_ip = sys.argv[1]
    targuet_port = int(sys.argv[2])
    metodo = sys.argv[3]
    dir = sys.argv[4]

    # Cria um socket TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conecta-se ao servidors
        client.connect((targuet_ip,targuet_port))

        # Envia uma solicitação HTTP básica
        client.send(('{} {} HTTP/1.1\r\nHost: {}\r\n\r\n'.format(metodo,dir,targuet_ip)).encode())

        # Recebe a resposta do servidor
        resposta = client.recv(4096)

        # Exibe a resposta decodificada
        print(resposta.decode())
    
    except Exception as e:
        print(f"ERRO ao conectar-se ao servidor: {e}")

    finally:
        # Fecha o socket
        client.close()
    
if __name__ == "__main__":
    main()
    