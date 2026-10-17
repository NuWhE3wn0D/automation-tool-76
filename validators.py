class ValidationError(Exception):
    pass

def validate_input(data: dict) -> None:
    required_fields = {"id", "payload", "timestamp"}
    if not isinstance(data, dict):
        raise ValidationError("input must be a dictionary")
    
    missing = required_fields - data.keys()
    if missing:
        raise ValidationError(f"missing required fields: {', '.join(missing)}")
    
    if not isinstance(data.get("id"), int):
        raise ValidationError("field 'id' must be an integer")

def process_stream(data_stream):
    for entry in data_stream:
        try:
            validate_input(entry)
            yield entry
        except ValidationError as e:
            print(f"skip invalid entry: {e}")
            continue