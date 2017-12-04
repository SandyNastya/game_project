import socket
from player import RADIUS
from window import WINDOW_WIDTH, WINDOW_HEIGHT


pos1_x = str(RADIUS).encode()
pos1_y = str(RADIUS).encode()
pos2_x = str(WINDOW_WIDTH - RADIUS).encode()
pos2_y = str(WINDOW_HEIGHT - RADIUS).encode()

class Server:
    def __init__(self, HOST, PORT):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST, PORT))

        self.g1_cur_xpos = 0
        self.g1_cur_ypos = 0
        self.g2_cur_xpos = 0
        self.g2_cur_ypos = 0

        self.s.listen(1)
        self.conn1, self.addr1 = self.s.accept()#conn - socket, addr[0] - client ip
        #self.conn1.setblocking(0)

        self.conn1_state = "None"
        self.serv_state = "None"

    def get_opp_state(self):
        state = self.conn1.recv(22).decode()
        if (state) in ("True" or "False"):
            self.conn1_state = state
    def check_own_state(self, state):
        if state in ("True" or "False"):
            self.serv_state = state

    def get_cur_opp_xpos(self):
        data = self.conn1.recv(20).decode()
        if data not in ("True" or "False"):
            self.g2_cur_xpos = data
            return self.g2_cur_xpos
    def get_cur_opp_ypos(self):
        data = self.conn1.recv(20).decode()
        if data not in ("True" or "False"):
            self.g2_cur_ypos = data
            return self.g2_cur_ypos

    def send_cur_xpos(self, x):
        self.g1_cur_xpos = x
        self.conn1.sendto(self.g1_cur_xpos, self.addr1)

    def send_cur_ypos(self, y):
        self.g1_cur_ypos = y
        self.conn1.sendto(self.g1_cur_ypos, self.addr1)

    def stop_connection(self):
        self.s.close()
