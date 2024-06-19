import json
import os

def load_all_words(filename):
    # Đọc dữ liệu từ file all_word.json
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def print_word_data(word_key, word_data):
    # Print word data in a simple list format
    print(f"Data for '{word_key}':")
    
    # Print spelling
    if 'spelling' in word_data:
        print(f"  Spelling: {word_data['spelling']}")
    
    # Print synonyms
    if 'synonyms' in word_data:
        print(f"  Synonyms: {', '.join(word_data['synonyms'])}")
    
    # Print meanings
    if 'meaning' in word_data:
        print(f"  Meanings:")
        for meaning in word_data['meaning']:
            print(f"    - {meaning['pos']}:")
            print(f"      - English: {meaning['en']}")
            print(f"      - Vietnamese: {meaning['vi']}")
    
    # Print sentences
    if 'sentences' in word_data:
        print(f"  Sentences:")
        for sentence in word_data['sentences']:
            print(f"    - English: {sentence['en']}")
            print(f"      Vietnamese: {sentence['vi']}")
    
    # Print words_form
    if 'words_form' in word_data:
        print(f"  Words Form:")
        if not word_data['words_form']:
            print(f"    - (none)")
    
    # Print meaning_vi
    if 'meaning_vi' in word_data:
        print(f"  Meaning (Vietnamese): {word_data['meaning_vi']}")

    print()

def search_word_in_files(search_term, all_words, words_dir):
    # Tìm kiếm từ trong các file JSON
    found = False
    for word_key in all_words:
        if word_key.lower() == search_term.lower():
            json_filename = word_key + '.json'
            json_path = os.path.join(words_dir, json_filename)
            
            if os.path.exists(json_path):
                try:
                    with open(json_path, 'r', encoding='utf-8') as json_file:
                        word_data = json.load(json_file)
                        print_word_data(word_key, word_data)
                        found = True
                except Exception as e:
                    print(f"Error reading file '{json_filename}': {str(e)}")
            else:
                print(f"File '{json_filename}' does not exist.")
    
    if not found:
        print(f"Word '{search_term}' not found.")

def main():
    all_words_filename = '5000-oxford-words-vietnamese/_all_word.json'
    words_dir = '5000-oxford-words-vietnamese/words/'

    try:
        all_words = load_all_words(all_words_filename)
        search_term = input("Search word: ")
        search_word_in_files(search_term, all_words, words_dir)
    except FileNotFoundError:
        print(f"File '{all_words_filename}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
