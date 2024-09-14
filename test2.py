import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu 


st.set_page_config(page_title="NutriTrack" , page_icon="💪🏻")
# Define custom CSS for title styling
custom_css = """
   
    <style>
        .custom-title {
            font-size: 48px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        body {
  background-image: url("https://png.pngtree.com/png-vector/20221217/ourlarge/pngtree-fitness-nutrition-word-concepts-green-banner-logo-wellness-design-vector-png-image_43498198.jpg");
}
    </style>
"""

# Inject the custom CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

# Use HTML to apply the custom CSS class

st.markdown('<div class="custom-title">NutriTrack! 🥗📊</div>', unsafe_allow_html=True)


with st.sidebar:
    selected= option_menu(menu_title= "Main Menu",
                          options=["Home", "Track Yourself", "Deficient", "Excess","About"],
                          icons=["house-fill","person","arrow-down-circle","arrow-up-circle","info-circle"],
                          )
deficiencies =  {
    "Iron": {
        "description": "Essential for the production of hemoglobin, which carries oxygen in the blood. Deficiency can lead to anemia, characterized by reduced red blood cells.",
        "symptoms": ["Fatigue", "Weakness", "Paleness", "Shortness of breath", "Dizziness"],
        "cure_foods": ["Red meat", "Beans", "Lentils", "Spinach"],
        "recommended_daily_intake": "8 mg for men, 18 mg for women (ages 19-50)",
        "food_sources": {
            "Red meat": "Contains heme iron, which is more easily absorbed",
            "Beans": "Rich in non-heme iron, which is less easily absorbed but still beneficial",
            "Lentils": "A good plant-based source of iron",
            "Spinach": "Contains non-heme iron; best absorbed with vitamin C-rich foods"
        },
        "interactions": ["Vitamin C enhances iron absorption", "Calcium can inhibit iron absorption if consumed in high amounts"]
    },
    "Vitamin D": {
        "description": "Important for calcium absorption and bone health. Deficiency can lead to bone pain and muscle weakness, and is linked to a higher risk of chronic diseases.",
        "symptoms": ["Bone pain", "Muscle weakness", "Fatigue", "Depression"],
        "cure_foods": ["Fatty fish", "Fortified dairy products", "Egg yolks"],
        "recommended_daily_intake": "600 IU for adults up to 70 years, 800 IU for those over 70",
        "food_sources": {
            "Fatty fish": "Salmon, mackerel, and sardines are high in vitamin D",
            "Fortified dairy products": "Milk and yogurt often have added vitamin D",
            "Egg yolks": "Contain a modest amount of vitamin D"
        },
        "interactions": ["Magnesium and vitamin K are important for effective vitamin D function"]
    },
    "Vitamin B12": {
        "description": "Essential for nerve function, DNA synthesis, and red blood cell production. Deficiency can cause fatigue, weakness, and neurological issues.",
        "symptoms": ["Fatigue", "Weakness", "Numbness", "Tingling", "Difficulty walking"],
        "cure_foods": ["Meat", "Dairy products", "Eggs", "Fortified cereals"],
        "recommended_daily_intake": "2.4 mcg for adults",
        "food_sources": {
            "Meat": "Beef and chicken are rich sources",
            "Dairy products": "Milk and cheese provide vitamin B12",
            "Eggs": "Egg yolks contain vitamin B12",
            "Fortified cereals": "Cereals fortified with B12 are beneficial for vegetarians"
        },
        "interactions": ["Vitamin B12 absorption can be affected by certain medications, such as proton pump inhibitors"]
    },
    "Calcium": {
        "description": "Crucial for maintaining strong bones and teeth. Deficiency can lead to osteoporosis and increased risk of fractures.",
        "symptoms": ["Bone pain", "Muscle cramps", "Numbness", "Tingling"],
        "cure_foods": ["Dairy products", "Leafy green vegetables", "Fortified plant-based milks"],
        "recommended_daily_intake": "1,000 mg for adults, 1,200 mg for women over 50 and men over 70",
        "food_sources": {
            "Dairy products": "Milk, cheese, and yogurt are high in calcium",
            "Leafy green vegetables": "Kale and bok choy are good sources",
            "Fortified plant-based milks": "Soy and almond milk often have added calcium"
        },
        "interactions": ["Vitamin D enhances calcium absorption", "High sodium intake can increase calcium excretion"]
    },
    "Vitamin C": {
        "description": "Important for immune function, skin health, and antioxidant protection. Deficiency can lead to scurvy, characterized by bleeding gums and poor wound healing.",
        "symptoms": ["Bleeding gums", "Skin rashes", "Fatigue", "Joint pain"],
        "cure_foods": ["Citrus fruits", "Strawberries", "Bell peppers", "Broccoli"],
        "recommended_daily_intake": "90 mg for men, 75 mg for women",
        "food_sources": {
            "Citrus fruits": "Oranges and grapefruits are excellent sources",
            "Strawberries": "High in vitamin C and antioxidants",
            "Bell peppers": "Red bell peppers are particularly rich",
            "Broccoli": "A versatile vegetable high in vitamin C"
        },
        "interactions": ["Vitamin C enhances iron absorption", "High doses of vitamin C may interfere with vitamin B12 absorption"]
    },
    "Vitamin A": {
        "description": "Vital for vision, immune function, and skin health. Deficiency can cause night blindness and increase susceptibility to infections.",
        "symptoms": ["Night blindness", "Dry skin", "Frequent infections"],
        "cure_foods": ["Carrots", "Sweet potatoes", "Spinach", "Kale"],
        "recommended_daily_intake": "900 mcg for men, 700 mcg for women",
        "food_sources": {
            "Carrots": "High in beta-carotene, which the body converts to vitamin A",
            "Sweet potatoes": "A rich source of beta-carotene",
            "Spinach": "Contains both vitamin A and other beneficial nutrients",
            "Kale": "Another good source of beta-carotene"
        },
        "interactions": ["Vitamin A absorption can be affected by low fat intake"]
    },
    "Vitamin E": {
        "description": "Acts as an antioxidant, protecting cells from damage. Deficiency can lead to muscle weakness and vision problems.",
        "symptoms": ["Muscle weakness", "Vision problems", "Immune system problems"],
        "cure_foods": ["Nuts", "Seeds", "Spinach", "Broccoli"],
        "recommended_daily_intake": "15 mg for adults",
        "food_sources": {
            "Nuts": "Almonds and hazelnuts are high in vitamin E",
            "Seeds": "Sunflower seeds are a good source",
            "Spinach": "Provides a moderate amount of vitamin E",
            "Broccoli": "Contains vitamin E and other antioxidants"
        },
        "interactions": ["Vitamin E may enhance the effect of anticoagulant medications"]
    },
    "Vitamin K": {
        "description": "Essential for blood clotting and bone health. Deficiency can lead to excessive bleeding and weakened bones.",
        "symptoms": ["Easy bruising", "Excessive bleeding", "Bone fractures"],
        "cure_foods": ["Leafy green vegetables", "Broccoli", "Brussels sprouts", "Green peas"],
        "recommended_daily_intake": "120 mcg for men, 90 mcg for women",
        "food_sources": {
            "Leafy green vegetables": "Kale and spinach are high in vitamin K",
            "Broccoli": "A versatile vegetable with vitamin K",
            "Brussels sprouts": "Another good source",
            "Green peas": "Contain vitamin K and other nutrients"
        },
        "interactions": ["Vitamin K can interfere with anticoagulant medications"]
    },
    "Folate (Vitamin B9)": {
        "description": "Vital for DNA synthesis and repair. Deficiency can lead to anemia and neural tube defects in pregnancy.",
        "symptoms": ["Fatigue", "Weakness", "Headaches", "Irritability"],
        "cure_foods": ["Leafy green vegetables", "Legumes", "Fortified cereals", "Citrus fruits"],
        "recommended_daily_intake": "400 mcg for adults, 600 mcg for pregnant women",
        "food_sources": {
            "Leafy green vegetables": "Spinach and kale are rich sources",
            "Legumes": "Beans and lentils contain high levels",
            "Fortified cereals": "Often enriched with folate",
            "Citrus fruits": "Oranges and grapefruits provide folate"
        },
        "interactions": ["Vitamin B12 is needed for the proper utilization of folate"]
    },
    "Magnesium": {
        "description": "Important for muscle and nerve function, as well as bone health. Deficiency can cause muscle cramps, fatigue, and other symptoms.",
        "symptoms": ["Muscle cramps", "Fatigue", "Nausea", "Loss of appetite"],
        "cure_foods": ["Nuts", "Seeds", "Whole grains", "Leafy green vegetables"],
        "recommended_daily_intake": "400-420 mg for men, 310-320 mg for women",
        "food_sources": {
            "Nuts": "Almonds and cashews are high in magnesium",
            "Seeds": "Pumpkin and chia seeds provide magnesium",
            "Whole grains": "Brown rice and quinoa are good sources",
            "Leafy green vegetables": "Spinach and Swiss chard are rich in magnesium"
        },
        "interactions": ["Calcium and magnesium compete for absorption in the body"]
    },
    "Zinc": {
        "description": "Essential for immune function, wound healing, and DNA synthesis. Deficiency can impair immune response and wound healing.",
        "symptoms": ["Hair loss", "Delayed wound healing", "Loss of appetite", "Impaired taste"],
        "cure_foods": ["Meat", "Shellfish", "Legumes", "Seeds"],
        "recommended_daily_intake": "11 mg for men, 8 mg for women",
        "food_sources": {
            "Meat": "Beef and lamb are high in zinc",
            "Shellfish": "Oysters and crab provide zinc",
            "Legumes": "Chickpeas and lentils are good sources",
            "Seeds": "Pumpkin and sunflower seeds contain zinc"
        },
        "interactions": ["High doses of zinc can interfere with copper absorption"]
    },
    "Copper": {
        "description": "Helps with iron absorption and the formation of red blood cells. Deficiency can cause anemia and bone abnormalities.",
        "symptoms": ["Anemia", "Fatigue", "Weak bones", "Cold intolerance"],
        "cure_foods": ["Shellfish", "Nuts", "Seeds", "Whole grains"],
        "recommended_daily_intake": "900 mcg for adults",
        "food_sources": {
            "Shellfish": "Oysters and lobster are rich in copper",
            "Nuts": "Cashews and almonds provide copper",
            "Seeds": "Sunflower seeds contain copper",
            "Whole grains": "Brown rice and oats are sources of copper"
        },
        "interactions": ["High zinc intake can inhibit copper absorption"]
    },
    "Selenium": {
        "description": "An antioxidant that helps protect cells from damage. Deficiency can lead to heart disease and immune system dysfunction.",
        "symptoms": ["Fatigue", "Weakness", "Hair loss", "Heart problems"],
        "cure_foods": ["Brazil nuts", "Seafood", "Meat", "Whole grains"],
        "recommended_daily_intake": "55 mcg for adults",
        "food_sources": {
            "Brazil nuts": "Extremely high in selenium",
            "Seafood": "Fish and shellfish contain selenium",
            "Meat": "Beef and poultry provide selenium",
            "Whole grains": "Brown rice and whole wheat products are sources"
        },
        "interactions": ["Excessive selenium can be toxic, affecting liver and kidneys"]
    },
    "Potassium": {
        "description": "Helps maintain fluid balance and proper muscle and nerve function. Deficiency can cause muscle weakness, fatigue, and irregular heartbeat.",
        "symptoms": ["Muscle weakness", "Fatigue", "Irregular heartbeat", "Leg cramps"],
        "cure_foods": ["Bananas", "Potatoes", "Spinach", "Avocados"],
        "recommended_daily_intake": "3,400 mg for men, 2,600 mg for women",
        "food_sources": {
            "Bananas": "A well-known source of potassium",
            "Potatoes": "Especially with skin on",
            "Spinach": "Contains a significant amount of potassium",
            "Avocados": "High in potassium and healthy fats"
        },
        "interactions": ["High sodium intake can exacerbate potassium deficiency"]
    },
    "Iodine": {
        "description": "Essential for thyroid function. Deficiency can lead to goiter and hypothyroidism, which affects metabolism and growth.",
        "symptoms": ["Goiter", "Fatigue", "Weight gain", "Cold intolerance"],
        "cure_foods": ["Iodized salt", "Seafood", "Dairy products", "Eggs"],
        "recommended_daily_intake": "150 mcg for adults",
        "food_sources": {
            "Iodized salt": "An easy way to ensure iodine intake",
            "Seafood": "Fish and seaweed are rich in iodine",
            "Dairy products": "Milk and yogurt contain iodine",
            "Eggs": "Provide a moderate amount of iodine"
        },
        "interactions": ["Excessive intake of iodine can affect thyroid function"]
    },
    "Chromium": {
        "description": "Enhances insulin action and glucose metabolism. Deficiency can lead to insulin resistance and blood sugar imbalances.",
        "symptoms": ["Weight gain", "Insulin resistance", "High blood sugar"],
        "cure_foods": ["Meat", "Whole grains", "Nuts", "Broccoli"],
        "recommended_daily_intake": "35 mcg for men, 25 mcg for women",
        "food_sources": {
            "Meat": "Beef and chicken provide chromium",
            "Whole grains": "Whole wheat and oats contain chromium",
            "Nuts": "Almonds and walnuts are sources",
            "Broccoli": "Contains a small amount of chromium"
        },
        "interactions": ["Chromium supplements may interact with medications for diabetes"]
    },
    "Omega-3 Fatty Acids": {
        "description": "Important for heart health and brain function. Deficiency can lead to dry skin, mood disorders, and increased risk of cardiovascular disease.",
        "symptoms": ["Dry skin", "Fatigue", "Mood swings", "Depression"],
        "cure_foods": ["Fatty fish", "Flaxseeds", "Chia seeds", "Walnuts"],
        "recommended_daily_intake": "250-500 mg of combined EPA and DHA for adults",
        "food_sources": {
            "Fatty fish": "Salmon, mackerel, and sardines are high in omega-3s",
            "Flaxseeds": "A plant-based source of omega-3s",
            "Chia seeds": "Rich in ALA, a type of omega-3",
            "Walnuts": "Contain ALA, supporting heart health"
        },
        "interactions": ["Omega-3s may enhance the effect of blood-thinning medications"]
    },
    "Manganese": {
        "description": "Involved in bone formation, metabolism, and antioxidant defense. Deficiency can lead to bone deformities and impaired growth.",
        "symptoms": ["Bone deformities", "Poor growth", "Skin rashes"],
        "cure_foods": ["Whole grains", "Nuts", "Leafy green vegetables", "Tea"],
        "recommended_daily_intake": "2.3 mg for men, 1.8 mg for women",
        "food_sources": {
            "Whole grains": "Brown rice and oats are good sources",
            "Nuts": "Almonds and pecans contain manganese",
            "Leafy green vegetables": "Spinach and kale are rich in manganese",
            "Tea": "Especially black and green teas"
        },
        "interactions": ["High levels of manganese can interfere with iron absorption"]
    },
    "Choline": {
        "description": "Important for liver function, brain development, and muscle movement. Deficiency can lead to liver damage and cognitive issues.",
        "symptoms": ["Liver damage", "Memory issues", "Fatigue"],
        "cure_foods": ["Eggs", "Meat", "Fish", "Brussels sprouts"],
        "recommended_daily_intake": "550 mg for men, 425 mg for women",
        "food_sources": {
            "Eggs": "One of the best sources of choline",
            "Meat": "Chicken and beef contain choline",
            "Fish": "Salmon and cod are rich in choline",
            "Brussels sprouts": "Contain a moderate amount of choline"
        },
        "interactions": ["Choline is involved in the synthesis of acetylcholine, which can affect neurotransmitter balance"]
    },
    "Vitamin B6": {
        "description": "Important for protein metabolism, cognitive function, and the production of neurotransmitters. Deficiency can cause anemia and neurological symptoms.",
        "symptoms": ["Anemia", "Depression", "Confusion", "Irritability"],
        "cure_foods": ["Poultry", "Fish", "Bananas", "Potatoes"],
        "recommended_daily_intake": "1.3-2.0 mg depending on age and sex",
        "food_sources": {
            "Poultry": "Chicken and turkey are good sources",
            "Fish": "Salmon and tuna contain vitamin B6",
            "Bananas": "Rich in vitamin B6 and other beneficial nutrients",
            "Potatoes": "Contain a good amount of vitamin B6"
        },
        "interactions": ["Vitamin B6 can interact with certain medications, such as those used for Parkinson’s disease"]
    },
    "Vitamin B3 (Niacin)": {
        "description": "Aids in energy production and DNA repair. Deficiency can cause pellagra, characterized by dermatitis, diarrhea, and dementia.",
        "symptoms": ["Dermatitis", "Diarrhea", "Dementia"],
        "cure_foods": ["Poultry", "Fish", "Whole grains", "Legumes"],
        "recommended_daily_intake": "16 mg for men, 14 mg for women",
        "food_sources": {
            "Poultry": "Chicken and turkey provide niacin",
            "Fish": "Tuna and salmon are good sources",
            "Whole grains": "Brown rice and whole wheat contain niacin",
            "Legumes": "Beans and lentils offer niacin"
        },
        "interactions": ["High doses of niacin can affect liver function and blood sugar levels"]
    },
    "Vitamin B5 (Pantothenic Acid)": {
        "description": "Essential for the synthesis of coenzyme A, which is involved in energy metabolism. Deficiency can cause fatigue and digestive issues.",
        "symptoms": ["Fatigue", "Digestive issues", "Irritability"],
        "cure_foods": ["Eggs", "Avocados", "Whole grains", "Legumes"],
        "recommended_daily_intake": "5 mg for adults",
        "food_sources": {
            "Eggs": "Rich in pantothenic acid",
            "Avocados": "Contain a good amount of vitamin B5",
            "Whole grains": "Brown rice and oats provide pantothenic acid",
            "Legumes": "Beans and lentils are sources"
        },
        "interactions": ["Pantothenic acid is involved in the synthesis of neurotransmitters, which can affect mood and cognitive function"]
    },
    "Vitamin B2 (Riboflavin)": {
        "description": "Important for energy production and cellular function. Deficiency can cause sore throat, redness and cracks on the outsides of the lips, and at the corners of the mouth.",
        "symptoms": ["Sore throat", "Cracks on lips", "Redness on the tongue", "Swollen throat"],
        "cure_foods": ["Dairy products", "Eggs", "Lean meats", "Green leafy vegetables"],
        "recommended_daily_intake": "1.3 mg for men, 1.1 mg for women",
        "food_sources": {
            "Dairy products": "Milk and yogurt are high in riboflavin",
            "Eggs": "Contain a good amount of riboflavin",
            "Lean meats": "Beef and pork provide riboflavin",
            "Green leafy vegetables": "Spinach and broccoli are sources"
        },
        "interactions": ["Riboflavin is involved in the metabolism of other B vitamins, affecting overall nutrient balance"]
    }
}

