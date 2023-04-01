import streamlit as st
import openai


# Api bağlantısı
openai.api_key = "APİ KEYİNİZ"
st.title("ChatGPT SEO UYUMLU MAKALE OLUSTURUCU")


#Chatgpt Bağlantısı ve ayarları
def generate_article(keyword, writing_style, word_count):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
        {"role":"user", "content":keyword + "Hakkında SEO için optimize edilmiş bir  makale yaz ve makalenin içindeki başlıkları h1, h2, h3 gibi özelliklerde kullan." },
        {"role":"user", "content":"Bu makale stil sahibi olmalı:" + writing_style},
        {"role":"user", "content":"Makale uzunluğu ise şu kadar olmalı " + str(word_count)}
        ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content

    print(result)
    return result
   
   #Kullanıcı arayüzü

keyword = st.text_input("Anahtar kelimenizi giriniz...")
writing_style = st.selectbox("Makale özelliğiniz seçiniz", 
    ["Hikaye", "Tanımlayıcı", "Akademik", "Açıklayıcı", "Vurgulu", "Yaratıcı", "Teknik", "Haber Tarzı"])
word_count = st.slider("Kelime sayısı:", min_value=300, max_value=1000, step=100, value=300)
submit_button = st.button(
    label="Makale Oluştur", 
    help="SEO makalenizi oluşturmak için tıklayın", 
    key="generate_button"
)
 #Buton
if submit_button:
    with st.spinner("Makale Oluşturuluyor..."):
        article = generate_article(keyword, writing_style, word_count)
        st.write(article)
        st.download_button(
            label="Makaleyi İndir", 
            data=article, 
            file_name='Makaleniz.txt', 
            mime='text/txt'
        )
