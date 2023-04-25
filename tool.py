import winsound

def testSound1():
    print("Testing Sound 1...")
    frequency = 1000  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


def testSound2():
    print("Testing Sound 2...")
    frequency = 600  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

