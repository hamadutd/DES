#Hamad Redha Alsafi


############Generate all the tables#############
def tablesFunc(tableName):
    
    #Initial permutation table
    if tableName=="initPermutationT":
        return [58, 50, 42, 34, 26, 18, 10, 2,  
                60, 52, 44, 36, 28, 20, 12, 4,  
                62, 54, 46, 38, 30, 22, 14, 6,  
                64, 56, 48, 40, 32, 24, 16, 8,  
                57, 49, 41, 33, 25, 17, 9, 1,  
                59, 51, 43, 35, 27, 19, 11, 3,  
                61, 53, 45, 37, 29, 21, 13, 5,  
                63, 55, 47, 39, 31, 23, 15, 7]
    
    #Expansion D-box table 
    elif tableName=="ExpansionDT":
        return [32, 1 , 2 , 3 , 4 , 5 , 4 , 5,  
         6 , 7 , 8 , 9 , 8 , 9 , 10, 11,  
         12, 13, 12, 13, 14, 15, 16, 17,  
         16, 17, 18, 19, 20, 21, 20, 21,  
         22, 23, 24, 25, 24, 25, 26, 27,  
         28, 29, 28, 29, 30, 31, 32, 1 ]

    #Straight permutaion table 
    elif tableName=="StrightPerT":
        return [ 16,  7, 20, 21, 
        29, 12, 28, 17,  
         1, 15, 23, 26,  
         5, 18, 31, 10,  
         2,  8, 24, 14,  
        32, 27,  3,  9,  
        19, 13, 30,  6,  
        22, 11,  4, 25 ]

    #Final permutaion table
    elif tableName=="finalPermutaionT":
        return [ 40, 8, 48, 16, 56, 24, 64, 32,  
               39, 7, 47, 15, 55, 23, 63, 31,  
               38, 6, 46, 14, 54, 22, 62, 30,  
               37, 5, 45, 13, 53, 21, 61, 29,  
               36, 4, 44, 12, 52, 20, 60, 28,  
               35, 3, 43, 11, 51, 19, 59, 27,  
               34, 2, 42, 10, 50, 18, 58, 26,  
               33, 1, 41, 9, 49, 17, 57, 25 ]

    #Key compression table 
    elif tableName =="keyCompressionT":
        return [14, 17, 11, 24, 1, 5,  
            3, 28, 15, 6, 21, 10,  
            23, 19, 12, 4, 26, 8,  
            16, 7, 27, 20, 13, 2,  
            41, 52, 31, 37, 47, 55,  
            30, 40, 51, 45, 33, 48,  
            44, 49, 39, 56, 34, 53,  
            46, 42, 50, 36, 29, 32 ]
    
    #Parity bit drop table
    elif tableName=="keyParityT":
        return [57, 49, 41, 33, 25, 17, 9,
                1, 58, 50, 42, 34, 26, 18,
                10, 2, 59, 51, 43, 35, 27, 
                19, 11, 3, 60, 52, 44, 36, 
                63, 55, 47, 39, 31, 23, 15, 
                7, 62, 54, 46, 38, 30, 22,  
                14, 6, 61, 53, 45, 37, 29, 
                21, 13, 5, 28, 20, 12, 4 ]

    #Number of left shifts table
    elif tableName=="shiftLeftT":
        return [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 ]
    
     #S-box table
    elif tableName=="sbox":
        return [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],  
          [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],  
          [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],  
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]], 
             
         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],  
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],  
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],  
           [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],  
    
         [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],  
           [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],  
           [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],  
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],  
        
          [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],  
           [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],  
           [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],  
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],  
         
          [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],  
           [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],  
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],  
           [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],  
        
         [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],  
           [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],  
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],  
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],  
          
          [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],  
           [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],  
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],  
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],  
         
         [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],  
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],  
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],  
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]

#############Conversion################
#Matching pursuit dictionary     
def mpDict(sw):
    #if turning from Hex To Bin
    if sw == 1:
        return {'0' : "0000", '1' : "0001", '2' : "0010", '3' : "0011", '4' : "0100", 
              '5' : "0101", '6' : "0110", '7' : "0111", '8' : "1000",  '9' : "1001", 'A' : "1010", 
              'B' : "1011",  'C' : "1100", 'D' : "1101",  'E' : "1110",'F' : "1111" }
    #if turning from Bin To Hex
    elif sw == 2:
        return {"0000" : '0',  "0001" : '1', "0010" : '2', "0011" : '3', "0100" : '4', "0101" : '5', "0110" : '6', "0111" : '7',  
          "1000" : '8', "1001" : '9',  "1010" : 'A', "1011" : 'B', "1100" : 'C',  "1101" : 'D', "1110" : 'E', "1111" : 'F' }   

def turningHexToBinFunc(inp): 
    binary = "" 
    for i in range(len(inp)): 
        binary = binary + mpDict(1)[inp[i]] 
    return binary
      
def turningBinToHexFunc(inp):
    hexadecimal = "" 
    for i in range(0,len(inp),4): 
        char = "" 
        char = char + inp[i] 
        char = char + inp[i + 1]  
        char = char + inp[i + 2]  
        char = char + inp[i + 3]  
        hexadecimal = hexadecimal + mpDict(2)[char]        
    return hexadecimal
  
