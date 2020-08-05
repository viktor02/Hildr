import cx_Freeze

exe = [cx_Freeze.Executable("daemon.py", 
                            base = "Console",
                            targetName = "Hildr",
                            shortcutName = "Hildr",
                            copyright = "Viktor Karpov")]

cx_Freeze.setup(
    name = "Hildr",
    version = "0.2.2",
    options = {"build_exe": {"packages": ["psutil", "Hildr", "configparser", "colorama", "sys"],  
        "include_files": ["config.ini", "games.txt"]}},
    executables = exe
) 