def filter_swears(text, swear_list):
    for word in swear_list:
        word = word.strip()
        if word:
            replacement = word[0] + '*' * (len(word) - 1)
            text = text.replace(word, replacement)
    return text

def get_swears():
    with open('swears.txt', 'r') as swears:
        return swears.readlines()

def check_swears(text, swear_list):
	for swear in swear_list:
		if text.contains(swear):
			return True
		else:
			return False
