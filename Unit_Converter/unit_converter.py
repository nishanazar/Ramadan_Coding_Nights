import streamlit as st

def converter_unit(value, unit_from, unit_to):
    conversion = {
     "meters_kilometers" : 0.001,
     "kilometers_meters" : 1000,
     "grams_kilograms" : 0.001,
     "kilograms_grams" : 1000,

    }

    key = f"{unit_from}_{unit_to}"

    if key in conversion:
       conversion = conversion[key]
       return value * conversion
    else:
        return "Conversion not available"

st.title("Unit Converter")
value = st.number_input("Enter the value to convert", min_value=1.0, step=1.0)
unit_from = st.selectbox("Converter From:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("Converter To:", ["meters", "kilometers", "grams", "kilograms"])

if st.button("Convert"):
    result = converter_unit(value, unit_from, unit_to)
    st.write(f"Converted value is: {result} ")