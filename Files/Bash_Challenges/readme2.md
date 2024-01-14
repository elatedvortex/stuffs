# Bash Challenges

## 1. 
### (a) Display the path of your current directory
**Command:** `pwd`  
![1a](1a.png)

### (b) List contents of the current directory
**Command:** `ls`  
![1b](1b.png)

### (c) List contents of the current directory (including hidden files)
**Command:** `ls -a`  
![1c](1c.png)

## 2. 
### (a) Create a new directory named 'a'
**Command:** `mkdir a`  
![2a](2a.png)

### (b) Move to the newly created directory 'a'
**Command:** `cd a`  
![2b](2b.png)

### (c) Create a blank file named 'file1'
**Command:** `touch file1`  
![2c](2c.png)

### (d) Display the file type of 'file1'
**Command:** `file file1`  
![2d](2d.png)

### (e) Add the line “Hello World” to 'file1'
**Command:** `echo Hello World > file1`  
![2e](2e.png)

### (f) Display the contents of 'file1'
**Command:** `cat file1`  
![2f](2f.png)

### (g) Display the file type of 'file1' again
**Command:** `file file1`  
![2g](2g.png)

## 3. 
### (a) Create 'file2' and add contents
**Command:** `cat > file2 ; cat file2`  
![3a](3a.png)

### (b) Display the contents of 'file2'
**Command:** `cat file2`  
![3b](3b.png)

### (c) Display 'file2' contents with reversed lines
**Command:** `tac file2`  
![3c](3c.png)

## 4. 
### (a) Concatenate 'file1' and 'file2' into 'file3'
**Command:** `cat file1 file2 > file3`  
![4a](4a.png)

### (b) Display the contents of 'file3'
**Command:** `cat file3`  
![4b](4b.png)

## 5. 
### (a) Create directories 'b/c' and 'd' in 'a'
**Command:** `mkdir -p b/c d`  
![5a](5a.png)

### (b) Copy 'd' to 'b/c'
**Command:** `cp -r d b/c`  
![5b](5b.png)

### (c) Delete 'd' in 'a'
**Command:** `rmdir d`  
![5d](5d.png)

### (d) Copy 'file3' to 'b/c/d'
**Command:** `cp file3 b/c/d`  
![5e](5e.png)

## 6. 
### (a) Rename 'file3' to 'file0' in 'b/c/d'
**Command:** `mv b/c/d/file3 b/c/d/file0`  
![6a](6a.png)

### (b) Move 'file0' to 'a'
**Command:** `mv b/c/d/file0 ../../..`  
![6b](6b.png)

## 7. 
### (a) Go to the home directory
**Command:** `cd ~`  
![7a](7a.png)

### (b) Create 'test' in 'a/b/c/d'
**Command:** `touch a/b/c/d/test`  
![7b](7b.png)

### (c) Find and display the path of 'test'
**Command:** `find -type f -name "test"`  
![7c](7c.png)

## 8. 
### (a) Get the man page of grep and save to 'grepman.txt'
**Command:** `man grep > ~/elatedvortex/readme/a/grepman.txt`  
![8a](8a.png)

### (b) Print lines containing 'FILE' (Case sensitive) in 'grepman.txt'
**Command:** `grep -w "FILE" ~/elatedvortex/readme/a/grepman.txt`  
![8b](8b.png)

## 9. 
### (a) Remove directory 'b' and its contents
**Command:** `rm -rf ~/elatedvortex/readme/a/b`  
![9a](9a.png)

### (b) Remove files starting with 'file'
**Command:** `rm -f ~/elatedvortex/readme/a/file*`  
![9b](9b.png)

## 10.
### (a) Download 'logo.png' from https://blog.bi0s.in/
**Command:** `wget https://blog.bi0s.in/assets/logo.png -O logo1.png`  
![10a](10a.png)

### (b) Download 'logo.png' using Python script
**Command:** `vim ~/elatedvortex/readme/a/10b.py; python ~/elatedvortex/readme/a/10b.py; ls`  
![10b](10b.png)  
> Content of 10b.py:
```python
import requests
response = requests.get("https://blog.bi0s.in/assets/logo.png")
with open("logo2.png", 'wb') as file:
    file.write(response.content)
```
![10bf](10bf.png)
### (c) Display metadata of 'logo.png'
**Command:** `identify -verbose logo.png`  
![10c](10c.png)

## 11. 
### (a) Use traceroute on google.com
**Command:** `traceroute google.com`  
![11a](11a.png)

### (b) Find subdomains and IP addresses of google.com
**Command:** `nslookup google.com; nslookup -type=ns google.com`  
![11b](11b.png)

## 12. 
**Command:** `python -m http.server 8080`  
![12](12a.png)

## 13. 
### (a) Scan your machine with nmap
**Command:** `nmap -iR 10`  
![13a](13a.png)

### (b) Scan IP address from https://tryhackme.com/room/furthernmap
**Command:** `nmap -v 10.10.14.137 -sV -sS -A`  
![13b](13b.png)

## 14. 
### (a) Start the server
**Command (Server):** `nc -nvlp <portno>`  
![14a](14at1.png)

**Command (Client):** `nc <ip addr> <portno>`  
![14b](14at2.png)

### (b) Transfer a file from server to client and display it
**Command (Server):** `touch test1; nc -v -w 30 <portno> < <filename>`  
![14bt1](14bt1.png)

**Command (Client):** `nc -v -w 3 <ip addr> <port no> < <filename>`  
![14bt2](14bt2.png)
