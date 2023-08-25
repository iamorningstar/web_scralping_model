# import the os module
import os
from os import makedirs
from os import mkdir
import requests
from bs4 import BeautifulSoup
import re
def delete_word(link,file_name,word):
    with open(f"{link}/{file_name}", "r",encoding="utf-8") as fin:
        text = fin.read()
        text = text.replace(word, "")
    fin.close()
    with open(f"{link}/{file_name}", "w",encoding="utf-8") as fout:
        fout.write(text)
    fout.close()
def word_filter(link,file_name):
    words = [")","(","[","]","}","{",".xml"]
    for word in words:
        delete_word(link,file_name,word)
def create_dir_and_file(file_name, link):
  dir_path = f"{link}/"
  complete_path = os.path.join(dir_path, file_name)
  if not os.path.exists(dir_path):
    os.mkdir(dir_path)
    print(f"Directory {dir_path} created!")
  else:
    print(f"Directory {dir_path} already exists")
  with open(complete_path, 'w', encoding='utf-8') as f:
    f.write(" ")
    print(f"File {file_name} created and written!")
  f.close()
def choping(link,filename,savename):
    gul = link
    fname = "resent.txt"
    with open(f"{gul}/{filename}", 'r', encoding='utf-8') as f:
        text = f.read()
    f.close()
    chars = sorted(list(set(text)))
    words = text.split()
    unique_words = set()
    for word in words:
        unique_words.add(word)
    unique_words = sorted(list(unique_words))
    unique_words_three = unique_words
    sentences = text.split(". ")
    unique_sentences = set()
    for sentence in sentences:
        unique_sentences.add(sentence)
    unique_sentences = sorted(list(unique_sentences))
    chars = chars + unique_words + unique_sentences
    i = 0
    with open(f"{gul}/{filename}", "w" ,encoding='utf-8') as file:
        while i < len(unique_words_three):
            file.write(unique_words_three[i]+"\n")
            # print(file.write(unique_words_three[i]+"\n"))
            # print(file)
            # ytt = unique_sentences_three.append()
            print(unique_words_three[i])
            i += 1
        # file.write(textold+"\n")
    file.close()
    i = 0  
def get_options(link,filename,savevame):
    gul = link
    data = []
    with open(f"{gul}/{filename}", 'r', encoding='utf-8') as f:
        text = f.read()
        textold = text
        urls = text.split()
    f.close()
    for url in urls:
        try:
            response = requests.get(url)
        except Exception as e:
            print ('An error occurred:', e)
            choping(gul,filename,savevame)
            delete_word(gul,filename, "url")
            # get_options(gul,filename,savevame)
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("a")
        img = soup.find("img")
        with open(f"{gul}/{savevame}", "a+",encoding="utf-8") as file:
            file.write(textold+"\n")
            for link in links:
                href = link.get("href")
                if href and re.match(r"^https?://", href):
                        file.write(href + "\n")
                data.append(href)
        file.close()
    # print(data)
def save_search(count):
    print("Startind def save_search(count):...........")
    link = input("Enter root link :")
    file_name = f"{link}.txt"
    wiki = f"https://bn.wikipedia.org/w/index.php?go=Go&search={link}"
    google = f"https://www.google.com/search?q={link}"
    bing = f"https://www.bing.com/search?q={link}"
    print(file_name)
    create_dir_and_file(file_name,link)
    with open(f"{link}\/{file_name}", "w",encoding="utf-8") as f:
        f.write(wiki+"\n")
        f.write(google+"\n")
        f.write(bing+"\n")
    f.close()
    num = 0
    word_filter(link,file_name)
    while num <= count:
        get_options(link,file_name,file_name)
        choping(link,file_name,file_name)
        word_filter(link,file_name)
        num = num + 1
def you_scrap(count):
    link = input("Enter root link :")
    file_name = f"{link}.txt"
    num = 0
    while num <= count:
        word_filter(link,file_name)
        num = num + 1
    num = 0
save_search(1)