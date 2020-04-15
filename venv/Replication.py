def search(text):
    gecici = dict()
    kmers = dict()
    kmer_list = []

    for j in range(5,len(text)):

        for i in range(0, len(text)):
            pattern = text[i:i+j]
            if (len(pattern) != j):
                break

            if ((pattern in gecici.keys()) and (pattern not in kmers.keys())):
                kmers[pattern] = 2  # Geçiciye eklerken de bir tane vardı o yüzden burası 2'den başlayacak
            elif (pattern in kmers.keys()):
                kmers[pattern] += 1  #Artık bundan 1'den fazla olduğu için bu string için geçiciyle işimiz yok
            else:
                gecici[pattern] = 1

        if len(kmers) < 1:
            break  # Bu k ile hiç tekrarlayan string bulunmadı o yüzden daha ileriye gitmeye gerek yok
        kmer_list.append(kmers.copy())
        gecici.clear()
        kmers.clear()  # Bunu da boşalttık çünkü bize en uzun k-merler lazım

    return kmer_list[len(kmer_list) - 1]  # Son elemanı döndür


def main():

    with open("wuhan.txt", 'r') as file:
        wuhan = file.read().replace('\n', '').replace(' ', '')
        wuhan = ''.join([i for i in wuhan if not i.isdigit()])

    longest_kmers = search(wuhan)
    print("wuhan", str(longest_kmers))

    with open("nepal.txt", 'r') as file:
        nepal = file.read().replace('\n', '').replace(' ', '')
        nepal = ''.join([i for i in nepal if not i.isdigit()])

    longest_kmers = search(nepal)
    print("nepal", str(longest_kmers))


if __name__ == "__main__":
    main()
