from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

app = Flask(__name__)

# Path to your model file (Ensure this path is correct)
model_path = os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'model_resnet50.h5')
model = load_model(model_path)

# Class labels for prediction
labels = ['Batik', 'Checked', 'Chevron', 'Dotted', 'Floral', 'Geometric', 'Herringbone', 'Paisley', 'Solid', 'Striped']

# Set the folder where the images will be uploaded
UPLOAD_FOLDER = r'C:\Users\Lenovo\OneDrive\Documents\ndn\Internship\SmartBridgeAIML\PatternSense-FabricPatternsUsingDL\app\static\uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# The getstarted route to upload image and show prediction
@app.route('/getstarted', methods=['GET', 'POST'])
def getstarted():
    prediction = None
    img_url = None

    if request.method == 'POST':
        # Get the file from the form
        file = request.files['file']

        if file and file.filename != '':
            # Ensure the uploads folder exists
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])

            # Save the file to the uploads folder
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Process the image for prediction
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img = load_img(img_path, target_size=(255, 255))
            x = img_to_array(img)
            x = np.expand_dims(x, axis=0)
            pred = model.predict(x, verbose=0)
            prediction = labels[pred.argmax()]
            img_url = filename

    return render_template('getstarted.html', prediction=prediction, img_url=img_url)

if __name__ == '__main__':
    app.run(debug=True)
