def learnDataType():
    #print
    print("Let's Learn Data Type with Python")
    
    greeting = "hello World"

    print(greeting+": apa kabar dunia")

    addition = 1+3

    result = addition - 1

    print(result)

    #input
    name = input("Masukkan nama anda: ")

    print(name)

    #this is comment with python

    #comment use tag
    """
    Ini adalah Block Comment,
    Teks ini akan diabaikan oleh Python.
    """

    #inisialitation and data type
    #int
    age = 17
    salary = 5000000.0

    print(type(age))
    print(type(salary))

    x = 6
    print(type(x))

    x = 6.0
    print(type(x))

    x = 1+2j
    print(type(x))

    var = 10
    print(var)
    print(id(var))
    var = 11
    print(var)
    print(id(var))

    #boolean
    x = True
    print(type(x))

    x = False
    print(type(x))

    #string
    x = 'Dicoding'
    y = "10"
    print(type(x))
    print(type(y))

    multi_line = """Halo!
    Kapan terakhir kali kita bertemu?
    Kita bertemu hari Jum’at yang lalu."""

    print(multi_line)

    x = 'Dicoding'
    print(x[0])

    x = 'Dicoding'
    print(x[2:])

    #Formatted String
    name = "Perseus Evans"
    print(f"Hello, nama saya {name}")

    # %-formatting
    name = "Perseus Evans"
    print("Nama saya %s" % (name))

    #str format
    name = "Perseus Evans"
    print("Nama saya {}".format(name))

    #list
    x = [1, 2.2, 'Dicoding']
    print(type(x))

    x = [1, 'Dicoding', True, 1.0]

    print(x[2])

    x = [1, 2.2, 'Dicoding']
    x[0] = 'Indonesia'
    print(x)

    x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

    print(x[0:3:3]) #first is index 0, midle is length of array what we want to use, last is index
    print(x[1:]) #delete the first one from front array
    print(x[:3]) # take the three from front array

    #tuple
    x = (1, "Dicoding", 1+3j)
    print(type(x))

    x = (5, 'program', 1+3j)
    print(x[1])
    print(x[0:3])
    
    """
    x = (5, 'program', 1+3j)
    x[1] = 'Dicoding'

    Output:
    'tuple' object does not support item assignment
    """

    #set
    x = {1, 2, 7, 2, 3, 13, 3}
    print(x)
    print(type(x))  


    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    union = set1.union(set2)
    print("Union:", union)

    intersection = set1.intersection(set2)
    print("Intersection:", intersection)

    #dictionari
    x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

    print(type(x))

    print(x ['name'])

    x ['Job'] = "Web Developer"
    print(x)

    del x['isMarried']

    print(x)

    #convertion
    print(float(5))

    print(int(5.6))
    print(int(-5.6)) 

    print(type(int("25")))
    print(type(str(25)))
    print(type(float("25")))
    print(type(str(25.6)))

    print(set([1,2,3]))
    print(tuple({5,6,7}))
    print(list('hello'))

    print(dict([[1,2],[3,4]]))
    print(dict([(3,26),(4,44)]))

