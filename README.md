# I3 Fuck

## Does anyone forgor to i3lock ?
Try executing this before they come back :
'''
$ curl -fsSL http://localhost:8001/payload.py | python3
'''

## How to add spell ?

- clone the project
- add your script in a subfolder in the spells folder
- reference it in the manifest.json
  as
  '''
    {
      "name": "foldername",
      "entrypoint": "script_name.sh/.py",
      "files": ["script_name.sh","dependencies"]
    }
  '''
- branch and pr
