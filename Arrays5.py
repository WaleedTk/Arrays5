from array import *
array_num = array('i', [1,3,5,7,9])
print('buffer size is '+str(array_num.buffer_info))
print('memory buffer is '+str(array_num.buffer_info()[1]))