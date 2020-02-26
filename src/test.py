import stationAlgorithm
import pandas as pd

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

df = stationAlgorithm.get_sparql_dataframe(location, query)

print(df.describe(exclude=['category']))
print(stationAlgorithm.describe_category(df))