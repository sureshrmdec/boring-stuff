class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        N = len(A)
        i = 0
        while i < N:
            if (A[i] > 0 and A[i] <= N):
                swap_pos = A[i]-1
                if A[swap_pos] != A[i]:
                    tmp = A[i]
                    A[i] = A[swap_pos]
                    A[swap_pos] = tmp
                    i-=1
            i+=1
        for i in range(N):
            if i+1 != A[i]:
                return i+1
        return N+1



sol = Solution()

print sol.firstMissingPositive([8,2,5,3,1])
print sol.firstMissingPositive([3,1,2,5])
print sol.firstMissingPositive([1,1,1])
print sol.firstMissingPositive([1,1,2,2,3,2,6,2,1])
print sol.firstMissingPositive([1, 2, 3, 4, 5, 6])
print sol.firstMissingPositive([ 699, 2, 690, 936, 319, 784, 562, 35, 151, 698, 126, 730, 587, 157, 201, 761, 956, 359, 198, 986, 915, 7, 703, 324, 814, 382, 294, 204, 120, 731, 615, 330, 486, 52, 223, 376, 649, 458, 564, 971, 72, 605, 177, 20, 461, 790, 872, 363, 916, 435, 991, 184, 410, 320, 16, 480, 768, 801, 117, 338, 650, 786, 17, 369, 979, 304, 445, 688, 862, 229, 311, 351, 985, 697, 135, 299, 310, 3, 643, 221, 831, 196, 887, 679, 484, 209, 824, 292, 588, 721, 140, 675, 827, 913, 271, 170, 812, 552, 334, 860, 981, 550, 308, 584, 442, 328, 251, 456, 976, 31, 507, 954, 982, 742, 45, 727, 794, 309, 527, 623, 56, 843, 436, 681, 143, 130, 689, 870, 362, 580, 560, 474, 385, 525, 881, 51, 890, 917, 820, 826, 139, 443, 978, 144, 512, 205, 682, 188, 344, 429, 497, 181, 749, 864, 664, 145, 621, 629, 886, 572, 89, 725, 945, 29, 553, 977, 783, 590, 236, 728, 125, 90, 492, 261, 543, 259, 662, 622, 285, 392, 561, 670, 200, 504, 246, 513, 910, 583, 460, 179, 207, 709, 127, 926, 816, 426, 520, 174, 464, 883, 780, 5, 268, 606, 1, 109, 704, 391, 661, 924, 516, 241, 477, 952, 405, 522, 247, 335, 356, 839, 423, 779, 4, 43, 720, 238, 965, 951, 914, 10, 496, 775, 651, 788, 373, 491, 746, 799, 518, 93, 86, 774, 652, 955, 494, 252, 781, 946, 412, 202, 741, 719, 612, 673, 896, 1000, 289, 554, 69, 424, 980, 506, 593, 889, 25, 959, 28, 736, 8, 969, 865, 657, 567, 434, 9, 167, 357, 929, 645, 250, 565, 94, 928, 473, 509, 823, 313, 762, -1, 208, 903, 922, 655, 948, 326, 485, 150, 73, 505, 225, 122, 129, 648, 838, 811, 972, 735, 78, 428, 740, 782, 632, 316, 440, 737, 297, 873, 281, 479, 654, 0, 633, 212, 152, 154, 470, 866, 79, 722, 958, 732, 900, 832, 278, 58, 842, 745, 540, 169, 347, 592, 438, 882, 462, 53, 34, 519, 489, 85, 757, 919, 701, 15, 211, 667, 637, 74, 573, 240, 559, -2, 472, 203, 112, 162, 776, -4, 155, 837, 99, 98, 64, 101, 983, 366, 853, 970, 482, 40, 921, 374, 758, 413, 339, 705, 771, 360, 734, 282, 219, 766, 535, 133, 532, 254 ])
print sol.firstMissingPositive([589, 929, 3, 4, 675, 6, 551, 8, 882, 567, 777, 12, 13, 14, 785, 563, 17, 18, 776, 20, 21, 548, 23, 24, 25, 801, 503, 817, 998, 638, 31, 32, 33, 805, 835, 480, 819, 462, 39, 823, 984, 643, 782, 44, 726, 989, 866, 706, 787, 538, 741, 52, 883, 729, 466, 56, 694, 607, 59, 821, 692, 62, 761, 954, 840, 66, 67, 68, 884, 70, 917, 687, 73, 74, 75, 76, 77, 433, 79, 80, 549, 82, 730, 711, 781, 738, 753, 793, 89, 90, 91, 505, 923, 553, 95, 96, 97, 481, 649, 600, 745, 102, 822, 457, 489, 106, 520, 830, 581, 671, 999, 432, 113, 944, 952, 637, 117, 494, 119, -4, 734, 908, 968, 541, 470, 126, 876, 128, 129, 130, 535, 132, 133, 772, 564, 136, 137, 138, 868, 465, 141, 966, 897, 619, 836, 818, 147, 592, 783, 150, 599, 839, 879, 154, 155, 941, 773, 635, 800, 160, 161, 162, 896, 164, 664, 166, 167, 435, 169, 575, 533, 647, 921, 713, 175, 478, 880, 844, 179, 886, 181, 672, 636, 184, 185, 186, 797, 719, 665, 190, 191, 192, 598, 724, 974, 196, 663, 831, 842, 662, 201, 928, 543, 508, 205, 487, 728, 997, 209, 210, 211, 890, 213, 493, 215, 216, 872, 218, 219, 220, 479, 222, 769, 224, 225, 506, 439, 228, 229, 590, 845, 232, 814, 234, 235, 236, 237, 656, 727, 240, 631, 242, 625, 683, 444, 436, 930, 518, 249, 948, 603, 252, 253, 743, 255, 744, 920, 620, 259, 260, 261, 262, 263, 264, 265, 958, 597, 268, 591, 270, 271, 550, 482, 274, 826, 276, 277, 914, 892, 280, 964, 282, 500, 640, 515, 286, 684, 288, 799, 290, 291, 292, 498, 294, 420, 296, 936, 542, 972, 935, 434, 302, 303, 690, 305, 673, 307, 308, -2, 674, 311, 909, 668, 443, 616, 316, 317, 864, 971, 760, 924, 681, 689, 608, 931, 427, 327, 328, 894, 330, 331, 660, 333, 867, 559, 994, 499, 488, 339, 490, 341, 957, 343, 344, 677, 346, 691, 348, 580, 350, 351, 667, 353, 354, 676, 356, 357, 358, 359, 477, 853, 362, 765, 557, 484, 366, 950, 514, 582, 593, 945, 824, 373, 622, 453, 376, 449, 378, 657, 380, 381, 811, 383, 384, 784, 386, 746, 858, 523, 390, 652, 903, 429, 614, 395, 396, 594, 398, 916, 813, 401, 990, 655, 795, 618, 623, 407, 981, 409, 410, 411, 412, 979, 913, 536, 416, 417, 418])