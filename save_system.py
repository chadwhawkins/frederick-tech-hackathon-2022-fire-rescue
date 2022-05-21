import streamlit as st
import os
import json

dir = "tempDir"

#saving file to the app
# data is the data you are saving as json format
# type is file name of the file you are saving to
def saveFile(data, type): 
    filePath = os.path.join(dir,type + ".json")
    if not os.path.isdir(dir):
        os.mkdir(dir)
    with open(filePath,"wb") as f:
        f.write(bytes(json.dumps(data, separators=(',', ':')), 'utf-8'))
        return st.success("Saved File:{} to tempDir".format(json.dumps(data, separators=(',', ':'))))




#loads a file from the app
# type loads the file name
def loadFile(type):
    with open (os.path.join(dir, type + ".json"),"r") as f:
        return json.loads(f.read())
