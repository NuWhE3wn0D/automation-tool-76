import sys

def process_items(items):
    if not items:
        raise ValueError("Input list cannot be empty")
    if not isinstance(items, list):
        raise TypeError("Input must be a list")
    results = []
    for idx, item in enumerate(items):
        try:
            if not isinstance(item, (int, float)):
                raise TypeError(f"Item at index {idx} must be a number")
            if item < 0:
                raise ValueError(f"Negative value not allowed at index {idx}")
            result = item ** 2
            results.append(result)
        except (TypeError, ValueError) as err:
            print(f"Error at item {idx}: {err}", file=sys.stderr)
            results.append(0)
        except Exception as err:
            print(f"Unexpected error at item {idx}: {err}", file=sys.stderr)
            results.append(None)
    return results

def main():
    sample_data = [4, -2, "three", 5.5, 0, 10]
    try:
        output = process_items(sample_data)
        print("Processed results:", output)
    except (ValueError, TypeError) as e:
        print(f"Input validation failed: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected failure: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()