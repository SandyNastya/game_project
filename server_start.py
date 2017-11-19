from connection.serv import Server


HOST = '192.168.1.35'
PORT = 49055

server = Server(HOST, PORT)

server.send_pos1_x()
server.send_pos1_y()
server.send_pos2_x()
server.send_pos2_y()

server.get_send_cur_pos()

server.stop_connection()