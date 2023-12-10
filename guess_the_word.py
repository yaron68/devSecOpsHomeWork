import time
import random
THREE_WORDS_PHRASES = ['Act as if','Act without expectation',
                       'All is well','Allow for delays','Ask powerful questions',
                       'Audit your metrics','Based on results','Be the change',
                       'Believe in yourself','Brainstorm alternative ideas',
                       'Branding is essential','Build for scalability']
THREE_WORDS_PHRASES_SEPERATED = []
for phrase in  THREE_WORDS_PHRASES:
    THREE_WORDS_PHRASES_SEPERATED.append(phrase.split())


AMOUNT_OF_PHRASES = len(THREE_WORDS_PHRASES_SEPERATED)
score = 0
quit = True
while(quit):
    split_words = THREE_WORDS_PHRASES_SEPERATED[random.randint(0,AMOUNT_OF_PHRASES-1)]
    selected_phrase = (" ".join(split_words)).lower()
    #  creat the template to fill user input
    selected_phrase_fill = '_' * len(split_words[0]) + ' ' + '_' * len(split_words[1]) + ' ' + '_' * len(split_words[2])
    begin_time = time.time()
    answer = 'yes'
    while(answer == 'yes'):  # get phrase
        while(True):  # get char
            print(selected_phrase_fill)
            # get user imput 1 letter or stop
            char = (input("enter 1 leter and stop to stop game : ")).lower()
            if char == 'stop':
                answer = 'no'
                quit = False
                break
            if len(char) > 1 or not char.isalpha():
                continue
            if char in selected_phrase:
                char_amount = selected_phrase.count(char)
                score += 5
                char_amount_index = 0
                #  fill user letter if exist on phrase on the blank template
                for index in range(len(selected_phrase)):
                    if selected_phrase[index] == char:
                        char_amount_index += 1
                        selected_phrase_fill = selected_phrase_fill[:index] + char + selected_phrase_fill[index +1:]
                    if char_amount_index == char_amount:
                        break
                if selected_phrase_fill == selected_phrase:
                    print(f"You success to find the phrase : {selected_phrase}")
                    # give bonus 100 points if user finish within 29 seconds
                    if time.time() - begin_time < 30:
                        score += 100
                    answer = 'no'
                    yes_no = ''
                    while yes_no != 'yes' and yes_no != 'no':
                        yes_no = input("If you like to play again answer yes/no :").lower()
                    if yes_no == 'no':
                        quit = False
                    break
            else:
                score -= 1
print(f"Your score is {score}")
