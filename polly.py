import boto3
import os
import sys

arg = sys.argv[1:]
string = ''.join(arg)

polly = boto3.client('polly')
text = polly.synthesize_speech(Text = string, OutputFormat = 'mp3', VoiceId = 'Joanna')

with open('output.mp3', 'wb') as file:
    file.write(text['AudioStream'].read())
    file.close()

print("MP3 file created successfully.")