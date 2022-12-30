"""
message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😃",
    ":(": "😞"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)
"""
#FUNCION


def emoji_conventor(message):
    words = message.split(" ")
    emojis = {
        ":)": "😃",
        ":(": "😞"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_conventor(message))