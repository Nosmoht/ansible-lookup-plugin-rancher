from ansible.compat.six.moves.urllib.error import HTTPError, URLError
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.module_utils.urls import open_url, ConnectionError, SSLValidationError
import json

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display

    display = Display()

ANSIBLE_RACHER_URL = 'http://127.0.0.1:8080'


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        validate_certs = kwargs.get('validate_certs', True)
        ret = []
        url = kwargs.pop('url', ANSIBLE_RACHER_URL)
        for term in terms:
            display.vvvv('rancher_account lookup of %s on %s' % (term, url))
            try:
                response = open_url('%s/v2-beta/accounts' % (url))
            except HTTPError as e:
                raise AnsibleError("Received HTTP error for %s : %s" % (term, str(e)))
            except URLError as e:
                raise AnsibleError("Failed lookup url for %s : %s" % (term, str(e)))
            except SSLValidationError as e:
                raise AnsibleError("Error validating the server's certificate for %s: %s" % (term, str(e)))
            except ConnectionError as e:
                raise AnsibleError("Error connecting to %s: %s" % (url, str(e)))

            data = json.loads(response.read())
            for account in data.get('data'):
                if account.get('name') == term:
                    ret.append(account)

        return ret
