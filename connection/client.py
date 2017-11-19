import socket


class Client:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.game_time = 0
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))

    def get_self_x0(self):
        return int(self.s.recv(20).decode())
    def get_self_y0(self):
        return int(self.s.recv(20).decode())
    def get_opp_x0(self):
        return int(self.s.recv(20).decode())
    def get_opp_y0(self):
        return int(self.s.recv(20).decode())

    def send_x(self, x):
        self.s.send(str(x).encode())
    def send_y(self, y):
        self.s.send(str(y).encode())

    def get_opp_x(self):
        return int(self.s.recv(20).decode())
    def get_opp_y(self):
        return int(self.s.recv(20).decode())

    def check_state(self, state):
        self.s.send(str(state).encode())

    def stop_connection(self):
        self.s.close()

