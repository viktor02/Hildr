import cx_Freeze

exe = [cx_Freeze.Executable("daemon.py", 
                            base = "Win32GUI",
                            targetName = "GTracker",
                            shortcutName = "GTracker",
                            copyright = "Viktor Karpov")]

cx_Freeze.setup(
    name = "GTracker",
    version = "0.2.2",
    options = {"build_exe": {"packages": ["psutil", "GTracker", "configparser", "sys"],  
        "include_files": ["config.ini", "games.txt"]}},
    executables = exe
) 