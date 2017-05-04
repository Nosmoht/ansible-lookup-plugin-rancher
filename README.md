Ansible lookup plugin Rancher
==========

- [Introduction](#introduction)
- [Example](#example)

# Introduction
Simple lookup plugin to get data from [Rancher].

# Example
__NOTE:__
The environment/project _project_name_ must be created first as the
__Default__ Environment does not provide any registration token (at least within rancher/server:)

```yaml
# test.yml
---
- hosts: localhost
  gather_facts: false
  connection: local
  vars:
    rancher_url: http://127.0.0.1:8080
    project_name: test-env
    rancher_project: '{{ lookup("rancher_project", project_name, url=rancher_url)}}'
    rancher_project_registrationtoken: '{{ lookup("rancher_registrationtoken", rancher_project["id"], url=rancher_url) }}'
    rancher_agent_registration_token: '{{ rancher_project_registrationtoken.token }}'
    rancher_agent_image_name: '{{ rancher_project_registrationtoken.image }}'
  tasks:
  - debug:
      msg: '{{ item }}'
    with_items:
    - '{{ rancher_project }}'
    - '{{ rancher_project_registrationtoken }}'
    - '{{ rancher_agent_image_name }}'
    - '{{ rancher_agent_registration_token }}'
```

Execute it with
```shell
$ ansible-playbook test.yml
```

Output
```shell
PLAY [localhost] *************************************************************************************************************************************

TASK [debug] *****************************************************************************************************************************************
ok: [localhost] => (item={u'mesos': False, u'actions': {u'deactivate': u'http://127.0.0.1:8080/v1/projects/1a8/?action=deactivate', u'setmembers': u'http://127.0.0.1:8080/v1/projects/1a8/?action=setmembers', u'update': u'http://127.0.0.1:8080/v1/projects/1a8/?action=update', u'delete': u'http://127.0.0.1:8080/v1/projects/1a8/?action=delete'}, u'removeTime': None, u'id': u'1a8', u'links': {u'databasechangelogs': u'http://127.0.0.1:8080/v1/projects/1a8/databasechangelogs', u'databasechangeloglocks': u'http://127.0.0.1:8080/v1/projects/1a8/databasechangeloglocks', u'machineDrivers': u'http://127.0.0.1:8080/v1/projects/1a8/machinedrivers', u'githubconfigs': u'http://127.0.0.1:8080/v1/projects/1a8/githubconfigs', u'externalStoragePoolEvents': u'http://127.0.0.1:8080/v1/projects/1a8/externalstoragepoolevents', u'serviceEvents': u'http://127.0.0.1:8080/v1/projects/1a8/serviceevents', u'registrationTokens': u'http://127.0.0.1:8080/v1/projects/1a8/registrationtokens', u'labels': u'http://127.0.0.1:8080/v1/projects/1a8/labels', u'hostStats': u'http://127.0.0.1:8080/v1/projects/1a8/projects/1a8/hoststats', u'snapshots': u'http://127.0.0.1:8080/v1/projects/1a8/snapshots', u'instances': u'http://127.0.0.1:8080/v1/projects/1a8/instances', u'composeServices': u'http://127.0.0.1:8080/v1/projects/1a8/composeservices', u'agents': u'http://127.0.0.1:8080/v1/projects/1a8/agents', u'ipAddresses': u'http://127.0.0.1:8080/v1/projects/1a8/ipaddresses', u'processInstances': u'http://127.0.0.1:8080/v1/projects/1a8/processinstances', u'images': u'http://127.0.0.1:8080/v1/projects/1a8/images', u'virtualMachines': u'http://127.0.0.1:8080/v1/projects/1a8/virtualmachines', u'loadBalancerServices': u'http://127.0.0.1:8080/v1/projects/1a8/loadbalancerservices', u'identities': u'http://127.0.0.1:8080/v1/projects/1a8/identities', u'backups': u'http://127.0.0.1:8080/v1/projects/1a8/backups', u'machines': u'http://127.0.0.1:8080/v1/projects/1a8/machines', u'kubernetesStacks': u'http://127.0.0.1:8080/v1/projects/1a8/kubernetesstacks', u'azureadconfigs': u'http://127.0.0.1:8080/v1/projects/1a8/azureadconfigs', u'healthcheckInstanceHostMaps': u'http://127.0.0.1:8080/v1/projects/1a8/healthcheckinstancehostmaps', u'localAuthConfigs': u'http://127.0.0.1:8080/v1/projects/1a8/localauthconfigs', u'auditLogs': u'http://127.0.0.1:8080/v1/projects/1a8/auditlogs', u'hostApiProxyTokens': u'http://127.0.0.1:8080/v1/projects/1a8/hostapiproxytokens', u'tasks': u'http://127.0.0.1:8080/v1/projects/1a8/tasks', u'processDefinitions': u'http://127.0.0.1:8080/v1/projects/1a8/processdefinitions', u'self': u'http://127.0.0.1:8080/v1/projects/1a8', u'projectMembers': u'http://127.0.0.1:8080/v1/projects/1a8/projectmembers', u'networks': u'http://127.0.0.1:8080/v1/projects/1a8/networks', u'instanceLinks': u'http://127.0.0.1:8080/v1/projects/1a8/instancelinks', u'certificates': u'http://127.0.0.1:8080/v1/projects/1a8/certificates', u'externalServices': u'http://127.0.0.1:8080/v1/projects/1a8/externalservices', u'apiKeys': u'http://127.0.0.1:8080/v1/projects/1a8/apikeys', u'externalVolumeEvents': u'http://127.0.0.1:8080/v1/projects/1a8/externalvolumeevents', u'composeProjects': u'http://127.0.0.1:8080/v1/projects/1a8/composeprojects', u'dnsServices': u'http://127.0.0.1:8080/v1/projects/1a8/dnsservices', u'registries': u'http://127.0.0.1:8080/v1/projects/1a8/registries', u'registryCredentials': u'http://127.0.0.1:8080/v1/projects/1a8/registrycredentials', u'backupTargets': u'http://127.0.0.1:8080/v1/projects/1a8/backuptargets', u'serviceConsumeMaps': u'http://127.0.0.1:8080/v1/projects/1a8/serviceconsumemaps', u'passwords': u'http://127.0.0.1:8080/v1/projects/1a8/passwords', u'kubernetesServices': u'http://127.0.0.1:8080/v1/projects/1a8/kubernetesservices', u'serviceExposeMaps': u'http://127.0.0.1:8080/v1/projects/1a8/serviceexposemaps', u'typeDocumentations': u'http://127.0.0.1:8080/v1/projects/1a8/typedocumentations', u'containerEvents': u'http://127.0.0.1:8080/v1/projects/1a8/containerevents', u'configItems': u'http://127.0.0.1:8080/v1/projects/1a8/configitems', u'resourceDefinitions': u'http://127.0.0.1:8080/v1/projects/1a8/resourcedefinitions', u'externalHostEvents': u'http://127.0.0.1:8080/v1/projects/1a8/externalhostevents', u'openldapconfigs': u'http://127.0.0.1:8080/v1/projects/1a8/openldapconfigs', u'physicalHosts': u'http://127.0.0.1:8080/v1/projects/1a8/physicalhosts', u'ldapconfigs': u'http://127.0.0.1:8080/v1/projects/1a8/ldapconfigs', u'environments': u'http://127.0.0.1:8080/v1/projects/1a8/environments', u'accounts': u'http://127.0.0.1:8080/v1/projects/1a8/accounts', u'externalEvents': u'http://127.0.0.1:8080/v1/projects/1a8/externalevents', u'credentials': u'http://127.0.0.1:8080/v1/projects/1a8/credentials', u'hosts': u'http://127.0.0.1:8080/v1/projects/1a8/hosts', u'pullTasks': u'http://127.0.0.1:8080/v1/projects/1a8/pulltasks', u'projects': u'http://127.0.0.1:8080/v1/projects/1a8/projects', u'processExecutions': u'http://127.0.0.1:8080/v1/projects/1a8/processexecutions', u'externalHandlers': u'http://127.0.0.1:8080/v1/projects/1a8/externalhandlers', u'haConfigInputs': u'http://127.0.0.1:8080/v1/projects/1a8/haconfiginputs', u'haConfigs': u'http://127.0.0.1:8080/v1/projects/1a8/haconfigs', u'extensionPoints': u'http://127.0.0.1:8080/v1/projects/1a8/extensionpoints', u'settings': u'http://127.0.0.1:8080/v1/projects/1a8/settings', u'storagePools': u'http://127.0.0.1:8080/v1/projects/1a8/storagepools', u'externalHandlerProcesses': u'http://127.0.0.1:8080/v1/projects/1a8/externalhandlerprocesses', u'register': u'http://127.0.0.1:8080/v1/projects/1a8/register', u'taskInstances': u'http://127.0.0.1:8080/v1/projects/1a8/taskinstances', u'ports': u'http://127.0.0.1:8080/v1/projects/1a8/ports', u'externalServiceEvents': u'http://127.0.0.1:8080/v1/projects/1a8/externalserviceevents', u'schemas': u'http://127.0.0.1:8080/v1/projects/1a8/schemas', u'containers': u'http://127.0.0.1:8080/v1/projects/1a8/containers', u'volumes': u'http://127.0.0.1:8080/v1/projects/1a8/volumes', u'configItemStatuses': u'http://127.0.0.1:8080/v1/projects/1a8/configitemstatuses', u'mounts': u'http://127.0.0.1:8080/v1/projects/1a8/mounts', u'externalHandlerExternalHandlerProcessMaps': u'http://127.0.0.1:8080/v1/projects/1a8/externalhandlerexternalhandlerprocessmaps', u'userPreferences': u'http://127.0.0.1:8080/v1/projects/1a8/userpreferences', u'externalDnsEvents': u'http://127.0.0.1:8080/v1/projects/1a8/externaldnsevents', u'services': u'http://127.0.0.1:8080/v1/projects/1a8/services', u'serviceProxies': u'http://127.0.0.1:8080/v1/projects/1a8/serviceproxies'}, u'virtualMachine': False, u'baseType': u'account', u'publicDns': False, u'swarm': False, u'state': u'active', u'allowSystemRole': False, u'transitioning': u'no', u'type': u'project', u'description': u'foo', u'kubernetes': False, u'transitioningProgress': None, u'transitioningMessage': None, u'members': None, u'removed': None, u'data': {u'fields': {u'servicesPortRange': {u'startPort': 49153, u'endPort': 65535}, u'allowSystemRole': False, u'virtualMachine': False, u'orchestration': u'cattle', u'createdStackIds': [5, 6, 7, 8]}}, u'uuid': u'3ef8ae38-08af-4d36-9c73-539ccd3b09a4', u'servicesPortRange': {u'type': u'servicesPortRange', u'startPort': 49153, u'endPort': 65535}, u'kind': u'project', u'name': u'test-env', u'created': u'2017-04-27T16:15:52Z', u'createdTS': 1493309752000}) => {
    "item": {
        "actions": {
            "deactivate": "http://127.0.0.1:8080/v1/projects/1a8/?action=deactivate",
            "delete": "http://127.0.0.1:8080/v1/projects/1a8/?action=delete",
            "setmembers": "http://127.0.0.1:8080/v1/projects/1a8/?action=setmembers",
            "update": "http://127.0.0.1:8080/v1/projects/1a8/?action=update"
        },
        "allowSystemRole": false,
        "baseType": "account",
        "created": "2017-04-27T16:15:52Z",
        "createdTS": 1493309752000,
        "data": {
            "fields": {
                "allowSystemRole": false,
                "createdStackIds": [
                    5,
                    6,
                    7,
                    8
                ],
                "orchestration": "cattle",
                "servicesPortRange": {
                    "endPort": 65535,
                    "startPort": 49153
                },
                "virtualMachine": false
            }
        },
        "description": "foo",
        "id": "1a8",
        "kind": "project",
        "kubernetes": false,
        "links": {
            "accounts": "http://127.0.0.1:8080/v1/projects/1a8/accounts",
            "agents": "http://127.0.0.1:8080/v1/projects/1a8/agents",
            "apiKeys": "http://127.0.0.1:8080/v1/projects/1a8/apikeys",
            "auditLogs": "http://127.0.0.1:8080/v1/projects/1a8/auditlogs",
            "azureadconfigs": "http://127.0.0.1:8080/v1/projects/1a8/azureadconfigs",
            "backupTargets": "http://127.0.0.1:8080/v1/projects/1a8/backuptargets",
            "backups": "http://127.0.0.1:8080/v1/projects/1a8/backups",
            "certificates": "http://127.0.0.1:8080/v1/projects/1a8/certificates",
            "composeProjects": "http://127.0.0.1:8080/v1/projects/1a8/composeprojects",
            "composeServices": "http://127.0.0.1:8080/v1/projects/1a8/composeservices",
            "configItemStatuses": "http://127.0.0.1:8080/v1/projects/1a8/configitemstatuses",
            "configItems": "http://127.0.0.1:8080/v1/projects/1a8/configitems",
            "containerEvents": "http://127.0.0.1:8080/v1/projects/1a8/containerevents",
            "containers": "http://127.0.0.1:8080/v1/projects/1a8/containers",
            "credentials": "http://127.0.0.1:8080/v1/projects/1a8/credentials",
            "databasechangeloglocks": "http://127.0.0.1:8080/v1/projects/1a8/databasechangeloglocks",
            "databasechangelogs": "http://127.0.0.1:8080/v1/projects/1a8/databasechangelogs",
            "dnsServices": "http://127.0.0.1:8080/v1/projects/1a8/dnsservices",
            "environments": "http://127.0.0.1:8080/v1/projects/1a8/environments",
            "extensionPoints": "http://127.0.0.1:8080/v1/projects/1a8/extensionpoints",
            "externalDnsEvents": "http://127.0.0.1:8080/v1/projects/1a8/externaldnsevents",
            "externalEvents": "http://127.0.0.1:8080/v1/projects/1a8/externalevents",
            "externalHandlerExternalHandlerProcessMaps": "http://127.0.0.1:8080/v1/projects/1a8/externalhandlerexternalhandlerprocessmaps",
            "externalHandlerProcesses": "http://127.0.0.1:8080/v1/projects/1a8/externalhandlerprocesses",
            "externalHandlers": "http://127.0.0.1:8080/v1/projects/1a8/externalhandlers",
            "externalHostEvents": "http://127.0.0.1:8080/v1/projects/1a8/externalhostevents",
            "externalServiceEvents": "http://127.0.0.1:8080/v1/projects/1a8/externalserviceevents",
            "externalServices": "http://127.0.0.1:8080/v1/projects/1a8/externalservices",
            "externalStoragePoolEvents": "http://127.0.0.1:8080/v1/projects/1a8/externalstoragepoolevents",
            "externalVolumeEvents": "http://127.0.0.1:8080/v1/projects/1a8/externalvolumeevents",
            "githubconfigs": "http://127.0.0.1:8080/v1/projects/1a8/githubconfigs",
            "haConfigInputs": "http://127.0.0.1:8080/v1/projects/1a8/haconfiginputs",
            "haConfigs": "http://127.0.0.1:8080/v1/projects/1a8/haconfigs",
            "healthcheckInstanceHostMaps": "http://127.0.0.1:8080/v1/projects/1a8/healthcheckinstancehostmaps",
            "hostApiProxyTokens": "http://127.0.0.1:8080/v1/projects/1a8/hostapiproxytokens",
            "hostStats": "http://127.0.0.1:8080/v1/projects/1a8/projects/1a8/hoststats",
            "hosts": "http://127.0.0.1:8080/v1/projects/1a8/hosts",
            "identities": "http://127.0.0.1:8080/v1/projects/1a8/identities",
            "images": "http://127.0.0.1:8080/v1/projects/1a8/images",
            "instanceLinks": "http://127.0.0.1:8080/v1/projects/1a8/instancelinks",
            "instances": "http://127.0.0.1:8080/v1/projects/1a8/instances",
            "ipAddresses": "http://127.0.0.1:8080/v1/projects/1a8/ipaddresses",
            "kubernetesServices": "http://127.0.0.1:8080/v1/projects/1a8/kubernetesservices",
            "kubernetesStacks": "http://127.0.0.1:8080/v1/projects/1a8/kubernetesstacks",
            "labels": "http://127.0.0.1:8080/v1/projects/1a8/labels",
            "ldapconfigs": "http://127.0.0.1:8080/v1/projects/1a8/ldapconfigs",
            "loadBalancerServices": "http://127.0.0.1:8080/v1/projects/1a8/loadbalancerservices",
            "localAuthConfigs": "http://127.0.0.1:8080/v1/projects/1a8/localauthconfigs",
            "machineDrivers": "http://127.0.0.1:8080/v1/projects/1a8/machinedrivers",
            "machines": "http://127.0.0.1:8080/v1/projects/1a8/machines",
            "mounts": "http://127.0.0.1:8080/v1/projects/1a8/mounts",
            "networks": "http://127.0.0.1:8080/v1/projects/1a8/networks",
            "openldapconfigs": "http://127.0.0.1:8080/v1/projects/1a8/openldapconfigs",
            "passwords": "http://127.0.0.1:8080/v1/projects/1a8/passwords",
            "physicalHosts": "http://127.0.0.1:8080/v1/projects/1a8/physicalhosts",
            "ports": "http://127.0.0.1:8080/v1/projects/1a8/ports",
            "processDefinitions": "http://127.0.0.1:8080/v1/projects/1a8/processdefinitions",
            "processExecutions": "http://127.0.0.1:8080/v1/projects/1a8/processexecutions",
            "processInstances": "http://127.0.0.1:8080/v1/projects/1a8/processinstances",
            "projectMembers": "http://127.0.0.1:8080/v1/projects/1a8/projectmembers",
            "projects": "http://127.0.0.1:8080/v1/projects/1a8/projects",
            "pullTasks": "http://127.0.0.1:8080/v1/projects/1a8/pulltasks",
            "register": "http://127.0.0.1:8080/v1/projects/1a8/register",
            "registrationTokens": "http://127.0.0.1:8080/v1/projects/1a8/registrationtokens",
            "registries": "http://127.0.0.1:8080/v1/projects/1a8/registries",
            "registryCredentials": "http://127.0.0.1:8080/v1/projects/1a8/registrycredentials",
            "resourceDefinitions": "http://127.0.0.1:8080/v1/projects/1a8/resourcedefinitions",
            "schemas": "http://127.0.0.1:8080/v1/projects/1a8/schemas",
            "self": "http://127.0.0.1:8080/v1/projects/1a8",
            "serviceConsumeMaps": "http://127.0.0.1:8080/v1/projects/1a8/serviceconsumemaps",
            "serviceEvents": "http://127.0.0.1:8080/v1/projects/1a8/serviceevents",
            "serviceExposeMaps": "http://127.0.0.1:8080/v1/projects/1a8/serviceexposemaps",
            "serviceProxies": "http://127.0.0.1:8080/v1/projects/1a8/serviceproxies",
            "services": "http://127.0.0.1:8080/v1/projects/1a8/services",
            "settings": "http://127.0.0.1:8080/v1/projects/1a8/settings",
            "snapshots": "http://127.0.0.1:8080/v1/projects/1a8/snapshots",
            "storagePools": "http://127.0.0.1:8080/v1/projects/1a8/storagepools",
            "taskInstances": "http://127.0.0.1:8080/v1/projects/1a8/taskinstances",
            "tasks": "http://127.0.0.1:8080/v1/projects/1a8/tasks",
            "typeDocumentations": "http://127.0.0.1:8080/v1/projects/1a8/typedocumentations",
            "userPreferences": "http://127.0.0.1:8080/v1/projects/1a8/userpreferences",
            "virtualMachines": "http://127.0.0.1:8080/v1/projects/1a8/virtualmachines",
            "volumes": "http://127.0.0.1:8080/v1/projects/1a8/volumes"
        },
        "members": null,
        "mesos": false,
        "name": "test-env",
        "publicDns": false,
        "removeTime": null,
        "removed": null,
        "servicesPortRange": {
            "endPort": 65535,
            "startPort": 49153,
            "type": "servicesPortRange"
        },
        "state": "active",
        "swarm": false,
        "transitioning": "no",
        "transitioningMessage": null,
        "transitioningProgress": null,
        "type": "project",
        "uuid": "3ef8ae38-08af-4d36-9c73-539ccd3b09a4",
        "virtualMachine": false
    },
    "msg": {
        "actions": {
            "deactivate": "http://127.0.0.1:8080/v1/projects/1a8/?action=deactivate",
            "delete": "http://127.0.0.1:8080/v1/projects/1a8/?action=delete",
            "setmembers": "http://127.0.0.1:8080/v1/projects/1a8/?action=setmembers",
            "update": "http://127.0.0.1:8080/v1/projects/1a8/?action=update"
        },
        "allowSystemRole": false,
        "baseType": "account",
        "created": "2017-04-27T16:15:52Z",
        "createdTS": 1493309752000,
        "data": {
            "fields": {
                "allowSystemRole": false,
                "createdStackIds": [
                    5,
                    6,
                    7,
                    8
                ],
                "orchestration": "cattle",
                "servicesPortRange": {
                    "endPort": 65535,
                    "startPort": 49153
                },
                "virtualMachine": false
            }
        },
        "description": "foo",
        "id": "1a8",
        "kind": "project",
        "kubernetes": false,
        "links": {
            "accounts": "http://127.0.0.1:8080/v1/projects/1a8/accounts",
            "agents": "http://127.0.0.1:8080/v1/projects/1a8/agents",
            "apiKeys": "http://127.0.0.1:8080/v1/projects/1a8/apikeys",
            "auditLogs": "http://127.0.0.1:8080/v1/projects/1a8/auditlogs",
            "azureadconfigs": "http://127.0.0.1:8080/v1/projects/1a8/azureadconfigs",
            "backupTargets": "http://127.0.0.1:8080/v1/projects/1a8/backuptargets",
            "backups": "http://127.0.0.1:8080/v1/projects/1a8/backups",
            "certificates": "http://127.0.0.1:8080/v1/projects/1a8/certificates",
            "composeProjects": "http://127.0.0.1:8080/v1/projects/1a8/composeprojects",
            "composeServices": "http://127.0.0.1:8080/v1/projects/1a8/composeservices",
            "configItemStatuses": "http://127.0.0.1:8080/v1/projects/1a8/configitemstatuses",
            "configItems": "http://127.0.0.1:8080/v1/projects/1a8/configitems",
            "containerEvents": "http://127.0.0.1:8080/v1/projects/1a8/containerevents",
            "containers": "http://127.0.0.1:8080/v1/projects/1a8/containers",
            "credentials": "http://127.0.0.1:8080/v1/projects/1a8/credentials",
            "databasechangeloglocks": "http://127.0.0.1:8080/v1/projects/1a8/databasechangeloglocks",
            "databasechangelogs": "http://127.0.0.1:8080/v1/projects/1a8/databasechangelogs",
            "dnsServices": "http://127.0.0.1:8080/v1/projects/1a8/dnsservices",
            "environments": "http://127.0.0.1:8080/v1/projects/1a8/environments",
            "extensionPoints": "http://127.0.0.1:8080/v1/projects/1a8/extensionpoints",
            "externalDnsEvents": "http://127.0.0.1:8080/v1/projects/1a8/externaldnsevents",
            "externalEvents": "http://127.0.0.1:8080/v1/projects/1a8/externalevents",
            "externalHandlerExternalHandlerProcessMaps": "http://127.0.0.1:8080/v1/projects/1a8/externalhandlerexternalhandlerprocessmaps",
            "externalHandlerProcesses": "http://127.0.0.1:8080/v1/projects/1a8/externalhandlerprocesses",
            "externalHandlers": "http://127.0.0.1:8080/v1/projects/1a8/externalhandlers",
            "externalHostEvents": "http://127.0.0.1:8080/v1/projects/1a8/externalhostevents",
            "externalServiceEvents": "http://127.0.0.1:8080/v1/projects/1a8/externalserviceevents",
            "externalServices": "http://127.0.0.1:8080/v1/projects/1a8/externalservices",
            "externalStoragePoolEvents": "http://127.0.0.1:8080/v1/projects/1a8/externalstoragepoolevents",
            "externalVolumeEvents": "http://127.0.0.1:8080/v1/projects/1a8/externalvolumeevents",
            "githubconfigs": "http://127.0.0.1:8080/v1/projects/1a8/githubconfigs",
            "haConfigInputs": "http://127.0.0.1:8080/v1/projects/1a8/haconfiginputs",
            "haConfigs": "http://127.0.0.1:8080/v1/projects/1a8/haconfigs",
            "healthcheckInstanceHostMaps": "http://127.0.0.1:8080/v1/projects/1a8/healthcheckinstancehostmaps",
            "hostApiProxyTokens": "http://127.0.0.1:8080/v1/projects/1a8/hostapiproxytokens",
            "hostStats": "http://127.0.0.1:8080/v1/projects/1a8/projects/1a8/hoststats",
            "hosts": "http://127.0.0.1:8080/v1/projects/1a8/hosts",
            "identities": "http://127.0.0.1:8080/v1/projects/1a8/identities",
            "images": "http://127.0.0.1:8080/v1/projects/1a8/images",
            "instanceLinks": "http://127.0.0.1:8080/v1/projects/1a8/instancelinks",
            "instances": "http://127.0.0.1:8080/v1/projects/1a8/instances",
            "ipAddresses": "http://127.0.0.1:8080/v1/projects/1a8/ipaddresses",
            "kubernetesServices": "http://127.0.0.1:8080/v1/projects/1a8/kubernetesservices",
            "kubernetesStacks": "http://127.0.0.1:8080/v1/projects/1a8/kubernetesstacks",
            "labels": "http://127.0.0.1:8080/v1/projects/1a8/labels",
            "ldapconfigs": "http://127.0.0.1:8080/v1/projects/1a8/ldapconfigs",
            "loadBalancerServices": "http://127.0.0.1:8080/v1/projects/1a8/loadbalancerservices",
            "localAuthConfigs": "http://127.0.0.1:8080/v1/projects/1a8/localauthconfigs",
            "machineDrivers": "http://127.0.0.1:8080/v1/projects/1a8/machinedrivers",
            "machines": "http://127.0.0.1:8080/v1/projects/1a8/machines",
            "mounts": "http://127.0.0.1:8080/v1/projects/1a8/mounts",
            "networks": "http://127.0.0.1:8080/v1/projects/1a8/networks",
            "openldapconfigs": "http://127.0.0.1:8080/v1/projects/1a8/openldapconfigs",
            "passwords": "http://127.0.0.1:8080/v1/projects/1a8/passwords",
            "physicalHosts": "http://127.0.0.1:8080/v1/projects/1a8/physicalhosts",
            "ports": "http://127.0.0.1:8080/v1/projects/1a8/ports",
            "processDefinitions": "http://127.0.0.1:8080/v1/projects/1a8/processdefinitions",
            "processExecutions": "http://127.0.0.1:8080/v1/projects/1a8/processexecutions",
            "processInstances": "http://127.0.0.1:8080/v1/projects/1a8/processinstances",
            "projectMembers": "http://127.0.0.1:8080/v1/projects/1a8/projectmembers",
            "projects": "http://127.0.0.1:8080/v1/projects/1a8/projects",
            "pullTasks": "http://127.0.0.1:8080/v1/projects/1a8/pulltasks",
            "register": "http://127.0.0.1:8080/v1/projects/1a8/register",
            "registrationTokens": "http://127.0.0.1:8080/v1/projects/1a8/registrationtokens",
            "registries": "http://127.0.0.1:8080/v1/projects/1a8/registries",
            "registryCredentials": "http://127.0.0.1:8080/v1/projects/1a8/registrycredentials",
            "resourceDefinitions": "http://127.0.0.1:8080/v1/projects/1a8/resourcedefinitions",
            "schemas": "http://127.0.0.1:8080/v1/projects/1a8/schemas",
            "self": "http://127.0.0.1:8080/v1/projects/1a8",
            "serviceConsumeMaps": "http://127.0.0.1:8080/v1/projects/1a8/serviceconsumemaps",
            "serviceEvents": "http://127.0.0.1:8080/v1/projects/1a8/serviceevents",
            "serviceExposeMaps": "http://127.0.0.1:8080/v1/projects/1a8/serviceexposemaps",
            "serviceProxies": "http://127.0.0.1:8080/v1/projects/1a8/serviceproxies",
            "services": "http://127.0.0.1:8080/v1/projects/1a8/services",
            "settings": "http://127.0.0.1:8080/v1/projects/1a8/settings",
            "snapshots": "http://127.0.0.1:8080/v1/projects/1a8/snapshots",
            "storagePools": "http://127.0.0.1:8080/v1/projects/1a8/storagepools",
            "taskInstances": "http://127.0.0.1:8080/v1/projects/1a8/taskinstances",
            "tasks": "http://127.0.0.1:8080/v1/projects/1a8/tasks",
            "typeDocumentations": "http://127.0.0.1:8080/v1/projects/1a8/typedocumentations",
            "userPreferences": "http://127.0.0.1:8080/v1/projects/1a8/userpreferences",
            "virtualMachines": "http://127.0.0.1:8080/v1/projects/1a8/virtualmachines",
            "volumes": "http://127.0.0.1:8080/v1/projects/1a8/volumes"
        },
        "members": null,
        "mesos": false,
        "name": "test-env",
        "publicDns": false,
        "removeTime": null,
        "removed": null,
        "servicesPortRange": {
            "endPort": 65535,
            "startPort": 49153,
            "type": "servicesPortRange"
        },
        "state": "active",
        "swarm": false,
        "transitioning": "no",
        "transitioningMessage": null,
        "transitioningProgress": null,
        "type": "project",
        "uuid": "3ef8ae38-08af-4d36-9c73-539ccd3b09a4",
        "virtualMachine": false
    }
}
ok: [localhost] => (item={u'kind': u'registrationToken', u'accountId': u'1a8', u'name': None, u'links': {u'images': u'http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14/images', u'instances': u'http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14/instances', u'self': u'http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14', u'account': u'http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14/account', u'registrationUrl': u'http://127.0.0.1:8080/v1/scripts/1CD1965A4BC67EB90972:1483142400000:OoHf2PxHihHu2Tc51CoUQJg3cLM'}, u'baseType': u'credential', u'transitioningMessage': None, u'description': None, u'created': u'2017-05-03T17:01:05Z', u'state': u'active', u'actions': {u'deactivate': u'http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14/?action=deactivate', u'update': u'http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14/?action=update'}, u'id': u'1c14', u'token': u'1CD1965A4BC67EB90972:1483142400000:OoHf2PxHihHu2Tc51CoUQJg3cLM', u'command': u'sudo docker run -d --privileged -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/rancher:/var/lib/rancher rancher/agent:v1.2.1 http://127.0.0.1:8080/v1/scripts/1CD1965A4BC67EB90972:1483142400000:OoHf2PxHihHu2Tc51CoUQJg3cLM', u'createdTS': 1493830865000, u'registrationUrl': u'http://127.0.0.1:8080/v1/scripts/1CD1965A4BC67EB90972:1483142400000:OoHf2PxHihHu2Tc51CoUQJg3cLM', u'transitioning': u'no', u'removed': None, u'type': u'registrationToken', u'image': u'rancher/agent:v1.2.1', u'transitioningProgress': None, u'uuid': u'423bf8f5-5321-4e2b-bfa0-1f2e19291ba8'}) => {
    "item": {
        "accountId": "1a8",
        "actions": {
            "deactivate": "http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14/?action=deactivate",
            "update": "http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14/?action=update"
        },
        "baseType": "credential",
        "command": "sudo docker run -d --privileged -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/rancher:/var/lib/rancher rancher/agent:v1.2.1 http://127.0.0.1:8080/v1/scripts/1CD1965A4BC67EB90972:1483142400000:OoHf2PxHihHu2Tc51CoUQJg3cLM", 
        "created": "2017-05-03T17:01:05Z",
        "createdTS": 1493830865000,
        "description": null,
        "id": "1c14",
        "image": "rancher/agent:v1.2.1",
        "kind": "registrationToken",
        "links": {
            "account": "http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14/account",
            "images": "http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14/images",
            "instances": "http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14/instances",
            "registrationUrl": "http://127.0.0.1:8080/v1/scripts/1CD1965A4BC67EB90972:1483142400000:OoHf2PxHihHu2Tc51CoUQJg3cLM",
            "self": "http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14"
        },
        "name": null,
        "registrationUrl": "http://127.0.0.1:8080/v1/scripts/1CD1965A4BC67EB90972:1483142400000:OoHf2PxHihHu2Tc51CoUQJg3cLM",
        "removed": null,
        "state": "active",
        "token": "1CD1965A4BC67EB90972:1483142400000:OoHf2PxHihHu2Tc51CoUQJg3cLM",
        "transitioning": "no",
        "transitioningMessage": null,
        "transitioningProgress": null,
        "type": "registrationToken",
        "uuid": "423bf8f5-5321-4e2b-bfa0-1f2e19291ba8"
    },
    "msg": {
        "accountId": "1a8",
        "actions": {
            "deactivate": "http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14/?action=deactivate",
            "update": "http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14/?action=update"
        },
        "baseType": "credential",
        "command": "sudo docker run -d --privileged -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/rancher:/var/lib/rancher rancher/agent:v1.2.1 http://127.0.0.1:8080/v1/scripts/1CD1965A4BC67EB90972:1483142400000:OoHf2PxHihHu2Tc51CoUQJg3cLM",
        "created": "2017-05-03T17:01:05Z",
        "createdTS": 1493830865000,
        "description": null,
        "id": "1c14",
        "image": "rancher/agent:v1.2.1",
        "kind": "registrationToken",
        "links": {
            "account": "http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14/account",
            "images": "http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14/images",
            "instances": "http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14/instances",
            "registrationUrl": "http://127.0.0.1:8080/v1/scripts/1CD1965A4BC67EB90972:1483142400000:OoHf2PxHihHu2Tc51CoUQJg3cLM",
            "self": "http://127.0.0.1:8080/v1/projects/1a8/registrationtokens/1c14"
        },
        "name": null,
        "registrationUrl": "http://127.0.0.1:8080/v1/scripts/1CD1965A4BC67EB90972:1483142400000:OoHf2PxHihHu2Tc51CoUQJg3cLM",
        "removed": null,
        "state": "active",
        "token": "1CD1965A4BC67EB90972:1483142400000:OoHf2PxHihHu2Tc51CoUQJg3cLM",
        "transitioning": "no",
        "transitioningMessage": null,
        "transitioningProgress": null,
        "type": "registrationToken",
        "uuid": "423bf8f5-5321-4e2b-bfa0-1f2e19291ba8"
    }
}
ok: [localhost] => (item=rancher/agent:v1.2.1) => {
    "item": "rancher/agent:v1.2.1",
    "msg": "rancher/agent:v1.2.1"
}
ok: [localhost] => (item=1CD1965A4BC67EB90972:1483142400000:OoHf2PxHihHu2Tc51CoUQJg3cLM) => {
    "item": "1CD1965A4BC67EB90972:1483142400000:OoHf2PxHihHu2Tc51CoUQJg3cLM",
    "msg": "1CD1965A4BC67EB90972:1483142400000:OoHf2PxHihHu2Tc51CoUQJg3cLM"
}

PLAY RECAP *******************************************************************************************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0
```

[Rancher]: https://www.rancher.com
