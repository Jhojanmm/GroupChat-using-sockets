import socket
import threading
import time

# Iniciar el cliente

host = "" # Host ngrok
port = "" # Port ngrok
print(host, port)

    
def receive_messages(client_socket):
    reconectar = threading.Thread(target=reconnect, args=(client_socket,))
    reconectar.start()
    while True:
        # Recibir mensajes del servidor
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode()
        print(message)

    # Cerrar la conexión del cliente
    client_socket.close()

def reconnect(client_socket):
    tiempo_inicio = time.time()

    # Definir el tiempo en minutos
    tiempo_espera = 3
    
    while True:
        # Calcular el tiempo actual
        tiempo_actual = time.time()
    
        # Verificar si han pasado 5 minutos
        if tiempo_actual - tiempo_inicio >= tiempo_espera * 60:
            client_socket.send("Reconectado".encode())
            # Reiniciar el tiempo de inicio
            tiempo_inicio = time.time()
    client_socket.close()



def start_client(host, port):
    # Configurar el cliente
    host = f'{host}'
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Iniciar un hilo para recibir mensajes del servidor
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    
    
    while True:
        
        # Enviar mensajes al servidor
        message = input("Usuario (Tú): ")
        client_socket.send(message.encode())

start_client(host, port)