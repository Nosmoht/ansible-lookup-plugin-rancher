from ansible.compat.six.moves.urllib.error import HTTPError, URLError
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.module_utils.urls import open_url, ConnectionError, SSLValidationError
import json
import re
import os

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
    def get_project(self, url, url_username, url_password, name, validate_certs):
        try:
            response = open_url(url=url,
                                url_username=url_username,
                                url_password=url_password,
                                validate_certs=validate_certs)
        except HTTPError as e:
            raise AnsibleError("Received HTTP while getting projects: %s" % (str(e)))
        except URLError as e:
            raise AnsibleError("Failed lookup url for %s : %s" % (url, str(e)))
        except SSLValidationError as e:
            raise AnsibleError("Error validating the server's certificate for %s: %s" % (url, str(e)))
        except ConnectionError as e:
            raise AnsibleError("Error connecting to %s: %s" % (url, str(e)))

        body = json.loads(response.read())
        projects = [item for item in body.get('data') if item.get('name') == name]
        l = len(projects)
        if l == 0:
            raise AnsibleError("Project %s not found on %s" % (name, url))
        elif l > 1:
            raise AnsibleError("Too many (%s) projects found named %s on %s" % (l, name, url))
        else:
            project = projects[0]
        return project

    def run(self, terms, variables=None, **kwargs):

        url = kwargs.pop('url', RANCHER_URL)
        api = kwargs.pop('api', RANCHER_API)
        url_username = kwargs.pop('url_username', RANCHER_ACCESS_KEY)
        url_password = kwargs.pop('url_password', RANCHER_SECRET_KEY)
        validate_certs = kwargs.get('validate_certs', True)

        url = '%s/%s/projects' % (url, api)

        project = kwargs.pop('project')
        p = re.compile("(\d+)(\w+)(\d+)")
        if not p.match(project):
            project = self.get_project(url=url, url_username=url_username, url_password=url_password, name=project,
                                       validate_certs=validate_certs)
            project_id = project.get('id')
        else:
            project_id = project

        display.vvvv(
            'rancher_registrationtoken lookup of Registration tokens in project with id %s on %s' % (project_id, url))
        try:
            response = open_url('%s/%s/registrationtokens' % (url, project_id),
                                url_username=url_username,
                                url_password=url_password,
                                validate_certs=validate_certs)
        except HTTPError as e:
            raise AnsibleError("Received HTTP error for %s : %s" % (url, str(e)))
        except URLError as e:
            raise AnsibleError("Failed lookup url for %s : %s" % (url, str(e)))
        except SSLValidationError as e:
            raise AnsibleError("Error validating the server's certificate for %s: %s" % (url, str(e)))
        except ConnectionError as e:
            raise AnsibleError("Error connecting to %s: %s" % (url, str(e)))

        data = json.loads(response.read())
        tokens = data.get('data')
        if terms:
            ret = [token for token in tokens if token.get('name') in terms]
        else:
            ret = tokens

        return ret
