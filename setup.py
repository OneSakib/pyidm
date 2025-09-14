from cx_Freeze import Executable, setup
import sys
import os
import shutil
PYTHON_INSTALL_DIR = os.path.dirname(sys.executable)
SYSTEM_PYTHON_DIR = os.environ.get(
    'SYSTEM_PYTHON_DIR', r'C:\Users\malik\AppData\Local\Programs\Python\Python311')
tcl_path = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
tk_path = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
tk_dll = os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll')
tcl_dll = os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')
if not os.path.exists(tcl_path) or not os.path.exists(tk_path):
    if SYSTEM_PYTHON_DIR:
        tcl_path = os.path.join(SYSTEM_PYTHON_DIR, 'tcl', 'tcl8.6')
        tk_path = os.path.join(SYSTEM_PYTHON_DIR, 'tcl', 'tk8.6')
        tk_dll = os.path.join(SYSTEM_PYTHON_DIR, 'DLLs', 'tk86t.dll')
        tcl_dll = os.path.join(SYSTEM_PYTHON_DIR, 'DLLs', 'tcl86t.dll')
if not os.path.exists(tcl_path) or not os.path.exists(tk_path) or not os.path.exists(tk_dll) or not os.path.exists(tcl_dll):
    raise FileNotFoundError(
        "TCL/TK files not found. Please set SYSTEM_PYTHON_DIR environment variable.")

os.environ['TCL_LIBRARY'] = tcl_path
os.environ['TK_LIBRARY'] = tk_path

include_files = [(tk_dll, os.path.join('lib', 'tk86.dll')),
                 (tcl_dll,
                  os.path.join('lib', 'tcl86.dll')),
                 ('icons/')]
base = None

if sys.platform == 'win32':
    base = "Win32GUI"
directory_table = [
    ("DesktopShortcut", "DesktopFolder",
     "pyIDM",
     "TARGETDIR",
     "[TARGETDIR]\pyIDM.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",)
]
msi_data = {"Shortcut": directory_table}
bdist_msi_option = {'data': msi_data}
executables = [
    Executable(script="pyIDM.py", base=base, icon="icon.ico")]
build_exe_options = {"packages": ["os", "sys",  "PySimpleGUI", "pyperclip", "plyer", "certifi", "youtube_dl", "pycurl"],
                     "include_files": include_files
                     }

setup(
    name="pyIDM",
    version="1.0",
    author='Sakib Malik',
    description="pyIDM is a downloading software where you can download any file with speed. max connections",
    options={"build_exe": build_exe_options, "bdist_msi": bdist_msi_option, },
    executables=executables
)

# Remove bdist folder
if os.path.exists('build'):
    shutil.rmtree('build')
