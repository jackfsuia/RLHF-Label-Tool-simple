# !/usr/bin/env python3
import pandas as pd
import streamlit as st
import json

st.set_page_config(page_title="Rank List Labeler simple", page_icon="📌", layout="wide")

CONFIGS = {
    "input_path": "./data/input_file.jsonl",
    "output_path": "./data/output_result.jsonl",
}

if "label_result" not in st.session_state:
    st.session_state["label_result"] = {}

label_tab, dataset_tab = st.tabs(["Label", "Dataset"])
label_result = {}


######################### 页面侧边栏：问题和参考答案页面########################

st.sidebar.title("📌 RLHF Preference label tool-simple")
dataset = []
with open(CONFIGS["input_path"], "r", encoding="utf-8") as f:
    for i in f:
        dataset.append(json.loads(i))
current_data_id = st.sidebar.number_input(
    "当前 Question ID（点击右边的➕➖前后跳转）：",
    min_value=0,
    max_value=len(dataset) - 1,
    value=0,
)
current_question = dataset[current_data_id]["question"]
current_reference = dataset[current_data_id]["reference"]
st.sidebar.header("📢Question")
st.sidebar.markdown(f"{current_question}")
st.sidebar.header("📢Reference")
st.sidebar.text(f"{current_reference}")


######################### 保存按钮########################

save_button = st.sidebar.button("Save for now")
if save_button:
    dataset_file = CONFIGS["output_path"]
    with open(dataset_file, "w", encoding="utf-8") as result_file:
        for res in st.session_state["label_result"].values():
            result_file.write(json.dumps(res) + "\n")
    st.sidebar.success("Save Success !")

######################### 打标页面 ########################

with label_tab:

    candidate_num = len(dataset[0]["response"])
    with st.expander("💡 Generate Results", expanded=True):
        result = {
            "question": current_question,
        }
        for i in range(candidate_num):
            st.markdown("---")
            st.markdown(
                f"""
            <h6 style='text-align: center; color: black;'>
                {i}
            </h6>
            """,
                unsafe_allow_html=True,
            )
            response_text = dataset[current_data_id]["response"][i]
            st.markdown(response_text)
            judge = st.radio(
                "Preference",
                ("Accept", "Reject", "dismiss"),
                index=2,
                key=f"{current_data_id}:{i}",
            )
            if judge == "Accept":
                result["Accept"] = response_text
            if judge == "Reject":
                result["Reject"] = response_text
            if judge == "dismiss":
                pass
        if "Reject" not in result:
            st.info("Reject not choosen !")
        if "Accept" not in result:
            st.info("Accept not choosen !")
        if "Accept" in result and "Reject" in result:
            st.session_state["label_result"][current_data_id] = result
        # 删除
        if "Reject" not in result and "Accept" not in result:
            st.session_state["label_result"].pop(current_data_id, None)

######################### 数据集页面 #######################

with dataset_tab:
    dataset_file = CONFIGS["output_path"]
    df = pd.read_json(dataset_file, lines=True)
    st.dataframe(df)
