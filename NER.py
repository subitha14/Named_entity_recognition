####large language library
import spacy
import re

def name_masking(sentence):
    nlp = spacy.load('en_core_web_lg')
    doc = nlp(sentence)
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            print(ent.text)
            pattern = ent.text+ r'\s*(\([^)]*\))'
            match=re.search(pattern, sentence)
            if match:
                sentence = sentence.replace(match.group(), '****')
    
    return sentence


if __name__=="__main__":
    sentence='Issuer Name:Subitha Murugesan (AB-ER-ABCD-PS)&lt;br/&gt;sample ticket please ignore it Akash  &lt;br/&gt;"flow":"pmt-feedback-product","source_name":"Tool Landscape","context":"ALM-ETM in MDG1","owner":"pmt-prod-crm-prm"'
    print(sentence)
    masked_sentence = name_masking(sentence)
    print('\n')
    print(masked_sentence)