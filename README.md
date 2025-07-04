
# 🧵 PatternSense: Fabric Pattern Classification using Deep Learning

PatternSense is an intelligent web-based application that uses deep learning models to accurately classify various fabric patterns from uploaded images. The system leverages both Convolutional Neural Networks (CNNs) and the powerful ResNet50 transfer learning model for high-performance pattern recognition. It targets applications in the fashion industry, textile quality control, and interior design.

## 🚀 Features

- Upload and classify fabric images in real-time
- Supports pattern types like **Floral**, **Checked**, **Dotted**, **Striped**, **Plain**, and more
- Powered by CNN and ResNet50 deep learning models
- Clean, responsive UI built with Flask and Bootstrap
- Google Maps integration and contact form for user interaction

## 🧠 Models Used

- **CNN Model**: Custom-built Convolutional Neural Network with 3 Conv layers and Dropout
- **Transfer Learning**: ResNet50 pretrained on ImageNet for improved accuracy

## 🗂️ Project Structure

```
PatternSense-FabricPatternsUsingDL/
│
├── 📁 Project files/
│   ├── app/                  # Flask web application
│   ├── data_pattern/         # Dataset
│   ├── models/               # Trained model files (.h5)
│   ├── notebooks/            # Jupyter Notebooks for model training
│
├── 📁 Video Demo/            # Project demo videos
├── 📁 Document/              # Final report, PDF, and supporting documentation
├── README.md                 # Project overview and setup guide
```

## 💻 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/narendra-nersu/PatternSense-FabricPatternsUsingDL.git
   ```

2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the web application:
   ```bash
   cd "Project files/app"
   python app.py
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## 📊 Performance

- **CNN Accuracy**: ~71% validation accuracy
- **ResNet50 Accuracy**: Improved to ~85% with transfer learning and fine-tuning

## 🧪 Manual Testing

Users can manually test the app by uploading custom fabric images to get real-time predictions.

## 🧾 License

This project is part of the AI/ML Internship at **SmartBridge** and intended for academic and demonstration purposes.

---

🎯 **Mentored by**: SmartBridge AI/ML Team  
📆 **Completed**: July 2025  
👨‍💻 **Author**: [Narendra Nersu](https://github.com/narendra-nersu)
