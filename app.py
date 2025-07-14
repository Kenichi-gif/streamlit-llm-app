from dotenv import load_dotenv

load_dotenv()

#以下メイン
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import streamlit as st

#入力テキストとラジオボタンでの選択値を引数として受け取りLLM回答を戻り値として返す関数
def get_llm_answer(input_text, selected_expert):
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    if selected_expert == "医療専門家":
        messages = [
            SystemMessage(content="You are a medical expert."),
            HumanMessage(content=input_text),
        ]
    else:
        messages = [
            SystemMessage(content="You are an educational expert."),
            HumanMessage(content=input_text),
        ]
    result = llm(messages)
    return result.content
    
#Streamlitの設定
st.title("課題:専門家問合せアプリ")

st.write("このアプリは、医療と教育の専門家に質問をすることができます。")
st.write("### 使用方法")
st.write("1. 質問したい内容を入力します。")
st.write("2. 医療専門家または教育専門家のどちらに質問するかを選択します。")
st.write("3. 「実行」ボタンをクリックすると、専門家からの回答が表示されます。")
st.write("##### 医療専門家")
st.write("医療関係の質問を入力すると医療の専門家が回答してくれます。")
st.write("##### 教育専門家")
st.write("教育関係の質問を入力すると教育の専門家が回答してくれます。")

selected_item = st.radio(
    "どちらの専門家に質問しますか",
    ["医療専門家", "教育専門家"]
)

st.divider()

if selected_item == "医療専門家":
    input_message = st.text_input(label="医療に関する質問を入力してください。")
else:
    input_message = st.text_input(label="教育に関する質問を入力してください。")


if st.button("実行"):
    st.divider()

    if selected_item == "医療専門家":
        medical_answer = get_llm_answer(input_message, selected_item)
        if medical_answer is None:
            st.write("回答が得られませんでした。")
        else:
            medical_answer = medical_answer
        st.write(f"回答: **{medical_answer}**")
    else:
        education_answer = get_llm_answer(input_message, selected_item)
        if education_answer is None:
            st.write("回答が得られませんでした。")
        else:
            education_answer = education_answer
        st.write(f"回答: **{education_answer}**")


