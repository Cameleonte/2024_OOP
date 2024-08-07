def vowel_filter(function):

    def wrapper():
        result = function()
        return [v for v in result if v in 'aeiouy']

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
