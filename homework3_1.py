calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    set_ = (len(string), string.upper(), string.lower())
    return set_

def is_contains(string, list_to_search):
    count_calls()
    lower_list = []
    for i in range(len(list_to_search)):
        lower_list.append(list_to_search[i].lower())
    if string.lower() in lower_list:
        return True
    else:
        return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)