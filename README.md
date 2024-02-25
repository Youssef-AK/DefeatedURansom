# DefeatedURansom
DefeatedURansom is an innovative cybersecurity solution designed to combat the ever-evolving landscape of ransomware threats. It leverages the power of Variational Autoencoder Generative Adversarial Networks (VEA-GANs) for image-based detection, providing a robust and efficient defense mechanism against ransomware attacks.

![image](https://github.com/Youssef-AK/DefeatedURansom/assets/40705538/99626ff9-1678-4c1d-bcf0-346587895c4a)



## Key Features

**Behavior Defense System:** DefeatedURansom employs a behavior-based detection system that monitors system activities to identify any malicious behavior associated with ransomware attacks.

**Image-Based Detection with VEA-GANs:** Our solution utilizes VEA-GANs to analyze and interpret system images, enabling it to detect subtle changes or anomalies that may indicate a ransomware attack.

**Threat Actor Identification:** Beyond just detecting potential threats, DefeatedURansom is also capable of identifying the threat actor or group behind the attack. This feature allows for a more proactive approach in dealing with ransomware threats by understanding their source and modus operandi.

## Promising Model Stability against Recent Ransomware Families
DefeatedURansom, our proposed model, exhibits remarkable stability across various recent trends in ransomware families. It leverages the power of Variational Autoencoder Generative Adversarial Networks (VEA-GANs) to effectively learn and adapt to the evolving landscape of ransomware threats.

The model’s stability stems from its ability to generalize well from the training data, enabling it to handle new, unseen ransomware families. It does this by learning the underlying data distributions of different ransomware behaviors, which allows it to detect anomalies that could indicate a ransomware attack, even from previously unseen ransomware families.

Moreover, DefeatedURansom’s use of image-based detection adds another layer of robustness. By converting system behavior data into images, the model can leverage the advanced pattern recognition capabilities of convolutional neural networks, further enhancing its stability and performance.

### Metrics: 
![performance_metrics](https://github.com/Youssef-AK/DefeatedURansom/assets/40705538/4edc53bf-479f-4143-a8a5-3efcb067254c)



## Installation Requirements

Before running the code, ensure you have the following dependencies installed:

- Python 3.11
- keras==2.15.0
- matplotlib==3.8.3
- numpy==1.26.4
- pandas==2.2.1
- Pillow==10.2.0
- scikit_learn==1.4.1.post1
- tensorflow==2.15.0
- tensorflow_intel==2.15.0
- OpenCV (cv2)
- chardet

```
pip install -r requirements.txt
```

### Setup Instructions

- Clone this repository to your local machine:
```
git clone https://github.com/Youssef-AK/DefeatedURansom.git
```

- Navigate to the project directory:
```
cd DefeatedURansom
```

### Feature Extractor

- Navigate to the Feature Extractor directory:

```
cd Data Preprocessing
```

- Run the Feature_Extractor.py script:

```
python Feature_Extractor.py --input_path /path/to/input/data --output_path /path/to/save/features
```

### VAE-Model

- Navigate to the VAE-Model directory:
```
cd Modeling
```

- Run the vae_model.py script:
```
python VEA-GANs.py --input_path /path/to/input/features --output_path /path/to/save/results
```


#### Thank you for using our solution!
