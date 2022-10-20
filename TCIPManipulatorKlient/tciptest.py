from TCIPManipulator import load_drivers,conncect_to_controller,is_connected,reference_axes, is_referencing, get_axes_positions,move_axes_to_abs,close_connection
import socket
 
TCP_IP = '172.30.254.65'
TCP_PORT = 22
BUFFER_SIZE = 1024


c848 = load_drivers()
print(c848)

controller_id = conncect_to_controller(c848)
print('controller_id:', controller_id)
print('is connected:', is_connected(controller_id,c848))
move_axes_to_abs(controller_id,c848, axes='xyz', positions=[25,25,25])


try:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    while True:
        data = s.recv(BUFFER_SIZE) 
        print("received data:", data)
        
        data = data.decode('utf8')
        
        if data=='non':
            break
            
        if data[0] == 'x':
          
            move_axes_to_abs(controller_id,c848, axes='z', positions=[float(data[1:])])
        
        else:
            move_axes_to_abs(controller_id,c848, axes='y', positions=[float(data[1:])])
    
finally:
    close_connection(controller_id,c848)
    print('is connected:', is_connected(controller_id,c848))
    s.close()