**Goal:** to break a cipher using a bijective map between letters

**Tools:** Used Wikipedia table of letter frequencies

**Procedure:**
	Since we have access to the letter frequencies of the English language, we can try to compute the frequency of each letter in our given encrypted text and compare it to the frequencies of the English alphabet. Namely, a simple heuristic to create a one-to-one mapping between letters is by sorting the English alphabet in terms of frequencies of occurrence from highest to lowest. Similarly, we can sort the frequencies of letters in the encrypted text from highest to lowest. Then, we can map the most frequently occurring letter in the encrypted text to the most frequently occurring letter in the English language, and so forth. This approach does not look at the particular frequency values themselves to construct the mapping, but rather, the relation of the frequencies amongst the letters (i.e. not the distribution but the order).

**Results:**
	Without the side information and with the procedure described above, the decryption was not very successful and the encrypted text did not become noticeably clearer to understand. This is because our text is very short, and due to the small sample size, the frequencies of the letters in our text do not match the frequencies of letters in the English alphabet. Therefore, the order of frequency matching approach to approximating the mapping of the encryption function is not effective.


**Improvement:** The letter frequencies is insufficient, and the decoded text is not readable. Hence we utilize partial information about the encryption function (this is sisde information, wich is informaiton about hte transmitted data that does not come from the received data but is nonethless helpful in decoding it).