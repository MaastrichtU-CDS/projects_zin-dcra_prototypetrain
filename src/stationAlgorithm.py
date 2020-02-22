import json, logging
import os
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON

def get_sparql_dataframe(service, query):
    """
    Helper function to convert SPARQL results into a Pandas data frame.
    """
    sparql = SPARQLWrapper(service)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    result = sparql.query()

    processed_results = json.load(result.response)
    cols = processed_results['head']['vars']

    out = []
    for row in processed_results['results']['bindings']:
        item = []
        for c in cols:
            item.append(row.get(c, {}).get('value'))
        out.append(item)

    return pd.DataFrame(out, columns=cols)

def stationAlgorithm(inputStr):
    outputStr = ''
    logging.info('starting new calculation')
    # --------------------------- PASTE YOUR ALGORITHM HERE -------------------------------
    # define the "outputStr" variable
    # perform station algorithm

    logging.info("Endpoint URL: " + os.environ.get("sparql_url"))

    query = """PREFIX db: <http://localhost/rdf/ontology/>
            select (COUNT(?s) AS ?myCount) where { 
                ?s ?p db:Tumour_Treatment.
            }
        """
    df = get_sparql_dataframe(os.environ.get("sparql_url"), query)

    outputStr = json.dumps(df.describe().to_json())

    logging.info('done with calculation')

    return outputStr