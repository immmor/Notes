from gradio_client import Client
import os

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:1083'
# os.environ['HTTPS_PROXY'] = 'https://127.0.0.1:1083'

# client = Client("https://facebook-musicgen--bzkz2.hf.space/")
# result = client.predict(
# 				"lofi slow bpm electro chill with organic samples",	# str  in 'Describe your music' Textbox component
# 				# "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",	# str (filepath or URL to file) in 'File' Audio component
# 				fn_index=2
# )
# print(result)


# client = Client("https://facebook-musicgen--bzkz2.hf.space/")
# result = client.predict(
# 				"lofi slow bpm electro chill with organic samples",	# str  in 'parameter_15' Dataset component
# 				fn_index=2
# )
# print(result)


client = Client("https://yentinglin-taiwan-llama2.hf.space")
result = client.predict(
				fn_index=9
)
print(result)