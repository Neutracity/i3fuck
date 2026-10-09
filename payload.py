import os
import random
import json
import urllib.request
import tempfile
import sys


BASE_URL = "http://localhost:8001/spells/"
MANIFEST_URL = f"{BASE_URL}manifest.json"

with urllib.request.urlopen(MANIFEST_URL) as resp:
    spells = json.loads(resp.read().decode())

chosen_spell = random.choice(spells)
    
with tempfile.TemporaryDirectory() as tmp_dir:
    # Downloading all dependencies of the spell
    for filename in chosen_spell["files"]:
        file_url = f"{BASE_URL}{chosen_spell['name']}/{filename}"
        dest_path = f"{tmp_dir}/{filename}"
        os.makedirs(os.path.dirname(dest_path),exist_ok=True)
        urllib.request.urlretrieve(file_url,dest_path)
        
    # Executing the spell
    os.system(f"chmod 766 {tmp_dir}/{chosen_spell["entrypoint"]}")
    os.system(f"{tmp_dir}/{chosen_spell["entrypoint"]}")
