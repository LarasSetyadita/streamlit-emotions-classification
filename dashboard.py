

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
    st.markdown('<h1 class="page-title">Emotion Classification Dashboard</h1>', unsafe_allow_html=True)

    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="card">
            <h3>Tentang</h3>
            <p>Dashboard ini dibuat untuk membarikan pengetahuan dan wawasan tentang emosi manusia melalui analisis 
            gambar. Dengan memanfaatkan teknologi machine learning dalam pengolahan citra gembar, kami akan membantu Anda
            mengidentifikasi secara akurat, memahami dengan mendalam, dan memberikan saran atas emosi yang anda alami.</p>
            
        </div>
        """,     unsafe_allow_html=True
    )
    # happy
    col1, col2 = st.columns([1, 4])

    with col1:
        st.image('./images/happy.jpg', caption='Deskripsi Gambar')  # Menampilkan gambar

    with col2:
        st.write('hello')

    # sad
    col1, col2 = st.columns([1, 4])
    with col1:

        st.image('./images/sad.jpg', caption='Deskripsi Gambar')  # Menampilkan gambar

    with col2:
        st.write('hello')

    # angry
    col1, col2 = st.columns([1, 4])
    with col1:

        st.image('./images/neutral.jpg', caption='Deskripsi Gambar')  # Menampilkan gambar

    with col2:
        st.write('hello')

    # surprised
    col1, col2 = st.columns([1, 4])
    with col1:

        st.image('./images/surprised.jpg', caption='Deskripsi Gambar')  # Menampilkan gambar

    with col2:
        st.write('hello')

    # neutral
    col1, col2 = st.columns([1, 4])
    with col1:

        st.image('./images/neutral.jpg', caption='Deskripsi Gambar')  # Menampilkan gambar

    with col2:
        st.write('hello')

    # ahegao
    col1, col2 = st.columns([1, 4])
    with col1:

        st.image('./images/ahegao.jpg', caption='Deskripsi Gambar')  # Menampilkan gambar

    with col2:
        st.write('hello')


#########################
# menjalankan kode main #
#########################
if __name__ == '__main__':
    main()