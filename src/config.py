import os

# user = os.environ['POSTGRES_USER']
# password = os.environ['POSTGRES_PASSWORD']
# host = os.environ['POSTGRES_HOST']
# database = os.environ['POSTGRES_DB']
# port = os.environ['POSTGRES_PORT']

# DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
# database_file = "sqlite:///{}".format(os.path.join(project_dir, "halo_database.db"))
project_dir = os.path.dirname(os.path.abspath(__file__))
print(project_dir)
DATABASE_CONNECTION_URI ="sqlite:///{}".format(os.path.join(project_dir, "halo_database.db"))
print(DATABASE_CONNECTION_URI)