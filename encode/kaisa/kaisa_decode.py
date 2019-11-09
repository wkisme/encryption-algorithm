# ord() transfer alpha to ascii
# chr() transfer ascii to alpha
# range()inclusive start, exclusive stop


def kaisa_decode(input_s):
    for bias in range(0, 27):
        output_s = ''
        for i in input_s:
            base = 'A' if i.isupper() else 'a'
            output_s += chr((ord(i) - ord(base) + bias) % 26 + ord(base))

        print(output_s)


if __name__ == "__main__":
    kaisa_decode('def')

