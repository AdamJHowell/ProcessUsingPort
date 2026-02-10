# ProcessUsingPort

### A simple script to report the Windows process using a port.

Create a batch file with this one line:

```batch
@python C:\Source\GitHub\ProcessUsingPort\ProcessUsingPort.py %1
```

Change the path to wherever this repo is cloned.  Save the file to a location in your path.

I name that file pup.bat and use it like this:

```
C:\>pup 8883
Searching for process listening on port 8883...
Found PID: 24396
Executable: faircom.exe

C:\>
```
