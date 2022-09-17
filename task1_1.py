# This is a sample Python script.
modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr', 'StELLa']
indices = [index for (index, item) in enumerate(modern_family)]
characters = []
for i in modern_family:
    characters.append(i)
for i in range(len(characters)):
   characters[i] = characters[i].lower()
   characters[i] = characters[i].replace("_", "-")
temp=list(map(lambda word:len(word),characters))
indices = [sum(i) for i in zip(indices, temp )]
indices.sort(reverse=True)
Phew_finally={indices[i]:characters[i] for i in range(len(characters))}
print(Phew_finally)