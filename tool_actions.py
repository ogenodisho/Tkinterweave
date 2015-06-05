import tool_names
import global_configs

# Dictates what happens when a paint tool is pressed.
# Sink the clicked button and raise all of the other ones.
# Also, change the current_tool which is global in the main
def paint_tool_pressed(button_object, tool_name, buttons_tuple):
    if button_object.cget("relief") == "raised":
        for b in buttons_tuple:
            b.config(relief="raised")
        button_object.config(relief="sunken")
        global_configs.CURRENT_TOOL = tool_name
