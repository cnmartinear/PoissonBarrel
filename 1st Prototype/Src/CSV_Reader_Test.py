'''
Created on Aug 26, 2016

@author: Skyler
'''

import CSV_Reader

def main():
    fileName = input( 'Enter the name of a file: ')
    
    reader = CSV_Reader.CSV_Reader()
    
    rowData = reader.readFile( fileName )
    
    if not rowData:
        error = reader.getLastError()
        
        if error == CSV_Reader.CSV_ERROR_INVALID_FILE_PATH:
            print( "Error: Invalid File Path" )
        
        elif error == CSV_Reader.CSV_ERROR_EMPTY_FILE:
            print( "Error: Empty File" )
        
        elif error == CSV_Reader.CSV_ERROR_INVALID_FILE_CONTENT:
            print( "Error: Invalid File Content" )
            
        return
            
    count = 1
    
    for row in rowData:
        rowString = "Row " + str( count )  + ": "
        
        count += 1
        
        for cell in row:
            rowString += cell + " "
            
        print( rowString )
        
        
def testDocString():
    
    print( CSV_Reader.CSV_Reader.__doc__ )
    print( CSV_Reader.CSV_Reader.getLastError.__doc__)
    print( CSV_Reader.CSV_Reader.readFile.__doc__ )
    
if __name__ == '__main__':
    #main()
    testDocString()
