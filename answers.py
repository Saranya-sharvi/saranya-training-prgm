1.Linux:
	Linux is a freesource as well opensource operating system.
  comand:
	ls:list
	pwd:present working directory
	touch:create new file
	cd:change directory
	mkdir:make new directory

2.Linux kernal:
	kernal is the central module of an os.
	it can connects the system hardware to the software.
	it can schedules the process and also manages the user input and output.

3.Diff between 32bit and 64 bit computer:
	2^32=4,294,967,296 values
	2^64=18,446,744,073,709,551
	32 bit and 64 bit computers can cabable of store the above values.
	The big difference is storage.
	Storage is one of the important needed thing of an computer.
	The maximum memory access they have from 64bit computers.
    we are have maximum memory access in 64 bit.
    

4.Git:
	It is an file sharing flatform.
	useful to share the files amoung many devices.
    saranya@saranya-Aspire-E1-431 ~/saranya-training-prgm $ git --version
    git version 2.7.4


5.My Github Account:

        username:Saranya-sharvi
        mail:a.saranya21214@gmail.com
        repository name:saranya-training-prgm
       

6.Low level language:
	Its a programming language that provides little abstraction from a computer's instruction set architecture.
	It can convert to machine code without a compiler or interpreter.
	eg:assembly language and machine level language
  High level language:
	Its a programming language that provides strong abstraction from the computer details.
	it may use natural language elements because easier to use programer.
	eg:fortran and pascal

7.Object:
	An object can be var,datastruct,func,or a method ...
	Is a value in memory referenced by an identifier.
	each object is an instance of a particular class or sub class.
	eg:
		class Employee{
		int empid;
		string empname;
		public static void main(String args[]){
		Employee e1=new Employee();
		System.out.println(e1.empid);
		System.out.println(e1.empname);
}
}
	here,e1 is object of Employee class.

8.kernal version and Linux Distribution name using comand:
        
        saranya@saranya-Aspire-E1-431 /home $ cat /etc/lsb-release
            DISTRIB_ID=LinuxMint
            DISTRIB_RELEASE=18.1
            DISTRIB_CODENAME=serena
            DISTRIB_DESCRIPTION="Linux Mint 18.1 Serena"

        saranya@saranya-Aspire-E1-431 /home $ uname -r
            4.4.0-53-generic

    kernal version and Linux Distribution name using coding:

        import platform
        import sys

        def linux_distribution():
            try:
        return platform.linux_distribution()
            except:
        return "N/A"

        print("""Python version: %s
        dist: %s
        linux_distribution: %s
        system: %s
        machine: %s
        platform: %s
        uname: %s
        version: %s
        mac_ver: %s
        """ % (
        sys.version.split('\n'),
        str(platform.dist()),
        linux_distribution(),
        platform.system(),
        platform.machine(),
        platform.platform(),
        platform.uname(),
        platform.version(),
        platform.mac_ver(),
        ))

       output:


        saranya@saranya-Aspire-E1-431 ~/saranya-training-prgm $ python fuct.py
Python version: ['2.7.12 (default, Nov 19 2016, 06:48:10) ', '[GCC 5.4.0 20160609]']
dist: ('LinuxMint', '18.1', 'serena')
linux_distribution: ('LinuxMint', '18.1', 'serena')
system: Linux
machine: x86_64
platform: Linux-4.4.0-53-generic-x86_64-with-LinuxMint-18.1-serena
uname: ('Linux', 'saranya-Aspire-E1-431', '4.4.0-53-generic', '#74-Ubuntu SMP Fri Dec 2 15:59:10 UTC 2016', 'x86_64', 'x86_64')
version: #74-Ubuntu SMP Fri Dec 2 15:59:10 UTC 2016
mac_ver: ('', ('', '', ''), '')

saranya@saranya-Aspire-E1-431 ~/saranya-training-prgm $ 


        


  

9.Python code using function,file input and print each line with line number in      terminal:

     

    def add(a,b):
       c=a+b
       return c

    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))


    sum=add(a,b)
    print(list(enumerate(str(sum))))

    output:
    
        saranya@saranya-Aspire-E1-431 ~/saranya-training-prgm $ python3 line.py
            enter the value of a:111
            enter the value of b:111
            [(0, '2'), (1, '2'), (2, '2')]



10.Python code using three functions within the class and Dictionary:


    """ assign of class"""
class maths():
    """ perform division operation """

    def division(a,b):
        c=a%b
        return c
    """ perform addition operation """

    def addition(a,b):
        c=a+b
        return c
    """ perform subtraction operation """

    def subtaction(a,b):
        c=a-b
        return c
    """get the input from user"""


a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))

    
ans={}
ans["division"]=maths.division(a,b)
ans["addition"]=maths.addition(a,b)
ans["subtraction"]=maths.subtaction(a,b)

print("result is:",ans)  
    

output:

        saranya@saranya-Aspire-E1-431 ~/saranya-training-prgm $ python3 tue.py
        enter the value of a:10
        enter the value of b:20
        result is: {'subtraction': -10, 'addition': 30}

    


