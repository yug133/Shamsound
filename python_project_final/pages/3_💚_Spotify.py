import streamlit as st
import webbrowser
from streamlit_extras.app_logo import add_logo
import streamlit.components.v1 as components

st.title("Musify-Spotify 💚")
st.markdown(''':green[**Note : It is recommended that you scan your face , for Musify to groove with you!**]''')
st.sidebar.success("Spotify has been selected as your music player.")
st.sidebar.text("")

if "run" not in st.session_state:
    st.write("**Looks like you have skipped the face scan on the homepage and came here, just for music, just choose your vibe manually for Musify to groove with you!**")
    option = st.selectbox(
    'What''s your vibe today?',
    ('Happy', 'Sad', 'Angry','Fear','Surprise','Neutral'))
    if option == "Happy":
        st.session_state["emotion"] = "Happy"
    elif option == "Sad":
        st.session_state["emotion"] = "Sad"
    elif option == "Angry":
        st.session_state["emotion"] = "Angry"
    elif option == "Fear":
        st.session_state["emotion"] = "Fear"
    elif option == "Surprise":
        st.session_state["emotion"] = "Surprise"
    else:
        st.session_state["emotion"] = "Neutral"
else:
    st.write("You current emotion is: " , st.session_state["emotion"])

col1, col2 = st.columns(2)

with col1:
    hindi = st.button("Hindi")
    if hindi:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWTwbZHrJRIgD?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Sad":
           components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXdFesNN9TzXT?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/2r9tRVoHG3AMBTvKJ8abOl?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7EZ4lWeM1OLxZYfGmhDbJI?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7vatYrf39uVaZ8G2cVtEik?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX0XUfTFmNBRM?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1E4mS880sTV9QE?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
            
with col2:
   english = st.button("English")
   if english:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXdPec7aLTmlC?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Sad":
           components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX7qK8ma5wgG1?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1EIgNZCaOGb0Mi?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1EIfgYPpPEriFK?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1EIfIhwClkyzKs?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZEVXbMDoHDwVN2tF?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/60eEo5VdhekyGJKTjK2xSV?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
            