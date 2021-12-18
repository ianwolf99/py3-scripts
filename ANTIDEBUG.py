
for proc in psutil.process_iter():
    try:
        processName = proc.name()
        if processName == "HTTPDebuggerUI.exe":
            proc.terminate()
        if processName == "HTTPDebuggerSvc.exe":
            proc.terminate()
    except:
        pass
