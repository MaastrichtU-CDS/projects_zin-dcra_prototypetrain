import stationAlgorithm as sa
import pandas as pd
import json

location = "http://sparql.cancerdata.org/namespace/pbdw_site_1"
query = """prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix xsd: <http://www.w3.org/2001/XMLSchema#>
prefix ncit: <http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#>
prefix roo: <http://www.cancerdata.org/roo/>

SELECT ?age ?gender ?survival
WHERE {
	?s rdf:type ncit:C16960.
  	?s roo:P100000 [
      roo:P100042 ?age;
    ];
       roo:P100018 [
      rdf:type ?gender;
    ].
    FILTER (?gender IN (ncit:C20197, ncit:C16576)).
    ?s roo:P100311 [
        rdf:type ?survival;
    ].
    FILTER (?survival IN (roo:C000000, roo:C000001)).
}"""
query = """PREFIX db: <http://localhost/rdf/ontology/>
    PREFIX dbo: <http://um-cds/ontologies/databaseontology/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT (IRI(concat("http://term.local/", ?genderString)) AS ?gender)
    WHERE {
        ?tt ?p db:Tumour_Treatment.
        ?tt dbo:has_column [
            rdf:type db:Tumour_Treatment.Geslacht;
            dbo:has_value ?genderString;
        ].
    }"""
location = "http://as-fair-01.ad.maastro.nl:7200/repositories/sage"

df = sa.get_sparql_dataframe(location, query)

numericalStats = { }
try:
  numericalStats = df.describe(exclude=['category']).to_json()
except:
  print("No numerical data available?")

outData = {
    "numericalStats": numericalStats,
    "categoricalStats": sa.describe_category(df).to_json()
}

outputStr = json.dumps(outData)

print(outputStr)