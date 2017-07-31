from cx_Freeze import setup, Executable

setup(name = "TESTApp",
    version = "0.1",
    description = "An example",
    executables = [Executable("GUI.py")]
    )
