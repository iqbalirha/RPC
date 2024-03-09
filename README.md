# RPC
A distributed system using Remote Procedure Calls (RPC) will be created. On Java, RPC is handled commonly through Java remote method invocation (RMI). For web applications, Representational state transfer (REST) is the most commonly linked term. In essence, RPC allows for a client to make a request for the server to run some functionalities based on given requirements. In this task, an RPC client-server system is created. It's first made to function between N clients and a single server.
Basic Requirements
The client should be able to:

Ask the user for input & send it to server
        Topic, Text, and timestamp for the note
        If the topic exists on the XML, the data will be appended to the structure
        If not, a new XML entry will be made
Get the contents of the XML database based on given topic
The server should be able to:

Process the client's input
Save data on a local database mock (XML)
Handle multiple client requests at once
Attached on the assignment page is an XML file, that shows how the XML database mock could be structured.

Additional requirements 
One of the key challenges in distributed systems is the interoperability of different platforms. For full marks on this assignment, the server should communicate with other sources of data for information. Add a functionality, that will query the Wikipedia API for more information of the given topic. For this tasks, an additional library can be used for queries, such as 'requests' on python or 'fetch' on Javascript.

The client should be able to:

Name search terms to lookup data on wikipedia
Append the data to an existing topic
The server should be able to:

Query wikipedia for user submitted articles
Add relevant information to user submitted topic
        At minimum, the server should give a link to a wikipedia article found
How usable the Wikipedia results are is not a priority, the main idea is to communicate through the API. Opensearch protocol, which is available in the link below, is good enough for this assignment.
