
def splitByDoubleZeros(doc_num):
    #print('sbdz')
    # finds index of last zero, not including any trailing zeroes
    num_trailing = 0
    temp_ind = len(doc_num) - 1
    while doc_num[temp_ind] == str(0):
        num_trailing += 1
        temp_ind -= 1
    
    last_zero_ind = doc_num[:len(doc_num) - num_trailing].rindex('0')
    
    # [qid, r]
    return [doc_num[:last_zero_ind - 1], doc_num[last_zero_ind + 1:]]
    
    
currqid = 1
old_qids = [1,5,6,15,25,29,36,40,42,44,46,49,54,56,57,58,63,67,77,78]
new_lines = []
currfile = '05gfp_a.txt'
with open(currfile, 'r') as fr:
    lines = fr.readlines()
for line in lines:
    pieces = line.split(" ")
    if currqid <= 20 and pieces[0][:-1] != str(old_qids[currqid - 1]):
        print(str(currqid) + " completed")
        currqid += 1
    pieces[0] = str(currqid) + pieces[0][-1]
    pieces[2] = str(currqid) + '00' + splitByDoubleZeros(pieces[2])[1]
    new_lines.append(" ".join(pieces))
with open("n" + currfile, 'w') as fw:
    fw.writelines(new_lines)
    