from typing import Any, Dict


def handle_request(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process the incoming request data.
    
    Args:
        data (Dict[str, Any]): The request data containing key-value pairs.
    
    Returns:
        Dict[str, Any]: The processed response data.
    """
    # Example processing logic (to be replaced with actual implementation)
    response = {"status": "success", "received": data}
    return response


def handle_error(error: Exception) -> Dict[str, Any]:
    """
    Handle errors that occur during request processing.
    
    Args:
        error (Exception): The error that occurred.
    
    Returns:
        Dict[str, Any]: The error response data.
    """
    return {"status": "error", "message": str(error)}


if __name__ == "__main__":
    sample_data = {"key": "value"}
    try:
        result = handle_request(sample_data)
        print(result)
    except Exception as e:
        error_response = handle_error(e)
        print(error_response)