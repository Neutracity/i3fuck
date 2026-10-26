import os
import random
import json
import urllib.request
import tempfile
import sys


BASE_URL = "https://i3.neutra.city/spells/"
MANIFEST_URL = f"{BASE_URL}manifest.json"

local = "-o" in sys.argv[1:]

if local :
    with open("spells/manifest.json",'r') as file :
        spells = json.load(file)
else :
    with urllib.request.urlopen(MANIFEST_URL) as resp:
        spells = json.loads(resp.read().decode())


# Set dry run
dry_run = "-D" in sys.argv[1:] or "-d" in sys.argv[1:]

# Set chosen spell
if "-c" in sys.argv[1:] :
    index = sys.argv.index("-c") + 1
    if index < len(sys.argv):
        expected = sys.argv[index]
        for i in spells:
            if i['name'] == expected:
                chosen_spell = i
                break;
else:
    chosen_spell = random.choice(spells)
    
with tempfile.TemporaryDirectory(delete=False) as tmp_dir:
    # Downloading all dependencies of the spell
    if local :
        for filename in chosen_spell["files"]:
            file_path = f"spells/{chosen_spell['name']}/{filename}"
            dest_path = f"{tmp_dir}/{filename}"
            os.makedirs(os.path.dirname(dest_path),exist_ok=True)
            os.system(f"cp -r {file_path} {dest_path}")
    else:
        for filename in chosen_spell["files"]:
            file_url = f"{BASE_URL}{chosen_spell['name']}/{filename}"
            dest_path = f"{tmp_dir}/{filename}"
            os.makedirs(os.path.dirname(dest_path),exist_ok=True)
            print(f"actual request: {file_url} ")
            urllib.request.urlretrieve(file_url,dest_path)
    if dry_run :
        print(chosen_spell)
        os.system(f"cat {tmp_dir}/{chosen_spell["entrypoint"]}")
    else :
        # Executing the spell
        os.system(f"chmod 766 {tmp_dir}/{chosen_spell["entrypoint"]}")
        os.system(f"{tmp_dir}/{chosen_spell["entrypoint"]}")
