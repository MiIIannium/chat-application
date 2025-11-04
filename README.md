# chat-application
Simple chat application for educational purposes

## Overview
Client-Server model

## Features
Server:
1. Accept incoming connections
2. Store active clients
3. Listen for messages
4. Broadcast messages (future versions will not broadcast but send to the intended recipient)
5. Handle disconnects/errors

Client:
1. Connect to server
2. Send messages
3. Listen for incoming messages

## Tech Stack

## How to run
1. Start server with command: python server.py
2. Start client with command: python client.py
    2.1. Choose a port to use, or just press enter for the client to find a valid port themselves
    2.2. Type anything, and press enter to send a message
    2.3. Repeat step 2 (Start client) as many times as you want to add more clients to send messages to
    2.4. Use "CTRL-C" to shut down the client
