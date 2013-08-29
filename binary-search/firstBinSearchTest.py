## test file for firstBinarSearch

import firstBinSearch as fs

print fs.binarysearch([0,1,2],1) == 1
print fs.binarysearch([0,1,2],2) == 2
print fs.binarysearch([0,1,2],0) == 0
print fs.binarysearch([0,1,2,3],1) == 1
print fs.binarysearch([0,1,2,3],2) == 2
print fs.binarysearch([0,1,2,3],3) == 3
print fs.binarysearch([0,1],1) == 1
print fs.binarysearch([0,1],0) == 0
print fs.binarysearch([0],0) == 0
#print fs.binarysearch([],0) == 1