def search_deficiency(query):
    for key in deficiencies:
        if query.lower() in key.lower():
            return key
    return None

if selected == "Home":
    st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background: rgba(255, 255, 255, 0.9);
    }
    </style>
    """, unsafe_allow_html=True)

    # Add a welcome image
    image_url = "https://png.pngtree.com/png-vector/20221217/ourlarge/pngtree-fitness-nutrition-word-concepts-green-banner-logo-wellness-design-vector-png-image_43498198.jpg"
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="{image_url}" width="1000" style="border-radius: 8px;" />
        </div>
    """, unsafe_allow_html=True)
    st.title("Welcome to our Nutrition and Macros Tracker!")
    st.write("""
    Welcome to our Nutrition Tracker System! 🥗📊

    Our mission is to help you monitor and improve your nutritional intake efficiently. Input your food items, and our system will analyze it to track nutritional information and provide personalized recommendations. Let's work together to achieve a balanced and healthier diet!

    ### How It Works
    1. **Logging Data:** Go to the **Track Yourself** section and enter the data required.
    2. **Analysis:** Our system will process your input using advanced algorithms to identify your nutritional information and assess your overall macros.
    3. **Results:** View detailed results and receive tailored recommendations to enhance your nutritional balance.

    ### Why Choose Us?
    - **Precision:** Our system employs advanced data analysis techniques for accurate nutrition tracking.
    - **User-Friendly:** Intuitive and straightforward interface for a seamless experience.
    - **Fast and Effective:** Get actionable insights and recommendations quickly to make informed dietary choices.

    ### Get Started
    Click on the **Track Yourself** section in the sidebar to input your daily diet and discover how our Nutrition Tracker System can help you achieve a healthier lifestyle!

    ### About Us
    Learn more about our project, understand our mission, and meet our team in the **About** section.

    """)


