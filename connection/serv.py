import socket



class Server:
    def __init__(self, HOST, PORT):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.game_time = 0
        self.s.bind((HOST, PORT))
        self.s.listen(1)
        self.conn, self.addr = self.s.accept()#conn - socket, addr[0] - client ip
    """
    def get_and_send_result(self):
        while True:
            data = float(self.conn.recv(25).decode())
            if data == 0:
                if self.game_time != 0:
                    winner_n = "WIN NASTYA"
                else:
                    winner_n = "WIN NOBODY"
            elif self.game_time == 0:
                winner_n = "WIN NASTYA"
            else:
                if self.game_time > data:
                    winner_n = "WIN LIZA"
                elif self.game_time < data:
                    winner_n = "WIN NASTYA"
                else:
                    winner_n = "WIN NOBODY"

            self.conn.sendall(winner_n.encode())

            print(winner_n)
            winner(winner_n)

            self.s.close()
            break
    """
