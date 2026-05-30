import time
import ctypes
from pypresence import Presence

CLIENT_ID = '1510145559552594082'

print("Starting Autodesk Inventor Discord RPC...")
print(f"Using Client ID: {CLIENT_ID}")
print("(Keep this window open in the background. Close it to stop.)\n")

rpc = None
presence_active = False
start_time = None

def connect_discord():
    global rpc
    while True:
        try:
            rpc = Presence(CLIENT_ID)
            rpc.connect()
            print(f"[{time.strftime('%X')}] Successfully connected to Discord!")
            return
        except Exception:
            print(f"[{time.strftime('%X')}] Waiting for Discord to open...")
            time.sleep(10)

connect_discord()

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

while True:
    try:
        EnumChildWindows = ctypes.windll.user32.EnumChildWindows

        def get_window_text(hwnd):
            length = GetWindowTextLength(hwnd)
            if length > 0:
                buff = ctypes.create_unicode_buffer(length + 1)
                GetWindowText(hwnd, buff, length + 1)
                return buff.value
            return ""

        doc_name = None
        activity_type = "Idling"

        def child_window_proc(hwnd, lParam):
            global doc_name
            if IsWindowVisible(hwnd):
                text = get_window_text(hwnd)
                lower = text.lower()
                # Check if this child window is a document
                if ".ipt" in lower or ".iam" in lower or ".dwg" in lower or ".idw" in lower or ".ipn" in lower:
                    # Strip any asterisks indicating unsaved changes
                    clean_name = text.replace("*", "").strip()
                    # MDI child windows often have the view name like "Part1.ipt - View1"
                    doc_name = clean_name.split(" - ")[0]
                    return False # Stop enumerating children
            return True

        def top_window_proc(hwnd, lParam):
            if IsWindowVisible(hwnd):
                text = get_window_text(hwnd)
                if "Autodesk Inventor" in text:
                    # Found Inventor main window, now look inside it!
                    EnumChildWindows(hwnd, ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))(child_window_proc), 0)
            return True

        EnumWindows(ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))(top_window_proc), 0)

        if doc_name is not None:
            lower_name = doc_name.lower()
            if ".ipt" in lower_name or lower_name.startswith("part"):
                activity_type = "Making a Part"
            elif ".iam" in lower_name or lower_name.startswith("assembly"):
                activity_type = "Assembling"
            elif ".dwg" in lower_name or ".idw" in lower_name or lower_name.startswith("drawing"):
                activity_type = "2D Layouting"
            elif ".ipn" in lower_name or lower_name.startswith("presentation"):
                activity_type = "Creating Presentation"
            else:
                activity_type = "Designing"
        
        if doc_name is not None:
            if start_time is None:
                start_time = int(time.time())
            
            print(f"[{time.strftime('%X')}] Detected {activity_type}. Active file: {doc_name}")
            rpc.update(
                state=f"File: {doc_name}",
                details=activity_type,
                start=start_time,
                large_image="inventor_logo", 
                large_text="Autodesk Inventor 2027"
            )
            presence_active = True
        else:
            if presence_active:
                print(f"[{time.strftime('%X')}] Inventor closed or on Home screen. Clearing Discord status.")
                rpc.clear()
                presence_active = False
                start_time = None

    except Exception as e:
        print(f"[{time.strftime('%X')}] Connection to Discord lost. Reconnecting...")
        presence_active = False
        start_time = None
        connect_discord()

    time.sleep(15)
