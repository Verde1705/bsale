#!/usr/bin/python
# -*- coding: UTF-8 -*-


from lp.json_util import loads


if __name__ == "__main__":

    file = open("emitteddocs.json")
    file_content = file.read().strip()

    json_data = loads(file_content)

    for item in json_data["items"]:
        print item["number"]
