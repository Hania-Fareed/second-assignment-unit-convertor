import streamlit as st

def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701,
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value

def convert_time(value, from_unit, to_unit):
    time_units = {
        "Seconds": 1,
        "Minutes": 1/60,
        "Hours": 1/3600,
        "Days": 1/86400,
    }
    return value * (time_units[to_unit] / time_units[from_unit])

st.set_page_config(page_title="Google Unit Converter", layout="wide")
st.sidebar.title("⚙️ Conversion Options")
st.sidebar.markdown("---")
conversion_type = st.sidebar.radio("👇 Select Conversion Type", ["Length", "Weight", "Temperature", "Time"], index=0)
st.sidebar.markdown("---")

st.markdown("""
     <style>
        .stApp { background-color: #f5f5f5; }
        .stSidebar { background-color: #2d3e50; color: white; }
        .stSidebar div, .stSidebar label { color: white !important; }
        .stButton>button { background-color: #007bff; color: white; border-radius: 10px; padding: 10px; }
        .stTextInput>div>div>input { border-radius: 10px; }
        .stNumberInput>div>div>input { border-radius: 10px; }
        .stSelectbox>div>div>select { border-radius: 10px; }
        .formula-box { background-color: #e3f2fd; padding: 15px; border-radius: 10px; margin-bottom: 15px; font-size: 16px; font-weight: bold; color: #333; text-align: center; border-left: 5px solid #007bff; }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 Google Unit Converter")
st.markdown("---")

def display_formula(formula_text):
    if formula_text:
        st.markdown(f"""
        <div class='formula-box'>
            {formula_text}
        </div>
        """, unsafe_allow_html=True)

if conversion_type == "Length":
    st.subheader("📏 Length Conversion")
    display_formula("Formula: Value × (To Unit / From Unit)")
    value = st.number_input("Enter Value", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
    to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Weight":
    st.subheader("⚖️ Weight Conversion")
    display_formula("Formula: Value × (To Unit / From Unit)")
    value = st.number_input("Enter Value", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Temperature":
    st.subheader("🌡️ Temperature Conversion")
    display_formula("""
        <b>Celsius to Fahrenheit:</b> (Value × 9/5) + 32 <br>
        <b>Fahrenheit to Celsius:</b> (Value - 32) × 5/9 <br>
        <b>Celsius to Kelvin:</b> Value + 273.15
    """)
    value = st.number_input("Enter Value", format="%.2f")
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Time":
    st.subheader("⏳ Time Conversion")
    display_formula("Formula: Value × (To Unit / From Unit)")
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From", ["Seconds", "Minutes", "Hours", "Days"])
    to_unit = st.selectbox("To", ["Seconds", "Minutes", "Hours", "Days"])
    if st.button("Convert"):
        result = convert_time(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
