import random

def generate_sequences(length):
    out =''
    for i in range(length):
            num = int(random.randint(0,100000)%4)
            if(num==0):
                out += 'A'
            if(num==1):
                out += 'T'
            if(num==2):
                out += 'G'
            if(num==3):
                out += 'C'
    return out

#2
def generate_multiple_sequences(num_seq, len_seq):
    sequences =[]
    for i in range(num_seq):
        sequences.append(generate_sequences(len_seq))
    return sequences
#3+4
def binding_sites(seq_len, num_var_pos, num_seq):
    b_sites = []
    seq = generate_sequences(seq_len)
    rand_pos = random.sample(range(seq_len), num_var_pos)
    for pos in rand_pos:
        seq[pos] = "*"
    for i in range(num_seq):
        site = list(seq)
        for pos in rand_pos:
            num = int(random.randint(0,100000)%4)
            if(num==0):
                site[pos] = 'A'
            if(num==1):
                out += 'T'
            if(num==2):
                out += 'G'
            if(num==3):
                out += 'C'
