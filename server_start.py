from connection.serv import Server


HOST = '192.168.1.35'
PORT = 49055

server = Server(HOST, PORT)

server.send_pos1_x()
server.send_pos1_y()
server.send_pos2_x()
server.send_pos2_y()

while server.conn1_state and server.conn2_state not in ("True" or "None"):
    server.get_cur_pos()

server.stop_connection()