def read_asignation_naturgy():
    text="""
        SELECT      *
        FROM        sinfin.asignacion
    """
    return text

def read_dictionary_campain():
    
    text = """
        select		"Vuelta",
			        "Tipo",
			        "Vuelta_correcta"
        from		sinfin.dic_naturgy
    """
    return text

def query_nomina():
    text = """
        select		sucursal, count(sucursal)as q_gestores
        from		data_sinfin.nomina
        where		"ID_CARTERA" = 1 AND CARGO = 'Gestor' AND ESTADO_GESTOR = 'Activo'
        group by	sucursal
    """
    return text