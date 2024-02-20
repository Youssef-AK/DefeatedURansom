# DefeatedURansom
DefeatedURansom is an innovative cybersecurity solution designed to combat the ever-evolving landscape of ransomware threats. It leverages the power of Variational Autoencoder Generative Adversarial Networks (VEA-GANs) for image-based detection, providing a robust and efficient defense mechanism against ransomware attacks.

![OIG2](https://github.com/Youssef-AK/DefeatedURansom/assets/40705538/1e143f5a-c336-4042-8104-0f41205bac86)


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


## Dependencies
- Python 3.11
- NumPy
- Pandas
- Matplotlib
- TensorFlow 2
- scikit-learn 
- OpenCV (cv2)
- chardet

