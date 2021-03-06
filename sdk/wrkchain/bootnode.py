import os
import shutil
import subprocess

BIN_BOOTNODE = shutil.which("bootnode")


class BootnodeNotFoundException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class BootnodeKey:
    def __init__(self, build_dir, ip, port, docker_ip, docker_port,
                 key_prefix=''):

        if not BIN_BOOTNODE:
            raise BootnodeNotFoundException('bootnode executable not found. '
                                            'Please install bootnode')

        if len(key_prefix) > 0:
            key_prefix = f'{key_prefix}'
        else:
            key_prefix = 'bootnode'

        node_dir = build_dir + '/node_keys'
        if not os.path.exists(node_dir):
            os.makedirs(node_dir)

        self.__bootnode_key_path = node_dir + f'/{key_prefix}.key'
        self.__ip = ip
        self.__port = port
        self.__docker_ip = docker_ip
        self.__docker_port = docker_port

    def generate_bootnode_key(self):
        if not self.have_key():
            cmd = [BIN_BOOTNODE, "-genkey", self.__bootnode_key_path]
            self.__run(cmd)

    def get_bootnode_address(self):
        if not self.have_key():
            self.generate_bootnode_key()

        cmd = [BIN_BOOTNODE, "-nodekey",
               self.__bootnode_key_path, "-writeaddress"]

        result = self.__run(cmd)

        if result.returncode == 0:
            bootnode_address = result.stdout.rstrip("\n\r")
        else:
            print(result)
            bootnode_address = None

        return bootnode_address

    def get_enode(self):
        if not self.have_key():
            self.generate_bootnode_key()

        return f'enode://{self.get_bootnode_address()}@{self.__ip}' \
            f':{self.__port}'

    def get_docker_enode(self):
        if not self.have_key():
            self.generate_bootnode_key()

        return f'enode://{self.get_bootnode_address()}@{self.__docker_ip}' \
            f':{self.__docker_port}'

    def have_key(self):
        return os.path.exists(self.__bootnode_key_path)

    def __run(self, cmd):
        result = subprocess.run(
            cmd, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, universal_newlines=True)
        return result
