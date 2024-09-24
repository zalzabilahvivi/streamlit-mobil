import pickle
import streamlit as st 

model = pickle.load(open('estimasi_mobil.sav', 'rb'))
st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('input tahun mobil')
mileage = st.number_input('input km mobil')
tax = st.number_input('input pajak mobil')
mpg = st.number_input('input konsumsi bbm mobil')
engineSize = st.number_input('input engine size')

predict =''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year,mileage,tax,mpg,engineSize]]
    )
    st.write('Estimasi harga mobil bekas dalam Ponds : ',predict)
    st.write('Estimasi harga mobil bekas dalam IDR (Juta):',)