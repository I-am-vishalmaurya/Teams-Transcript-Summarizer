import requests

url = "https://wordcab.com/api/v1/summarize?source=vtt&summary_type=narrative&context=null&summary_lens=3&source_lang=en&target_lang=en&split_long_utterances=true&pipeline=transcribe%2Csummarize&ephemeral_data=false"

headers = {
    "accept": "application/json",
    "content-type": "multipart/form-data",
    "authorization": "Bearer edb69951d2cfd425a09317b5400e7ca69ece8621"
}

# Open the VTT file and send it to the API
with open('/Users/vishalmaurya/Desktop/BITS/summarizer/uploads/Computer Organization and Architecture (S2-22_SSJPZC353).vtt', 'rb') as f:
    files = {'file': ('Computer Organization and Architecture (S2-22_SSJPZC353).vtt', f)}
    response = requests.post(url, headers=headers, files=files)

print(response.text)