import os
from pathlib import Path

# Locally, we need the folder of the duck DB to exist

if __name__ == "__main__":

    for db in ("BASICS_IO_DB","BASICS_RSC_DB"):
        db_path = os.getenv(db)
        if db_path is None:
            raise ValueError(f"{db} should be defined")

        Path(db_path).parent.mkdir(parents=True,exist_ok=True)
    print("DEPLOYMENT DONE")
