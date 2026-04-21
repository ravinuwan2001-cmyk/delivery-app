import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Nippon Paint Logistics", page_icon="📦")

st.title("📊 මාසික බෙදාහැරීම් සහ ගබඩා සැලසුම් පෝරමය")

# සේවක දත්ත (EPF: Name)
employee_map = {
    "2500": "R.G.I.K.RAJAPAKSHA", "2878": "H.M.W KUMARA", "3446": "P.B.INDIKA BANDARAWATTE",
    "4225": "M.S.B RATHNAYAKA", "4346": "P.A.RANJITH RUPASINGHE", "4384": "S.K.G.V.KURUPPU",
    "4542": "K.A.SAMAN PRIYANTHA", "4654": "B.M.A. PERERA", "4935": "W.M.T.B.WEERASEKARA",
    "5002": "H.B.D.CHAMPIKA", "1232": "M.D.VIPULA SISIRA KUMARA", "2655": "L.S SISIRA KUMARA",
    "2822": "R.G.A.U KUMARA", "3557": "A.P.S.SILVA", "5070": "V.A.SUSANTHA DILSHAN",
    "5326": "A.A.JEEWAN JANAKA HERATH", "5354": "R.M.S. PRASANNA BANDARA RATHNAYAKE",
    "5449": "A.A.VIMUKTHI LAKSHAN AMARASIGHE", "5484": "K.A.NUWANTHA MANUSHALYA",
    "5540": "A.M.NAMAL", "5605": "S.P.RANJITH SENARATHNE", "5606": "E.M.A.D.B.EKANAYAKE",
    "5607": "W.M.SURESH HARSHANA WIJENAYAKA", "15003": "S.L.A.PRASAD NIROSHANA ARAVINDA",
    "15060": "D.M.T.D.DISSANAYAKE", "15061": "R.P.P.M.PATHIRANA", "15079": "W.M.P.K.WEERASINGHE",
    "15082": "R.M.D.S.RATHNAYAKE", "15093": "P.G.M.N.PALLEWELA", "15095": "T.M.S.D.THENNAKOON",
    "15096": "M.G.S.PRIYANKARA", "15124": "K.M.S.K.KONARA", "15125": "M.M.R.S.B.MARASINGHE",
    "15126": "D.M.P.L.DISSANAYAKE", "15127": "P.M.A.S.K.PATHIRAJA", "15128": "E.M.N.M.EKANAYAKE",
    "15129": "W.P.A.M.PATHIRANA", "15130": "H.M.K.L.HERATH", "15131": "G.M.S.S.B.GANEGODA",
    "15147": "W.M.N.S.WIJETHUNGA", "15152": "P.G.K.C.PRIYADARSHANA", "15155": "M.R.C.M.KUMARA",
    "15156": "W.M.C.N.WEERASEKARA", "15157": "H.M.I.G.B.HERATH"
}

data_file = "responses.csv"

with st.form("my_form", clear_on_submit=True):
    epf = st.text_input("ඔබේ EPF අංකය ඇතුළත් කරන්න:").strip()
    name = employee_map.get(epf, "")
    
    if epf:
        if name: st.success(f"නම: {name}")
        else: st.warning("EPF අංකය ලැයිස්තුවේ නැත.")
    
    q_name = st.text_input("සම්පූර්ණ නම:", value=name)
    
    st.divider()
    
    q1 = st.selectbox("1. ඉදිරි මාසය සඳහා Delivery යාමට වඩාත්ම පහසු ආකාරය?", 
                      ["හැමදාම Delivery යා හැකී", "සතියේ දින 4ක් Delivery යා හැකී", 
                       "අවශ්‍යනම් කළමනාකරණාකාර තුමා දැනුවත් කරනවා", "හදිසි අවස්තා වල පමණක් යා හැකි"])
    
    q2 = st.text_input("2. ඉදිරි මාසය තුළ ලබා ගැනීමට බලාපොරොත්තු වන නිවාඩු දින මොනවාද?")
    
    q3 = st.text_area("3. Delivery යාමේදී නිතර ගැටලු ඇතිවන මාර්ග හෝ ස්ථාන තිබේද?")
    
    q4 = st.text_input("4. පෞද්ගලික හේතූන් මත Delivery යා නොහැකි ප්‍රදේශ මොනවාද?")
    
    q5 = st.text_area("5. ගබඩාව තුළ භාණ්ඩ හානි වීම් (Damages) අවම කිරීමට ඔබේ යෝජනා මොනවාද?")
    
    q6 = st.text_area("6. ගබඩා තුල සිදු කරන කාර්යයන් වඩාත් ඵලදායීව සහා ඉක්මනින් කිරීමට ඇති ඔබගේ යෝජනා:")
    
    submit = st.form_submit_button("Submit කරන්න")

if submit:
    if epf and q_name:
        new_data = pd.DataFrame([{
            "Date": datetime.now().strftime("%Y-%m-%d"), 
            "EPF": epf, 
            "Name": q_name, 
            "Q1_Delivery": q1, 
            "Q2_Holidays": q2, 
            "Q3_Route_Issues": q3, 
            "Q4_Restricted_Areas": q4,
            "Q5_Damage_Suggestions": q5,
            "Q6_Efficiency_Suggestions": q6
        }])
        new_data.to_csv(data_file, mode='a', header=not os.path.exists(data_file), index=False)
        st.balloons()
        st.success("දත්ත සාර්ථකව යොමු කළා!")
    else:
        st.error("කරුණාකර EPF අංකය සහ නම ඇතුළත් කරන්න.")

# Admin Only Section with Password Protection
st.divider()
if st.checkbox("දත්ත පරීක්ෂා කරන්න (Admin Only)"):
    # Password input field
    admin_password = st.text_input("Admin Password එක ඇතුළත් කරන්න:", type="password")
    
    if admin_password == "Kurunegala@nplk":
        st.success("Access Granted!")
        if os.path.exists(data_file): 
            st.dataframe(pd.read_csv(data_file))
        else:
            st.info("තවම දත්ත කිසිවක් ඇතුළත් කර නොමැත.")
    elif admin_password != "":
        st.error("Password එක වැරදියි! කරුණාකර නැවත උත්සාහ කරන්න.")
