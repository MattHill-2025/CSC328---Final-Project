CSC328 Final Project Chat Server
Authors:
    Matthew Hill
    R-E Miller
    Elliot Swan
Major:
    Computer Science/Information Technology
Creation Date:
    November 23, 2023
Due Date:
    December 14, 2023
Course:
    CSC328
Professor Name: 
    Dr. Dylan Schwesinger
Assignment:
    Final
FileNames:
    server.py
    client.py
    shared.py
    makefile
Purpose:
    The purpose of this assignment was to create a chat server that accepts multiple clients 
    and they are able to converse with one another. They must all have unique nicknames
    and the server must send their messages to everyone connected. The server also logs and stores
    all of the information that is recieved as well as when they logged in and their ip.

How to build and run the program
    To start, get the server running. This can be acheived by doing make server. This will create server on 
    the localhost and will allow connections. The next step is to then run make client which will execute the client program and connect
    to the server. Multiple connections can be made to the server (Maximum of 10). From there the connected clients must choose a unique nickname and then
    they are able to chat with one another. To leave the server simply hit command c. To shutdown the server also hit command c, but it has a 5 second wait time as it
    informs the connected clients that the server is shutting down.

Purpose of the files
    The shared.py file is the shared library used to send and recieve messages that both the client and server use.
    server.py is the code to create the server and handles multiple client connections as well as broadcasting messages.
    cleint.py is the code to create the client that is able to connect to the server and handles information from the server to the client.
    makefile is the script to create a server and client easily and is prebound to localhost for both as well as using socket 12345.

Responsibility matrix

Tasks involved
Our project involves a plan in which a specific task i assigned to each team member. We have
divided the project into key areas - Server, Client, and Library code portions, with each area
having its own set of tasks and sub-tasks.
    ● Server Tasks (Matthew Hill):
        ● Creating the Server: This involves setting up the server infrastructure, ensuring it
          can handle multiple client connections. Estimated time: [X hours/days].
        ● Name Verification: Implementing functionality to verify and manage unique
        client nicknames. Estimated time: [3 hours].
        ● Handling Multiple Connections: Ensuring the server can efficiently manage
        simultaneous client connections. Estimated time: [12 hours].
        ● Graceful Shutdown: Developing a mechanism for the server to shut down
        gracefully, including sending notifications to all connected clients. Estimated
        time: [1/2 an hour].
    ● Client Tasks (R-E Miller):
        ● Connecting to Server: Establishing a reliable connection to the server. Estimated
        time: [A hours/days].
        ● Nickname Decision: Enabling clients to choose and confirm a unique nickname.
        Estimated time: [B hours/days].
        ● Message Sending and Receiving: Facilitating the sending and receiving of
        messages through the client interface. Estimated time: [C hours/days].
        ● Disconnecting: Implementing a smooth and user-friendly disconnection process.
        Estimated time: [D hours/days].
    ● Library Code/Curses Integration (Elliot Swan):
        ● Encoding/Decoding JSON Packets: Developing methods to encode and decode
        messages in JSON format for efficient communication. Estimated time: [E
        hours/days].
        ● Sending/Receiving JSON Packets: Establishing protocols for message
        transmission and reception. Estimated time: [F hours/days].
        ● UI Research and Design in Curses: Designing and implementing the user
        interface using the curses library, ensuring a seamless user experience. Estimated
        time: [G hours/days]


Protocol – the details of your developed protocol, including the initial protocol defined above, and how the protocol for socket reads/writes

Assumptions – clearly list and describe any assumptions made about running the application or how the application works

Discussion on your development process, including any decisions and/or major problems you encountered and your solution for each

Status – current status of applications in terms of specifications, and any known issues with the application