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
        url_base = variables['url'] if 'url' in variables else ANSIBLE_RACHER_URL

        for term in terms:
            url = '%s/v1/projects' % (url_base)
            display.vvvv('rancher_project lookup of %s on %s' % (term, url))
            try:
                response = open_url(url)
            except HTTPError as e:
                raise AnsibleError("Received HTTP error for %s : %s" % (term, str(e)))
            except URLError as e:
                raise AnsibleError("Failed lookup url for %s : %s" % (term, str(e)))
            except SSLValidationError as e:
                raise AnsibleError("Error validating the server's certificate for %s: %s" % (term, str(e)))
            except ConnectionError as e:
                raise AnsibleError("Error connecting to %s: %s" % (term, str(e)))

            data = json.loads(response.read())
            for item in data.get('data'):
                if item.get('name') == term and item.get('type') == 'project':
                    ret.append(item)

        return ret
