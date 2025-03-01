import os
import json
import PyPDF2
# import wrapper

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
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ''
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
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

if __name__ == '__main__':
    main()