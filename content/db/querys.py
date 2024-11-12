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