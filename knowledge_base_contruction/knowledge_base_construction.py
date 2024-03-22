import rdflib

g = rdflib.Graph()

g.parse("vocabulary/vocabulary.ttl", format="turtle")

for s,p,o in g:
    # Print the subject, predicate and the object
    print (s,p,o)

with open("knowledge_base_contruction/n-triple.nt", "wb") as file:
    n_triple = g.serialize(format="nt")
    file.write(n_triple)