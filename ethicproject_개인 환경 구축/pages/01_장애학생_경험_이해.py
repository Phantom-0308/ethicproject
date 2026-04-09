import streamlit as st
import streamlit.components.v1 as components

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
    t1, t2, t3 = st.tabs(['서브1', '서브2', '서브3'])
    with t1:
        c1, c2 = st.columns((7, 3))
        with c1:
            with st.expander('교과내용1'):
                st.subheader('정보통신기술이란?')
                txtdata = '''
            정보통신 기술은 보통 ICT라고 부르며, 정보 기술(IT)에 대한 넓은 의미의 동의어로 사용되기도 하지만, 현대 정보 기술의 통합 커뮤니케이션(통신), 전기 통신(전화선과 무선 신호)의 결합, 지능형 빌딩 관리 시스템 및 시청각 시스템의 역할을 강조하기 위해 일반적인 용어로 사용된다.
            '''
                st.markdown(txtdata)
        with c2:
            with st.expander('Tips...'):
                st.info(' 2차적저작물')
                st.write('① 원저작물을 번역·편곡·변형·각색·영상제작 그 밖의 방법으로 작성한 창작물(이하 "2차적저작물"이라 한다)은 독자적인 저작물로서 보호된다. ② 2차적저작물의 보호는 그 원저작물의 저작자의 권리에 영향을 미치지 아니한다.')
    
    with t2:
        st.success('서브2입니다.')
        import streamlit.components.v1 as components
        url = 'https://www.algeomath.kr/algeo/algeomath/app/make.do'
        components.iframe(url, width=1024, height=768)

        st.success('서브2입니다.')
        import streamlit.components.v1 as components
        url = 'https://wordcloud.kr/'
        components.iframe(url, width=1024, height=768)

    with t3:
        st.success('서브3입니다.')
        import streamlit.components.v1 as components
        url = 'https://www.moralmachine.net'
        components.iframe(url, width=1024, height=768)