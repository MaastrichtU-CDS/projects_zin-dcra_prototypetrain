import json, logging
import os
from SPARQLWrapper import SPARQLWrapper, JSON

def stationAlgorithm(inputStr):
    outputStr = ''
    logging.info('starting new calculation')
    # --------------------------- PASTE YOUR ALGORITHM HERE -------------------------------
    # define the "outputStr" variable
    # perform station algorithm

    logging.info("Endpoint URL: " + os.environ.get("sparql_url"))

    sparql = SPARQLWrapper(os.environ.get("sparql_url"))
    sparql.setQuery("""PREFIX db: <http://localhost/rdf/ontology/>
            select (COUNT(?s) AS ?myCount) where { 
                ?s ?p db:Tumour_Treatment.
            }
        """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    outputStr = json.dumps(results)

    logging.info('done with calculation')

    return outputStr