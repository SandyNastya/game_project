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
        self.s.listen(1)
        self.conn2, self.addr2 = self.s.accept()

        self.conn1_state = "None"
        self.conn2_state = "None"


    #send start positions
    def send_pos1_x(self):
        self.conn1.sendto(pos1_x, self.addr1)
        self.conn2.sendto(pos2_x, self.addr2)
    def send_pos1_y(self):
        self.conn1.sendto(pos1_y, self.addr1)
        self.conn2.sendto(pos2_y, self.addr2)
    def send_pos2_x(self):
        self.conn1.sendto(pos2_x, self.addr1)
        self.conn2.sendto(pos1_x, self.addr2)
    def send_pos2_y(self):
        self.conn1.sendto(pos2_y, self.addr1)
        self.conn2.sendto(pos1_y, self.addr2)

    def get_state(self):
        if (self.conn1.recv(22).decode()) in ("True" or "False"):
            self.conn1_state = self.conn1.recv(22).decode()
        if (self.conn2.recv(22).decode()) in ("True" or "False"):
            self.conn2.recv(22).decode()

    #get and send current positions
    def get_cur_pos(self):
        if (self.conn1.recv(20).decode()) not in ("True" or "False"):
            self.g1_cur_xpos = self.conn1.recv(20)
            self.g1_cur_ypos = self.conn1.recv(20)

            self.conn1.sendto(self.g1_cur_xpos, self.addr1)
            self.conn1.sendto(self.g1_cur_ypos, self.addr1)

        if (self.conn2.recv(20).decode()) not in ("True" or "False"):
            self.g2_cur_xpos = self.conn2.recv(20)
            self.g2_cur_ypos = self.conn2.recv(20)

            self.conn2.sendto(self.g2_cur_xpos, self.addr2)
            self.conn2.sendto(self.g2_cur_ypos, self.addr2)

    def stop_connection(self):
        self.s.close()
