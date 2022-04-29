from PIL import Image
import streamlit as st
import time
from page_content import _Home, Init_sidebar
from page_content import _Test
from page_content import Init_tabs, _CV


#----------------------------------------------------------------#
## Déclaration des variables de travail
#----------------------------------------------------------------#
query_params = st.experimental_get_query_params()
tabs = ["Home", "Présentation", "Histoire", "CV", "st_Test"]
img = Image.open('bender.png')

#----------------------------------------------------------------#
## Déclaration du side bar
#----------------------------------------------------------------#
## active_tab = Variable courante pour le changement de page 
## Init_sidebar = fonction de chargement de la sidebar
#       a chaque chargement de page 
active_tab = Init_sidebar(query_params, tabs, img)

#----------------------------------------------------------------#
## Initialisation des tabs
#----------------------------------------------------------------#
# active_tab = Init_tabs(query_params, tabs)

#----------------------------------------------------------------#
## Mise en route
#----------------------------------------------------------------#
if active_tab == "Home":
    _Home(active_tab)

if active_tab == "st_Test":
    _Test(active_tab, st.sidebar)

if active_tab == "CV":
    _CV(active_tab, st.sidebar)








