#!/usr/bin/env python3
import sys  # Importa o módulo sys para acessar argumentos da linha de comando.

from scapy.all import sr1, IP, ICMP  # Importa classes específicas da biblioteca Scapy
                                     # para enviar pacotes e realizar operações de rede.

if len(sys.argv) != 2:
    print("Modo de Uso: ./solicitacao_de_eco_ICMP.py 192.162.0.1")
else:
    p = sr1(IP(dst=sys.argv[1])/ICMP())  # Constrói um pacote ICMP Echo Request     
                                         # usando o endereço IP fornecido.
                                         # Utiliza a função sr1 para enviar o pacote e receber a primeira resposta.

    if p:  # Verifica se uma resposta foi recebida (se p existe).git
        p.show()  # Exibe os detalhes do pacote no console usando o método show.
