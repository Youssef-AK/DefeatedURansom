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
        # features['total_generic_behaviors'] = len(generic_behavior)

        # API stats features
        features['apistats']= data.get("behavior", {}).get("apistats", {})
        # features['total_apistats_entries'] = len(apistats_behavior)
        # Extracting specific API stats features
        # api_keys = [key for key in apistats_behavior.keys() if key.isdigit()]  # Assuming API keys are integers
        # features['total_unique_api_keys'] = len(api_keys)

        # Processes behavior features
        features['processes'] = data.get("behavior", {}).get("processes", [])
        # features['total_process_behaviors'] = len(processes_behavior)

        # Process tree behavior features
        features['processtree']= data.get("behavior", {}).get("processtree", [])
        # features['total_process_tree_behaviors'] = len(processtree_behavior)

        # Summary features
        features['summary'] = data.get("behavior", {}).get("summary", {})

        # File created summary feature
        # file_created_summary = summary.get("file_created", [])
        # features['total_files_created'] = len(file_created_summary)
    except Exception as e:
        print(f"Error extracting features from JSON: {e}")

    return features

# Directory containing JSON files
directory = r'Updated_Samples_23'



# List to store extracted features from all JSON files
all_features = []
directory_labels = []

# Iterate over all directories in the main directory
for main_dir in os.listdir(directory):
    main_dir_path = os.path.join(directory, main_dir)
    if os.path.isdir(main_dir_path):
        reports_dir = os.path.join(main_dir_path, 'reports')
        if os.path.exists(reports_dir):
            for root, dirs, files in os.walk(reports_dir):
                for file in files:
                    if file.endswith('.json'):
                        json_file = os.path.join(root, file)
                        try:
                            # Load JSON file
                            with open(json_file, 'r') as f:
                                data = json.load(f)
                            # Extract features from JSON file
                            features = extract_features_from_json(data)
                            all_features.append(features)
                            # Add main directory name as label
                            directory_labels.append(main_dir)
                        except Exception as e:
                            print(f"Error processing JSON file {json_file}: {e}")

# Convert list of dictionaries to pandas DataFrame
df = pd.DataFrame(all_features)

# Add a column with the label of the main directory names
df['Label'] = directory_labels

# Save DataFrame to CSV file with a unique name based on the directory
output_dir = os.path.basename(directory)  # Extract directory name
output_csv = os.path.join(directory, f"{output_dir}_features.csv")  # Construct output CSV file path

# Save DataFrame to CSV file
df.to_csv(output_csv, index=False)

print(f"Features saved to CSV file: {output_csv}")