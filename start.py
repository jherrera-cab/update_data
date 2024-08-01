from content.connection.credentials import read_credentials
from content.connection.connect_db import create_conection
from content.extraction.read_db import read_file


credentials = read_credentials()

engine_local = create_conection(credentials)

read_file(engine_local)
