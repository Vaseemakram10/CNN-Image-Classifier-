<<<<<<< HEAD
# CNN Image Classifier Web Application

A Flask-based web application for image classification using a Convolutional Neural Network (CNN) trained on the CIFAR-10 dataset.

## 📁 Project Structure

```
cnn-web-app/
│
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── cnn-web-app.ipynb        # Jupyter notebook with model training code
├── README.md                # This file
│
├── templates/
│   └── index.html           # Web interface HTML
│
├── static/
│   └── style.css            # CSS styling
│
└── models/
    └── improved_model.h5    # Trained CNN model (you need to add this)
```

## 🚀 Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### 2. Install Dependencies

Open a terminal in the `cnn-web-app` directory and run:

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- TensorFlow (deep learning)
- NumPy (numerical computing)
- Pillow (image processing)

### 3. Train and Save the Model

Before running the web app, you need to train the CNN model:

1. Open `cnn-web-app.ipynb` in Jupyter Notebook or JupyterLab:
   ```bash
   jupyter notebook cnn-web-app.ipynb
   ```

2. Run all cells in the notebook to:
   - Load and preprocess the CIFAR-10 dataset
   - Build and train the CNN model
   - Save the trained model

3. The notebook will save the model as `improved_model.h5`

4. **Important**: Make sure the saved model file is placed in the `models/` directory:
   ```
   cnn-web-app/models/improved_model.h5
   ```

### 4. Run the Web Application

Once you have the trained model in place, start the Flask server:

```bash
python app.py
```

The application will start on `http://localhost:5000`

## 🖥️ Using the Web App

1. Open your web browser and navigate to `http://localhost:5000`

2. **Upload an Image**:
   - Click the upload box or drag and drop an image
   - Supported formats: PNG, JPG, GIF (up to 10MB)

3. **Classify**:
   - Click the "Classify Image" button
   - Wait for the model to process the image

4. **View Results**:
   - See the predicted class and confidence score
   - View the top 3 predictions with confidence bars

## 🎯 CIFAR-10 Classes

The model can classify images into 10 categories:

- ✈️ Airplane
- 🚗 Automobile
- 🐦 Bird
- 🐱 Cat
- 🦌 Deer
- 🐕 Dog
- 🐸 Frog
- 🐴 Horse
- 🚢 Ship
- 🚚 Truck

## 📊 Model Architecture

The CNN model includes:
- 3 convolutional blocks (Conv → ReLU → MaxPool → Dropout)
- Fully connected layers with dropout for regularization
- Softmax output layer for 10 classes

Key hyperparameters:
- Image size: 32×32 pixels (RGB)
- Batch size: 64
- Optimizer: Adam
- Loss function: Categorical Cross-Entropy

## 🛠️ Troubleshooting

### Model Not Loading

**Error**: `Model not loaded. Please check server logs.`

**Solution**: 
1. Verify that `improved_model.h5` exists in the `models/` directory
2. Check that you've trained the model using the notebook
3. Ensure the model file path in `app.py` is correct

### Port Already in Use

**Error**: `Address already in use`

**Solution**:
- Change the port in `app.py`:
  ```python
  app.run(debug=True, host='0.0.0.0', port=5001)  # Use different port
  ```

### Image Upload Fails

**Error**: `No file uploaded` or `No file selected`

**Solution**:
- Ensure you're uploading an image file (PNG, JPG, GIF)
- Check file size (must be under 10MB)
- Try a different image format

## 🔧 Customization

### Change Model Path

Edit `app.py` line 21:
```python
model = keras.models.load_model('path/to/your/model.h5')
```

### Modify Styling

Edit `static/style.css` to customize:
- Colors
- Fonts
- Layout
- Responsive design

### Add More Classes

If you train on a different dataset:
1. Update `CLASS_NAMES` in `app.py`
2. Update the class badges in `templates/index.html`

## 📝 Notes

- The model is trained on 32×32 pixel images
- Best results with images similar to CIFAR-10 dataset
- For production use, consider:
  - Adding user authentication
  - Implementing rate limiting
  - Using a production WSGI server (e.g., Gunicorn)
  - Adding HTTPS support

## 📄 License

This project is for educational purposes.

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements!

## 📧 Support

If you encounter any issues:
1. Check that all dependencies are installed correctly
2. Verify the model file is in the correct location
3. Check the console output for error messages
4. Ensure you're using a compatible Python version (3.8+)

---

**Happy Classifying! 🎉**
=======
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
>>>>>>> f2b45be145bb4ae7649377a1e1dd258985fd5ccd
