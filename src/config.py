import os

print(project_dir)
DATABASE_CONNECTION_URI ="sqlite:///{}".format(os.path.join(project_dir, "halo_database.db"))
print(DATABASE_CONNECTION_URI)