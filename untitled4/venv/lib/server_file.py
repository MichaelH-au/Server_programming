import socket
from multiprocessing import Process

HTML_ROOT_DIR = "./html"

def handle_client(client_socket):
    request_data = client_socket.recv(1024)
    # print("request data:", request_data.decode("utf-8"))
    request_lines = request_data.decode("utf-8").splitlines()
    print(request_lines)

    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_heards = "Server: My server\r\n"
    response_body = "hello itcast"
    response = response_start_line + response_heards + "\r\n" + response_body
    print("response data:", response)
    client_socket.send(bytes(response,"utf-8"))
    client_socket.close()

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(("",3000))
    server_sock.listen(128)


    while(True):
        client_socket, client_address = server_sock.accept()
        # print("[%s, %s] connected" % (client_address[0],client_address[1]))
        print("[%s, %s] connected" % client_address)
        handle_client_process = Process(target=handle_client,args=(client_socket,))
        handle_client_process.start()
        client_socket.close()


if __name__ == "__main__":
    main()