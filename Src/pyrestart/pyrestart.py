# PyRestart
# Python script restart


def newRestart(**kwargs):
    """
    Restart script with this
    the kwargs accepts these params:
    noargs, accept bool and used to tell if arguments are going to be passed, true if not
    argv, accept array of strings, meant to be used with sys.argv or something else, used if noargs is true
    """

    import subprocess
    import platform
    import sys

    noargs = kwargs["noargs"]


    cmd = []

    if __name__ == '__main__':
        cmd += [__file__]
    else:
        try:
            cmd += [sys.modules['__main__'].__file__]
        except AttributeError:
            pass
        
    
    if not noargs:
        cmd += kwargs["argv"]
    
    try:

        if cmd == []:
            cmd.insert(0, sys.executable)
            subprocess.run(cmd)
        else:
            subprocess.run(cmd)
        
    except OSError:
        if platform.system() == "Windows" or platform.system() == "Linux" or platform.system() == "Darwin":
            cmd.insert(0, sys.executable)
            subprocess.Popen(cmd)
        elif platform.system() == "":
            raise OSError("The platform cannot be determined, restarting failed.")
        else:
            raise OSError("Other platforms are not supported!")

def new_restart(**kwargs):
    newRestart(kwargs)

if __name__ == '__main__':
    print("a")
    newRestart(noargs=True)