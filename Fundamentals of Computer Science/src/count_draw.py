from collections import Counter
import matplotlib.pyplot as plt

def wc_from_file(infilename, topn=10):

    infile = open(infilename, 'r', encoding='utf-8')
    data = infile.read()
    words = data.split()

    wc_list = Counter(words).most_common(topn)
    #print(wc_list)
    infile.close()

    w_list = [w for w,_ in wc_list]
    c_list = [c for _,c in wc_list]

    return w_list, c_list

def draw_bar(w_list, c_list):

    plt.bar(w_list, c_list, width=0.5)
    plt.ylabel('counts')

    plt.title('# of w(i)')
    plt.savefig('bar_of_wcounts.png')
    plt.show()

#w_list, c_list = wc_from_file('out.txt', 5)
#draw_bar(w_list, c_list)
if __name__ == "__main__":
    w_list, c_list = wc_from_file('out.txt', 5)
    draw_bar(w_list, c_list)
