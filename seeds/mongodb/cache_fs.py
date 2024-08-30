"""

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""

from extensions_mongo import fs_upload
from secrets_jobs.credentials import path_to_base


with open(path_to_base +
          """LICENSE""", "rb") as f:
    result = fs_upload(input_to_upload=f.read())
    print(str("Database seeded successfully!" if result != -1 else "Failed"))
