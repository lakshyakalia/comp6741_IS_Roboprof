import spacy
import requests


def file_content_as_string(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        content=f.read()
        print(type(content))
        return content

def annotate_text_with_dbpedia_spotlight(text,confidence=0.5,support=20):
    headers={'Accept':'Application/json'}
    data={
        'text':text,
        'confidence':confidence,
        'support':support
    }
    response=requests.get('http://api.dbpedia-spotlight.org/en/annotate',headers=headers,params=data)
    return response.json()
def process_string(file_cotent):
    nlp=spacy.load("en_core_web_sm")
    doc=nlp(file_cotent)
    named_entity=[ent.text for ent in doc.ents]
    return named_entity

def main():
    file = 'COMP6721_AI_Lab_2_Winter2024'
    file_path='phase2/output/' + file + '.txt'
    output_path='phase2/output_ttl/' + file + '.ttl'
    file_content_string=file_content_as_string(file_path)
    list_of_named_entity=process_string(file_content_string)
    single_text=' '.join(list_of_named_entity)
    response=annotate_text_with_dbpedia_spotlight(single_text)
    print(response['Resources'])
    topic_dict=dict()
    for data in response['Resources']:
        if data['@surfaceForm'].lower() in topic_dict:
            pass
        else:
            topic_dict[data['@surfaceForm'].lower()]=data['@URI']
        # print(data['@URI'],data['@surfaceForm'])
        # print(type(data['@surfaceForm']))
            
    topic_dict = {key.replace(" ", "_"): value for key, value in topic_dict.items()}
    # print(topic_dict)
    str = ''
    for t in topic_dict:
        str = str + '\tex:hasTopicsCovered dbpedia:' + t + ';\n'
        # print(t)
    str = str + '\n\n\n'

    for t in topic_dict:
        str = str + 'dbpedia:' + t + ' a ex:Topics;\n\t'

        word = t.split('_')
        label = ''.join(w[0].upper() for w in word)
        str = str + 'rdfs:label "' + t + '"@en;\n\t'
        str = str + 'rdfs:seeAlso <' + topic_dict[t] + '>;\n\t'
        str = str + '.\n\n'

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(str)
        
main()