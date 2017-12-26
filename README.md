# Multiplayer Hangman Game
## 1. Overview
This python code will use python default socket library to create multi-player hangman game. Main thread will wait and accept new connection from clients and count how many clients have been connected. If new client that tries to connect to server is 4th one, it will terminate the connection to that client. 
This resembles normal hangman game. When connected to a client, the server chooses random word from the list and the client will ask a user to guess a letter and the letter is sent to the server. Server will respond with word and incorrect guesses.
This uses python 2.7 default socket, random so there should not be libraries that need to be installed other than python 2.7 itself
## 2. Run Server/Client
In order to run server,
python server.py [port] [txtfile(optional)]
port 80 might require sudo permission.
you can also 
python server.py --help to see command you have to type.
In order to run client,
python client.py [ip] [port]
## 3. Test Result
Words used
length 3 words
"are",
"Fax",
length 4 words
"Jinx",
"Quad",
"Waxy",
"Chip",
"Buff",
length 5 words
"Zippy",
"Today",
"Toady",
length 6 words
"Oxygen",
"Sphinx",
"Zombie",
length 7 words
"chatbot",
"Buzzing",
length 8 words
See server.txt to see server output
This is the output of 
Client1 connects (say y)
Client2 connects (say y)
Client3 connects (say n)
Closed connection
Client3 connects (say y)
Client4 connects (say y)
Rejected Closed Connection
Client3 finished the game
Client1 finished the game
Client4 now connects (say y)
Client4 finished the game
Client2 finished the game
See client1.txt to see client1 output
Normal game flow with win
See client2.txt to see client2 output
Normal game flow with some illegal argument input and lose
See client3.txt to see client3 output
Normal game flow with some illegal argument and win
See client4.txt to see client4 output
Normal game flow with some illegal argument and win
