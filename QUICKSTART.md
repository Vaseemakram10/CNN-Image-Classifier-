# Quick Start Guide

## ⚡ Fast Setup (5 Minutes)

### Step 1: Install Dependencies
```bash
cd cnn-web-app
pip install -r requirements.txt
```

### Step 2: Train the Model

**Option A - Using Jupyter Notebook:**
```bash
jupyter notebook cnn-web-app.ipynb
```
Then run all cells and wait for training to complete (~20-30 minutes on CPU).

**Option B - If you already have a trained model:**
- Place your `improved_model.h5` file in the `models/` directory

### Step 3: Run the Web App
```bash
python app.py
```

### Step 4: Open in Browser
Navigate to: http://localhost:5000

## 🎯 Test the App

Try uploading images of:
- Airplanes ✈️
- Cars 🚗
- Animals (cats, dogs, birds, deer, frogs, horses) 🐱🐕🐦
- Ships 🚢
- Trucks 🚚

## ⚠️ Important Notes

1. **Model File Required**: The app won't work without `models/improved_model.h5`
2. **First Run**: Model loading takes a few seconds on startup
3. **Best Results**: Use images similar to CIFAR-10 (32x32 pixels, clear objects)
4. **Image Size**: Any size works, but will be resized to 32x32 internally

## 🐛 Common Issues

**"Model not loaded"**
→ Check that `models/improved_model.h5` exists

**"Port 5000 already in use"**
→ Edit `app.py` and change port to 5001

**"ModuleNotFoundError"**
→ Run `pip install -r requirements.txt` again

## 📱 Mobile Friendly

The web interface is responsive and works on:
- 💻 Desktop browsers
- 📱 Mobile devices
- 📟 Tablets

---

Need help? Check the full README.md for detailed instructions.
