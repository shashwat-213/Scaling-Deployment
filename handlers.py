import kopf
import logging
import datetime
import kubernetes

@kopf.on.create('ScalingDeploy')
def create_fn(spec, name, namespace, **kwargs):
    # Get the current date and time
    now = datetime.datetime.now()

    # Get the day of the week (Monday is 0 and Sunday is 6)
    day_of_week = now.weekday()
    logging.info(f"todays day is: {day_of_week}")
    # Checking if Deployment already exists or not
    api = kubernetes.client.AppsV1Api()
    DEPLOYMENT_NAME = spec.get('deploymentName')
    MAX_REPLICA= spec.get('replicamax')
    MIN_REPLICA= spec.get('replicamin')
    deployments = api.list_namespaced_deployment(namespace=namespace)
    deployment = next((dep for dep in deployments.items if dep.metadata.name == DEPLOYMENT_NAME), None)

    if deployment == None:
        logging.info(f"not able to find the {DEPLOYMENT_NAME} in {namespace}")
    else:
        if day_of_week < 5:
            deployment.spec.replicas = MAX_REPLICA
            resp = api.patch_namespaced_deployment(
                 name=DEPLOYMENT_NAME, namespace=namespace, body=deployment
                )
    
        else:
            deployment.spec.replicas = MIN_REPLICA
            resp = api.patch_namespaced_deployment(
                 name=DEPLOYMENT_NAME, namespace=namespace, body=deployment
                )
        logging.info(f"scaling deployment created {name} in {namespace} : {resp}")

@kopf.on.update('ScalingDeploy')
def update_fn(spec, name, namespace, **kwargs):
    # Get the current date and time
    now = datetime.datetime.now()

    # Get the day of the week (Monday is 0 and Sunday is 6)
    day_of_week = now.weekday()
    logging.info(f"todays day is: {day_of_week}")
    # Checking if Deployment already exists or not
    api = kubernetes.client.AppsV1Api()
    DEPLOYMENT_NAME = spec.get('deploymentName')
    MAX_REPLICA= spec.get('replicamax')
    MIN_REPLICA= spec.get('replicamin')
    deployments = api.list_namespaced_deployment(namespace=namespace)
    deployment = next((dep for dep in deployments.items if dep.metadata.name == DEPLOYMENT_NAME), None)

    if deployment == None:
        logging.info(f"not able to find the {DEPLOYMENT_NAME} in {namespace}")
    else:
        if day_of_week < 5:
            deployment.spec.replicas = MAX_REPLICA
            resp = api.patch_namespaced_deployment(
                 name=DEPLOYMENT_NAME, namespace=namespace, body=deployment
                )
    
        else:
            deployment.spec.replicas = MIN_REPLICA
            resp = api.patch_namespaced_deployment(
                 name=DEPLOYMENT_NAME, namespace=namespace, body=deployment
                )
        logging.info(f"updating deployment {name} in {namespace} : {resp}")