elif selected == "Track Yourself":
    option = st.sidebar.radio("Select an option", ["Know YourTake", "Log Food"])

    # Display different interfaces based on the selected option
    if option == "Log Food":
        food_data = {
            # Fruits
            "Apple": {"Carbohydrates": 25, "Protein": 0.5, "Fat": 0.3},
            "Banana": {"Carbohydrates": 27, "Protein": 1.3, "Fat": 0.3},
            "Orange": {"Carbohydrates": 12, "Protein": 0.9, "Fat": 0.1},
            "Strawberry": {"Carbohydrates": 7.7, "Protein": 0.7, "Fat": 0.3},
            "Blueberry": {"Carbohydrates": 14, "Protein": 0.7, "Fat": 0.3},
            "Grapes": {"Carbohydrates": 17, "Protein": 0.7, "Fat": 0.2},
            "Pineapple": {"Carbohydrates": 13, "Protein": 0.5, "Fat": 0.1},
            "Mango": {"Carbohydrates": 15, "Protein": 0.8, "Fat": 0.4},
            "Kiwi": {"Carbohydrates": 15, "Protein": 1.1, "Fat": 0.5},
            "Watermelon": {"Carbohydrates": 8, "Protein": 0.6, "Fat": 0.2},
            "Pear": {"Carbohydrates": 15, "Protein": 0.4, "Fat": 0.2},
            "Peach": {"Carbohydrates": 10, "Protein": 0.9, "Fat": 0.3},
            "Grapefruit": {"Carbohydrates": 9, "Protein": 0.8, "Fat": 0.1},
            "Cherry": {"Carbohydrates": 16, "Protein": 1, "Fat": 0.2},
            "Plum": {"Carbohydrates": 11, "Protein": 0.5, "Fat": 0.3},
    
            # Vegetables
            "Broccoli": {"Carbohydrates": 7, "Protein": 2.8, "Fat": 0.4},
            "Spinach": {"Carbohydrates": 3.6, "Protein": 2.9, "Fat": 0.4},
            "Carrot": {"Carbohydrates": 10, "Protein": 0.9, "Fat": 0.2},
            "Bell Pepper": {"Carbohydrates": 6, "Protein": 1, "Fat": 0.3},
            "Tomato": {"Carbohydrates": 3.9, "Protein": 0.9, "Fat": 0.2},
            "Cucumber": {"Carbohydrates": 3.6, "Protein": 0.7, "Fat": 0.1},
            "Cauliflower": {"Carbohydrates": 5, "Protein": 1.9, "Fat": 0.3},
            "Zucchini": {"Carbohydrates": 3.1, "Protein": 1.2, "Fat": 0.3},
            "Kale": {"Carbohydrates": 8, "Protein": 2.9, "Fat": 0.9},
            "Sweet Potato": {"Carbohydrates": 20.7, "Protein": 1.6, "Fat": 0.1},
            "Brussels Sprouts": {"Carbohydrates": 9, "Protein": 3.4, "Fat": 0.3},
            "Green Beans": {"Carbohydrates": 7, "Protein": 1.8, "Fat": 0.2},
            "Asparagus": {"Carbohydrates": 3.7, "Protein": 2.2, "Fat": 0.2},
            "Onion": {"Carbohydrates": 9, "Protein": 1.1, "Fat": 0.1},
            "Garlic": {"Carbohydrates": 33, "Protein": 6.4, "Fat": 0.5},
    
            # General Food Items
            "Chicken Breast": {"Carbohydrates": 0, "Protein": 31, "Fat": 3.6},
            "Almonds": {"Carbohydrates": 22, "Protein": 21, "Fat": 49},
            "Oats": {"Carbohydrates": 66, "Protein": 16.9, "Fat": 6.9},
            "Egg": {"Carbohydrates": 1.1, "Protein": 13, "Fat": 10.6},
            "Salmon": {"Carbohydrates": 0, "Protein": 20, "Fat": 13},
            "Quinoa": {"Carbohydrates": 21, "Protein": 4.1, "Fat": 1.9},
            "Greek Yogurt": {"Carbohydrates": 3.6, "Protein": 10, "Fat": 0.4},
            "Tofu": {"Carbohydrates": 1.9, "Protein": 8, "Fat": 4.8},
            "Peanuts": {"Carbohydrates": 16.1, "Protein": 25.8, "Fat": 49.2},
            "Avocado": {"Carbohydrates": 8.5, "Protein": 2, "Fat": 15},
            "Chia Seeds": {"Carbohydrates": 42, "Protein": 16.5, "Fat": 30.7},
            "Cheddar Cheese": {"Carbohydrates": 1.3, "Protein": 25, "Fat": 33},
            "Turkey Breast": {"Carbohydrates": 0, "Protein": 29, "Fat": 1},
            "Lentils": {"Carbohydrates": 20, "Protein": 9, "Fat": 0.4},
            "Pistachios": {"Carbohydrates": 28, "Protein": 20, "Fat": 45},
            "Beef Steak": {"Carbohydrates": 0, "Protein": 26, "Fat": 20},
            "Cottage Cheese": {"Carbohydrates": 3.4, "Protein": 11, "Fat": 4.3},
            "Brown Rice": {"Carbohydrates": 77, "Protein": 7.5, "Fat": 2.7},
            "Whole Wheat Bread": {"Carbohydrates": 41, "Protein": 13, "Fat": 3.4},
            "Pasta": {"Carbohydrates": 71, "Protein": 12, "Fat": 1.1},
            "Mushrooms": {"Carbohydrates": 3.3, "Protein": 3.1, "Fat": 0.3},
            "Pork Chop": {"Carbohydrates": 0, "Protein": 26, "Fat": 21},
            "Shrimp": {"Carbohydrates": 0.2, "Protein": 24, "Fat": 0.3},
            "Hummus": {"Carbohydrates": 14, "Protein": 8, "Fat": 6.5},
            "Couscous": {"Carbohydrates": 23, "Protein": 3.6, "Fat": 0.2},
            "Edamame": {"Carbohydrates": 9, "Protein": 11, "Fat": 5},
            "Beetroot": {"Carbohydrates": 10, "Protein": 1.6, "Fat": 0.2},
            "Seaweed": {"Carbohydrates": 9, "Protein": 1.5, "Fat": 0.6}
        }

        # Initialize session state to store logged items
        if 'logged_items' not in st.session_state:
            st.session_state.logged_items = []

        # Function to add a food item to the logged list
        def add_food_item(name):
            if name in food_data:
                st.session_state.logged_items.append(food_data[name])
                st.success(f"Added {name} to the list!")

        # Create a Streamlit selectbox for choosing a food item
        st.title("Food Macros Logger")
        selected_food = st.selectbox("Select a food item", list(food_data.keys()))

        # Add the selected food item to the logged list
        if st.button("Add to List"):
            add_food_item(selected_food)

        # Display logged food items
        if st.session_state.logged_items:
            df = pd.DataFrame(st.session_state.logged_items)
    
            st.subheader("Logged Food Items")
            st.dataframe(df)
    
            # Calculate total macros
            total_macros = df.sum()
    
            # Create a pie chart of total macros
            st.subheader("Total Macronutrient Distribution")
            fig, ax = plt.subplots()
            labels = total_macros.index
            sizes = total_macros.values
            colors = ['#ff9999','#66b3ff','#99ff99']
    
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
            ax.set_title("Total Macronutrient Distribution")
            st.pyplot(fig)
        else:
            st.write("No food items logged yet.")

    elif option == "Know YourTake":
        age = st.number_input('Enter your age:', min_value=0, max_value=120, value=0)
        height = st.number_input('Enter your height (cm):', min_value=30, max_value=250, value=30)
        weight = st.number_input('Enter your weight (kg):', min_value=30, max_value=300, value=30)
        gender = st.radio("Gender", ("Male", "Female"))
        activity_level = st.selectbox(
            "Activity Level",
            [
                "Sedentary (little or no exercise)",
                "Lightly active (light exercise/sports 1-3 days/week)",
                "Moderately active (moderate exercise/sports 3-5 days/week)",
                "Very active (hard exercise/sports 6-7 days a week)",
                "Super active (very hard exercise/sports and a physical job)"
            ]
        )

        if st.button('Show Results'):
            def calculate_bmr(weight, height, age, gender):
                if gender == "Male":
                    return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
                else:
                    return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

            # Function to calculate maintenance calories based on activity level
            def calculate_maintenance_calories(bmr, activity_level):
                activity_factors = {
                    "Sedentary (little or no exercise)": 1.2,
                    "Lightly active (light exercise/sports 1-3 days/week)": 1.375,
                    "Moderately active (moderate exercise/sports 3-5 days/week)": 1.55,
                    "Very active (hard exercise/sports 6-7 days a week)": 1.725,
                    "Super active (very hard exercise/sports and a physical job)": 1.9
                }
                return bmr * activity_factors[activity_level]

            # Calculate BMR and maintenance calories
            bmr = calculate_bmr(weight, height, age, gender)
            maintenance_calories = calculate_maintenance_calories(bmr, activity_level)

            # Display results
            st.header("Your Results")
            st.write(f"Basal Metabolic Rate (BMR): **{bmr:.2f}** calories/day")
            st.write(f"Maintenance Calories: **{maintenance_calories:.2f}** calories/day")

            def calculate_bmi(height, weight):
                height_m = height / 100
                bmi = weight / (height_m ** 2)
                return bmi

            bmi = calculate_bmi(height, weight)
            st.markdown(f'Your BMI is: **{bmi:.2f}**')
    
            if bmi < 18.5:
                st.markdown("<p style='color: aqua;'>You are classified as underweight.</p>", unsafe_allow_html=True)
            elif 18.5 <= bmi < 24.9:
                st.markdown("<p style='color: greenyellow;'>You have a normal weight.</p>", unsafe_allow_html=True)
            elif 25 <= bmi < 29.9:
                st.markdown("<p style='color: darkorange;'>You are classified as overweight.</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p style='color: red;'>You are classified as obese.</p>", unsafe_allow_html=True)
        
            # Optionally, add a download button for results
            st.download_button(
                label="Download Results",
                data=f"Basal Metabolic Rate: {bmr:.2f} calories/day\nMaintenance Calories: {maintenance_calories:.2f} calories/day\nBMI: {bmi:.2f}",
                file_name="calorie_results.txt",
                mime="text/plain"
            )

