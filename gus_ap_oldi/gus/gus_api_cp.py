from dataclasses import dataclass

from requests import Session
from zeep import Client, Transport
import xmltodict
import yaml

sandbox = True

with open ('./gus_ap_oldi/args.yml','r') as f:
    r = f.read()
    const = yaml.load(r, yaml.SafeLoader)
    __version__ = const['version']

if sandbox:
    const = const['sandbox']