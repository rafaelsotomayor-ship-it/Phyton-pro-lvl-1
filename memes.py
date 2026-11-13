meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "aura": "expresion para alguien o algo chevere"
            "laura": "cuando alguien hace algo raro o no chevere o embarazoso"
            "rizz" : "sinonimo para coquetear"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(word,": ", meme_dict[word])
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    print("palabra no encontrada")
    # ¿Qué hacer si no se encuentra la palabra?
