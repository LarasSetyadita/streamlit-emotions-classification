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
    st.markdown('<h1 class="page-title">Artikel untuk Emosi</h1>', unsafe_allow_html=True)
    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

    st.markdown('<h6 class="page-title happy-card" style="">Penanganan Emosi</h6>', unsafe_allow_html=True)


    st.markdown(
        """
        <div class="card">
            <h5>Penanganan yang Tepat untuk Berbagai Emosi</h5>
            <p>
                Emosi adalah bagian penting dari pengalaman manusia yang memengaruhi cara kita berinteraksi 
                dengan dunia di sekitar kita. Setiap emosi, baik itu kejutan, kebahagiaan, ketenangan, 
                kemarahan, kesedihan, atau ekspresi ahegao, memiliki makna dan dampaknya sendiri. Memahami 
                dan menangani emosi dengan tepat dapat membantu kita menjalani kehidupan yang lebih seimbang 
                dan sehat.
            </p>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="card">
            <h5>Menangani Kejutan</h5>
            <p>
                Kejutan adalah emosi yang bisa muncul dari berita baik atau buruk. Saat menghadapi kejutan, 
                penting untuk memberi diri kita waktu untuk merenung. Mengambil napas dalam-dalam dan mencerna 
                situasi sebelum bereaksi dapat membantu kita merespons dengan lebih bijaksana. Salah satu cara 
                yang efektif untuk memproses perasaan kejutan adalah dengan mencatatnya. Menuliskan pengalaman 
                ini bisa membantu kita memahami reaksi kita dan menemukan makna di balik situasi yang terjadi.
            </p>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="card">
            <h5>Merayakan Kebahagiaan</h5>
            <p>
                Kebahagiaan adalah emosi yang positif dan memberi energi. Ketika kita merasa bahagia, sangat 
                penting untuk merayakan momen-momen kecil yang membawa kebahagiaan. Hal ini tidak hanya membuat 
                kita lebih menghargai kebahagiaan itu sendiri, tetapi juga memperkuat hubungan kita dengan orang 
                lain. Berbagi kebahagiaan dengan teman dan keluarga dapat meningkatkan suasana hati kita dan 
                menjadikan momen tersebut lebih berarti. Selain itu, penting untuk terus melakukan hal-hal yang 
                kita nikmati agar kebahagiaan tetap terjaga.
            </p>
    </div>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="card">
            <h5>Merenungkan Ketenangan</h5>
            <p>
                Ketika kita merasa netral atau tenang, saat tersebut bisa dimanfaatkan untuk refleksi diri. 
                Merenungkan tujuan hidup dan mengevaluasi prioritas dapat memberikan arah yang lebih jelas dalam 
                hidup kita. Ini juga bisa menjadi waktu yang tepat untuk mencoba aktivitas baru. Mengambil langkah 
                untuk mengeksplorasi hobi atau minat baru dapat menghidupkan kembali semangat dan kreativitas kita.
            </p>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="card">
            <h5>Mengelola Kemarahan</h5>
            <p>
            Namun, emosi marah adalah hal yang wajar, tetapi perlu dikelola dengan hati-hati. Ketika marah, 
            memberikan waktu untuk tenang sangatlah penting. Menjauh dari situasi yang memicu kemarahan dapat 
            membantu kita meredakan emosi tersebut. Setelah tenang, kita bisa mengekspresikan perasaan kita 
            dengan bijaksana. Berbicara dengan seseorang yang kita percayai tentang kemarahan yang kita rasakan 
            bisa menjadi langkah baik untuk mencari solusi.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
            <h5>Menghadapi Kesedihan</h5>
            <p>
            Kesedihan juga merupakan emosi yang wajar, sering kali diperlukan untuk proses penyembuhan. Dalam 
            menghadapi kesedihan, penting untuk memberi diri kita izin untuk merasa. Menyadari bahwa merasa 
            sedih adalah hal yang normal bisa membantu kita mengatasi perasaan tersebut. Mencari dukungan dari 
            teman, keluarga, atau profesional juga sangat penting dalam mengatasi kesedihan yang mendalam. 
            Dukungan dari orang-orang terdekat bisa memberikan rasa nyaman dan membantu kita pulih.
            </p>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="card">
            <h5>Ekspresi Ahegao dan Kreativitas</h5>
            <p>
            Sementara itu, ekspresi ahegao sering kali berkaitan dengan budaya pop. Meskipun terlihat ringan, 
            penting untuk mengelola emosi ini dengan cara yang positif. Menggunakan kreativitas kita, seperti 
            menggambar atau menulis, untuk mengekspresikan perasaan ini bisa menjadi cara yang menyenangkan 
            dan menghibur. Kita juga bisa bersikap santai dan menikmati elemen humor dalam ekspresi tersebut, 
            tanpa merasa tertekan.
            </p>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="card">
            <h5>Kesimpulan</h5>
            <p>
            Secara keseluruhan, menghadapi emosi adalah bagian tak terpisahkan dari kehidupan. Dengan mengenali 
            dan memahami emosi kita serta menerapkan penanganan yang tepat, kita bisa menjalani hidup dengan 
            lebih seimbang. Ingatlah bahwa semua emosi memiliki perannya masing-masing dalam perjalanan hidup 
            kita. Luangkan waktu untuk memahami emosi Anda dan terapkan pendekatan yang tepat untuk menghadapinya. 
            Dengan cara ini, kita dapat lebih baik dalam mengelola emosi dan menciptakan hidup yang lebih memuaskan.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

#########################
# menjalankan kode main #
#########################
if __name__ == '__main__':
    main()