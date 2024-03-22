# COMP6741 (IS) - ROBOPROF


## Files and Folders-

### AI_material (Folder)

Contains course material for Applied Artificial Intelligence such as Labs, Lectures and reading material. References used in schema.ttl file and vocabulary.ttl.

### COMP6741 (Folder)

Contains course material for Intelligent Systems such as Labs and Lectures. References used in schema.ttl file and vocabulary.ttl.

### triple_converter.py (File)

Contains python code for converting CU_SR_OPEN_DATA_CATALOG.csv file to triple format.
```
To run: Go to csv_to_triple_converter folder and run triple_converter.py
```
### knowledge_base_construction.py (File)

Contains python code for knowledge base construction which parses the schema.ttl file and prints the graph.
```
To run: Go to the knowledge_base_construction folder and run 
    python3 knowledge_base_construction.py
```
<b>Note:</b> Please install rdflib prior to running the code.
### Query (Folder)

Contains 13 SPARQL query syntax for traversing over the vocabulary.ttl file and the output for those queries.

### Vocabulary (Folder)

Consist of the following 3 files-
1) schema.nt: Constructed knowledge base in N-Triples.
2) schema.ttl: Knowledge base in turtle format.
3) vocabulary.ttl: Knowledge base along with data, which can be fed to fuseki server for querying.


