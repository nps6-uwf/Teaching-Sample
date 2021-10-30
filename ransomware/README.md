# ransomware

This is a really basic piece of malware that I wrote in python that encrypts all of the text files in the directory that the malware executable is launched.  The script can be run without using the executable: <code> python worm.py </code>.  The executable is in the sandbox directory with some test files that will get encrypted if you launch the executable.  

<b>XOR Encryption</b>

XOR outputs 1 or True if both input bits are different (1 & 0) and it outputs 0 or False if both ouput bits are the same (1 & 1 or 0 & 0).

<table>
  <tbody>
    <tr>
      <td> variable name</td><td>base 10 (decimal)</td><td>base 2 (binary)</td>
     </tr>
    <tr>
      <td> A</td><td>4</td><td>0100</td>
     </tr>
    <tr>
      <td> B</td><td>11</td><td>1011</td>
     </tr>
    <tr>
      <td> A XOR B</td><td> 0100 XOR 1011 </td><td>1111</td>
     </tr>
  </tbody>
</table>

You can use the XOR operation to encrypt text files by mapping each character in a string to the unicode character code, the <code>ord()</code> function in python and the <code> ^ </code> operator is XOR.  You then apply the following transformation to each character in the file <code> ord(c) ^ secret_key </code> where secret key is some integer or collection of integers.  For maximum security the secret_key should be an array of integers and to encrypt the ith character in a string you will <code> ord(s[i]) ^ secret_key[i % len(secret_key)]</code> where <i>s</i> is the string to be encrypted.

<b style="color: indigo;">Creating the Executable</b>

If you want to create an executable, so that you can get unsuspecting targets to deploy the worm use the <a href="https://www.pyinstaller.org/">pyinstaller</a> module.  To install with python: <code>pip install pyinstaller</code>.  To create the executable <code> pyinstaller --onefile --icon=file.ico worm.py </code> the <code> --icon=file.ico </code> flag is only if you want to add an icon for your executable (I'm trying to disguise my executable as a text file).  The onefile flag ensures that the executable can run without dependencies and be moved from the <i>dist</i> folder after created.

<b style="color: indigo;">Spoofing the File Extension</b>

To spoof the file extension so the target does not see the <i>.exe</i> suffix attached to executable files, you can use the <code>spoof_file.py</code> python file.  This code takes two command line arguments: <i>file_name</i> and <i>file_extension</i> and can be run from the command line: <code>python spoof_file.py "worm" "exe"</code>.  So what this code does is it leverages a special unicode character called "right to left" or <b>\u202e</b> which reverses the characters that follow it.  For example: "\u202e txt.exe" -> "exe.txt", in other words we can mask file extensions.  If you check out the executable, <i>"worm exe.txt"</i> in the sandbox directory you will notice the suffix been spoofed.  An unsuspecting target might think they are opening a text file, but in reality they just encrypted all text files in the current directory.

<b>Conclusions</b>

If you decide to download this code take extreme caution not to launch the executable in a directory with important text files, as a rule of thumb this executable should not be launched in any system folder (Documents, Desktop, etc.) because these folders may have hidden text files that you need.  Testing should be carried out in dedicated user created folders.  Although this code only encrypts <i>.txt</i> files in the current directory, modifying this code to encrypt virtually every file in every folder would not be difficult; however, you would encounter some permissions errors when trying to encrypt in special folders like system32.  This code should be partially alarming in that it shows how easy it is to create & deploy a piece of malware in python that can wreak havoc on an insecure system.

Nick
