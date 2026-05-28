import socket
import threading

ROBOT_IP="192.168.0.10"
PORT=30002
PORT_CMD=5000
file_name="palete_tcp2.script"

tcp_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_socket.connect((ROBOT_IP, PORT))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("0.0.0.0", PORT_CMD))
server.listen(1)


try:
    with open(file_name) as f:
        script=f.read()
except FileNotFoundError:
    print("Arquivo não encontrado")
except IOError:
    print("Não foi possível abrir o arquivo")


tcp_socket.sendall(script.encode("utf-8"))
print("Aguardando conexão do robô...")
conn, addr = server.accept()
print("Conectado:", addr)

def receber_comando():
    while True:
        data=conn.recv(1024)
        if not data:
            break

        print(f"Mensagem do Robô: {data.decode('utf-8').strip()}\n")


def enviar_comando():
    while True:
        cmd=input("Digite aqui um comando, STOP, PAUSE, SAIR: \n").upper()
        if cmd=="SAIR": break
        conn.sendall((cmd+"\n").encode('utf-8'))

           
            
def start_program():
    prompt="""Vamos começar o programa! Escolha a velocidade, a aceleração e o blend da operação, nesta ordem\n
    Exemplo de input para o programa: 0.5,0.5,0.05 -- sempre entre vírgulas e números com ponto"""
    cmd=input(prompt)
    conn.sendall(("("+cmd+")").encode('utf-8'))

    cmd=input("Digite a quantidade de layers, número de linhas e colunas\n")
    conn.sendall(("("+cmd+")").encode('utf-8'))

    cmd=input("Digite a altura de aproximação/retração\n")
    conn.sendall(("("+cmd+")").encode('utf-8'))

    cmd=input("Digite um vetor com o tamanho das caixas para a paletização\n")
    conn.sendall(("("+cmd+")").encode('utf-8'))

    cmd=input("Digite um vetor com as orientações das caixas de acordo com o padrão que quer\n")
    conn.sendall(("("+cmd+")").encode('utf-8'))

    cmd=input("Digite FIXO para usar os pontos setados ou alterar para mudar a paletização:\n").upper()
    conn.sendall((cmd+"\n").encode('utf-8'))


thread=threading.Thread(target=receber_comando,daemon=True)
thread.start()

try:
    start_program()
    enviar_comando()
finally:
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()
    server.close()
    tcp_socket.shutdown(socket.SHUT_RDWR)
    tcp_socket.close()
    print("Portas liberadas")
