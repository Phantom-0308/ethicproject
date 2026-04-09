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
    st.subheader('데이터셋 기반 워드클라우드 구현')
    st.markdown('<p style="font-size: 17px;">학습목표: 장애 학생 인식에 대한 데이터를 시각화하여, 주요 키워드를 도출하고 이해한다.</p>', unsafe_allow_html=True)

    t1, t2, t3, t4 = st.tabs(['데이터셋 📊', '워드클라우드 ⛅️', '파이썬 🧑‍💻', '학습 자료 제출 📮'])
    with t1:

        st.subheader('몸풀기 퀴즈 🙋‍♂️')
        answer = st.radio("장애 인식 개선을 위한 첫 번째 단계는 무엇인가요?", 
                        ('정보 제공', '정신적 지원', '물리적 접근성 개선'))

        if st.button('제출'):
            if answer:
                if answer == '정보 제공':
                    st.success("정답입니다! 👏")
                else:
                    st.error("오답입니다. 다시 시도해보세요. 😡")
            else:
                st.warning("답변을 선택해주세요.")

        st.subheader('데이터 셋 공유 및 분석')
        st.markdown('<p style="font-size: 17px;">다른 조와 데이터 셋을 공유하는 시간입니다.</p>', unsafe_allow_html=True)
        st.success('다른 조원이 작성한 데이터 셋과 비교하며, 자신이 작성한 내용을 점검해 보아요.')
        st.markdown("[데이터셋 다운로드 링크](https://drive.google.com)", unsafe_allow_html=True)

        import streamlit.components.v1 as components
        url = 'https://padlet.com'
        components.iframe(url, width=800, height=768)

    with t2:
        st.subheader('워드클라우드란?')
        st.success('문서의 문구와 단어를 분석하여 중요도나 사용 빈도를 직관적으로 파악할 수 있도록 시각화하는 표현 기법.')

        st.subheader('핵심 단어 시각화 (Word Cloud)의 주의점')
        st.success("사용자가 문서의 주요 키워드나 중요도를 한눈에 보고 이해할 수 있다는 장점이 있지만, "
                    "단어 간의 관계를 표현할 수 없고 정보가 편향될 수 있는 단점이 있다.")

        st.subheader('워드클라우드 체험하기')
        import streamlit.components.v1 as components
        url = 'https://wordcloud.kr/'
        components.iframe(url, width=1024, height=800)

    with t3:
        st.subheader("파이썬 코딩 실습")

        code = st.text_area("아래에 파이썬 코드를 입력하세요:", height=300)

        if st.button("코드 실행"):
            try:
                exec(code)
            except Exception as e:
                st.error(f"오류 발생: {e}")
        
    with t4:
        st.success('오늘 제작한 학습 자료를 제출해주세요.')

        uploaded_file = st.file_uploader("학습 자료를 업로드하세요", type=['csv', 'txt', 'xlsx'])

        if uploaded_file is not None:
            st.success("파일이 업로드되었습니다.")
        else:
            st.info("업로드된 파일이 없습니다.")


















        # -3차시: 워드 클라우드 코딩 교육
        # 교사는 Python 기반의 워드 클라우드 코드를 설명한다.
        # 학생들은 코드를 실습하며 프로그래밍의 기본 개념을 이해하고, 직접 자신이 만든 핵심 단어 리스트를 적용해 결과를 도출한다.
        # 이 과정에서 학생들은 데이터 시각화의 필요성을 인식하고, 프로그래밍과 데이터 분석의 기초 능력을 익힌다.
        # 학습목표: 코딩 구현을 통해 장애학생에 대한 인식의 심각성 인지하기
        # 준비물: 구글 계정, 2차시에 작성한 대화록(단어 데이터셋)
        # 도입(5분)
        #조별로 모여서 착석한다.
        #2차시에 작성했던 대화록을 검토하여 평소 본인이 사용하는 화법에 대한 간단한 인지 과정을 거친다.
        #코딩 구현을 위해 구글에 로그인을 하고, Google Colab에 접속한다. 
        #본 수업(35분)
        #지도자의 파이썬 코드를 받아적으며 각자 코딩을 구현해본다.
        #● 코딩 오류가 나는 학생이 있을 것이므로 돌아다니면서 오류가 난 학생을 도와준다.
        #교사는 코딩을 타이핑하는 중에도 설명을 이어나가야 하며, 학생의 타이핑 실력은 서로 상이하기 때문에 다 썼는지 확인하면서 수업을 진행해야 한다. 
        #저번 2차시에서 작성했던 대화록을 전처리하는 코딩을 수행한다.
        #전처리된 데이터셋과 추가로 작성한 코드를 통해 워드클라우드와 바 그래프를 실행해본다. 
    # ● 이를 통해 학생들은 본인의 장애학생에 대한 인식을 시각적으로 확인하다 보니 보다 직접적으로 느낄 수 있음.
        #워드클라우드와 바 그래프를 통해 시각화한 뒤, 각자 느낀 점을 조원들과 간단히 나눠보는 시간을 가진다.
        #l 마무리(5분)
        #파일을 저장하고 교사에게 저장한 파일을 제출함.
        #다음 차시 안내: 다음 시간에는 코랩을 토대로 보고서를 작성하고 인식 제고 영상을 볼 것임을 안내.
        #과제: 구글 코랩으로 작성한 코드 파일, 워드클라우드, 바 그래프로 시각화한 것을 캡쳐하여 사진 제출.