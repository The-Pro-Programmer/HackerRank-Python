import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    words = wrapper.wrap(text=string)
    result = ''
    for word in words:
        result += word + '\n'
    return result