import streamlit as st
st.set_page_config(page_title='24년 2학기 정보윤리교육개론', layout='wide')

def filteringApp(df, userid):
    if userid == '12':
        return df
    else:
        return df[df['userid'] == userid]


if st.session_state.login != '':
    if st.sidebar.button('로그오프'):
        st.session_state.login = ''

if st.session_state.login == '':
    st.error('로그인을 먼저하세요.')
else:
    st.subheader('두번째 메뉴입니다.')
    t1, t2, t3 = st.tabs(['학습영상', '서브22', '서브23'])
    with t1:
        st.success('장애인식개선 교육 영상입니다. 시청 후 내용을 정리해주세요.')
        c1, c2 = st.columns((7, 3))
        with c1:
            url = 'https://youtu.be/NG6p3W_fEH4?si=6aniKxUSIlWi7g86'
            st.video(url)
        with c2:
            with st.form('mynoteform'):
                txtString = st.text_area('정리하기', height=200)
                if st.form_submit_button('저장하기'): 
                    if txtString != '':
                        with open('./learninghistory.csv', 'a') as f:
                            inputtxt = f'{st.session_state.login},"{txtString}"\n'
                            f.write(inputtxt)
                            f.close()
                            st.rerun()
                            # st.info(txtString + '<BR>저장되었습니다.', unsafe_allow_html=True)
                    else:
                        st.error('노트가 비어 있어요 ㅠㅠㅠ')
            import pandas as pd
            df = pd.read_csv('./learninghistory.csv', encoding='utf-8')
            newdf = filteringApp(df, st.session_state.login)
            st.table(newdf)
            st.table(df)
    with t2:
        st.success('서브22입니다.')
    with t3:
        st.success('서브23입니다.')