import streamlit as st

# 페이지 제목 설정
st.title("⚖️ 범죄 처벌 예상 결과 조회 시스템")
st.caption("기존 콘솔 코드를 스트림릿 웹 버젼으로 변환한 프로그램입니다.")
st.markdown("---")

# 1. 죄목 입력 (기존 crime=input)
crime = st.text_input(
    '죄목을 입력하세요:', 
    placeholder='ex: 절도, 모욕 등의 경범죄'
)

# 2. 질문 리스트 정의 및 입력 받기 (기존 ask, rep 구조 보존)
# 스트림릿에서는 반복문 안에서 즉시 입력을 받기 위해 라디오 버튼을 활용합니다.
ask = ['초범입니까?', '반성하고 있습니까?', '소년범 입니까?']
rep = []

st.subheader("📋 경감 조건 확인")
for i in range(3):
    # 각 질문을 라디오 버튼(Y/N)으로 구성
    ans = st.radio(
        f'{i+1}번째 질문입니다. {ask[i]}',
        options=['Y', 'N'],
        index=1, # 기본값을 'N'으로 설정
        key=f"q_{i}" # 스트림릿 위젯 고유 키
    )
    rep.append(ans)

st.markdown("---")

# 3. 결과 출력 버튼
# 버튼을 누르면 기존 콘솔의 print문들이 스트림릿 화면에 예쁘게 표시됩니다.
if st.button('결과 분석하기', type='primary'):
    if not crime.strip():
        st.warning("죄목을 입력해주세요!")
    else:
        # ===[사건요약]===
        st.subheader('=== [사건요약] ===')
        st.info(f'**[죄목]:** {crime}')
        
        # ===[소년범 여부]===
        st.subheader('=== [소년범 여부] ===')
        if rep[2] == 'Y':
            st.success('소년범입니다, 소년법이 적용됩니다.')
        else:
            st.error('소년범이 아닙니다, 일반 법규가 적용됩니다.')
            
        # ===예상결과===
        st.subheader('=== 예상결과 ===')
        count = rep.count('Y')
        
        if count == 3:
            st.success('✨ 모든 경감조건 충족, 선처확률이 높습니다')
        elif count == 2:
            st.info('✅ 경감조건 다수 충족, 집행유예등의 선처를 기대할수 있습니다')
        elif count == 1:
            st.warning('⚠️ 경감조건 부족, 일반적인 처벌이 예상됩니다.')
        else:
            st.error('🚨 경감조건에 충족되는것 없음, 가중처벌이 예상됩니다.')