import cx_Freeze
import sys
import os

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

# Update paths to point to Python 3.12 installation
os.environ['TCL_LIBRARY'] = r"C:\Users\Akhan\AppData\Local\Programs\Python\Python312\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Akhan\AppData\Local\Programs\Python\Python312\tcl\tk8.6 "

executables = [
    cx_Freeze.Executable("Face_Recognition_Software.py", base=base, icon="icon.png")
]

cx_Freeze.setup(
    name="Facial Recognition Software",
    options={
        "build_exe": {
            "packages": ["tkinter", "os"],
            "include_files": [
                "icon.png",
                os.path.join(os.environ['TCL_LIBRARY'], 'tcl86t.dll'),
                os.path.join(os.environ['TK_LIBRARY'], 'tk86t.dll'),
                'images pro',  # Ensure this folder exists and is correctly referenced
                'data',
                'database',
                'attendance_report'
            ]
        }
    },
    version="1.0",
    description="Face Recognition Automatic Attendance System | Developed By Akhand Chaurasiya",
    executables=executables
)
