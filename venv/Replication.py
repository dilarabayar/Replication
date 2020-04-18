
def search(text):
    temp_kmers = dict()
    kmers = dict()
    temp_reverse_complement = []
    temp_kmers_has_reverse = []
    kmer_list = []
    reverse_list = []
    counter = 0

    for j in range(5,len(text)):

        for i in range(0, len(text)):
            pattern = text[i:i+j]
            if (len(pattern) != j):
                break
            if ((pattern in temp_kmers.keys()) and (pattern not in kmers.keys())):
                kmers[pattern] = 2  # Geçiciye eklerken de bir tane vardı o yüzden burası 2'den başlayacak
                reverse_pattern = reverse_complement(pattern) #kmer olduğu için artık reverse arayabilirim.
                temp_reverse_complement.append(reverse_pattern) #temp bir reverse_complemente ekliyorum ki bunu textte aratabilmek için.
                temp_kmers_has_reverse.append(pattern) #patternın kendisini ekliyorum kmerlerin aslını tutabilmek için.
            elif (pattern in kmers.keys()):
                kmers[pattern] += 1  #Artık bundan 1'den fazla olduğu için bu string için geçiciyle işimiz yok
            else:
                temp_kmers[pattern] = 1

        if len(kmers) < 1:
            break  # Bu k ile hiç tekrarlayan string bulunmadı o yüzden daha ileriye gitmeye gerek yok

        kmer_list.append(kmers.copy())
        temp_kmers.clear()
        kmers.clear()  # Bunu da boşalttık çünkü bize en uzun k-merler lazım

    # En uzun kmerleri bastırır.
    print("Longest kmers in text:")
    print(kmer_list[len(kmer_list) - 1])
    print("---------------------------------------")
    #temp_reverse_complementteki elementlerin textte olup olmadığını bulur.Eğer varsa asıl liste olan reverse_liste atar.
    for i in range(0, len(temp_reverse_complement)):
        if ((text.find(temp_reverse_complement[i])) != -1):
            reverse_list.append(temp_kmers_has_reverse[i])

    #En uzun reverse'ü textin içinde olan kmerleri bastırır
    size_of_max_reverse = (max(len(x) for x in reverse_list)) #Reverse_list içerisindeki en uzun elementi bulur.

    print("Longest kmers that has reverse in text:")
    for i in range(0, len(reverse_list)):
        if (len(reverse_list[i]) == size_of_max_reverse) :
            print(reverse_list[i])

def reverse_of_string(s):  #kelimeyi ters çevirmek için
  str = ""
  for i in s:
    str = i + str
  return str

def reverse_complement(seq):  #harfleri değiştirmek için
    seq = reverse_of_string(seq)
    output = ""
    for i in range(0, len(seq)):
        if seq[i] == "a":
            output += "t"
        elif seq[i] == "t":
            output += "a"
        elif seq[i] == "c":
            output += "g"
        elif seq[i] == "g":
            output += "c"
    return output


def main():

    with open("wuhan.txt", 'r') as file:
        wuhan = file.read().replace('\n', '').replace(' ', '')
        wuhan = ''.join([i for i in wuhan if not i.isdigit()])

    print("WUHAN")
    print("*******************************************")
    search(wuhan)

    with open("nepal.txt", 'r') as file:
        nepal = file.read().replace('\n', '').replace(' ', '')
        nepal = ''.join([i for i in nepal if not i.isdigit()])

    print("*******************************************")
    print("NEPAL")
    print("*******************************************")
    search(nepal)
    print("*******************************************")

if __name__ == "__main__":
    main()