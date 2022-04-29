from PIL import Image
import streamlit as st
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

#----------------------------------------------------------------#
## Déclaration des variables de travail
#----------------------------------------------------------------#
## variable pour le calcul du scors
##  peut être importer du fichier stProject pour eviter de 
##  surcharger la pag 
mean = 0 
std = 1
# on defini l'interval de travail pour le plot (xminp = xmin_plot..)
xl = np.linspace(-std*3.8, std*3.8, 100)
# établissement de la loi de probabilité
# peut etre placé en argument d'entrée 
## y1 distribution gaussienne
y1 = scipy.stats.norm.pdf(xl, loc=mean, scale=std)
## y2 distribution de type x^3 (?) 
y2 = scipy.stats.norm.cdf(xl,loc=0,scale=1)
#----------------------------------------------------------------#


# fonction de création du sidebar
def Init_sidebar(query_params = st.experimental_get_query_params, tabs = [], img = Image):

    with st.sidebar:
        # with st.echo():
        #     st.write("exemple de print dans sidebar")
        col1,col2,col3 = st.columns(3)
        with col1:
            my_radio  = st.radio("Bien ou bien ?", ("Bien","bien"))
        with col2:
            my_radio2 = st.radio("Sur ?", ("oui","peut-être"))
        with col3:
            st.image(img, width = 85)


        st.write("# Sommaire")
        active_tab = Init_tabs(query_params, tabs)
        
        # my_component = st.sidebar.selectbox("Hello", ("how are you ?", "do I know YOU ?"))
        # active_tab = Init_tabs(query_params, tabs)
        # Quand on modifie l'element slider,, cela recharge le spinner (recharge la page ? => (resynchronisation!, recompilation !))
        # with st.spinner("chargement en cours"):
            # time.sleep(0.5)
            # st.success("Compil Ok !")       
        # hour_to_filter = st.slider('hour', 0, 23, 17)
        # if st.on_change(hour_to_filter):
    return active_tab


