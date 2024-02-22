#!/usr/bin/python3

import socket
import sys

def main():
    # Verifica se o número correto de argumentos foi fornecido
    if len(sys.argv) != 3:
        print(f'Modo de Uso: {sys.argv[0]} <IP> <PORTA>')
        sys.exit(1)

    # Obtém o IP e a porta a partir dos argumentos de linha de comando
    ip_alvo = sys.argv[1]
    port = int(sys.argv[2])

    # Cria um socket UDP
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Envia dados para o servidor especificado
        client.sendto(b"AAABBBCCC", (ip_alvo, port))

        # Aguarda a resposta do servidor
        data, addr = client.recvfrom(4096)

        # Imprime a resposta recebida do servidor
        print(f"Recebidos: {data.decode()}")

    except Exception as e:
        # Trata exceções, se ocorrerem
        print(f"Erro: {type(e).__name__} - {e}")

    finally:
        # Fecha o socket após o uso
        client.close()

if __name__ == "__main__":
    # Chama a função principal se o script for executado diretamente
    main()
