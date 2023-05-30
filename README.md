# GroupChat-using-sockets
Group Chat Application with Python and Sockets.

This GitHub repository contains the code for a group chat application implemented in Python using socket programming. The repository includes both the client and server components necessary to establish connections and facilitate communication between multiple users in a chat room.

Features:

Client-Side Code: The repository provides the necessary Python code for the client application, enabling users to connect to the chat server and participate in group conversations.
Server-Side Code: The repository includes the server implementation, which manages client connections, receives and relays messages, and maintains the integrity of the chat room.
Socket Programming: The application utilizes socket programming to establish communication channels between the clients and the server. Sockets enable the exchange of messages over the network using TCP/IP protocols.
Group Chat Functionality: Users can join a chat room and send messages that will be visible to all other participants in real-time. The server relays the messages to all connected clients, facilitating group communication.
TCP Connectivity with ngrok: The repository also incorporates the ability to access the chat application from outside the local network by leveraging ngrok. By utilizing ngrok, which creates secure tunnels to localhost, the application can be accessed via TCP connections over the internet.
How to Use:

Clone the Repository: Start by cloning this repository to your local machine using the Git command git clone <repository_url>.
Set Up the Server: Navigate to the server directory and execute the server Python script to start the chat server.
Run the Client: Open a separate terminal or command prompt window and go to the client directory. Execute the client Python script to connect to the server.
Join the Chat: Once connected, the client can start sending messages to the chat room. All connected clients will receive these messages.
Accessing the Chat via ngrok: To enable external access, sign up for ngrok and configure it to forward TCP traffic to the server's IP address and port.
Dependencies:
The repository has the following dependencies:

Python 3.x: Ensure that you have Python 3.x installed on your machine.
ngrok: Install and configure ngrok to enable external TCP connectivity.
Contributing:
Contributions to this repository are welcome. If you find any issues or have improvements to suggest, feel free to submit a pull request.
