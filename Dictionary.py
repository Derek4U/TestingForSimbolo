print()
print()


dict1 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}

def max_dict(d):
    max_value = 0
    for key, value in d.items():
        if value > max_value:
            max_value = value
    
    for key, value in d.items():
        if value == max_value:
            return key
# print(max_dict(dict1))

def max_value_key(d):
    return max(d, key = d.get)
# print(max_value_key(dict1))

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 

def count_word_frequency(l):
    set_list = set(l)
    ans = dict()

    for word in set_list:
        ans[word] = l.count(word)

    ans = dict(sorted(ans.items(), key = lambda x:x[1], reverse = True))
    return ans
# print(count_word_frequency(words))

def count_word_frequency2(words):
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# print(count_word_frequency2(words))

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def merge_dict(x, y):
    ans = x.copy()

    for key, value in y.items():
        ans[key] = ans.get(key, 0) + value
    return ans
# print(merge_dict(dict1, dict2))


def filter_dict(x, condition):
    ans = {key : value for key, value in x.items() if condition(key, value)}
    return ans

dict_x = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
filtered_dict = filter_dict(dict_x, lambda key, value: value % 2 == 0)
# print(filtered_dict)



def filter_dict2(x):
    ans = {key : value for key, value in x.items() if value % 2 == 0}
    return ans

dict_x = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
filtered_dict = filter_dict2(dict_x)
# print(filtered_dict)

print()
print()