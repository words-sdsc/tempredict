def conn_str (usrname, passwd):
    postgres_str = 'postgresql+psycopg2://'+usrname+':'+passwd+'@awesome-graph.sdsc.edu:5432/postgres'
    return postgres_str