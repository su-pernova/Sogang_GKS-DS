input = '''Korean studies is an academic discipline that focuses on the study of Korea, which includes the Republic of Korea, the Democratic People's Republic of Korea, and diasporic Korean populations. Areas commonly included under this rubric include Korean history, Korean culture, Korean literature, Korean art, Korean music, Korean language and linguistics, Korean sociology and anthropology, Korean politics, Korean economics, Korean folklore, Korean ethnomusicology and increasingly study of Korean popular culture. It may be compared to other area studies disciplines, such as American studies and Chinese studies. Korean studies is sometimes included within a broader regional area of focus including "East Asian studies".'''

freq = 0
for w in input.split():
    if w.lower().find('korea') != -1 :
        freq = freq + 1

print(freq)
        
