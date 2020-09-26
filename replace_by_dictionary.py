import argparse


def get_parser():
    parser = argparse.ArgumentParser(description="Replace words by dictionary and do BPE operations for XLM")

    parser.add_argument("--dict_path", type=str, default="./dict.zh-en.unique", help="Path of the dictionary")
    parser.add_argument("--src_path", type=str, default="", help="Path of source")
    parser.add_argument("--tgt_path", type=str, default="", help="Path of target")

    return parser


if __name__ == '__main__':

    # generate parser / parse parameters
    parser = get_parser()
    params = parser.parse_args()

    dict_pth = params.dict_path
    dict_unique = {}

    print('---------------------read dictionary---------------------')
    with open(dict_pth, 'r', encoding='utf-8') as fin:
        for line in fin:
            line = line.strip()
            idx = line.find(' ')
            word_src = line[:idx]
            word_tgt = line[idx + 1:]
            if word_src not in dict_unique.keys():
                dict_unique[word_src] = word_tgt
    fin.close()

    print('------------------replace by dictionary------------------')
    src_path = params.src_path
    src2tgt_path = params.tgt_path


    count = 0
    n = 0

    fin_src = open(src_path, 'r', encoding='utf-8')
    fout_src2tgt = open(src2tgt_path, 'w', encoding='utf-8')
    sentences = []
    for line in fin_src:
        line = line.strip()
        words = line.split()
        words2tgt = []
        for word in words:
            if word in dict_unique:
                count += 1
            words2tgt.append(dict_unique.get(word, word))
            n += 1
        sentences.append(' '.join(words2tgt))
    fout_src2tgt.write('\n'.join(sentences) + '\n')
    fout_src2tgt.close()
    print('Replace %i words， %i words in total，percentage: %f' % (count, n, count / float(n)))
