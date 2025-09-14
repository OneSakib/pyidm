import subprocess
import sys
import os
import shutil

# Run PyInstaller after setup


def run_pyinstaller():
    print("Running PyInstaller...")
    command = [
        sys.executable, "-m", "PyInstaller",
        "--windowed",
        "--icon=icons/icon.ico",
        "pyIDM.py"
    ]
    subprocess.run(command, check=True)
    print("PyInstaller build complete.")


# Example: call this function at the end of your setup script
if __name__ == "__main__":
    # After everything, optionally run PyInstaller
    run_pyinstaller()
    # Remove bdist folder
    if os.path.exists('build'):
        shutil.rmtree('build')
