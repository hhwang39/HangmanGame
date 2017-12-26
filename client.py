"""
You have to run "python client.py [serverIp] [port]"
You can also type python client.py --help to see help
"""

import socket
import sys
import getopt

"""
    return true if given guess is alphabet and length 1
"""
def is_one_alpha(c):
    c = c.lower()
    if len(c) != 1:
        return False
    if (c < 'a') or (c > 'z'):
        return False
    return True


guesses = []


# main function
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
        # print(args)
        if len(args) != 2:
            print(__doc__)
            sys.exit(0)
        # print(opts)

        for o, a in opts:
            if o in ("-h", "--help"):
                print(__doc__)
                sys.exit(0)
        host = args[0]
        port = int(args[1])
        # this value might change
        buffer_size = 1024
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        m = raw_input("Ready to start game? (y/n):")

        if m.lower() == "y":
            client.send(chr(0))
        else:
            print("Closed Connection")
            client.shutdown(1)
            client.close()
            return
        # data = client.recv(buffer_size)
        # ans = raw_input(data[1:1 + ord(data[0])])
        # client.send(chr(len(ans)) + ans)
        while True:
            data = client.recv(buffer_size)
            if len(data) != 0:
                if ord(data[0]) != 0:
                    print(data[1:1 + ord(data[1])])
                    break
                else:
                    print(data[3:3 + ord(data[1])])
                    print("Incorrect Guesses:"),
                    for i in range(0, ord(data[2])):
                        print(data[3 + ord(data[1]) + i]),
                        # print(" "),
                    print("\n")
            else:
                break
            c = raw_input("Letter to guess: ")
            while (not is_one_alpha(c)) or (c in guesses):
                if not is_one_alpha(c):
                    print("Error! Please guess one letter.")
                if c in guesses:
                    print("Error! Letter " + c.upper()
                          + " has been guessed before, "
                          + "please guess another letter.")
                c = raw_input("Letter to guess: ")
            guesses.append(c)
            client.send(chr(1) + c.lower())
        print("Closed Connection")
        client.shutdown(1)
        client.close()
    except getopt.error, msg:
        print(msg)
        print("for help use ")


if __name__ == "__main__":
    main()