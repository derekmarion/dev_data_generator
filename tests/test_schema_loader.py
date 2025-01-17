from src import SchemaLoader
import pytest
import sqlite3
import os

# Define constants for tests
SCHEMA_FILEPATH_SQLITE = "/tests/fixtures/test_schema_loader/schema_sqlite.sql"
DATABASE_FILEPATH_SQLITE = os.path.join(os.getcwd() + "/database.db")


# Define fixtures for tests
@pytest.fixture(scope="module")
def clean_db_sqlite():
    """Fixture to remove existing SQLite database file if it exists"""

    if os.path.exists(DATABASE_FILEPATH_SQLITE):
        os.remove(DATABASE_FILEPATH_SQLITE)
    yield
    # Cleanup after tests
    if os.path.exists(DATABASE_FILEPATH_SQLITE):
        os.remove(DATABASE_FILEPATH_SQLITE)


@pytest.fixture(scope="module")
def schema_loader_sqlite(clean_db_sqlite):
    """Initialize the SchemaLoader with a SQLite schema"""

    return SchemaLoader("sqlite", SCHEMA_FILEPATH_SQLITE)


class TestSchemaLoader:
    """Test class for the SchemaLoader object"""

    def test_load_schema_sqlite(self, schema_loader_sqlite):
        """Test the load_schema method of the SchemaLoader for a SQLite schema"""

        schema_loader_sqlite.load_schema()

        # Fetch tables from DB
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        conn.close()

        # Filter out the sqlite_sequence table
        tables = [table[0] for table in tables if table[0] != "sqlite_sequence"]
        # Assert expected tables were created
        assert len(tables) == 3
        assert "users" in tables
        assert "posts" in tables
        assert "comments" in tables
