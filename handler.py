from typing import Dict


def process_data(data: Dict[str, str]) -> None:
    """
    Process the input data and perform necessary actions.

    Args:
        data (Dict[str, str]): A dictionary containing data to process.
    """
    for key, value in data.items():
        print(f'{key}: {value}')


def handle_request(request: Dict[str, str]) -> None:
    """
    Handle an incoming request and process the data from it.

    Args:
        request (Dict[str, str]): A dictionary representing the request data.
    """
    if 'data' in request:
        process_data(request['data'])
    else:
        print('No data to process')


if __name__ == '__main__':
    sample_request = {
        'data': {
            'name': 'Automation Tool',
            'version': '76'
        }
    }
    handle_request(sample_request)