def binaryToDecimalFunc(binary):        
    binary1 = binary  
    decimal, i, n = 0, 0, 0
    while(binary != 0):  
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)  
        binary = binary//10
        i += 1
    return decimal 
  
def decimalToBinary(number):  
    decimalToBinary
    result = bin(number).replace("0b", "") 
    return result.zfill(4)

############Functions#############
#XOR function to calculate two strings of binary numbers 
def xorfUNC(a, b): 
    calculate = "" 
    for i in range(len(a)): 
        if a[i] == b[i]: 
            calculate = calculate + "0"
        else: 
            calculate = calculate + "1"
    return calculate

#Shift the bits to left by nth NumberOfshifts function
def shiftleftFUNC(k, NumberOfshifts): 
    s = "" 
    for i in range(NumberOfshifts): 
        for j in range(1,len(k)): 
            s = s + k[j] 
        s = s + k[0] 
        k = s 
        s = ""  
    return k

#Permute function to rearrange bits 
def permuteFUNC(key, InputArray, n): 
    permutProcess = "" 
    for i in range(0, n): 
        permutProcess = permutProcess + key[InputArray[i] - 1] 
    return permutProcess   
 
    
##############DES ENCRYPTION FUNCTION################
def encryptFUNC(pt, RoundKeysBin, RoundKeysHexa): 
    pt = turningHexToBinFunc(pt) 
      
    #perform initial permutation on the plain text where 64 bit plain text block is Transferred to an initial Permutation
    pt = permuteFUNC(pt, tablesFunc("initPermutationT"), 64) 
      
    #the resulting of 64 bit permuted block of text is divided into two half blocks,where each half consists of 32 bits
    left = pt[0:32] 
    right = pt[32:64]

    #each half of block consist of 16 rounds
    for i in range(0, 16):
        
        #expand the 32 bits data into 48 bits using expansion D-box table 
        rightExpand = permuteFUNC(right, tablesFunc("ExpansionDT"), 48) 
          
        #XOR for RoundKeysBin[i] and rightExpand by call xorFunc
        XOR = xorfUNC(rightExpand, RoundKeysBin[i]) 
  
        #substitue values from s-box table by calculating row and column  
        straightPer = "" 
        for j in range(0, 8): 
            row = binaryToDecimalFunc(int(XOR[j*6] + XOR[j*6 + 5])) 
            column = binaryToDecimalFunc(int(XOR[j*6 + 1] + XOR[j*6 + 2] + XOR[j*6 + 3] + XOR[j*6 + 4])) 
            value = tablesFunc("sbox")[j][row][column] 
            straightPer = straightPer + decimalToBinary(value) 
              
        #after substituting, rearranging the bits by using straight permutaion table   
        straightPer = permuteFUNC(straightPer,tablesFunc("StrightPerT"), 32) 
          
        #XOR for left and straightPer 
        result = xorfUNC(left, straightPer) 
        left = result 
          
        #swap 
        if(i != 15):
            temp=right
            right=left
            left=temp
   
    #combine the permuted two blocks
    combine = left + right 
      
    #final permutaion of bits to get cipher text 
    cipherText = permuteFUNC(combine, tablesFunc("finalPermutaionT"), 64) 
    return cipherText

#################User Input########################
print("------------------------------------")
print('   Welcome to DES algorithm tool    ')
print("------------------------------------")

#user enter the plain text and store the value in pt
messageInput = input("Enter the message: ")
pt=messageInput.upper()

#user enter the key and store the value in key
keyInput = input("Enter the key: ")
key=keyInput.upper()

#################Key generation##################### 
#convert key from hex to binary 
key = turningHexToBinFunc(key) 
  
#call parity bit drop table and store the value in keyParity
keyParity= tablesFunc("keyParityT")
  
#By using the parity bits, get 56 bit key from 64 bit  
key = permuteFUNC(key, keyParity, 56) 
  
#call number of bit shifts table and store value in shiftTable
shiftTable = tablesFunc("shiftLeftT")
  
#call Key compression table and store value in keyCompression
keyCompression = tablesFunc("keyCompressionT")
  
#split the key into right and left, where RoundKeysBin for Round keys in binary and RoundKeysHexa for Round keys in hexadecimal
left = key[0:28]     
right = key[28:56]    
  
RoundKeysBin = [] 
RoundKeysHexa  = []

for i in range(0, 16): 
    #shifting the bits from shift table to nth changes
    left = shiftleftFUNC(left, shiftTable[i]) 
    right = shiftleftFUNC(right, shiftTable[i]) 
      
    #after shifting compine left and right string 
    combineString = left + right 
      
    #compression the key from 56 into 48 bits  
    roundKey = permuteFUNC(combineString, keyCompression, 48) 
   
    RoundKeysBin.append(roundKey) 
    RoundKeysHexa.append(turningBinToHexFunc(roundKey))
    

print("------------------------------------") 
cipherText = turningBinToHexFunc(encryptFUNC(pt, RoundKeysBin, RoundKeysHexa)) 
print("Cipher Text: ",cipherText) 
  

#reverse  
RoundKeysBinReverse = RoundKeysBin[::-1] 
RoundKeysHexaReverse = RoundKeysHexa[::-1]

plainText = turningBinToHexFunc(encryptFUNC(cipherText,RoundKeysBinReverse,RoundKeysHexaReverse))
print("Plain Text: ",plainText)

print("------------------------------------")
print("-------------Thank You--------------")
