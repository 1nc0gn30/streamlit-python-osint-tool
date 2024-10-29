import subprocess

def extract_metadata(file_path):
    try:
        result = subprocess.check_output(["exiftool", file_path])
        return result.decode("utf-8")
    except Exception as e:
        return f"Error extracting metadata: {str(e)}"

