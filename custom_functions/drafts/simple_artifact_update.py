def simple_artifact_update(container_id=None, artifact_id=None, artifact_json=None, **kwargs):
    """
    This CF updates an arftifact based on the JSON provided.
    
    Args:
        container_id: If no container ID is specified, the CF uses the id in the container context where the playbook is currently being executed.
        artifact_id: The Artifact ID is required
        artifact_json: The JSON must be structured as shown at https://docs.splunk.com/Documentation/SOARonprem/6.2.0/PlatformAPI/RESTArtifacts
    
    Returns a JSON-serializable object that implements the configured data paths:
        message
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    if container_id:
        c_id = container_id
    else:
        c_id = phantom.get_current_container_id_()
        
    if artifact_id:     
        a_id = artifact_id
    else:
        phantom.debug("Artifact ID is missing)
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
