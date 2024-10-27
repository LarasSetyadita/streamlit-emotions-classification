import streamlit as st

#######################
# pengaturan tampilan #
#######################
st.set_page_config(layout='wide')

# load css file
with open('./css/style.css') as f :
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

###############
# main method #
###############
def main():
    st.markdown('<h1 class="page-title">Emosi Saya</h1>', unsafe_allow_html=True)
    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="card">
            <h3>Petunjuk</h3>
            <ol>Pilihlah salah satu menu pada dropdown untuk menentukan metode andan mengunggah file gambar, gambar dapat
            diupload dari lokal maupun diambil secara langsung</ol>
            <ol>klik tombol analyze untuk mulai menganalisa emosi pada foto yang di unggah</ol>


        </div>
        """, unsafe_allow_html=True
    )
    option = st.selectbox(
        "Pilih input gambar",
        ("Camera", "Upload image")
    )
    picture = None

    if option == "Camera":
        picture = st.camera_input("Take a picture")
    else:
        picture = st.file_uploader("Choose a file",  type=["jpg", "jpeg", "png"])

    if picture:
        st.image(picture, caption="Gambar yang dipilih")

#########################
# menjalankan kode main #
#########################
if __name__ == '__main__':
    main()