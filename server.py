"""
You have to run "python server.py [port] or python server.py [port] [txtfile]"
You can also type python server.py --help to see help
"""
# imports
import socket
import sys
import getopt
from threading import Thread
from threading import Lock
import random


"""
code excerpted from 
https://stackoverflow.com/questions/11122291/python-find-char-in-string-can-i-get-all-indexes
find all the indexes of character and return as list
"""
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

# Hangman class that will randomly choose a word and update word with guesses
class Hangman:
    global word_dict

    def __init__(self):
        self.lives = 6
        # will get it from dictionary
        self.origiWord = word_dict[random.randint(0, len(word_dict) - 1)]
        self.selectedWord = self.origiWord.lower()
        self.guessedChars = []
        self.guessedWord = []
        for l in range(0, len(self.selectedWord)):
            self.guessedWord.append("_")
    """
    return 'o' if game is still ongoing, 'w' if player won, 'l' if player loses 
    """
    def guess(self, c):
        idx = find(self.selectedWord, c.lower())
        # print(idx)
        if len(idx) != 0:
            for i in idx:
                # print(i)
                self.guessedWord[i] = self.origiWord[i]
                if "".join(self.guessedWord) == self.origiWord:
                    return 'w'
            return 'o'
        else:
            if self.lives > 0:
                self.guessedChars.append(c)
                self.lives = self.lives - 1
            if self.lives == 0:
                return 'l'

    def get_guessed_word(self):
        return "".join(self.guessedWord)

    def get_guessed_chars(self):
        return "".join(self.guessedChars)

    def get_lives(self):
        return self.lives

"""
Client Thread that will handle each client requested, takes upto 3 clients
"""
class ClientThread(Thread):
    def __init__(self, conn, ip, port):
        print("Get connected from " + str(ip)
              + ":" + str(port))
        global num_connected_client
        # more than 3 created
        with num_lock:
            if num_connected_client >= 3:
                msg = "server-overloaded"
                conn.send(chr(len(msg)) + msg)
                conn.shutdown(1)
                conn.close()
                print("End the connection from " + str(ip)
                      + ":" + str(port))
                self.__inited = False
                return
        self.__inited = True
        self.conn = conn
        self.ip = ip
        self.port = port

        buf = self.conn.recv(1024)
        if (len(buf) != 1) or (ord(buf[0]) != 0):
            print("End the connection from " + str(self.ip)
                  + ":" + str(self.port))
            self.conn.shutdown(1)
            self.conn.close()
            self.__inited = False
        else:

            Thread.__init__(self)

    def run(self):
        global num_connected_client
        hangman = Hangman()
        isDone = False
        final_status = "o"
        self.conn.send(self.format_packet_normal(hangman))
        while not isDone:
            # length 1 and one character
            buf = self.conn.recv(2)
            if len(buf) == 0:
                break
            # print(buf)
            c = buf[1]
            status = hangman.guess(c)
            isDone = status == "l" or status == "w"
            if isDone:
                final_status = status
            else:
                self.conn.send(self.format_packet_normal(hangman))
        if isDone:
            self.conn.send(self.format_packet_string(final_status))
        with num_lock:
            num_connected_client = num_connected_client - 1
        print("End the connection from " + str(self.ip)
              + ":" + str(self.port))
        self.conn.shutdown(1)
        self.conn.close()
    """
       return if class is initated or not 
    """
    def is_inited(self):
        return self.__inited

    def format_packet_string(self, final_status):
        if final_status == "w":
            msg = "You Win!"
            return chr(len(msg)) + msg
        else:
            msg = "You Lose:("
            return chr(len(msg)) + msg

    def format_packet_normal(self, hangman):
        return chr(0) + chr(len(hangman.guessedWord)) \
               + chr(6 - hangman.get_lives()) + hangman.get_guessed_word() \
               + hangman.get_guessed_chars()


num_connected_client = 0
num_lock = Lock()
# default word dictionary
word_dict = [
    # length 3 words
    "are",
    "Fax",
    # length 4 words
    "Jinx",
    "Quad",
    "Waxy",
    "Chip",
    "Buff",
    # length 5 words
    "Zippy",
    "Today",
    "Toady",
    # length 6 words
    "Oxygen",
    "Sphinx",
    "Zombie",
    # length 7 words
    "chatbot",
    "Buzzing",
    # length 8 words

]


# create a dictonary if user wants to input his/her own dictionary
def create_dict(fname):
    word_list = []
    fh = open(fname, "r")
    # read first line
    fh.readline()
    for line in fh:
        # remove carriage return and new line
        word_list.append(line.rstrip("\r\n"))
    global word_dict
    word_dict = word_list
    fh.close()


# main function
def main():
    global num_connected_client
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
        # print(args)
        if len(args) > 3 or len(args) == 0:
            print(__doc__)
            sys.exit(0)
        if len(args) == 2:
            # print("length 2")
            # print(args[1])
            create_dict(args[1])
        # print(opts)
        for o, a in opts:
            if o in ("-h", "--help"):
                print(__doc__)
                sys.exit(0)

                # socket creatiton
        port = int(args[0])

        threshold_player = 3
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr = ("0.0.0.0", port)
        sock.bind(server_addr)
        sock.listen(threshold_player)
        threads = []
        while True:
            (client_socket, (client_ip, client_port)) = sock.accept()
            # create new client to serve client -> check number and send message
            client = ClientThread(client_socket, client_ip,
                                  client_port)
            if client.is_inited():
                client.start()
                threads.append(client)
                with num_lock:
                    num_connected_client = num_connected_client + 1

        # for t in threads:
        #     t.join()
    except getopt.error, msg:
        # print(msg)
        print("for help use ")


if __name__ == "__main__":
    main()
