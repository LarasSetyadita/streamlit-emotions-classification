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
    st.write('hello world')
    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

#########################
# menjalankan kode main #
#########################
if __name__ == '__main__':
    main()