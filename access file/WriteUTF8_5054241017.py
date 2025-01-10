file = open(r"D:\aaa\piton\dasprog\access file\quotes.txt", "w", encoding="utf8")

quotes = "Ignorance is a Bliss"
jepun = "猿も木から落ちる"
file.write(quotes)
file.write("\n")
file.write(jepun)

file.close()

with open(r"D:\aaa\piton\dasprog\access file\quotes.txt", encoding="utf8") as f:
    for line in f:
        print(line.strip())