import time
from naive_algorithm import search as search_naive
from kmp_algorithm import search as search_kmp
from boyer_moore import search as search_bm

with open('letters.txt', 'r') as file_handle:
    letters = file_handle.read()

start = time.process_time()
print(search_naive('TAGGACCTGAGCATAGTCTTGCCGAATACCATAATGAATCTGGCTTGAAAACCATTCTTCGTAAGGGTGG\nTCGCACTATTGCCTTTGGAGGCTGTGTGTTCTCTTATGTTGGTTGCCATAACAAGTGTGCCTATTGGGTT', letters))
stop = time.process_time()
print(stop-start)

start = time.process_time()
print(search_kmp('TAGGACCTGAGCATAGTCTTGCCGAATACCATAATGAATCTGGCTTGAAAACCATTCTTCGTAAGGGTGG\nTCGCACTATTGCCTTTGGAGGCTGTGTGTTCTCTTATGTTGGTTGCCATAACAAGTGTGCCTATTGGGTT', letters))
stop = time.process_time()
print(stop-start)

start = time.process_time()
print(search_bm('TAGGACCTGAGCATAGTCTTGCCGAATACCATAATGAATCTGGCTTGAAAACCATTCTTCGTAAGGGTGG\nTCGCACTATTGCCTTTGGAGGCTGTGTGTTCTCTTATGTTGGTTGCCATAACAAGTGTGCCTATTGGGTT', letters))
stop = time.process_time()
print(stop-start)
