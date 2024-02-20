# Modeling with VEA-GANs for DefeatedURansom
This repository contains the modeling scripts used in the DefeatedURansom project. The scripts are designed to train a Variational Autoencoder Generative Adversarial Network (VEA-GAN) on the preprocessed data.

## Overview
The modeling stage involves training a VEA-GAN on the images generated from the data preprocessing stage. VEA-GANs are a type of generative model that can generate new data samples that are similar to the training data.

## VEA-GANs
VEA-GANs combine the strengths of Variational Autoencoders (VAEs) and Generative Adversarial Networks (GANs). VAEs are good at learning data distributions and generating new data, while GANs are good at generating sharp, realistic images. By combining these two models, VEA-GANs can generate realistic images that accurately represent the data distribution.

## Usage
1. Ensure that the preprocessed data is in the correct directory.
2. Run the VEA-GAN training script.