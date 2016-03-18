#!/usr/bin/env python

import json
from jinja2 import Environment, FileSystemLoader


if __name__ == "__main__":
    with open("data.json") as f:
        data = json.loads(f.read())

    env = Environment(loader=FileSystemLoader("./"),
                      trim_blocks=True, lstrip_blocks=True)
    template = env.get_template("README.template.md")

    with open("README.md", "w") as f:
        f.write(template.render(data=data).encode('utf8'))
