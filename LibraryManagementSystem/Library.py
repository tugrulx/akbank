class Library:
    __file = None

    def __init__(self):  # const
        self.__file = open("books.txt", 'a+')

    def __del__(self):  # deconst
        self.__file.close()

    def list_books(self):
        self.__file.seek(0)  # cursoru en başa almalıyım
        all_books = str.splitlines(self.__file.read())
        count = 1
        for book in all_books:  # her bir kitap için
            fields = book.split(',')  # kitabı oluşturan bilgiler (,) ile ayrıldığından ayırıp
            print()
            print("Title " + str(count) + " " + fields[0])
            # projede istenilen şekilde sadece name ve author yazdırıyorum bu da ilk 2 fielde tekabul ediyor
            print("Author " + str(count) + " " + fields[1])
            count += 1

    def add_book(self):
        title = input("What is the book title? ")
        author = input("Who is the author?  ")
        reyear = int(input("Release year? "))
        num_of_pages = int(input("How many pages is the book? "))
        book = title + "," + author + "," + str(reyear) + "," + str(num_of_pages) + "\n"
        # kitabı oluşturacak gerekli bilgileri alıp
        # , kullanarka oluşturuyorum,sonuna newline ekliyorum
        self.__file.write(book)
        print("Added succesfully")

    def remove(self):
        title = input("What is the title of the book you want to remove? ")
        self.__file.seek(0)
        old_all_books = str.splitlines(self.__file.read())
        new_all_books = list()
        for book in old_all_books:
            fields = book.split(",")
            if title.lower() != fields[0].lower():  # fields[0] kitabın title attribute'ne karsılık geliyor, eğer ki
                new_all_books.append(book)  # kitabın title'i input olarak alınan title'a eşitse listeye eklemiyorum
                # tümünü ekleyip istenileni silmek yerine başlangıçta oluştururken eklemiyorum yani.

        self.__file.truncate(0)  # books.txt'nin boyutunu 0'a indiriyorum yani içindekiler siliniyor.
        for new_book in new_all_books:  # yeni listeyi ekliyorum.
            self.__file.write(new_book + "\n")
        print("Removed succesfully")


lib = Library()


def show_menu():
    print("*** MENU ***")
    print("1-) List Books ")
    print("2-) Add Book ")
    print("3-) Remove Book ")
    return int(input("What you want to do? (Exit for anything else) : "))


choice = show_menu()
while choice in [1, 2, 3]:
    if choice == 1:
        lib.list_books()
    elif choice == 2:
        lib.add_book()
    else:
        lib.remove()
    choice = show_menu()

del lib
