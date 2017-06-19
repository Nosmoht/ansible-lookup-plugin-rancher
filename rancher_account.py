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

RANCHER_API = 'v2-beta'
RANCHER_URL = os.environ.get('RANCHER_URL', 'http://127.0.0.1:8080')
RANCHER_ACCESS_KEY = os.environ.get('RANCHER_ACCESS_KEY', None)
RANCHER_SECRET_KEY = os.environ.get('RANCHER_SECRET_KEY', None)


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        ret = []
        url = kwargs.pop('url', RANCHER_URL)
        url_username = kwargs.pop('url_username', RANCHER_ACCESS_KEY)
        url_password = kwargs.pop('url_password', RANCHER_SECRET_KEY)
        api = kwargs.pop('api', RANCHER_API)
        validate_certs = kwargs.get('validate_certs', True)
        for term in terms:
            display.vvvv('rancher_account lookup of %s on %s' % (term, url))
            try:
                response = open_url('%s/%s/accounts' % (url, api),
                                    url_username=url_username,
                                    url_password=url_password,
                                    validate_certs=validate_certs)
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
