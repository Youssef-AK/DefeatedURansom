import os

def is_valid_report_json(directory):
    """
    Check if a 'reports' directory contains a 'report.json' file.

    Parameters:
    - directory: Path to the 'reports' directory to check.

    Returns:
    - True if the 'reports' directory contains a 'report.json' file, False otherwise.
    """
    report_json_path = os.path.join(directory, 'report.json')
    return os.path.isfile(report_json_path)

def check_reports_directories(root_directory):
    """
    Check all 'reports' directories within the root_directory for 'report.json' files.

    Parameters:
    - root_directory: Root directory containing the directories to check.

    Returns:
    - A list of tuples, where each tuple contains the directory path and a boolean indicating if it contains a 'report.json' file.
    """
    directory_checks = []
    for root, dirs, _ in os.walk(root_directory):
        # Exclude directories that start with 'Benign'
        dirs[:] = [d for d in dirs if not d.startswith('Benign')]
        for dirname in dirs:
            if dirname == 'reports':
                full_path = os.path.join(root, dirname)
                is_valid = is_valid_report_json(full_path)
                directory_checks.append((full_path, is_valid))
    return directory_checks

# Example usage:
root_directory = r'F:\Ransom_samples_22'
directory_checks = check_reports_directories(root_directory)
for directory, is_valid in directory_checks:
    print(f"{directory}: {'Valid' if is_valid else 'Invalid'}")