# fonction pour créer plusieurs page. 
# Non optimisé tel quel, et ouvre nouvel page a chaque clique ==> NO USER FRIENDLY
def Init_tabs(query_params_init = st.experimental_get_query_params(), tabs = []):
    if "tab" in query_params_init:
        active_tab = query_params_init["tab"][0]
    else:
        active_tab = "Home"

    if active_tab not in tabs:
        st.experimental_get_query_params(tab="Home")
        active_tab = "Home"

    li_items = "".join(
        f"""
        <li class="nav-item">
            <a class="nav-link{' active' if t==active_tab else ''}" href="/?tab={t}">{t}</a>
        </li>
        """
        for t in tabs
    )
    tabs_html = f"""
        <ul class="nav nav-tabs">
        {li_items}
        </ul>
    """
    st.markdown(tabs_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    # st.title("Bienvenue sur la page de ma vie")
    # st.write("Je vous souhaites une bonne continuation et un agréable séjour")

    ## Retourne la variable courante de changement de page
    return active_tab


def _Home (active_tab = "", query_params = st.experimental_get_query_params, tabs = []):

    st.set_option('deprecation.showPyplotGlobalUse', False)   

    if active_tab == "Home":
        st.title("Bienvenue sur la page de ma vie")
        st.write("Je vous souhaites une bonne continuation et un agréable séjour")
        # with st.sidebar:
        # sigma_filter = st.slider('sigma', 0.0, 1.0,  0.5)
        # mean_filter = st.slider('mean', 0, 1, 0,5,step = float)
        score_filter = st.slider('sigma', 0.000 , 1.000, 0.5)
        mean_filter = 0
        y11 = plot_air(y1, xl,mean_filter,1, score_filter)
        y22 = plot_air(y2, xl,mean_filter,1, score_filter)
        st.pyplot(y11)
        st.pyplot(y22)

# fonction pour tracer une repartition normal, calcul du Z et plot
def plot_air(yb, xlb = np.linspace, loca = float, scalea=float, score=float):
# def plot_air(ya = plt.plot() , xla = np.linspace, loca = float, scalea=float, score=float):
# def plot_air(xminp = float, xmaxp = float ,xmina=np.float64, loca = float, scalea=float, score=float):
    
    if yb.all(): 
        ya = yb
        xla = xlb
    else:
        ya = scipy.stats.norm.pdf(xl, loc=mean, scale=std)
        xla = np.linspace(-std*3.8, std*3.8, 100)
        
    # calcul du Z
    ppfa = scipy.stats.norm.ppf(score, loc=mean, scale=std)
    
    # on plot notre répartion
    ax1 = plt.plot(xla,ya, color="r")
    
    # plot de l'air sous la courbe
    plt.fill_between(xla, ya, 0, where=(xla<ppfa),alpha = 0.5)
    plt.show()


def _Test (active_tab = "", side_bar = st.sidebar, query_params = st.experimental_get_query_params(), tabs = []):
    st.write("Test")
    if active_tab == "st_Test":
        hour_to_filter  = st.slider('hour 1', 0, 23, 17)
        hour_to_filter2 = st.slider('hour 2', 1, 23, 17)

        st.subheader('Hour 2')
        st.write("H2 : " ,hour_to_filter2)

        if st.checkbox('Montrer la différence entre H2 et H1 ?'):
            st.subheader('donnée')
            st.write("H2 - H1 = ", hour_to_filter2 - hour_to_filter)
        
        with st.sidebar:
            st.write("## Information réservé uniquement à la page test")
            st.write("Hour 1 : ", hour_to_filter)


def _CV (active_tab = "", side_bar = st.sidebar):
  with open("style.css") as f:
      st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

  #####################
  # Header 
  st.write('''
  # Chanin Nantasenamat, Ph.D.
  ##### *Resume* 
  ''')

  image = Image.open('bender.png')
  st.image(image, width=150)

  st.markdown('## Summary', unsafe_allow_html=True)
  st.info('''
  - Experienced Educator, Researcher and Administrator with almost twenty years of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
  - Strong verbal and written communication skills as demonstrated by extensive participation as invited speaker at `10` conferences as well as publishing 149 research articles.
  - Strong track record in scholarly research with H-index of `32` and total citation of 3200+.
  ''')

  #####################
  # Navigation

  st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

  st.markdown("""
  <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
    <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Chanin Nantasenamat</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#education">Education</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#work-experience">Work Experience</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#social-media">Social Media</a>
        </li>
      </ul>
    </div>
  </nav>
  """, unsafe_allow_html=True)

  #####################
  # Custom function for printing text
  def txt(a, b):
    col1, col2 = st.columns([4,1])
    with col1:
      st.markdown(a)
    with col2:
      st.markdown(b)

  def txt2(a, b):
    col1, col2 = st.columns([1,4])
    with col1:
      st.markdown(f'`{a}`')
    with col2:
      st.markdown(b)

  def txt3(a, b):
    col1, col2 = st.columns([1,2])
    with col1:
      st.markdown(a)
    with col2:
      st.markdown(b)
    
  def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5,2,2])
    with col1:
      st.markdown(f'`{a}`')
    with col2:
      st.markdown(b)
    with col3:
      st.markdown(c)

  #####################
  st.markdown('''
  ## Education
  ''')

  txt('**Doctor of Philosophy** (Medical Technology), *Mahidol University*, Thailand',
  '2002-2006')
  st.markdown('''
  - GPA: `3.89`
  - Research thesis entitled `Computer-aided molecular design for biological and chemical applications : Quantum chemical and machine learning approach`.
  - Received Royal Golden Jubilee Ph.D. Scholarship of `2.152 million THB` covering tuition and stipend.
  - Thesis awarded `1st` Prize by the National Research Council of Thailand.
  ''')

  txt('**Bachelors of Science** (Biological Science), *Mahidol University International College*, Thailand',
  '1998-2002')
  st.markdown('''
  - GPA: `3.65`
  - Graduated with First Class Honors.
  ''')

  #####################
  st.markdown('''
  ## Work Experience
  ''')

  txt('**Head, Center of Data Mining and Biomedical Informatics**, Faculty of Medical Technology, Mahidol University, Thailand',
  '2011-2021')
  st.markdown('''
  - Managing a Center of `10` professors, researchers and students to ensure KPIs are strategically achieved namely to publish at least `20+` research publications annually. 
  - Actively took part in the talent hiring process as well as help employees to plan and develop their career path.
  - Set budget and handle procurement in order to facilitate education and research activities. Secured `> 10 million THB` budget.
  - Set and reflect on OKR on an annual basis to ensure productivity strategically matches the organization's direction.
  ''')

  txt('**Associate Professor**, Faculty of Medical Technology, Mahidol University, Thailand',
  '2012-2021')
  txt('**Assistant Professor**, Faculty of Medical Technology, Mahidol University, Thailand',
  '2009-2012')
  txt('**Lecturer**, Faculty of Medical Technology, Mahidol University, Thailand',
  '2006-2009')
  st.markdown('''
  - Provided mentorship and supervision to junior faculty, researchers, Ph.D./M.Sc./B.Sc. students. Mentored `3` Post-doctoral fellows, supervised `13` Ph.D. students, supervised `8` M.Sc. students, supervised `13` B.Sc. students and hosted `6` visiting students from U.S., Sweden and India.
  - Wrote and applied for research grants. Served as Principal Investigator for research grants that have been awarded `12.5 million THB` and `1.117 million SEK` in research funding from Thai and Swedish grant agencies.
  - Conducted research by applying machine learning to computational drug discovery and ensuring that research output exceeds `20+` articles per year.
  - Taught `10+` undergraduate/graduate classes on Bioinformatics, Data Mining, Scientific Research and Presentation, Research Methodology, Graduate Seminar, Programming for Health Data Science, etc.
  - Peer reviewed `100+` research articles for leading scientific journals.
  ''')

  txt('**Co-Chair**, International Conference on Pharmaceutical Bioinformatics at Pattaya, Thailand',
  '2016')
  st.markdown('''
  - Oversee all aspects of the conference preparations from conception to launch. This include inviting keynote and plenary speakers, create advertisement flyers, create abstract book, etc.
  - Conference attracted `200+` participants from `40+` countries from university and industry sector.
  - Chaired keynote session, technical workshop and some of the parallel sessions.
  ''')

  txt('**Content Creator**, [Data Professor YouTube Channel](https://youtube.com/dataprofessor/)',
  '2019-Present')
  st.markdown('''
  - `100,000+` subscribers on YouTube
  - Created `261` educational videos on data science, machine learning and bioinformatics as well as hosted several podcast episodes with data scientists.
  - Created `3` sponsored videos for Notion, Gradio and Classpert.
  ''')

  txt('**Content Creator**, [Coding Professor YouTube Channel](https://youtube.com/codingprofessor/)',
  '2019-Present')
  st.markdown('''
  - `3,200+` subscribers on YouTube
  - Created `38` educational videos on Python and R programming.
  ''')

  txt('**Technical Writer**, [Data Professor Blog](https://data-professor.medium.com/) on Medium.com',
  '2019-Present')
  st.markdown('''
  - `4,100+` subscribers on Medium
  - Written `68` technical blogs on data science, machine learning and bioinformatics.
  ''')

  #####################
  st.markdown('''
  ## Bioinformatics Tools
  ''')
  txt4('ABCpred', 'A web server for the discovery of acetyl- and butyryl-cholinesterase inhibitors', 'http://codes.bio/abcpred/')
  txt4('AutoWeka', 'An automated data mining software based on Weka', 'http://www.mt.mahidol.ac.th/autoweka/')
  txt4('ACPred', 'A computational tool for the prediction and analysis of anticancer peptides','http://codes.bio/acpred/')
  txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
  txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
  txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
  txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')
  txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
  txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
  txt4('Meta-iAVP', 'A sequence-based meta-predictor for improving the prediction of antiviral peptides', 'http://codes.bio/meta-iavp/')
  txt4('osFP', 'A web server for predicting the oligomeric state of fluorescent proteins', 'http://codes.bio/osfp/')
  txt4('PAAP', 'A web server for predicting antihypertensive activity of peptides', 'http://codes.bio/paap/')
  txt4('PepBio', 'A web server for predicting the bioactivity of host defense peptide', 'http://codes.bio/pepbio')
  txt4('PyBact', 'Open source software written in Python for bacterial identification', 'https://sourceforge.net/projects/pybact/')
  txt4('TargetAntiAngio', 'A sequence-based tool for the prediction and analysis of anti-angiogenic peptides','http://codes.bio/targetantiangio/')
  txt4('ThalPred', 'Development of decision model for discriminating Thalassemia trait and Iron deficiency anemia','http://codes.bio/thalpred/')
  txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')


  #####################
  st.markdown('''
  ## Skills
  ''')
  txt3('Programming', '`Python`, `R`, `Linux`')
  txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
  txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
  txt3('Machine Learning', '`scikit-learn`')
  txt3('Deep Learning', '`TensorFlow`')
  txt3('Web development', '`Flask`, `HTML`, `CSS`')
  txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

  #####################
  st.markdown('''
  ## Social Media
  ''')
  txt2('LinkedIn', 'https://www.linkedin.com/in/chanin-nantasenamat')
  txt2('Twitter', 'https://twitter.com/thedataprof')
  txt2('GitHub', 'https://github.com/chaninn/')
  txt2('', 'https://github.com/chaninlab/')
  txt2('', 'https://github.com/dataprofessor')
  txt2('ORCID', 'http://orcid.org/0000-0003-1040-663X')
  txt2('Scopus', 'http://www.scopus.com/authid/detail.url?authorId=12039071300')
  txt2('ResearcherID', 'http://www.researcherid.com/rid/F-1021-2010')
  txt2('ResearchGate', 'https://www.researchgate.net/profile/Chanin_Nantasenamat')
  txt2('Publons', 'https://publons.com/a/303133/')
  return active_tab
