from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper(
    'http://localhost:3030/ds/query'
    
    )

#Pizzas
def get_response_pizzas():
    sparql.setQuery('''
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX saidi: <http://www.semanticweb.org/japor/ontologies/2021/5/PizzasLojanitas#>
        SELECT DISTINCT ?name 
        WHERE { 
            ?s rdfs:subClassOf saidi:NamePizza .
            ?s rdfs:label ?name
            FILTER (lang(?name) = 'es')
        }

    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    return qres

#CarnesTopping
def get_response_carnes():
    sparql.setQuery('''
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX saidi: <http://www.semanticweb.org/japor/ontologies/2021/5/PizzasLojanitas#>
        SELECT DISTINCT ?name 
        WHERE { 
            ?s rdfs:subClassOf saidi:CarnesTopping .
            ?s rdfs:label ?name
            FILTER (lang(?name) = 'es')
        }

    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    return qres

#EmbutidosTopping
def get_response_embutidos():
    sparql.setQuery('''
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX saidi: <http://www.semanticweb.org/japor/ontologies/2021/5/PizzasLojanitas#>
        SELECT DISTINCT ?name 
        WHERE { 
            ?s rdfs:subClassOf saidi:EmbutidosTopping .
            ?s rdfs:label ?name
            FILTER (lang(?name) = 'es')
        }

    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    return qres

#EspeciasTopping
def get_response_especias():
    sparql.setQuery('''
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX saidi: <http://www.semanticweb.org/japor/ontologies/2021/5/PizzasLojanitas#>
        SELECT DISTINCT ?name 
        WHERE { 
            ?s rdfs:subClassOf saidi:EspeciasTopping .
            ?s rdfs:label ?name
            FILTER (lang(?name) = 'es')
        }

    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    return qres


#FrutasTopping
def get_response_frutas():
    sparql.setQuery('''
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX saidi: <http://www.semanticweb.org/japor/ontologies/2021/5/PizzasLojanitas#>
        SELECT DISTINCT ?name 
        WHERE { 
            ?s rdfs:subClassOf saidi:FrutasTopping .
            ?s rdfs:label ?name
            FILTER (lang(?name) = 'es')
        }

    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    return qres

#QuesosTopping
def get_response_quesos():
    sparql.setQuery('''
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX saidi: <http://www.semanticweb.org/japor/ontologies/2021/5/PizzasLojanitas#>
        SELECT DISTINCT ?name 
        WHERE { 
            ?s rdfs:subClassOf saidi:QuesosTopping .
            ?s rdfs:label ?name
            FILTER (lang(?name) = 'es')
        }

    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    return qres

#SalsasTopping
def get_response_salsas():
    sparql.setQuery('''
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX saidi: <http://www.semanticweb.org/japor/ontologies/2021/5/PizzasLojanitas#>
        SELECT DISTINCT ?name 
        WHERE { 
            ?s rdfs:subClassOf saidi:SalsasTopping .
            ?s rdfs:label ?name
            FILTER (lang(?name) = 'es')
        }

    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    return qres


#VegetalesTopping
def get_response_vegetales():
    sparql.setQuery('''
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX saidi: <http://www.semanticweb.org/japor/ontologies/2021/5/PizzasLojanitas#>
        SELECT DISTINCT ?name 
        WHERE { 
            ?s rdfs:subClassOf saidi:VegetalesTopping .
            ?s rdfs:label ?name
            FILTER (lang(?name) = 'es')
        }

    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    return qres


if __name__ == '__main__':
    get_response_pizzas()
    get_response_carnes()
    get_response_embutidos()
    get_response_especias()
    get_response_frutas()
    get_response_quesos()
    get_response_salsas()
    get_response_vegetales()

