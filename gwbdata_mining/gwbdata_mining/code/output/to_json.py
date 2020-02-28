import json
import datetime
import codecs


def myconverter(o):
    """function to serialise datetime"""
    if isinstance(o, datetime.datetime):
        return o.__str__()


def write_to_file(data, path, date_format="%Y-%m-%d"):
    """Export extracted fields to json"""
    if path.endswith(".json"):
        filename = path
    else:
        filename = path + ".json"

    with codecs.open(filename, "w", encoding="utf-8") as json_file:
        for line in data:
            for k, v in line.items():
                if k.startswith("date") or k.endswith("date"):
                    line[k] = v.strftime(date_format)
        print(type(json))
        print(json)
        json.dump(
            data,
            json_file,
            indent=4,
            sort_keys=True,
            default=myconverter,
            ensure_ascii=False,
        )