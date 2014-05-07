Facebook to Neo4j Graph
============

Python script to get Facebook friends and output them to a Neo4j graph. Neo4j is
a highly scalable, robust graph database.


##Install Dependencies

```python
pip install facebook-sdk
pip install py2neo
pip install requests json
```

##Facebook User Token
A user access token is required in order to get friends and mutual friends from the
Facebook Graph API.

One option is to create a dummy app at [developer.facebook.com](developer.facebook.com)
to generate a token. Once the app is created, go to Tools -> Access Tokens to
retrieve the user token.

##Start Neo4j Server
Head to [neo4j.org](www.neo4j.org) to download and install neo4j on your system.

##Execute python script

###1. Add Facebook Token
```python
TOKEN = 'INSERT FACEBOOK TOKEN HERE'
```

###2. Configure Neo4j Server IP
If the neo4j server is running on localhost, no action is needed.
If the server is running on a different computer, insert the relevant IP address.
```python
#Remote Neo4j Server:
graph_db = neo4j.GraphDatabaseService('<Server Address>')

#Localhost:
graph_db = neo4j.GraphDatabaseService()
```
###3. Run facebookToNeo4j.py
```
python facebookToNeo4j.py
```

###4. View Graph Database
In a browser, go to http://localhost:7474 to view your Facebook graph.


Note: If the graph nodes display the Facebook id instead of the
friend's name, you can click on any node and in the pop-up choose "Style" ->
"caption" -> "name" to switch.
