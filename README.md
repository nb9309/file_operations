# file_operations

==============================================
				Operations on Files
==============================================
=>On the files, we can perform Two Types of Operations. They are
		1) Write Operation
		2) Read Operation.
  
------------------------------
Write Operation:
------------------------------
=>The  purpose of write operation is that " To transfer or save the object data of main memory as record in the file of secondary memory".
=>Steps:		
		1) Choose the File Name
		2) Open the File Name in Write  Mode   
		3) Perform cycle of Write Operations.
=>While we are performing write operations, we get the following exceptions.
			a) IOError
			b) OSError
			c) FileExistError
   
------------------------------
Read Operation:
------------------------------
=>The  purpose of read operation is that " To transfer or read the record from file of secondary memory into the object of main memory".
=>Steps
		a) Choose the file name
		b) Open the file name in Read Mode  
		c) Perform cycle of read operations.
=>While we are performing read operations, we get the following exceptions.
		a) FileNotFoundError
		b) EOFError
================================x==============================================================




==================================================
						File Opening Modes
==================================================
=>The purpose of File Opening Modes is that "To Open a Perticular File with the Specified Mode".
=>In Otherwords, File Opening Modes makes us to understand In which Mode we are opening the File.
=>In Python Programming, we have 8 File Opening Modes. They are

			1. r
			2. w
			3. a
			4. r+
			5. w+
			6. a+
			7. x
			8. x+
-------------------------------------------------------------------------------------------------------------------------------------------------------------
 r
-------------------------------------------------------------------------------------------------------------------------------------------------------------
=>This Mode is used for Opening the Specified File Name in Read Mode and we perform Read Operations only.
=>If we don't specify any file opening mode then by default PVM treated  as "r" mode as deafult file mode.
=>If we open any file name in "r" mode and If that file name does not exist in Secondary Memory then we get 
    FileNotFoundError.
    
-------------------------------------------------------------------------------------------------------------------------------------------------------------
 w
-------------------------------------------------------------------------------------------------------------------------------------------------------------
=>This mode is used for Creating New File and Opens in Write Mode.
=>If we Choose NEW FILE and the Mode is "w" then PVM Creates New File and Opened in write Mode and we Can 
    Perform Write Operations Only.
=>If we Choose EXISTING FILE and the Mode is "w" then PVM Opens Existing File  in write Mode and Existing Data of 
    EXisting File OVERLAPPED with New Data.
    
-------------------------------------------------------------------------------------------------------------------------------------------------------------
 a
-------------------------------------------------------------------------------------------------------------------------------------------------------------
=>This mode is used for Creating New File and Opens in Write Mode.
=>If we Choose NEW FILE and the Mode is "a" then PVM Creates New File and Opened in write Mode and we Can 
    Perform Write Operations Only.
=>If we Choose EXISTING FILE and the Mode is "a" then PVM Opens Existing File  in write Mode and Existing Data of 
    Existing File APPENDED with New Data.
    
-------------------------------------------------------------------------------------------------------------------------------------------------------------
 r+
-------------------------------------------------------------------------------------------------------------------------------------------------------------
=>This Mode is used for Opening the Specified File Name in Read Mode and  First we perform Read Operation  and  
    Later we can also Perform Write Operation.
=>If we open any file name in "r+" mode and If that file name does not exist in Secondary Memory then we get 
    FileNotFoundError.
    
-------------------------------------------------------------------------------------------------------------------------------------------------------------
 w+
-------------------------------------------------------------------------------------------------------------------------------------------------------------
=>This mode is used for Creating New File and Opens in Write Mode.
=>If we Choose NEW FILE and the Mode is "w+" then PVM Creates New File and Opened in write Mode and First we 
   Can  Perform Write Operation and Later we can perform Read Operation also.
=>If we Choose EXISTING FILE and the Mode is "w+" then PVM Opens Existing File  in write Mode and Existing Data of 
     File OVERLAPPED with New Data.
     
-------------------------------------------------------------------------------------------------------------------------------------------------------------
 a+
-------------------------------------------------------------------------------------------------------------------------------------------------------------
=>This mode is used for Creating New File and Opens in Write Mode.
=>If we Choose NEW FILE and the Mode is "a+" then PVM Creates New File and Opened in write Mode and  First we 
    Can Perform Write Operations  and Later we can perform Read Operations also.
=>If we Choose EXISTING FILE and the Mode is "a+" then PVM Opens Existing File  in write Mode and Existing Data of 
    Existing File APPENDED with New Data.
    
-------------------------------------------------------------------------------------------------------------------------------------------------------------
 x
-------------------------------------------------------------------------------------------------------------------------------------------------------------
=>This mode is used for Creating New File  eXclusively in Write Mode Only Once  and We can Perform Write 
   Operations Only.
=>If we Open Existing File in "x" Mode then we get FileExistError.

