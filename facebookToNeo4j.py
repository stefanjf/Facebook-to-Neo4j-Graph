import facebook
from py2neo import neo4j

facebook_user_token = ""

graph = facebook.GraphAPI(facebook_user_token)
friends = graph.get_connections("me","friends")

graph_db = neo4j.GraphDatabaseService() #Connects to running Neo4j server on default port

def executeCypherQuery(query): #function for executing queries on Neo4j
		result = neo4j.CypherQuery(graph_db, query).execute()

#First, delete all nodes and relationships in Neo4j if they exist
executeCypherQuery("start r=relationship(*) delete r")
executeCypherQuery("MATCH n DELETE n")

#For every friend, create a node with name and id attributes
for friend in friends["data"]:
	executeCypherQuery("CREATE (n:Person {name:\"" + friend["name"] + "\", id:\"" + friend["id"] + "\"})")

#Two lists for keeping track of what relationships have been added
personListA = []
personListB = []

for friend in friends["data"]:
	for mutualfriend in friend["mutual_friends"]: #For every combination of friend and mutual friend...
			if friend["id"] in personListB and mutualfriend in personListA: #If a relationship has already been added, this will be true
						print "This relationship has already been added, do nothing."
			else:
						print "Added relationship between " + friend["id"] + " and " + mutualfriend
						executeCypherQuery("MATCH (a:Person), (b:Person) WHERE a.id = \"" + friend["id"] + "\" AND b.id = \"" + mutualfriend + "\"  CREATE (a)-[r:FRIEND]->(b)")
						personListA.append(friend["id"]) #Add the two people to the lists, to prevent adding the rel again
						personListB.append(mutualfriend)


