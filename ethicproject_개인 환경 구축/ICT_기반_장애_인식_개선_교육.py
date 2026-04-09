import streamlit as st
st.set_page_config(page_title='24년 2학기 정보윤리교육개론', layout='wide')

if 'login' not in st.session_state:
    st.session_state['login'] = ''

if st.session_state.login != '':
    if st.sidebar.button('로그오프'):
        st.session_state.login = ''
        
c1, c2 = st.columns(2)
with c1:
    st.title('정보통신기술(ICT) 기반 장애 인식 개선 교육 프로그램')
    st.image('./images/01.png')
with c2:
    t1, t2 = st.tabs(['Login', 'Register'])
    with t1: 
        if st.session_state['login'] != '':
            st.info(f'{st.session_state.login}님 환영합니다.😊 로그인에 성공하였습니다.🎉')
        else:
            with st.form('loginform'):
                userid = st.text_input('userID', key='luserid')
                passwd = st.text_input('passWD', key='lpasswd')
                if st.form_submit_button('Login'):
                    if all([userid, passwd]):
                        import pandas as pd
                        df = pd.read_csv('./users.csv', encoding='utf-8')
                        idlist = list(df.iloc[:, 1])
                        passwdlist = list(df.iloc[:, 2])
                        #st.write(userid,idlist,passwdlist)
                        if userid in idlist and passwd in passwdlist:
                            st.session_state['login'] = userid
                            st.success(f'{userid}의 로긴이 성공했습니다.')
                            st.rerun()
                        else:
                            st.error('🚫등록된 사용자가 아닙니다. 또는 ID와 PASSWD 일치하지 않습니다.🚫')
                    else:
                        st.error('🚫모든 정보를 입력해야 합니다.🚫')

    with t2: 
        with st.form('register'):
            grade = st.selectbox('학년선택', [f'{x}학년' for x in range(1,13)], key='grade')
            userid = st.text_input('userID', key='ruserid')
            passwd = st.text_input('passWD', key='rpasswd')
            if st.form_submit_button('Register'):
                if all([grade, userid, passwd]):
                    with open('./users.csv', 'a') as f:
                            inputtxt = f'{grade},{userid},{passwd}\n'
                            f.write(inputtxt)
                            f.close()

                    st.success('등록 성공')
                else:
                    st.error('🚫모든 정보를 입력해야 합니다.🚫')

st.markdown(
    """
    <style>
        .copyright {
            font-size: 14px;
            color: #666;
            text-align: center;
            margin-top: 30px;
            padding: 10px;
            background-color: transparent; /* 투명 배경 */
            font-family: 'Arial', sans-serif;
            border-top: 1px solid #d1d1d1; /* 위쪽에 얇은 선 */
        }
    </style>
    <div class="copyright">
            &copy; 2024 All rights reserved.<br>
            | Powered by KO-Minwoo | Information and Communication Engineering & Computer Education<br>
            Email: radsky336@smail.kongju.ac.kr
            
    </div>
    """,
    unsafe_allow_html=True
)