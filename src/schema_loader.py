import sqlite3
import os


class SchemaLoader:
    """Loads a schema file into the appropriate database"""

    def __init__(self, database_type: str, path_to_schema_file: str) -> "SchemaLoader":
        self.database_type = database_type
        self.path_to_schema_file = self.path_to_schema_file

    def load_schema(self):
        """Loads the schema"""

        # Read schema into variable
        with open(os.getcwd() + self.path_to_schema_file, "r") as file:
            schema = file.read()

        # Load schema according to database type
        if self.database_type == "sqlite":
            conn = sqlite3.connect("database.db")

            with conn:
                conn.executescript(schema)
