# maps
def formatText(text):
    return f"- {text} "


myText = ["Mido", "Ahmed", "Saved"]
print("#" * 50)
print("map:")
for name in  list(map(lambda text: f"-{text.strip().capitalize()} -", myText)):
    print(name)

print("#" * 50)