elif selected == "Deficient":
    st.title("Common Nutritional Deficiencies")

    # Search box for deficiencies page
    search_term_def = st.text_input("Search for a deficiency:", "")

    if search_term_def:
        # Find matching deficiency
        matched_deficiency = search_deficiency(search_term_def)
        
        if matched_deficiency:
            details = deficiencies[matched_deficiency]
            st.subheader(matched_deficiency)
            st.write("### Description")
            st.write(details["description"])
            st.write("### Symptoms")
            for symptom in details["symptoms"]:
                st.write(f"- {symptom}")
            st.write("### Foods rich in this nutrient:")
            for food in details["cure_foods"]:
                st.write(f"- {food}")
            st.write("### Recommended Daily Intake")
            st.write((details["recommended_daily_intake"]))
            st.write("### Food Sources")
            for food, description in details["food_sources"].items():
                st.write(f"- **{food}**: {description}")
            st.write("### Interactions")
            for interaction in details["interactions"]:
                st.write(f"- {interaction}")
        else:
            st.write("No results found. Try searching for a different term.")
    else:
        st.write("Enter a nutrient name to search for its details.")
if selected == "Excess":
    st.title("Search for Foods low in Nutrients")

    # Nutrient-rich foods
    rich_foods = {
     "Iron": [
        "White rice", "Pasta", "White bread", "Apples", "Potatoes", "Cucumbers", "Bell peppers", 
        "Lettuce", "Green beans", "Carrots", "Peaches", "Strawberries"
    ],
    "Vitamin D": [
        "Non-fortified milk", "Cheddar cheese", "Bananas", "Cucumbers", "Rice cakes", "Oatmeal", 
        "Apples", "Pasta", "Peppers", "Tomatoes", "Lettuce", "Spinach"
    ],
    "Vitamin B12": [
        "Apples", "Carrots", "Almonds", "Chia seeds", "Potatoes", "Peas", "Mangoes", "Zucchini", 
        "Squash", "Cabbage", "Cucumber", "Bell peppers"
    ],
    "Calcium": [
        "Beef", "Chicken eggs", "Oranges", "Bell peppers", "Pork", "Lamb", "Rice", "Pasta", 
        "Apples", "Avocado", "Sweet potatoes", "Corn"
    ],
    "Vitamin C": [
        "White rice", "Pasta", "Chicken", "Cheese", "Pork", "Beef", "Potatoes", "Eggs", 
        "Onions", "Cucumber", "Cauliflower", "Romaine lettuce"
    ],
    "Vitamin A": [
        "Pork", "Tuna", "Chicken eggs", "Milk", "Turkey", "Lamb", "White rice", "Pasta", 
        "Potatoes", "Mushrooms", "Apples", "Peppers"
    ],
    "Vitamin E": [
        "Pork", "Eggs", "Cheddar cheese", "Apples", "Potatoes", "Rice", "White bread", "Chicken", 
        "Cucumbers", "Tomatoes", "Peas", "Bell peppers"
    ],
    "Vitamin K": [
        "Apples", "White rice", "White bread", "Chicken", "Beef", "Eggs", "Potatoes", "Corn", 
        "Peppers", "Cucumber", "Rice cakes", "Bananas"
    ],
    "Folate (Vitamin B9)": [
        "Beef", "Cheese", "Oranges", "Potatoes", "Apples", "Pasta", "Rice", "Chicken", 
        "Zucchini", "Peas", "Cabbage", "Carrots"
    ],
    "Magnesium": [
        "White rice", "Pasta", "Chicken", "Eggs", "Potatoes", "Corn", "Apples", "Peas", 
        "Bell peppers", "Tomatoes", "Cucumber", "Squash"
    ],
    "Zinc": [
        "Apples", "Cucumbers", "Cheddar cheese", "Chicken", "Potatoes", "Rice", "Pasta", "Peppers", 
        "Onions", "Tomatoes", "Squash", "Carrots"
    ],
    "Copper": [
        "Beef", "Cheddar cheese", "Apples", "Carrots", "Potatoes", "Rice", "Chicken", "Peas", 
        "Squash", "Tomatoes", "Bell peppers", "Cauliflower"
    ],
    "Selenium": [
        "White rice", "Bananas", "Cucumbers", "Chicken", "Potatoes", "Corn", "Peas", "Apples", 
        "Tomatoes", "Squash", "Bell peppers", "Lettuce"
    ],
    "Potassium": [
        "Bananas", "White rice", "Pasta", "Chicken", "Apples", "Potatoes", "Corn", "Peas", 
        "Bell peppers", "Tomatoes", "Carrots", "Cucumbers"
    ],
    "Iodine": [
        "Beef", "Bananas", "Cucumbers", "Eggs", "Apples", "Potatoes", "Corn", "Peas", 
        "Bell peppers", "Tomatoes", "Carrots", "Lettuce"
    ],
    "Chromium": [
        "White rice", "Pasta", "Bananas", "Cucumbers", "Potatoes", "Corn", "Apples", "Peas", 
        "Bell peppers", "Tomatoes", "Carrots", "Chicken"
    ],
    "Omega-3 Fatty Acids": [
        "Beef", "Eggs", "Apples", "Bell peppers", "Potatoes", "Rice", "Corn", "Peas", 
        "Chicken", "Tomatoes", "Carrots", "Cucumbers"
    ],
    "Manganese": [
        "White rice", "Pasta", "Chicken", "Eggs", "Potatoes", "Corn", "Apples", "Peas", 
        "Bell peppers", "Tomatoes", "Carrots", "Cucumbers"
    ],
    "Choline": [
        "Beef", "Bananas", "Cucumbers", "Eggs", "Apples", "Potatoes", "Corn", "Peas", 
        "Bell peppers", "Tomatoes", "Carrots", "Chicken"
    ],
    "Vitamin B6": [
        "Bananas", "Cucumbers", "White rice", "Pasta", "Potatoes", "Corn", "Peas", "Apples", 
        "Bell peppers", "Tomatoes", "Carrots", "Chicken"
    ],
    "Vitamin B3 (Niacin)": [
        "Bananas", "Cucumbers", "Beef", "Eggs", "Potatoes", "Corn", "Rice", "Peas", 
        "Bell peppers", "Tomatoes", "Carrots", "Chicken"
    ],
    "Vitamin B5 (Pantothenic Acid)": [
        "Beef", "Bananas", "Cucumbers", "Eggs", "Potatoes", "Corn", "Rice", "Peas", 
        "Bell peppers", "Tomatoes", "Carrots", "Chicken"
    ],
    "Calories": [
        "Apples", "Bell peppers", "White rice", "Pasta", "Potatoes", "Corn", "Peas", 
        "Cucumbers", "Tomatoes", "Carrots", "Chicken", "Beef"
    ],
    "Carbohydrates": [
        "Beef", "Eggs", "Apples", "Bell peppers", "Potatoes", "Rice", "Corn", "Peas", 
        "Cucumbers", "Tomatoes", "Carrots", "Chicken"
    ],
    "Protein": [
        "White rice", "Bananas", "Bell peppers", "Pasta", "Potatoes", "Corn", "Peas", 
        "Cucumbers", "Tomatoes", "Carrots", "Chicken", "Beef"
    ],
    "Fat": [
        "Apples", "White rice", "Bell peppers", "Pasta", "Potatoes", "Corn", "Peas", 
        "Cucumbers", "Tomatoes", "Carrots", "Chicken", "Beef"
    ],
    "Sugar": [
        "White rice", "Apples", "Bell peppers", "Pasta", "Potatoes", "Corn", "Peas", 
        "Cucumbers", "Tomatoes", "Carrots", "Chicken", "Beef"
    ],
    "Cholesterol": [
        "Apples", "Bell peppers", "White rice", "Pasta", "Potatoes", "Corn", "Peas", 
        "Cucumbers", "Tomatoes", "Carrots", "Rice cakes", "Oatmeal"
    ],
    
    # Additional nutrients
    "Vitamin B1 (Thiamine)": [
        "White rice", "Pasta", "Potatoes", "Apples", "Bananas", "Cucumbers", "Carrots", 
        "Peas", "Bell peppers", "Tomatoes", "Chicken", "Beef"
    ],
    "Vitamin B2 (Riboflavin)": [
        "White rice", "Pasta", "Potatoes", "Apples", "Bananas", "Cucumbers", "Carrots", 
        "Peas", "Bell peppers", "Tomatoes", "Chicken", "Beef"
    ],
    "Vitamin B7 (Biotin)": [
        "White rice", "Pasta", "Potatoes", "Apples", "Bananas", "Cucumbers", "Carrots", 
        "Peas", "Bell peppers", "Tomatoes", "Chicken", "Beef"
    ],
    "Vitamin B8 (Inositol)": [
        "White rice", "Pasta", "Potatoes", "Apples", "Bananas", "Cucumbers", "Carrots", 
        "Peas", "Bell peppers", "Tomatoes", "Chicken", "Beef"
    ],
    "Sodium": [
        "Fresh fruits like apples and bananas", "Vegetables like cucumbers and carrots", 
        "Rice", "Pasta", "Potatoes", "Bell peppers", "Tomatoes", "Chicken (fresh, not processed)", 
        "Beef (fresh, not processed)"
    ],
    "Fiber": [
        "Meat (beef, chicken)", "Cheese", "Eggs", "Refined grains (white rice, pasta)", 
        "Potatoes (without skin)", "Bananas", "Apples (without skin)", "Cucumbers", 
        "Bell peppers", "Tomatoes", "Carrots", "Peas"
    ],
    "Phosphorus": [
        "Fresh fruits like apples and bananas", "Vegetables like cucumbers and carrots", 
        "White rice", "Pasta", "Potatoes", "Bell peppers", "Tomatoes", "Chicken (fresh, not processed)", 
        "Beef (fresh, not processed)"
    ],
    "Molybdenum": [
        "White rice", "Pasta", "Potatoes", "Apples", "Bananas", "Cucumbers", "Carrots", 
        "Peas", "Bell peppers", "Tomatoes", "Chicken", "Beef"
    ]
}
    # Search box for rich foods page
    search_term_rich = st.text_input("Search for low in nutrient Foods:")

    # Display results based on the search term
    if search_term_rich:
        filtered_rich_foods = {k: v for k, v in rich_foods.items() if search_term_rich.lower() in k.lower()}
        
        if filtered_rich_foods:
            for nutrient, foods in filtered_rich_foods.items():
                st.subheader(f"Foods low in {nutrient}")
                for food in foods:
                    st.write(f"- {food}")
        else:
            st.write("No results found. Try searching for a different term.")
    else:
        st.write("Please enter a nutrient to search for.")


