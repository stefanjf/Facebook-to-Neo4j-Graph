import facebook
from py2neo import neo4j
import requests
import json

graph_db = neo4j.GraphDatabaseService() #Connects to running Neo4j server on default port

def executeCypherQuery(query): #function for executing queries on Neo4j
    result = neo4j.CypherQuery(graph_db, query).execute()

#First, delete all nodes and relationships in Neo4j if they exist
#executeCypherQuery("start r=relationship(*) delete r")
#executeCypherQuery("MATCH n DELETE n")

TOKEN = ""

url = 'https://graph.facebook.com/me/friends/'
parameters = {'access_token': TOKEN}
r = requests.get(url, params = parameters)
friendList = json.loads(r.text)
print friendList
#Two lists for keeping track of what relationships have been added
personListA = []
personListB = []


for friend in friendList['data']:
    print friend
    executeCypherQuery("CREATE (n:Person {name:\"" + friend["name"] + "\", id:\"" + friend["id"] + "\"})")
    url = 'https://graph.facebook.com/me/mutualfriends/%d/' % int(friend['id'])
    parameters = {'access_token': TOKEN}
    r = requests.get(url, params = parameters)
    mutualFriendList = json.loads(r.text)
    for mutualFriend in mutualFriendList["data"]:
        if friend["id"] in personListB and mutualfriend["id"] in personListA: #If a relationship has already been added, this will be true
            print "This relationship has already been added, do nothing."
        else:
            print "Added relationship between " + friend["id"] + " and " + mutualfriend["id"]
            executeCypherQuery("MATCH (a:Person), (b:Person) WHERE a.id = \"" + friend["id"] + "\" AND b.id = \"" + mutualfriend["id"] + "\"  CREATE (a)-[r:FRIEND]->(b)")
            personListA.append(friend["id"]) #Add the two people to the lists, to prevent adding the rel again
            personListB.append(mutualfriend["id"])






