
import requests
import player

def convert_hebrew_number(number_string):
    number_dict = {
        'אחד': 1,
        'אחת': 1,
        'שניים': 2,
        'שתיים': 2,
        'שלוש': 3,
        'ארבע': 4,
        'חמש': 5,
        'שש': 6,
        'שבע': 7,
        'שמונה': 8,
        'תשע': 9,
        'עשר': 10,
        'אחת עשרה': 11,
        'אחד עשרה': 11,
        'שתיים עשרה': 12,
        'שניים עשרה': 12,
        'שלוש עשרה': 13,
        'ארבע עשרה': 14,
        'חמש עשרה': 15,
        'שש עשרה': 16,
        'שבע עשרה': 17,
        'שמונה עשרה': 18,
        'תשע עשרה': 19,
        'עשרים': 20,
        'עשרים ואחד': 21,
        'עשרים ושתיים': 22,
        'עשרים ושלוש': 23,
        'עשרים וארבע': 24,
        'עשרים וחמש': 25,
        'עשרים ושש': 26,
        'עשרים ושבע': 27,
        'עשרים ושמונה': 28,
        'עשרים ותשע': 29,
        'שלושים': 30,
        'שלושים ואחד': 31,
        'שלושים ושניים': 32,
        'שלושים ושתיים': 32,
    }
    num = number_dict.get(number_string, None)
    if num is not None:
        return num
    else:
        return number_string


def parse(text):
    text = text.replace(r'"', r'\"')

    # Set the API URL and the request body
    url = 'https://www.langndata.com/api/heb_parser?token=9347b1703ec71cceb882ef7e924ae280'
    _json = '{"data":"' + text + '"}'

    # Send the POST request
    r = requests.post(url, data=_json.encode('utf-8'), headers={'Content-type': 'application/json; charset=utf-8'})

    # Get the JSON response
    data = r.json()

    # Initialize variables
    teeth = []
    tooth = []
    diagnosis = []
    num_of_teeth = 0
    known_symptoms = {'עששת', 'חור', 'דלקת'}
    free_text = []

    # Check if dep_tree key is present
    if 'dep_tree' in data:
        # Iterate through the dependency tree
        for i in range(len(data['dep_tree'])):
            i = str(i)
            # Find tooth number
            if data['dep_tree'][i]['pos'] == 'CD':
                num_of_teeth = num_of_teeth + 1
                if num_of_teeth > 1:
                    print("המממ זיהיתי שני מספרים, כרגע אני יכול להזין רק שן אחת כל פעם. נסה שנית...")
                    player.play(player.sound_fail)
                    return -1
                print(data['dep_tree'][i]['word'])
                tooth = convert_hebrew_number(data['dep_tree'][i]['word'])
                tooth = float(tooth)
                tooth = int(tooth)

            # Find symptoms
            if (data['dep_tree'][i]['pos'] == 'NN') and (data['dep_tree'][i]['word'] not in {"שיניים", 'שן'}) and (
                    data['dep_tree'][i]['word'] in known_symptoms):
                diagnosis.append(data['dep_tree'][i]['word'])

            # Find free text
            if (data['dep_tree'][i]['pos'] == 'NN') and (data['dep_tree'][i]['word'] not in {"שיניים", 'שן'}) and (
                    data['dep_tree'][i]['word'] not in known_symptoms):
                free_text.append(data['dep_tree'][i]['word'])

        # Append results to teeth list and clear variables
        if ((tooth != []) and (diagnosis != [])) or ((tooth != []) and (free_text != [])):
            teeth.append([(tooth, diagnosis, free_text)])
            player.play(player.sound_success)

        else:
            teeth = -1
            print("מצטער לא זיהיתי שן ומחלה. רוצה לנסות שוב?")
            player.play(player.sound_fail)

    return teeth
