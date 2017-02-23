#Configuring Linux Web Servers

- Everytime you visit web application, browser is requesting a number of files that are sitting on a server somewhere out there on the Internet

- These servers are most likely running Linux. 

##What is Linux

- By far the most popular operating system (Ex. Like Windows or OSx) on web servers today.

- Free as in speech, literally hundreds of versions or distributions of Linux available

##Intro to Distributions

- People get free choice to what's included in their distribution of Linux. 

Ex. Ubuntu has various versions, some made for desktop, mobile, and servers.

##Linux Distribution Comparision

**Redhat** - Large enterprise / corporate customers

**Ubuntu** - Ease of use on servers, desktops, laptops

**Linux Mint** - Desktop users with proprietary media support

**Core OS** - Clustered, containerized deployment of apps

##Important Directories

**etc** - Configuration files live

**var** - Variable files: simply files that grow / change in size ex. system and application logs

**bin** - Executable binaries: applications that you would run (Ex. LS command is in it)

#Linux Security

- Putting out a computer accessible by anyone on the internet means we need security.

- If someone malicious gets access to this computer they can perform acts such as sending spam, launch DDOS attacks, and much more.

##Rule of Least Privilege

- A user or application only has enough permission to its job - nothing extra.

##Super User

- User named Root, can do anything they want on machine.

**sudo vs. su**

- Typicall regarded that you should not use su command. Do you need to change entire working context to su just to make commands? It might lead you you to perform harmful operations without prompt.

##Package Source Lists

- All of available package sources are listed in /etc/app/sources.list

##Connecting as a New User

- SSH is what we use to remotely connect to the server
- Example: ssh student@127.0.0.1 -p 2222
- student is the user we are logging in with
- 127.0.0.1 is the standard IP address or local host (same computer as I am on)
- **-p 2222** shows to connect to port 2222

#Public Key Encryption

- Server will send random message to the client and they will encrypt that message with their private key and then send that encrypted message back to the server.

- The server will decrypt this message with their public key and if that vlue equals the same value they sent, then everything checks out and the client has authenticated

##Generating Key Pairs

- You can generate a RSA key (there are other types) with ssh keygen
WARNING: Don't generate it on your server or then it's not private

Then you must put the public key on the server 
