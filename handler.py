from typing import Any, Dict, Optional


def handle_request(data: Dict[str, Any], timeout: Optional[int] = 30) -> Dict[str, Any]:
    """Processes a request and returns a response.

    Args:
        data (Dict[str, Any]): The input data for processing.
        timeout (Optional[int], optional): The timeout for the request. Defaults to 30.

    Returns:
        Dict[str, Any]: The processed response.
    """
    response = {}  # Initialize response
    # Simulated processing logic
    response['status'] = 'success'
    response['data'] = data
    return response


def handle_error(error: Exception) -> Dict[str, Any]:
    """Handles exceptions and formats the error response.

    Args:
        error (Exception): The exception that occurred.

    Returns:
        Dict[str, Any]: The formatted error response.
    """
    return {'status': 'error', 'message': str(error)}


if __name__ == '__main__':
    sample_data = {'key': 'value'}
    try:
        result = handle_request(sample_data)
        print(result)
    except Exception as e:
        error_response = handle_error(e)
        print(error_response)
