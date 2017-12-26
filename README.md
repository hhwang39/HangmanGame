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
Words used<br />
length 3 words<br />
"are",<br />
"Fax",<br />
length 4 words<br />
"Jinx",<br />
"Quad",<br />
"Waxy",<br />
"Chip",<br />
"Buff",<br />
length 5 words<br />
"Zippy",<br />
"Today",<br />
"Toady",<br />
length 6 words<br />
"Oxygen",<br />
"Sphinx",<br />
"Zombie",<br />
length 7 words<br />
"chatbot",<br />
"Buzzing",<br />
length 8 words<br />
See server.txt to see server output<br />
This is the output of<br />
Client1 connects (say y)<br />
Client2 connects (say y)<br />
Client3 connects (say n)<br />
Closed connection<br />
Client3 connects (say y)<br />
Client4 connects (say y)<br />
Rejected Closed Connection<br />
Client3 finished the game<br />
Client1 finished the game<br />
Client4 now connects (say y)<br />
Client4 finished the game<br />
Client2 finished the game<br />
See client1.txt to see client1 output<br />
Normal game flow with win<br />
See client2.txt to see client2 output<br />
Normal game flow with some illegal argument input and lose<br />
See client3.txt to see client3 output<br />
Normal game flow with some illegal argument and win<br />
See client4.txt to see client4 output<br />
Normal game flow with some illegal argument and win<br />
