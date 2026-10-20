import sys

def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError("input must be a dictionary")
    if "task_id" not in data or not isinstance(data["task_id"], int):
        raise ValueError("missing or invalid task_id")
    return True

def process_stream(stream):
    for entry in stream:
        try:
            if validate_input(entry):
                execute_task(entry)
        except (ValueError, TypeError) as e:
            print(f"skip malformed input: {e}", file=sys.stderr)
            continue

def execute_task(task):
    print(f"processing task {task['task_id']}")

if __name__ == "__main__":
    mock_data = [{"task_id": 1}, "invalid", {"task_id": 2}]
    process_stream(mock_data)