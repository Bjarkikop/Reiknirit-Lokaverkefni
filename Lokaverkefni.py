#Bjarki Ellertsson
import random
import datetime
import sys
minMerge = 32
def fillList(l, amount):
    for x in range(0,amount):
        x= random.randint(0, 1000000)
        l.append(x)

def bubbleSort(l):
    for x in range(len(l) - 1):
        for j in range(len(l) - 1 - x):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

def mergeSort(a):
    currSize = 1
    while currSize < len(a) - 1:
        vinstri = 0
        while vinstri < len(a) - 1:
            mid = min((vinstri + currSize - 1), (len(a) - 1))
            haegri = ((2 * currSize + vinstri - 1,
                      len(a) - 1)[2 * currSize
                                  + vinstri - 1 > len(a) - 1])
            merge(a, vinstri, mid, haegri)
            vinstri += currSize * 2
        currSize *= 2

def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = R[j]
            j += 1
        else:
            a[k] = L[i]
            i += 1
        k += 1
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

def partition(l, low, high):
    index = low - 1
    x = l[high]
    for j in range(low, high):
        if l[j] <= x:
            index += 1
            l[index], l[j] = l[j], l[index]

    l[index + 1], l[high] = l[high], l[index + 1]
    return index + 1

def quickSort(l):
    low = 0
    high = len(l) -1
    size = high - low + 1
    stack = [0] * size
    top = -1
    top += 1
    stack[top] = low
    top += 1
    stack[top] = high
    while top >= 0:
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1
        pivot = partition(l, low, high)
        if pivot - 1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = pivot - 1
        if pivot + 1 < high:
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = high
def calcMinRun(numer):
    run = 0
    while numer >= minMerge:
        run |= numer & 1
        numer >>= 1
    return numer + run
def insertionSort(l, vinstri, haegri):
    for x in range(vinstri + 1, haegri + 1):
        j = x
        while j > vinstri and l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1
def timSort(l):
    lengd = len(l)
    minRun = calcMinRun(lengd)
    for byrjun in range(0, lengd, minRun):
        endir = min(byrjun + minRun - 1, lengd - 1)
        insertionSort(l, byrjun, endir)
    staerd = minRun
    while staerd < lengd:
        for vinstri in range(0, lengd, 2*staerd):
            midja = min(lengd-1, vinstri + staerd -1)
            haegri = min((vinstri+2*staerd-1), lengd-1)
            merge(l, vinstri, midja, haegri)
        staerd *= 2
on = True
while on:
    listi = []
    listi2 = []
    print("1. Bubblesort VS Quicksort")
    print("2. Bubblesort VS Mergesort")
    print("3. Quicksort VS Mergesort")
    print("4. Mergesort VS Timsort")
    print("0. Hætta")

    valmynd = int(input("Sláðu inn tölu fyrir aðgerð\n"))
    if valmynd == 1:
        print("----------------------")
        fjoldi = int(input("Sláðu inn heiltölu fyrir hversu langur listin verður"))
        fillList(listi, fjoldi)
        fillList(listi2, fjoldi)
        worst = input("Viltu hafa reverse lista: j/n ")
        if worst == "n":
            print("----------------------")
            print("Bubblesort")
            a = datetime.datetime.now()
            bubbleSort(listi)
            b = datetime.datetime.now()
            print(b - a, "\n")
            print("Quicksort")
            c = datetime.datetime.now()
            quickSort(listi2)
            d = datetime.datetime.now()
            print(d-c)
        else:
            listi2.sort()
            listi.sort()
            listi.reverse()
            listi2.reverse()
            print("----------------------")
            print("Bubblesort")
            a = datetime.datetime.now()
            bubbleSort(listi)
            b = datetime.datetime.now()
            print(b - a, "\n")
            print("Quicksort")
            c = datetime.datetime.now()
            quickSort(listi2)
            d = datetime.datetime.now()
            print(d - c)
    elif valmynd == 2:
        print("----------------------")
        fjoldi = int(input("Sláðu inn heiltölu fyrir hversu langur listin verður"))
        fillList(listi, fjoldi)
        fillList(listi2, fjoldi)
        print("----------------------")
        print("Bubblesort")
        a = datetime.datetime.now()
        bubbleSort(listi)
        b = datetime.datetime.now()
        print(b - a, "\n")
        print("----------------------")
        print("Mergesort")
        c = datetime.datetime.now()
        mergeSort(listi2)
        d = datetime.datetime.now()
        print(d - c)
        print("----------------------")
    elif valmynd == 3:
        print("----------------------")
        fjoldi = int(input("Sláðu inn heiltölu fyrir hversu langur listin verður"))
        fillList(listi, fjoldi)
        fillList(listi2, fjoldi)
        print("----------------------")
        print("Quicksort")
        a = datetime.datetime.now()
        quickSort(listi)
        b = datetime.datetime.now()
        print(b - a, "\n")
        print("----------------------")
        print("Mergesort")
        c = datetime.datetime.now()
        mergeSort(listi2)
        d = datetime.datetime.now()
        print(d - c, "\n")
        print("----------------------")
    elif valmynd == 4:
        print("----------------------")
        fjoldi = int(input("Sláðu inn heiltölu fyrir hversu langur listin verður"))
        fillList(listi, fjoldi)
        fillList(listi2, fjoldi)
        print("----------------------")
        print("Mergesort")
        a = datetime.datetime.now()
        mergeSort(listi)
        b = datetime.datetime.now()
        print(b - a, "\n")
        print("----------------------")
        print("Timsort")
        c = datetime.datetime.now()
        timSort(listi2)
        d = datetime.datetime.now()
        print(d - c, "\n")
        print("----------------------")
    elif valmynd == 0:
        on = False

