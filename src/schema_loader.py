import sqlite3
import os


class SchemaLoader:
    """
    Loads a schema file into the appropriate database.

    :param path_to_schema_file: The full path to the schema file starting at project root (e.g. /tests/fixtures/test_schema_loader/schema.sql).
    :type path_to_schema_file: str
    """

    def __init__(self, database_type: str, path_to_schema_file: str):
        """
        Initializes the SchemaLoader with the given database type and schema file path.

        :param path_to_schema_file: The full path to the schema file starting at project root (e.g. /tests/fixtures/test_schema_loader/schema.sql).
        :type path_to_schema_file: str
        """
        self.database_type = database_type
        self.path_to_schema_file = path_to_schema_file

    def load_schema(self):
        """Loads the schema"""

        # Read schema into variable
        with open(os.getcwd() + self.path_to_schema_file, "r") as file:
            schema = file.read()

        # Load schema according to database type
        if self.database_type.lower() == "sqlite":
            conn = sqlite3.connect("database.db")

            with conn:
                conn.executescript(schema)

    def clean_db(self):
        # TODO: implement this
        # Should remove existing DBs based on the type and schema
        pass
