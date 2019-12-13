import logging
import sys

from kubernetes import client, config, watch
from kubernetes.client.rest import ApiException


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler(sys.stdout))


def main():
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    pod_watch = watch.Watch()
    for event in pod_watch.stream(v1.list_pod_for_all_namespaces):
        log.info("Got event: %s pod '%s'!", event['type'], event['object'].metadata.name)


if __name__ == '__main__':
    main()
