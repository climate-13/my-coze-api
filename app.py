from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 从环境变量读取（安全！）
COZE_API_KEY = os.getenv("pat_qsW8Ng1I3SGU224UuHBNUoC3Lt8r8kkoTYhe159IZoRec0LZpg6UNkFySdLGx9Ll")  # 你的令牌
COZE_WORKFLOW_ID = "7533122299790131236"             # 你的工作流ID

@app.route('/run-workflow', methods=['POST'])
def run_workflow():
    user_input = request.json.get('input')
    headers = {"Authorization": f"Bearer {COZE_API_KEY}"}
    payload = {
        "workflow_id": COZE_WORKFLOW_ID,
        "parameters": {"user_query": user_input}  # 和工作流输入参数名一致！
    }
    response = requests.post("https://api.coze.cn/v1/workflow/run", headers=headers, json=payload)
    return jsonify(response.json().get('data', {}))