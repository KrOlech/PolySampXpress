
from TCIPManipulator import load_drivers,conncect_to_controller,is_connected,reference_axes, is_referencing, get_axes_positions,move_axes_to_abs,close_connection

from time import sleep

c848 = load_drivers()
print(c848)

controller_id = conncect_to_controller(c848)
print('controller_id:', controller_id)
print('is connected:', is_connected(controller_id,c848))


reference_axes(controller_id, c848,axes='xyz')
sleep(10)
#while not is_referencing(controller_id, c848, axes='xyz'):
#    print(get_axes_positions(controller_id,c848, axes='xyz'))
    
move_axes_to_abs(controller_id,c848, axes='xyz', positions=[25.0, 26.0, 26.0])

sleep(10)

close_connection(controller_id,c848)
print('is connected:', is_connected(controller_id,c848))