import streamlit as st
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from PIL import Image
import tensorflow as tf

# Suppress TensorFlow warnings
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

# Display settings
st.set_page_config(layout='wide')

# Load CSS for additional styling
with open('./css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the Keras model for predictions
model = load_model('model/model.h5')


# Show suggestions for "Happy" emotion
def saran_happy():
    st.markdown(
        """
        <div class="card">
            <h5>Rayakan Momen Kecil</h5>
            <p>Jangan ragu untuk merayakan kebahagiaan, baik besar maupun kecil. 
            Luangkan waktu untuk menghargai momen-momen ini dan berbagi dengan 
            orang-orang terkasih.</p>
            <h5>Bagikan Kebahagiaan</h5>
            <p>Berbagi kebahagiaan Anda dengan orang lain dapat meningkatkan suasana 
            hati Anda dan membuat pengalaman tersebut lebih berarti.</p>
        </div>
        """, unsafe_allow_html=True
    )

# Show suggestions for "Sad" emotion
def saran_sad():
    st.markdown(
        """
        <div class="card">
            <h5>
                Izinkan Diri untuk Merasa
            </h5>
            <p>
                Sadari bahwa kesedihan adalah emosi yang wajar. Izinkan diri Anda 
                untuk merasakan tanpa rasa bersalah.
            </p>
            <h5>
                Cari Dukungan
            </h5>
            <p>
                Jangan ragu untuk berbicara dengan teman, keluarga, atau profesional 
                ketika perasaan sedih Anda berlarut-larut. Menerima dukungan dapat 
                sangat membantu dalam proses penyembuhan.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

# Show suggestions for "Surprised" emotion
def saran_surprised():
    st.markdown(
        """
        <div class="card">
            <h5>Ambil Waktu untuk Merenung</h5>
            <p>Ketika Anda terkejut, baik dengan berita baik maupun buruk, ambil 
            sejenak untuk mencerna apa yang terjadi. Ini membantu Anda merespons 
            dengan lebih bijaksana.</p>
            <h5>Tuliskan Perasaan Anda</h5>
            <p>Mencatat pengalaman mengejutkan dapat membantu Anda memproses dan 
            memahami reaksi Anda.</p>
        </div>
        """, unsafe_allow_html=True
    )

def saran_neutral():
    st.markdown(
        """
        <div class="card">
            <h5> Ambil Waktu untuk Refleksi </h5>
            <p>Perasaan netral bisa menjadi kesempatan untuk merenungkan apa yang 
            penting bagi Anda. Luangkan waktu untuk menetapkan tujuan baru atau 
            mengevaluasi prioritas hidup Anda.</p>
            
            <h5> Cobalah Aktivitas Baru </h5>
            <p> Ketika Anda merasa netral, itu bisa menjadi saat yang tepat untuk 
            mencoba sesuatu yang baru, baik itu hobi, makanan, atau aktivitas 
            sosial. </p>
        </div>
        """, unsafe_allow_html=True
    )


def saran_ahegao():
    st.markdown(
        """
        <div class="card">
            <h5>Ekspresikan Kreativitas Anda</h5>
            <p>
                Jika Anda menikmati bentuk ekspresi ini dalam budaya pop, gunakan 
                kreativitas Anda untuk menggambarkan emosi melalui seni atau 
                tulisan.
            </p>

            <h5>Bersikap Terbuka dan Santai</h5>
            <p>
                Jangan ragu untuk mengungkapkan diri dalam konteks yang sesuai, dan 
                nikmati aspek humor dalam ekspresi ini.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

def saran_angry():
    st.markdown(
        """
        <div class="card">
            <h5>Luangkan Waktu untuk Menenangkan Diri</h5>
            <p>
                Ketika marah, penting untuk memberi diri Anda waktu untuk tenang 
                sebelum bereaksi. Pertimbangkan untuk menarik napas dalam-dalam 
                atau berjalan-jalan.
            </p>

            <h5>Berbicara tentang Perasaan Anda</h5>
            <p>
                Berbicara dengan seseorang yang Anda percayai dapat membantu Anda 
                mengatasi kemarahan dan mencari solusi.
            </p>
        </div>
        """, unsafe_allow_html=True
    )
# Preprocess image before prediction
def image_preprocessing(picture):
    # Ensure the picture is a PIL.Image object
    if isinstance(picture, bytes):
        img = Image.open(BytesIO(picture))
    elif isinstance(picture, Image.Image):
        img = picture
    else:
        img = Image.open(picture)
    img = img.convert("RGB")
    # Resize image to fit model input
    img = img.resize((150, 150))

    # Convert image to numpy array and normalize
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  # Normalize pixel values to 0-1
    img_array = np.expand_dims(img_array, axis=0)
    images = np.vstack([img_array])  # Combine array for batch prediction
    return images


# Display prediction result as text
def image_prediction(prediction):
    emotions = ["Ahegao", "Angry", "Happy", "Neutral", "Sad", "Surprise", "Tidak dikenali"]

    # Menentukan emotion yang sesuai
    if 0 <= prediction < len(emotions) - 1:
        emotion = emotions[prediction]
    else:
        emotion = "Tidak dikenali"

    # Memberikan class CSS yang sesuai untuk emosi
    css_class = emotion.lower().replace(" ", "-") if emotion != "Tidak dikenali" else "unknown"

    # Menampilkan hasil prediksi dengan styling CSS
    st.markdown(
        f"""
        <div class="emotion-card {css_class}">
            {emotion}
        </div>
        """,
        unsafe_allow_html=True
    )  # Show if prediction is not recognized


def main():
    # Page title and separator
    st.markdown('<h1 class="page-title">Ekspresikan Diri dan Temukan Emosi</h1>', unsafe_allow_html=True)
    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

    # Instruction section
    st.markdown(
        """
        <div class="card">
            <h3>Petunjuk</h3>
            <p>Pilihlah salah satu metode input untuk mengunggah gambar, lalu klik tombol "Analyze" untuk menganalisis emosi pada gambar yang diunggah.</p>
        </div>
        """, unsafe_allow_html=True
    )

    # Image input options
    option = st.selectbox(
        "Pilih input gambar",
        ("Camera", "Upload image")
    )

    # Variable to store input image
    picture = None

    # Input image via camera or file upload
    if option == "Camera":
        picture = st.camera_input("Ambil gambar")
    else:
        picture = st.file_uploader("Pilih file gambar", type=["jpg", "jpeg", "png"])

    # Display selected image
    if picture:
        st.image(picture, caption="Gambar yang dipilih")

    # Button to start analysis
    analisis = st.button('Analyze')

    # If an image is uploaded and Analyze button is pressed
    if picture and analisis:
        images = image_preprocessing(picture)  # Preprocess image
        classes = model.predict(images, batch_size=10)  # Predict
        prediction = np.argmax(classes[0])  # Get prediction index
        image_prediction(prediction)  # Show prediction result
        if prediction == 0:
            saran_ahegao()
        elif prediction == 1:
            saran_angry()
        elif prediction == 2:
            saran_happy()
        elif prediction == 3:
            saran_neutral()
        elif prediction == 4:
            saran_sad()
        elif prediction == 5:
            saran_surprised()


# Run Main Method
if __name__ == '__main__':
    main()
