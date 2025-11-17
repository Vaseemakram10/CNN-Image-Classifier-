# CNN-Image-Classifier-

A deep learning project implementing a Convolutional Neural Network (CNN) trained on the Fashion-MNIST dataset to classify 28×28 grayscale clothing images into 10 categories.  
This repository contains the full training pipeline, evaluation results, saved models, and a detailed academic-style report.
## 📘 Project Summary
This project demonstrates how to build, train, and evaluate a Convolutional Neural Network for image classification.  
The CNN learns to recognize fashion items such as T-shirts, trousers, pullovers, dresses, coats, shoes, and bags, using the Fashion-MNIST dataset.
The repository includes:
- End-to-end data preprocessing  
- CNN model architecture  
- Training and validation workflows  
- Confusion matrix & classification report  
- Accuracy and loss visualizations  
- Saved models for deployment  
- A detailed project report  
- Placeholders for UI screenshots and result images  
## 🧠 Model Overview
The CNN architecture includes:
- Conv2D → MaxPool (32 filters)  
- Conv2D → MaxPool (64 filters)  
- Flatten layer  
- Dense(128, ReLU)  
- Dropout(0.3) for regularization  
- Dense(10, Softmax) output  
This lightweight model provides strong performance on Fashion-MNIST while remaining deployable and efficient.
## 📊 Dataset
**Fashion-MNIST**  
- 70,000 grayscale images  
- Size: 28×28×1  
- 10 clothing categories  
- Train/Val/Test split: **70% / 15% / 15%**
Each image is normalized and reshaped to meet CNN requirements. Labels are converted using one-hot encoding.
## 🚀 Training & Evaluation
The model is trained using:
- **Loss:** Categorical Crossentropy  
- **Optimizer:** Adam  
- **Batch Size:** 32  
- **Epochs:** 10  
- **Validation included** during training  
Typical performance: **85–92%** accuracy on test data.
Evaluation includes:
- Confusion matrix  
- Classification report  
- Accuracy/Loss curves  
- Sample predictions  
Graphs and result images should be placed in the `results/` folder.
## 📁 Project Structure
CNN-Image-Classifier-/
│
├── cnn_training.ipynb # Training + evaluation workflow
├── models/
│ ├── cnn_image_classifier.h5 # Saved model (HDF5)
│ └── saved_cnn_model/ # SavedModel format
│
├── results/ # Add your UI & result images here
│ ├── accuracy_curve.png
│ ├── loss_curve.png
│ └── confusion_matrix.png
│
├── report/
│ └── Final_Report.docx # Full academic-style report
│
├── requirements.txt # Dependencies
└── README.md # This file
## 📦 Installation
Install dependencies:
pip install -r requirements.txt
Run the notebook:
jupyter notebook cnn_training.ipynb
Replace or update model outputs in the models/ folder.
📁 Adding Screenshots & Results
Place all UI screenshots, accuracy/loss graphs, and confusion matrix images inside:
/results
These will be referenced in your report and future documentation.
🎯 Future Enhancements
Integration with a Flask or FastAPI web application
Batch normalization for improved stability
Data augmentation for better generalization
Transfer learning experiments
