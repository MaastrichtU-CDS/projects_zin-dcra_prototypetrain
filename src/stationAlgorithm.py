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
                if dataType=="http://www.w3.org/2001/XMLSchema#int":
                    df[c] = pd.to_numeric(df[c], errors='coerce')
                if dataType=="http://www.w3.org/2001/XMLSchema#integer":
                    df[c] = pd.to_numeric(df[c], errors='coerce')
                if dataType=="http://www.w3.org/2001/XMLSchema#double":
                    df[c] = pd.to_numeric(df[c], errors='coerce')
                if dataType=="http://www.w3.org/2001/XMLSchema#string":
                    df[c] = df[c].astype("category")
    
    return df

def stationAlgorithm(inputStr):

    # --------------------------- PASTE YOUR ALGORITHM HERE -------------------------------
    # define the "outputStr" variable
    # perform station algorithm

    logging.info("Endpoint URL: " + os.environ.get("sparql_url"))

    inputStruct = json.loads(inputStr)
    query = inputStruct["query"]

    data = get_sparql_dataframe(os.environ.get("sparql_url"), query)
  
    outputStr = ''
    logging.info('starting new calculation')
    
    ###### Indicator 2b #########

    try:
        data['diagnosedatum'] =  pd.to_datetime(data['diagnosedatum'], format='%m/%d/%Y')
        data['datum_van_chirurgische_therapie']=pd.to_datetime(data['datum_van_chirurgische_therapie'], format='%m/%d/%Y',errors='coerce')
        data['datum_van_neoadjuvante_therapie']=pd.to_datetime(data['datum_van_neoadjuvante_therapie'], format='%m/%d/%Y',errors='coerce')
        colon_values = ['Colon ascendens','Colon Ascendens','Colon sigmoideum','Colon Sigmoideum','Colon transversum', 'Colon Transversum','overgang rectum/sigmoid']
        fdata = data.loc[data['lokalisatie'].isin(colon_values)]
    except:
        data['diagnosedatum'] =  pd.to_datetime(data['diagnosedatum'], format='%Y-%m-%d', errors='coerce')
        data['datum_van_chirurgische_therapie']=pd.to_datetime(data['datum_van_chirurgische_therapie'], format='%Y-%m-%d',errors= 'coerce')
        data['datum_van_neoadjuvante_therapie']=pd.to_datetime(data['datum_van_neoadjuvante_therapie'], format='%Y-%m-%d',errors='coerce')
        colon_values = ['Colon ascendens','Colon Ascendens','Colon sigmoideum','Colon Sigmoideum','Colon transversum', 'Colon Transversum','overgang rectum/sigmoid']
        fdata = data.loc[data['lokalisatie'].isin(colon_values)]
    
    #days calculation
    datediff_neo = fdata.datum_van_neoadjuvante_therapie - fdata.diagnosedatum
    datediff_surg = fdata.datum_van_chirurgische_therapie - fdata.diagnosedatum
    fdata['datediff_neo']=datediff_neo
    fdata['datediff_surg']=datediff_surg

    limit = 56
    count_neo = fdata.loc[fdata['datediff_neo']<pd.to_timedelta(limit, unit='D')].shape[0]
    count_surg = fdata.loc[fdata['datediff_surg']<pd.to_timedelta(limit, unit='D')].shape[0]

    total_count_colon = count_neo + count_surg
    total_population_colon = fdata.shape[0]

    try:
        percentage_of_short_waitlist = total_count_colon/total_population_colon
    except ZeroDivisionError:
        percentage_of_short_waitlist = 0


    ################# Indicator 8 ######################
    rectum_values = ['Rectum','rectum']
    fdata2 = data.loc[data['lokalisatie'].isin(rectum_values)]
    #count_rectum = fdata2.loc[fdata2['gecompliceerd_beloop']=='Ja'].shape[0]
    count_rectum = fdata2[fdata2['gecompliceerd_beloop'].isin(["Ja","1"])].shape[0]
    total_population_rectum = fdata2.shape[0]

    try:
        complication_rate = count_rectum/total_population_rectum
    except ZeroDivisionError:
        complication_rate = 0
    

    outData = {
        'total_count_colon':total_count_colon,
        'total_population_colon':total_population_colon,
        'percentage_of_short_waitlist':percentage_of_short_waitlist,
        'count_rectum': count_rectum,
        'total_population_rectum':total_population_rectum,
        'complication_rate':complication_rate,
        }

    
    outputStr = json.dumps(outData)

    logging.info('done with calculation') 

    return outputStr
