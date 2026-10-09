from i3ipc import Connection, Event
import time

# Create the Connection object that can be used to send commands and subscribe
# to events.
i3 = Connection()

# Print the name of the focused window
focused = i3.get_tree().find_focused()
print(type(focused))
print('Focused window %s is on workspace %s' %
      (focused.name , focused.workspace().name))
i3.command('floating enable')
# while(True):
#     print(f"x: {focused.rect.x},y: {focused.rect.y},height: {focused.rect.height},width: {focused.rect.width}")

focused = i3.get_tree().find_focused()

x = focused.window_rect.x
y = focused.window_rect.y

# def on_window(i3,e):
for i in range(30):
    print("")
print("  ______  _    _ ______\n \
 |     \\  \\  /  |     \\ \n \
 |_____/   \\/   |_____/ \n \
")
# print(focused.id)
height = focused.rect.height
width = focused.rect.width
height = 320
width = 240
i3.command(f"[con_id=\"{focused.id}\"]resize set {height} px {width} px")
dir = 0;
while(True):

    if(y <= 0):
        if(dir == 0):
            dir = 3
        else:
            dir = 2
    elif(y >= 1080-width):
        if(dir == 3):
            dir = 0
        else:
            dir = 1
    elif(x <= 0):
        if(dir == 0):
            dir = 1
        else:
            dir = 2
    elif(x >= 1920-height):
        if(dir == 1):
            dir = 0
        else:
            dir = 3

    
    if(dir == 0):
        x-=1
        y-=1
    if(dir == 1):
        x+=1
        y-=1
    if(dir == 2):
        x+=1
        y+=1
    if(dir == 3):
        x-=1
        y+=1
    i3.command(f"[con_id=\"{focused.id}\"]move position {x} px {y} px")
    # print(f"x: {x},y: {y},height: {focused.window_rect.height},width: {focused.window_rect.width}")
        
    time.sleep(0.005)

    

# i3.on('window', on_window)


# i3.main()

# Query the ipc for outputs. The result is a list that represents the parsed
# reply of a command like `i3-msg -t get_outputs`.
# outputs = i3.get_outputs()

# print('Active outputs:')

# for output in filter(lambda o: o.active, outputs):
#     print(output.name)

# i3.command('floating enable')
# i3.command('move left 20px')
# # Send a command to be executed synchronously.
# i3.command('focus left')

# # Take all fullscreen windows out of fullscreen
# for container in i3.get_tree().find_fullscreen():
#     container.command('fullscreen')

# # Print the names of all the containers in the tree
# root = i3.get_tree()
# print(root.name)
# for con in root:
#     print(con.name)

# # Define a callback to be called when you switch workspaces.
# def on_workspace_focus(self, e):
#     # The first parameter is the connection to the ipc and the second is an object
#     # with the data of the event sent from i3.
#     if e.current:
#         print('Windows on this workspace:')
#         for w in e.current.leaves():
#             print(w.name)

# # Dynamically name your workspaces after the current window class
# def on_window_focus(i3, e):
#     focused = i3.get_tree().find_focused()
#     ws_name = "%s:%s" % (focused.workspace().num, focused.window_class)
#     i3.command('rename workspace to "%s"' % ws_name)

# # Subscribe to events
# i3.on(Event.WORKSPACE_FOCUS, on_workspace_focus)
# i3.on(Event.WINDOW_FOCUS, on_window_focus)

# # Start the main loop and wait for events to come in.
# i3.main()
