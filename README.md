# Chat-PGP-P2P
The goal of this project is to create a P2P chat application secure.
It will use the PGP concept to secure its communications.

## Local architecture
The application can be defined on two processes :
  - a core process that manage all interactions with other contacts;
  - an GUI process that display and receive order from the user.
  
![alt tag](https://docs.google.com/drawings/d/1QxrPv2GBXfWVg0UZ9v2EOpYFAVSnTN4NwQdItwjrMog/pub?w=1151&h=592)

### The core process
The core process is a background process working like a server.

When this process is launch, it open a UDP listener to add new contacts and a TCP listener to allow discussion requests. 
It will also open other TCP listeners for each new discussion created.

It will listen each listener to get new contacts and new messages.
It will also check the GUI process for new message to send and for new discussion to create.
Only non-block sockets is used to allow the core process to listen two or more listeners. 

It memorize each opened TCP connections, each generated/shared key and each messages send and received from/to other contacts.
That make a good separation between the GUI interface and the working process.

### The GUI process
The GUI process has an interface to communicate with the core process.
A web interface, a command application, or a GUI application could be used independantly to the core process.

## Protocol
Each application have several couples of public/private keys :
 - one in general to begin a discussion and to authentificate every messages from this contact;
 - one for each discussion to separe each of them.

The client and server have many roles.

### Who's there (UDP mode)
First of them is to find contacts arround.
For that, there are two ways:
 - the core process send an UDP broadcast request to be seen by other contacts and wait for responses;
 - when the core process receive an UDP request from other contacts.
 
![alt tag](https://docs.google.com/drawings/d/1Ztd4E9MDaGBN20A3rO09nqmKqa9q4oCFvaX7XVc6CbI/pub?w=670&h=366)
 
For this recognition task, the general couple of keys will be used to authentificate each contact when discussion request is made.
The UDP broadcast message contains the owner public key and the UDP response message contains the distant contact public key.
Neither of theses messages are crypted.

This step only help the application to be seen by others and is done regulary.

### Let's talk together (TCP mode)
After some UDP messages exchanged, a list of contact should be available and the user can send a request to open a discussion.


Then when an user wants to open a conversation to another, it create an TCP tunnel to communicate.

At this time, a couple of public/private key specific to this connection is created and the client send an request of conversation including this public key.

The distant user has the choice to keep the connection or to refuse it. If it accept the conversation, it send its public key created for this connection. In the other case, it will just send an error message.

### What's up
The conversation established, both users can send signed and crypted messages by using its private key and the distant user's public key.

Sending a message is made like this:
```
  clear message -> signe using private key -> crypt using public key -> send the crypted message
```

On receive a message, the server can easly decrypt the message like this:
```
  crypted message -> decrypt using private key -> authentificate using public key -> prompt the clear message
```


### Who's there (UDP mode)
First of them is to upload a list of contacts arround him.

It's just like upload a file: the client send a request to another user then the distant server send a list of its contacts including itself.

Two servers can have differents contacts lists. That's why the client will group all these contacts in a single contacts list.