elif selected == "About":
    st.title("About Our Website")
    st.write("""
    **NutriTrack** is a comprehensive online platform designed to empower users with personalized nutritional information. By simply entering details about themselves and the foods they consume, users receive tailored insights into the nutritional value, including calories and macronutrients. NutriTrack combines an intuitive interface with a robust database of foods to offer accurate and up-to-date information, helping users make informed dietary choices and achieve their health goals.

    ### Our Mission
    Our mission at NutriTrack is to make nutrition accessible and understandable for everyone. We are dedicated to providing accurate, personalized nutritional information that helps individuals lead healthier lives. By simplifying the complexities of food data and offering actionable insights, we aim to support our users in making informed decisions about their diet and wellness. At NutriTrack, we believe that knowledge is the first step towards a healthier lifestyle, and we are committed to being a trusted resource in that journey.
    
    ### Our Team
    """)
    ### Our Team
    team_members = [
        {
            "name": "Himanshu Singh",
            "url": "https://cdn3.iconfinder.com/data/icons/letters-and-numbers-1/32/letter_H_blue-512.png",
            "instagram": "https://instagram.com/__himans.hu_",
            "github": "https://github.com/himanshusinghhls"
        },
        {
            "name": "Omkar Mishra",
            "url": "https://cdn3.iconfinder.com/data/icons/letters-and-numbers-1/32/letter_O_blue-1024.png",
            "instagram": "https://instagram.com/om.ish_ra",
            "github": "https://github.com/OmkarMishra07"
        },
        {
            "name": "Prince Raj",
            "url": "https://cdn3.iconfinder.com/data/icons/letters-and-numbers-1/32/letter_P_blue-1024.png",
            "instagram": "https://instagram.com/geet_prince07",
            "github": "https://github.com/Geet-Prince"
        }
    ]

    # Display team members
    for member in team_members:
        # Create a container for each team member
        with st.container():
            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(member["url"], width=150)

            with col2:
                st.subheader(member["name"])
                st.write(f"**Social links:**")
                st.markdown(f"[Instagram]({member['instagram']}) | [GitHub]({member['github']})")

            st.markdown("---")

