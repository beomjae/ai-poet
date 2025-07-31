from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
# from dotenv import load_dotenv
import os

# OpenRouter API 키를 위한 환경 변수 로딩
# load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter를 통한 ChatOpenAI 초기화
llm = init_chat_model(
    model="deepseek/deepseek-chat-v3-0324:free", 
    model_provider="openai",
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

# 프롬프트 템플릿 생성
prompt = ChatPromptTemplate.from_messages([
  ("system", "You are a helful assistant."),
  ("user", "{input}")
])

# 문자열 출력 파서
output_parser = StrOutputParser()

# LLM 체인 구성
chain = prompt | llm | output_parser

# streamlit으로 화면 출력
# 제목
st.title("인공지능 시인")

# 시 주제 입력 필드
content = st.text_input("시의 주제를 제시해주세요", max_chars=15)
st.write("시의 주제는", content)

# 시 작성 요청하기
if st.button("시 작성 요청하기"):
  with st.spinner('Wait for it...'):
    result = chain.invoke({"input": content + "에 대한 시를 써줘. 시의 제목을 처음에 표시하고 시 본문을 다음에 표시해줘. 그외에 다른 내용은 더하지 말아줘."})
    st.write(result)