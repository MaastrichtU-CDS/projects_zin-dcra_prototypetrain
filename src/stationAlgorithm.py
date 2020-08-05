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

    df = pd.DataFrame(out, columns=cols)

    if len(processed_results['results']['bindings']) > 0:
        firstRow = processed_results['results']['bindings'][0]
        for c in cols:
            varType = firstRow.get(c,{}).get("type")
            if varType == "uri":
                df[c] = df[c].astype("category")
            if varType == "literal" or varType == "typed-literal":
                dataType = firstRow.get(c,{}).get("datatype")
                targetType = "category"
                
                if dataType=="http://www.w3.org/2001/XMLSchema#int":
                    targetType = "int"
                if dataType=="http://www.w3.org/2001/XMLSchema#integer":
                    targetType = "int"
                if dataType=="http://www.w3.org/2001/XMLSchema#double":
                    targetType = "float"
                if dataType=="http://www.w3.org/2001/XMLSchema#string":
                    targetType = "category"
                
                df[c] = df[c].astype(targetType)
    
    return df

def describe_category(df):
    outSeries = pd.DataFrame()
    for column in df.columns:
        if str(df[column].dtype) == "category":
            counts = df[column].value_counts()
            rowNames = counts.index.values
            counts = counts.to_frame(name="count")
            counts["category"] = rowNames
            counts["variable"] = column
            counts = counts.reset_index(drop=True)
            outSeries = outSeries.append(counts)
    return outSeries

def stationAlgorithm(inputStr):
    outputStr = ''
    logging.info('starting new calculation')
    # --------------------------- PASTE YOUR ALGORITHM HERE -------------------------------
    # define the "outputStr" variable
    # perform station algorithm

    logging.info("Endpoint URL: " + os.environ.get("sparql_url"))

    inputStruct = json.loads(inputStr)
    query = inputStruct["query"]
    df = get_sparql_dataframe(os.environ.get("sparql_url"), query)

    numericalStats = { }
    try:
        numericalStats = json.loads(df.describe().to_json())
    except:
        print("No numerical data available?")

    outData = {
        "numericalStats": numericalStats,
        "categoricalStats": json.loads(describe_category(df).to_json(orient='records'))
    }
    outputStr = json.dumps(outData)

    logging.info('done with calculation')

    return outputStr
