

import os
import yaml
import pkg_resources
from collections import OrderedDict
import logging
from .invoice_template import InvoiceTemplate
import codecs
import chardet

logging.getLogger("chardet").setLevel(logging.WARNING)


def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    """load mappings and ordered mappings

    loader to load mappings and ordered mappings into the Python 2.7+ OrderedDict type,
    instead of the vanilla dict and the list of pairs it currently uses.
    """

    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping
    )

    return yaml.load(stream, OrderedLoader)


def read_templates(folder=None):
    """
    Load yaml templates from template folder. Return list of dicts.

    Use built-in templates if no folder is set.
    """
    output = []

    if folder is None:
        folder = pkg_resources.resource_filename(__name__, "templates")

    for path, subdirs, files in os.walk(folder):
        for name in sorted(files):
            if name.endswith(".yml"):
                with open(os.path.join(path, name), "rb") as f:
                    encoding = chardet.detect(f.read())["encoding"]
                with codecs.open(
                    os.path.join(path, name), encoding=encoding
                ) as template_file:
                    tpl = ordered_load(template_file.read())
                tpl["template_name"] = name

                # Test if all required fields are in template:
                assert "keywords" in tpl.keys(), "Missing keywords field."

                # Keywords as list, if only one.
                if type(tpl["keywords"]) is not list:
                    tpl["keywords"] = [tpl["keywords"]]

                output.append(InvoiceTemplate(tpl))
    return output
