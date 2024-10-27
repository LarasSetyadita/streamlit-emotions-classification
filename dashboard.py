
import time
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
            <b>! analisis emosi pada gambar dapat anda lakukan pada menu emotion recognition pada sidebar</b>
        </div>
        """,     unsafe_allow_html=True
    )

    st.write("") # memberi jarak
    st.write("")
    st.write("")
    st.write("")

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.image('./images/happy.jpg', caption='Happy')
    with col2:
        st.image('./images/sad.jpg', caption='Sad')
    with col3:
        st.image('./images/angry.jpg', caption='Angry')
    with col4:
        st.image('./images/neutral.jpg', caption='Neutral')
    with col5:
        st.image('./images/surprised.jpg', caption='Surprised')
    with col6:
        st.image('./images/ahegao.jpg', caption='Ahegao')

    st.write("") # memberi jarak
    st.write("")
    st.write("")
    st.write("")

    # Daftar elemen yang ingin ditampilkan
    elements = [
        {
            "title": "Happy",
            "content": "Bahagia adalah perasaan yang muncul saat kita merasakan kepuasan, kehangatan, dan kedamaian dalam "
                       "diri. Emosi ini sering ditandai dengan senyuman, tawa, dan semangat untuk berbagi. Saat bahagia, "
                       "dunia terasa lebih cerah, dan segala tantangan tampak lebih ringan. Bahagia adalah anugerah yang "
                       "mendorong kita untuk menghargai momen-momen sederhana dalam hidup.",
            "background_color": "#FFFDDB",  # Kuning
            "border_color": "#FFF603"  # Kuning gelap
        },
        {
            "title": "Sad",
            "content": "Sedih adalah perasaan yang muncul saat kita menghadapi kehilangan, kekecewaan, atau kesedihan mendalam. "
                       "Emosi ini sering disertai dengan rasa hampa, air mata, dan keinginan untuk menyendiri. Meskipun menyakitkan, "
                       "sedih juga merupakan bagian penting dari pengalaman manusia, mengajarkan kita untuk menghargai kebahagiaan "
                       "dan mengembangkan empati terhadap orang lain.",
            "background_color": "#DBFCFF",  # Biru
            "border_color": "#01ECFD"  # Biru gelap
        },
        {
            "title": "Excited",
            "content": "Gembira adalah perasaan antusiasme yang muncul ketika kita berhadapan dengan pengalaman yang menyenangkan atau menantang. "
                       "Emosi ini sering kali disertai dengan perasaan harap, energi tinggi, dan semangat yang membara. "
                       "Kegembiraan dapat memotivasi kita untuk mengambil risiko, mengejar impian, dan mencoba hal-hal baru. "
                       "Dengan mengelola energi ini, kita bisa menggunakannya sebagai pendorong untuk mencapai tujuan dan menghadapi tantangan dengan optimisme.",
            "background_color": "#DEFFD1",  # Hijau
            "border_color": "#4EFD09"  # Hijau gelap
        },
        {
            "title": "Angry",
            "content": "Marah adalah perasaan yang muncul sebagai respons terhadap ketidakadilan, frustrasi, atau ancaman. "
                       "Emosi ini sering ditandai dengan peningkatan detak jantung, ketegangan otot, dan keinginan untuk "
                       "beraksi. Meskipun bisa merusak, marah juga memiliki peran penting, mendorong kita untuk mengatasi "
                       "masalah, memperjuangkan hak, dan membangun batasan. Memahami dan mengelola kemarahan dapat mengubahnya "
                       "menjadi kekuatan positif.",
            "background_color": "#FFD9D9",  # Merah
            "border_color": "#FE0608"  # Merah gelap
        },
        {
            "title": "Surprised",
            "content": "Terkejut adalah reaksi spontan terhadap sesuatu yang tak terduga, baik positif maupun negatif. "
                       "Emosi ini sering diiringi dengan reaksi fisik seperti mata membesar atau mulut terbuka. "
                       "Kejutan dapat merangsang rasa ingin tahu atau, sebaliknya, memicu kewaspadaan. "
                       "Dengan merangkul kejutan, kita bisa belajar untuk lebih fleksibel dan terbuka terhadap pengalaman baru yang mungkin membawa perubahan positif.",
            "background_color": "#FFE2D1",  # Oranye
            "border_color": "#FE843D"  # Oranye gelap
        },
        {
            "title": "Bored",
            "content": "Bosan adalah keadaan emosional di mana kita merasa tidak ada yang menarik atau menantang untuk dilakukan. "
                       "Perasaan ini sering ditandai dengan kurangnya minat, energi yang rendah, dan keinginan untuk mencari stimulasi baru. "
                       "Meskipun tampak negatif, kebosanan juga dapat memotivasi kita untuk mengeksplorasi minat baru atau memicu kreativitas. "
                       "Mengatasi kebosanan dengan cara yang sehat bisa membantu kita menemukan inspirasi dalam rutinitas sehari-hari.",
            "background_color": "#E5E5E5",  # Abu-abu
            "border_color": "#606060"  # Abu-abu gelap
        }
    ]

    # Tempat untuk menampilkan elemen
    placeholder = st.empty()

    # Menampilkan elemen secara bergantian dengan efek animasi
    while True:
        for element in elements:
            with placeholder:
                st.markdown(
                    f"""
                    <div class="happy-card " style="background-color: {element['background_color']}; border: 2px solid {element['border_color']};">
                        <h3>{element['title']}</h3>
                        <p>{element['content']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            time.sleep(2)  # Menunggu 2 detik sebelum menampilkan elemen berikutnya  # Menunggu 2 detik sebelum menampilkan elemen berikutnya

#########################
# menjalankan kode main #
#########################
if __name__ == '__main__':
    main()