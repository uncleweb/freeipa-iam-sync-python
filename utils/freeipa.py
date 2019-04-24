import os
from python_freeipa import Client

if 'IPA_HOST' not in os.environ:
    raise Exception("UNABLE TO COMMUNICATE WITH FreeIPA HOST. Please set IPA_HOST env var.")

if 'IPA_USERNAME' not in os.environ:
    raise Exception("UNABLE TO LOGIN. Please set IPA_USERNAME env var.")

if 'IPA_PASSWORD' not in os.environ:
    raise Exception("UNABLE TO LOGIN. Please set IPA_PASSWORD env var.")

ipa_server = os.environ['IPA_HOST']
ipa_service_user = os.environ['IPA_USERNAME']
ipa_service_pass = os.environ['IPA_PASSWORD']

def get_ipa_client():
    client = Client(ipa_server, version='4.6.4', verify_ssl=False)
    client.login(ipa_service_user, ipa_service_pass)
    return client

def get_ipa_users():
    client = get_ipa_client()
    return client.group_show('ipausers')