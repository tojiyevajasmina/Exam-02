def format_name(fish: str) -> str:
    parts = fish.split()
    if len(parts) < 3:
        return fish
    familiya = parts[0]
    ism = parts[1]

    sharif_str = ""
    for i in range(2, len(parts)):
        sharif_str += parts[i]
        if i != len(parts) - 1:
            sharif_str += " "

    return ism + " " + sharif_str + ", " + familiya

print(format_name("Aliyev Vali G'aniyevich"))
# "Vali G'aniyevich, Aliyev"