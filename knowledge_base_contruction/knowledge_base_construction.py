import rdflib

g = rdflib.Graph()

g.parse("vocabulary/schema.ttl", format="turtle")

for s,p,o in g:
    # Print the subject, predicate and the object
    print (s,p,o)