-------------------------------------------------------------------------------------------------------------------------------------------------------------
 x+
-------------------------------------------------------------------------------------------------------------------------------------------------------------
=>This mode is used for Creating New File  eXclusively in Write Mode Only Once and  First We can Perform Write Operations  and Later we can Perform Read Operations also.
=>If we Open Existing File in "x+" Mode then we get FileExistError.

-----------------------------------------------------------------------------------------------------------------




=========================================================
					Number of Approaches to Open the Files
=========================================================
=>In Python Programming, we have Two Approaches to Open the File. They are

			1. By using open()
			2. By using " with open() as "
------------------------------------------------------------------------------------------------------------------------------------------------------------
 By using open()
------------------------------------------------------------------------------------------------------------------------------------------------------------
Syntax:     varname=open("File Name","File Mode")
------------------
Explanation

------------------
=>Here Varname Represents File pointer which will point to the Opened File and whose type is 
    <class, _io.TextIOWrapper>.
=>open() is used for Opening the File in Specified File Mode
=>FileName Represents Name of the File to be specified by the Programmer
=>File Mode Represents any one of the File Opening Modes ( r,w,a,r+,w+,a+,x,x+)
=>Once we open any file name with open() then we must close the File by using close() and It is  mandatory for maintaining  Consistency of Data(Manual Closing--- there is no concept of Auto-Closeability).

------------------------------------------------------------------------------------------------------------------------------------------------------------
By using " with open() as "
------------------------------------------------------------------------------------------------------------------------------------------------------------
Syntax:       with  open("File Name","File Mode") as varname:
            				---------------------------------
            				---------------------------------
            				Block of Statements--Performs File Operations
            				---------------------------------
            				---------------------------------
            		    ----------------------------------------
      		    Other Statements
      		    -----------------------------------------
************************
Explanation
************************
=>Here "with" and "as" are the Keywords.
=>Here Varname Represents File pointer which will point to the Opened File and whose type is 
    <class, _io.TextIOWrapper>.
=>open() is used for Opening the File in Specified File Mode
=>FileName Represents Name of the File to be specified by the Programmer
=>File Mode Represents any one of the File Opening Modes ( r,w,a,r+,w+,a+,x,x+)
=>The execution Process of "with open(---) as " is that "As Long as PVM present in side of " with open(---) as " Indentation then File Name is actively Available and once PVM comes out-off " with open(---) as" Indentation then File name closed Automatically and This Facility is Called Auto-Closeability of File". No Need to close the  file by using close() manually.

------------------------------------------------------------------------------------------------------------------------------------------------------------






=======================================================
					Writing the Data to the File
=======================================================
=>To write the Data to the File, we have Two Pre-Defined Functions present in the object of File Pointer . They are
				1. write()
				2. wrilines()
    
-----------------------------------------------------------------------------------------------------------------------------------------------------
 write()
-----------------------------------------------------------------------------------------------------------------------------------------------------
Syntax:    FilePointerobj.write(str data)
-----------------------------------------------------------------------------------------------------------------------------------------------------
=>This function is used for writing any type of Data to the File in the form of str.
=>If we have non-str data then we must convert into str and we must write that str to the file.

-----------------------------------------------------------------------------------------------------------------------------------------------------
writelines()
-----------------------------------------------------------------------------------------------------------------------------------------------------
Syntax:    FilePointerobj.writelines(str(Iterable-object))
-----------------------------------------------------------------------------------------------------------------------------------------------------
=>This function is used for writing any Iterable Object type  to the File in the form of str.

-----------------------------------------------------------------------------------------------------------------------------------------------------
NOTE: The above Two Functions writes the Data to the file in the form of Value by Value (It is one of the Limitation--we 
            want all the values to write at a time to File)
-----------------------------------------------------------------------------------------------------------------






=======================================================
						Reading the Data from the File
=======================================================
=>To read the Data from the File, we have 2 Pre-Defined Functions present in File Pointer object. They are

			1. read()
			2. readlines()
------------------------------------------------------------------------------------------------------------------------------------------------------------
read()
------------------------------------------------------------------------------------------------------------------------------------------------------------
Syntax:  varname=FilePointerObj.read()
------------------------------------------------------------------------------------------------------------------------------------------------------------
=>This Function is used for reading entire Data of the File and Placed in LHS Varname in the form of str.

------------------------------------------------------------------------------------------------------------------------------------------------------------
readlines()
------------------------------------------------------------------------------------------------------------------------------------------------------------
Syntax:	varname=FilePointerObj.readlines()
------------------------------------------------------------------------------------------------------------------------------------------------------------
=>This Function is used for reading the entire data of the file Placed in LHS Varname in the form of list

------------------------------------------------------------------------------------------------------------------------------------------------------------
NOTE: The above Two Functions Reads the Data from  the file in the form of Value by Value (It is one of the Limitation--we want all the values to read at a time from File)
