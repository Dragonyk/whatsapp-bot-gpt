import uuid
import codecs
import csv

def write_file(text, filepath):
    f = codecs.open(filepath, "w", "utf-8")
    f.write(text)
    f.close()


def save_input(input_text, query_text, output_text):
    uuid_name = str(uuid.uuid4())
    text = 'INPUT:'+input_text+'\n'
    text += 'OUTPUT:'+output_text
    write_file(text, './inout_texts/'+uuid_name+'.txt')


def read_promptfile(filepath):
    f = codecs.open(filepath, "r", "utf-8")
    input_text = f.readline().split(':')[1]
    query_text = f.readline().split(':')[1]
    output_text = f.readline().split(':')[1]
    return (input_text, query_text, output_text)


def csv_write(data, filepath):
    with open(filepath,'a',newline='') as fd:
        writer = csv.writer(fd)
        for item in data:
            writer.writerow([item])