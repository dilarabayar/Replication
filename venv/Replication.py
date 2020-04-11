
def bruteForce(text,pattern):

    count = 0

    if pattern in text:
        ind = text.find(pattern)
        while ind!=-1:
            ind = text.find(pattern,ind+1)
            count = count + 1
#eğer patterndan sadece 1 tane vaarsa kmers olmuyor o yüzden eklemesin.
    if (count > 1):
        kmers.append(pattern)
        print(pattern)
        rates.append(count)
    pass

def search(text):
    i = 0

#Inner for loop doğru çalışıyor ancak outer ekleyince çok uzun sürüyor ve ikinci for loopa sadece 1 kez giriyor.
    for j in range(5,len(text)):
        for pattern in range(0, len(text)):
            pattern = text[i:i+j]
            #if statement sadece boyutu (ör:başta 5 olanları) alsın ve kmers'de yoksa brute force yapsın dedim.aynı string için tekrar tekrar arama yapmasın diye.
            if ((len(pattern) == j) and (pattern not in kmers)):
                bruteForce(text,pattern)
            i = i + 1
        print(j)
        j = j + 1
pass


def main():

    global rates, kmers
#kmers pattern tutmak için rates de kaç defa stringde bulunduklarını tutmak için. nepal ve wuhan için ayrı ayrı array gerekiyor.
    rates = []
    kmers = []

    '''Texti bütün tek bir string haline getiriyor.
        Method olarak yapacaktım aslında ama open içine variable yazmak sürekli hata verdiği için beceremedim LOL o yüzden her text için
        ayrı ayrı open methodları var.'''

    with open("wuhan.txt", 'r') as file:
        wuhan = file.read().replace('\n', '').replace(' ', '')
        wuhan = ''.join([i for i in wuhan if not i.isdigit()])

    with open("nepal.txt", 'r') as file:
        nepal = file.read().replace('\n', '').replace(' ', '')
        nepal = ''.join([i for i in nepal if not i.isdigit()])

    search(nepal)

    for x in kmers:
        print(x)
    for y in rates:
        print(y)
    pass

if __name__ == "__main__":
    main()