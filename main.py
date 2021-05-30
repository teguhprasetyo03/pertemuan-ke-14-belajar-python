# arbitrary keyword arguments

def sambung_kata(**kwargs):
    print(kwargs)
    print(type(kwargs))

sambung_kata(a="Belajar", b="Python", c="di", d="KelasCoding\n")

# menampilkan stringnya
def sambung(**kata):
    for i in kata:
        print(i)

sambung(a="Belajar", b="Python", c="di", d="KelasCoding", e="John")

# menampilkan isi di dalamnya, dengan menambahkan .values()
def sambung(**kata):
    for i in kata.values():
        print(i)

sambung(a="Belajar", b="Python", c="di", d="KelasCoding", e="John")

def menyambung(**kata):
    hasil = ""
    for i in kata.values():
        hasil += i
    return hasil

print(menyambung(a="Belajar", b="Python", c="di", d="KelasCoding", e="John"))

def menyambung(**kata):
    hasil = ""
    for i in kata.values():
        hasil += i + " "
    return hasil

print(menyambung(a="Belajar", b="Python", c="di", d="KelasCoding", e="John"))

# menggabungkan parameter biasa, artbitrary argument dan arbitrary keyword argument
def coba(var1, var2, *args, **kwargs):
    print(var1)
    print(var2)
    print(args)
    print(kwargs)

coba(10,20,30,40,50, a= 60, b = 70, c=80)

# def coba(var1, var2, **kwargs, *args):
#    print(var1)
#    print(var2)
#    print(args)
#    print(kwargs)

# coba(10,20,a= 60, b = 70, c=80,30,40,50, )

def my_function(**kid):
    print("Hi last name is "+ kid["fname"])

my_function(fname="Tobing", lname="Jun")

