import socket




class Client:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.game_time = 0
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))
    """
    def start_game(self):
        self.game_time = (str(game())).encode()

    def get_result(self):
        result = self.s.recv(10).decode()
        print(result)
        winner(result)
        self.s.close()
    """

