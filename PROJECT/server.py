# R-E Miller (IT), Matthew Hill (CS), Elliot Swan (CS)
import socket 
import select
import sys
import json
import shared as sh

def check_nick(s, storedname):
    #read nickname from the client
    bannedname = ["SERVER"]
    world = "HELLO"
    name = "SERVER"
    proto = ''
    sh.send_message(s,world, name, proto)
    message = ""
    while message != "READY":
        nic,msg,proto = sh.read_message(s)
        if msg in storedname or msg in bannedname: 
            message = "RETRY"
            sh.send_message(s, message, name,proto)
            continue
        message = "READY"
        sh.send_message(s, message, name,proto)
    # check nickname if nickname is taken 
    #reply back with either approved name or already taken
    #


def main():
    nickname = []
    port = int(sys.argv[1])
    host = sys.argv[2]
    if not (10000 <= port <= 65535):
        print("Port number not available")
        sys.exit(-1)
    try:
        print("working")
        with socket.socket() as s:
            #s.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host, port))
            s.listen(10)
            print("\n Server listening")
            while True:
                connection, _ = s.accept()
                with connection:
                    print("Got connection")
                    check_nick(connection, nickname )
                    print("SERVER TIME")
            
    except OSError as e:
        print(e)
    except KeyboardInterrupt:
        s.close()






if __name__ == "__main__":
    main()
