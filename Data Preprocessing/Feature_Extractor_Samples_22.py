import os
import json
import pandas as pd

# Step 1: Enhance feature extraction process
def extract_features_from_json(data):
    # Initialize feature dictionary
    features = {}

    try:
        # Generic behavior features
        features['generic'] = data.get("behavior", {}).get("generic", [])

        # API stats features
        features['apistats'] = data.get("behavior", {}).get("apistats", {})

        # Processes behavior features
        features['processes'] = data.get("behavior", {}).get("processes", [])

        # Process tree behavior features
        features['processtree'] = data.get("behavior", {}).get("processtree", [])

        # Summary features
        features['summary'] = data.get("behavior", {}).get("summary", {})

    except Exception as e:
        print(f"Error extracting features from JSON: {e}")

    return features

# Define function to check if a directory contains a report.json file
def is_valid_report_json(directory):
    report_json_path = os.path.join(directory, 'report.json')
    return os.path.isfile(report_json_path)

# Define function to process valid directories
def process_valid_directories(root_directory):
    all_features = []
    directory_paths = []

    # Iterate over all directories in the root directory
    for root, dirs, files in os.walk(root_directory):
        # Exclude directories that start with 'Benign'
        dirs[:] = [d for d in dirs if not d.lower().startswith('benign')]
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if is_valid_report_json(dir_path):
                report_json_path = os.path.join(dir_path, 'report.json')
                try:
                    # Load JSON file
                    with open(report_json_path, 'r') as f:
                        data = json.load(f)
                    # Extract features from JSON file
                    features = extract_features_from_json(data)
                    all_features.append(features)
                    # Add directory path
                    directory_paths.append(dir_path)
                    # Print progress
                    print(f"Processed: {report_json_path}")
                except Exception as e:
                    print(f"Error processing JSON file {report_json_path}: {e}")

    return all_features, directory_paths

# Define root directory
root_directory = r'F:\Ransom_samples_22'

# Process valid directories
all_features, directory_paths = process_valid_directories(root_directory)

# Convert list of dictionaries to pandas DataFrame
df = pd.DataFrame(all_features)

# Set 'Label' column based on the sample directory names
df['Label'] = [os.path.basename(os.path.dirname(os.path.dirname(path))) for path in directory_paths]


# Save DataFrame to CSV file with a unique name based on the root directory
output_csv = os.path.join(root_directory, f"{os.path.basename(root_directory)}_features.csv")
df.to_csv(output_csv, index=False)

print(f"Features saved to CSV file: {output_csv}")
