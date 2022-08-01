import streamlit as st

st.markdown("""
<style>
    .flex-container {
    display: flex;  
    }

    .flex-child {
        flex: 1
    }  

    .flex-child:first-child {
        margin-right: 20px;
    } 

    p {
        position: absolute;
        bottom:0;
        text-align: center;
    }


</style>

<div class="flex-container">
    <div class="flex-child">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.1.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M288 256C288 273.7 273.7 288 256 288C238.3 288 224 273.7 224 256C224 238.3 238.3 224 256 224C273.7 224 288 238.3 288 256zM0 256C0 114.6 114.6 0 256 0C397.4 0 512 114.6 512 256C512 397.4 397.4 512 256 512C114.6 512 0 397.4 0 256zM325.1 306.7L380.6 162.4C388.1 142.1 369 123.9 349.6 131.4L205.3 186.9C196.8 190.1 190.1 196.8 186.9 205.3L131.4 349.6C123.9 369 142.1 388.1 162.4 380.6L306.7 325.1C315.2 321.9 321.9 315.2 325.1 306.7V306.7z"/></svg>
    </div>
    <div class="flex-child">
        <p> 
        Examples moved to: <br> <a href="https://pablocfonseca-streamlit-aggrid-examples-example-jyosi3.streamlitapp.com/">https://pablocfonseca-streamlit-aggrid-examples-example-jyosi3.streamlitapp.com/</a>
        </p>
    </div>
</div>

""", unsafe_allow_html=True)