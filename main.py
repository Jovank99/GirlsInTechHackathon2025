import os
import json
import PyPDF2
import wrapper
from UI import *

environment = {
    'Folder': ''
}

def change_folder(folder):
    environment['Folder'] = folder + '/'
    try:
        os.mkdir(environment['Folder'])
    except FileExistsError:
        pass

def pdf_to_text(file):
    pdf_file = open(environment['Folder'] + file, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in pdf_reader.pages:
        # page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

def parse_data(data):
    # while True:
    #     try:
    #         return json.loads(wrapper.parse_data(data))
    #     except json.JSONDecodeError:
    #         pass
    return json.loads(wrapper.parse_data(data))

def save_json(data, file):
    with open(environment['Folder'] + file, 'w') as f:
        f.write(json.dumps(data, indent=4))

def main():
    change_folder('Burks2024')
    text = pdf_to_text('test.pdf')
    # data = parse_data(text)
    # save_json(data, 'data.json')
    
    
    root.mainloop()
    
    

if __name__ == '__main__':
    main()