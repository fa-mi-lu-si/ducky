import json

def read_json_file(filename):
    try:
        with open(filename, "r") as file:
            # Filter out comment lines and combine into a single string
            filtered_content = "".join(
                line
                for line in file
                if not any(line.strip().startswith(prefix) for prefix in ("#", "//"))
            )

            # Parse the cleaned JSON
            data = json.loads(filtered_content)
            return data
    except OSError as e:
        print(f"Error opening file: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return None
