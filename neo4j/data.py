import os
import py2neo

def Neo4Article():
    # Connect to graph and add constraints.
    neo4jUrl = os.environ.get('NEO4J_URL',"http://localhost:17474/db/data/")
    graph = neo4j.GraphDatabaseService(neo4jUrl)
    tx = graph.cypher.begin()
    
    #ParseJSON DATA
    tx = graph.cypher.begin()
    for name in ["Alice", "Bob", "Carol"]:
        tx.append("CREATE (person:Person {name:{name}}) RETURN person", name=name)
        alice, bob, carol = [result.one for result in tx.commit()]

    friends = Path(alice, "KNOWS", bob, "KNOWS", carol)
    graph.create(friends)
        
    return 0;



def Articles():
    articles = [
        
        {
            'id':1,
            'title': 'Article One',
            'body': 'Lorem ipsum',
            'author':'Kahina Ferroukhi',
            'create_date':'12-02-2016'
            
        },
        
         {
            'id':2,
            'title': 'Article Two',
            'body': 'Lorem ipsum',
            'author':'Kahina Ferroukhi',
            'create_date':'22-02-2017'
            
        },
         {
            'id':3,
            'title': 'Article Three',
            'body': 'Lorem ipsum',
            'author':'Kahina Ferroukhi',
            'create_date':'23-02-2018'
            
        }
    ]
    return articles