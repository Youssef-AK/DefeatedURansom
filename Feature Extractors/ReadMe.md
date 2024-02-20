# DefeatedURansom: Feature Extraction and Image Conversion

DefeatedURansom is a cybersecurity solution that uses advanced techniques to detect and identify ransomware threats. This repository focuses on the feature extraction from report.json files and their conversion into images using vectorization and OpenCV (cv2).

## Overview
The process begins with report.json files extracted from the Cuckoo Sandbox. These files contain valuable information about the behavior of potential ransomware. We extract key features from these files and convert them into a format that can be used for image-based detection.

## Feature Extraction
The feature extraction process involves parsing the report.json files to identify key characteristics of potential ransomware. This includes behaviors such as file system activity, registry activity, network activity, and more.

## Image Conversion
Once the features have been extracted, they are converted into images using vectorization and OpenCV. This involves representing the features as vectors and then converting these vectors into images. These images can then be used for image-based detection of ransomware.

## Usage
1. Extract report.json files from Cuckoo Sandbox.
2. Run the feature extraction script on the report.json files.
3. Run the image conversion script on the extracted features.

### Examples:
<img src="https://github.com/Youssef-AK/DefeatedURansom/assets/40705538/0c90c62c-d434-4ec8-88e2-9592c7e4981b" width="400" height="300"> ; <img src="https://github.com/Youssef-AK/DefeatedURansom/assets/40705538/b7c63ed0-86d7-4228-942c-3372908f0465" width="500" height="400">
