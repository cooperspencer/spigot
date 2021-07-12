#!/bin/env python3

import requests

r = requests.get("https://getbukkit.org/download/spigot")
content = r.text

versionSplit = content.split("<h4>Version</h4>\n")

version = "0"
for v in versionSplit:
	if v.startswith("<h2>"):
		version = v.split(">")[1].split("<")[0]
		break
print("latest version is {}".format(version))
downloadurl = "https://download.getbukkit.org/spigot/spigot-{}.jar".format(version)

r = requests.get(downloadurl, allow_redirects=True)
open('spigot.jar', 'wb').write(r.content)