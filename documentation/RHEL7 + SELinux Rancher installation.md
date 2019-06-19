# GeoNode Docker / Rancher installation on RHEL7 + SELinux

1) Login to server

    Use ksu or run commands with sudo

2) Check RedHat Subscriptions key for Docker CE:
    ```
    subscription-manager list --available
    ```

3) Add subscription for Docker CE (replace key with real one):
    ```
    subscription-manager attach --pool ff808081628fdce60162f6e12b9a2b50
    ```

    If not using subscriptions, check help: \
    https://docs.docker.com/install/linux/docker-ce/centos/

4) Install Docker Ce:
    ```
    yum install docker-ce
    ```

5) Start Docker:
    ```
    systemctl start docker
    ```

6) Make Docker start on boot:
    ```
    systemctl enable docker
    ```

7) Install & connect Rancher client: \
    https://rancher.com/docs/rancher/v1.6/en/installing-rancher/installing-server/

8) Make directories for files outside containers: \
    database, customised files, geoserver files

9) Set correct security context so directories are accessible:
    ```
    chcon -R system_u:object_r:container_file_t:s0 /srv/geonode
    ```

10) Open Rancher

11) Add new host to Rancher from Catalog (Git) or manually (Add Stack) \
    This requires customised [rancher-compose.yml](https://github.com/resilienceacademy/geonodera/blob/master/server-configurations/rancher-1.6-catalog/templates/0/rancher-compose.yml) and [docker-compose.yml](https://github.com/resilienceacademy/geonodera/blob/master/server-configurations/rancher-1.6-catalog/templates/0/docker-compose.yml)

12) Configure Rancher load balancer with Catalogue (Git) or manually: \
    https://rancher.com/docs/rancher/v1.6/en/rancher-services/load-balancer/

13) Start services

14) Check that everything starts up

15) Upgrade services: celery, django and geoserver

    Add environment variable: \
    GEOSERVER_ADMIN_PASSWORD = xxx

16) Start upgraded services

17) Change GeoServer password to given