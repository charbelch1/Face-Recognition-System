# Face Recognition System
# Face Recognition System

This project implements a **Face Recognition System** using a **Siamese Neural Network (SNN)** built from scratch in TensorFlow. The system is designed for real-time face recognition and features a user-friendly application interface developed with Kivy. 

## Project Overview

Face recognition technology has numerous applications, including security systems, access control, and user identification. This project aims to create an efficient and accurate face recognition system that can identify individuals in real time using a webcam feed.

### Objectives
- To develop a robust Siamese Neural Network for extracting facial features and comparing them.
- To create a user-friendly application that allows users to register their faces and recognize them using webcam input.
- To ensure the system operates in real-time, providing immediate feedback and recognition results.

### Features
- **Real-time Face Recognition**: The system can identify and verify faces in real-time using a webcam.
- **User Registration**: Users can register their faces, which are then stored for future recognition.
- **Siamese Neural Network**: A custom-built SNN that computes similarity scores between facial embeddings, enabling effective face comparison.
- **Graphical User Interface**: Built with Kivy, the interface is intuitive and easy to navigate.

## Architecture

The face recognition system consists of the following components:

- **Siamese Neural Network (SNN)**: 
  - Trained on a dataset of facial images to learn the unique features of different individuals.
  - Utilizes contrastive loss to optimize the model for distinguishing between similar and dissimilar faces.

- **Webcam Access**: 
  - Uses OpenCV to capture video frames from the webcam, enabling real-time processing.

- **Kivy Application**: 
  - Provides a graphical user interface (GUI) for user interactions, including registration and face recognition.

## Dependencies

This project requires the following Python libraries:

- **TensorFlow**: For building and training the neural network.
- **NumPy**: For numerical operations and data manipulation.
- **OpenCV**: For capturing and processing video feed from the webcam.
- **Kivy**: For creating the graphical user interface.

You can install all dependencies using the command provided in the Installation section.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/face-recognition-system.git
   cd face-recognition-system
   ```

2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

4. Follow the on-screen instructions to register faces and start recognition.

