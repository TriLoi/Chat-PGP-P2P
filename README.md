# Chat-PGP-P2P
The goal of this project is to create a P2P chat application secure.
It will use the PGP concept to secure its communications.

## Protocol
The client and server have many roles.

First of them is to upload a list of contacts arround him.
It's just like upload a file: the client send a request to another user then the distant server send a list of its contacts including itself.
Two servers can have differents contacts lists. That's why the client will group all these contacts in a single contacts list.
At this moment, a list of contact is available and the user can send a request to open a conversation.
This step is done regulary by using UDP packets.

Then when an user wants to open a conversation to another, it create an TCP tunnel to communicate.
At this time, a couple of public/private key specific to this connection is created and the client send an request of conversation including this public key. The distant user has the choice to keep the connection or to refuse it. If it accept the conversation, it send its public key created for this connection. In the other case, it will just send an error message.

The conversation established, both users can send signed and crypted messages by using its private key and the distant user's public key.
Sending a message is made like this:
  clear message -> signe using private key -> crypt using public key -> send the crypted message
On receive a message, the server can easly decrypt the message like this:
  crypted message -> decrypt using private key -> authentificate using public key -> prompt the clear message
