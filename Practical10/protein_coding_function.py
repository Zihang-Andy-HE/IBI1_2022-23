def protein_coding(input):
    sequence = input.upper()
    start = sequence.find('ATG')
    stop = sequence.rfind('TGA')
    distance = stop - start
    all_length = len(sequence)
    if distance > 0.5 * all_length:
        print('protein-coding')
    elif distance < 0.1 * all_length:
        print('non-coding')
    else:
        print('unclear')

#example:
protein_coding('ATgaaattgcTGaacccc')
