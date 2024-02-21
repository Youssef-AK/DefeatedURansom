{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "de6b1b42-8e99-4473-a9af-c4bea43a1020",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import tensorflow as tf\n",
    "from tensorflow.keras import layers\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3b8dc505-ee09-4c7d-95fa-3cff2bff05fe",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Define the generator (similar to an autoencoder)\n",
    "def make_generator_model():\n",
    "    model = tf.keras.Sequential()\n",
    "    model.add(layers.Dense(7*7*256, use_bias=False, input_shape=(100,)))\n",
    "    model.add(layers.BatchNormalization())\n",
    "    model.add(layers.LeakyReLU())\n",
    "\n",
    "    model.add(layers.Reshape((7, 7, 256)))\n",
    "    assert model.output_shape == (None, 7, 7, 256)\n",
    "\n",
    "    model.add(layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False))\n",
    "    assert model.output_shape == (None, 7, 7, 128)\n",
    "    model.add(layers.BatchNormalization())\n",
    "    model.add(layers.LeakyReLU())\n",
    "\n",
    "    model.add(layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))\n",
    "    assert model.output_shape == (None, 14, 14, 64)\n",
    "    model.add(layers.BatchNormalization())\n",
    "    model.add(layers.LeakyReLU())\n",
    "\n",
    "    model.add(layers.Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh'))\n",
    "    assert model.output_shape == (None, 28, 28, 1)\n",
    "\n",
    "    return model\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8f3b6110-722c-4b15-904a-95b8c0fe6f46",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Define the discriminator (similar to a CNN classifier)\n",
    "def make_discriminator_model():\n",
    "    model = tf.keras.Sequential()\n",
    "    model.add(layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same',\n",
    "                                     input_shape=[28, 28, 1]))\n",
    "    model.add(layers.LeakyReLU())\n",
    "    model.add(layers.Dropout(0.3))\n",
    "\n",
    "    model.add(layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same'))\n",
    "    model.add(layers.LeakyReLU())\n",
    "    model.add(layers.Dropout(0.3))\n",
    "\n",
    "    model.add(layers.Flatten())\n",
    "    model.add(layers.Dense(1))\n",
    "\n",
    "    return model\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53a70df2-8855-4eaf-a617-a6d424288336",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define the number of epochs\n",
    "EPOCHS = 50\n",
    "\n",
    "# Define the batch size\n",
    "# As you have 9 images, let's set the batch size to 1\n",
    "BATCH_SIZE = 1\n",
    "\n",
    "# Define the training loop\n",
    "@tf.function\n",
    "def train_step(images):\n",
    "    noise = tf.random.normal([BATCH_SIZE, 100])\n",
    "\n",
    "    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:\n",
    "        generated_images = generator(noise, training=True)\n",
    "\n",
    "        real_output = discriminator(images, training=True)\n",
    "        fake_output = discriminator(generated_images, training=True)\n",
    "\n",
    "        gen_loss = generator_loss(fake_output)\n",
    "        disc_loss = discriminator_loss(real_output, fake_output)\n",
    "\n",
    "    gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)\n",
    "    gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)\n",
    "\n",
    "    generator_optimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))\n",
    "    discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))\n",
    "\n",
    "# Train the model\n",
    "for epoch in range(EPOCHS):\n",
    "    for image_batch in tf.data.Dataset.from_tensor_slices(images_ready).batch(BATCH_SIZE):\n",
    "        train_step(image_batch)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "360dcede-f585-4222-a2e1-83ef2def1541",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define a function to generate and save images\n",
    "def generate_and_save_images(model, epoch, test_input):\n",
    "    # Generate images from the model\n",
    "    predictions = model(test_input, training=False)\n",
    "\n",
    "    # Rescale the pixel values from [-1, 1] to [0, 1]\n",
    "    predictions = (predictions + 1) / 2.0\n",
    "\n",
    "    # Plot the generated images\n",
    "    fig = plt.figure(figsize=(4, 4))\n",
    "    for i in range(predictions.shape[0]):\n",
    "        plt.subplot(4, 4, i+1)\n",
    "        plt.imshow(predictions[i, :, :, 0], cmap='gray')\n",
    "        plt.axis('off')\n",
    "\n",
    "    # Save the figure\n",
    "    plt.savefig('image_at_epoch_{:04d}.png'.format(epoch))\n",
    "    plt.show()\n",
    "\n",
    "# Generate a random noise vector as a test input to the generator\n",
    "test_input = tf.random.normal([16, 100])\n",
    "\n",
    "# Train the model\n",
    "for epoch in range(EPOCHS):\n",
    "    for image_batch in tf.data.Dataset.from_tensor_slices(images_ready).batch(BATCH_SIZE):\n",
    "        train_step(image_batch)\n",
    "    \n",
    "    # Generate and save images every 5 epochs\n",
    "    if (epoch + 1) % 5 == 0:\n",
    "        generate_and_save_images(generator, epoch + 1, test_input)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
