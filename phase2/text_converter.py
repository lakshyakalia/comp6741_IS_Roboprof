from tika import parser
import os
import re

def text_converter(path):
    text = parser.from_file(path)
    cleaned_content = remove_whitespace(text['content'])
    return cleaned_content

def remove_whitespace(text):
    cleaned_text=re.sub(r'\s+',' ',text)
    return cleaned_text.strip()

def main():

    filename = 'AAI_Reading_Material_01'

    path = 'AI_material/ReadingMaterials/' + filename + '.pdf'

    text = text_converter(path)

    output_path = 'phase2/output/'

    with open(output_path + filename + ".txt", "w", encoding="utf-8") as file:
        file.write(text)

main()