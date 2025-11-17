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
