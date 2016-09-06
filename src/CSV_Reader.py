'''
CSV_Reader
Authors:
Richard Dunham

'''
import csv

#Error Constants returned by CSV_Reader.getLastError()
CSV_NO_ERROR = 0
CSV_ERROR_INVALID_FILE_PATH = 1
CSV_ERROR_EMPTY_FILE = 2
CSV_ERROR_INVALID_FILE_CONTENT = 3


class CSV_Reader( object ):
    '''Class: CSV_Reader
    Desc: This class's responsibilities includes validating and parsing 
          comma and tab separated value files
    Public Methods:
        __init__()
        readFile()
        getLastError()'''
    
    def __init__( self ):
        '''class constructor'''
        self.lastError = CSV_NO_ERROR
        self.delimiter = None
        self.quotechar = None
    
    def getLastError( self ):
        '''Method: getLastError()
        Desc: returns a value describing the last error that 
              occurred from calling readFile()
        Access: Public
        Returns: an error constant integer, see Error Constants '''
        
        return self.lastError
    
    def getRowData( self, fileHandle ):
        '''Method: getRowData()
        Desc: given a valid csv file object, the method returns
        a list of rows, where each row is a list of string values
        Args:
        fileHandle - file object
        Access: Private
        Returns: a list of rows of string values'''
        self.lastError = CSV_NO_ERROR
        reader = csv.reader( fileHandle, delimiter = self.delimiter, quotechar = self.quotechar )
        
        rowData = []
        
        for row in reader:
            rowData.append( row )
            
        return rowData
        
    
    def validate(self, fileContent ):
        '''Method: validate()
        Desc: determines whether the contents of a file conforms to
              either comma or tab delimited files
              
        Args:
            fileContent - the content of the file to be parsed
        Access: Private
        Returns: True if the file content is valid otherwise returns False
        '''
        dialect = None
        
        try:
            dialect = csv.Sniffer().sniff( fileContent )
            
        except:
            return False
        
        #verify the delimiter type
        if dialect.delimiter == ',' or dialect.delimiter == '\t':
            self.delimiter = dialect.delimiter
            self.quotechar = dialect.quotechar
            return True
        
        return False
    
    def readFile( self, filePath ):
        '''Method: readFile()
        Desc: given a valid path to a .csv file, this method validates 
              the file content and parses the file content into rows of string values
        Args:
                filePath - the path of the .csv file
        Access: Public
        Returns: if the path and file content are valid the method returns
                 a list rows where each row is a list of string values, 
                 otherwise returns None'''
        try:
            fileHandle = open( filePath, 'r' )
            
            
        except:
            self.lastError = CSV_ERROR_INVALID_FILE_PATH
            return None
        
        fileContent = fileHandle.read()
        
        #return if the file is empty
        if len( fileContent ) == 0 :
            self.lastError = CSV_ERROR_EMPTY_FILE
            fileHandle.close()
            return None
        
        #validate the file content
        if not self.validate( fileContent ):
            self.lastError = CSV_ERROR_INVALID_FILE_CONTENT
            fileHandle.close()
            return None
        
        #reset the file handle
        fileHandle.seek( 0 )
    
        rowData = self.getRowData( fileHandle )
        
        fileHandle.close()
        
        return rowData