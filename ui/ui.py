import gradio as gr
import requests
import json

def get_prediction(json_input):
    try:
        data = json.loads(json_input)
        response = requests.post("http://localhost:5000/predict", json=data)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

iface = gr.Interface(
    fn=get_prediction,
    inputs=gr.Textbox(lines=6, label="JSON Input"),
    outputs=gr.JSON(label="Response"),
    title="Flask API Interface",
    description="Send JSON to /predict endpoint on your Flask server"
)

iface.launch()
