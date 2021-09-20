import pynvim
import platform
import socket


@pynvim.plugin
class MayaScriptEditor(object):

    def __init__(self, nvim):
        self.nvim = nvim

        self.HOST = '127.0.0.1'
        self.PORT = 54321
        self.ADDR = (self.HOST, self.PORT)

        if platform.system() == "Darwin":
            self.TEMP = "/var/tmp/mayaScriptTmp.py"
        else:
            self.TEMP = None

    @pynvim.command('SendToMaya', nargs='*', range='')
    def send_to_maya(self, args, range):

        buffer = self.nvim.current.buffer

        if self.TEMP is None:
            print("Failed to get temp file path")
            return

        f = open(self.TEMP, 'w')
        f.truncate(0)

        for i in buffer[:]:
            f.write(i)
            f.write("\n")

        f.close()

        cmd = """exec(open("{}").read())""".format(self.TEMP)

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client.connect(self.ADDR)
            client.send(cmd.encode())
        except ConnectionRefusedError:
            print("Failed to connect. Make sure Maya command port is open.")

        # data = client.recv(1024)
        client.close()

        return 0
