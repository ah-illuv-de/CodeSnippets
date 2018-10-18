# MonkeyPatching

## PythonPath to A:   BasePath.Module.SubModule.A
# File A:
def bar(): return 5
  
# File B:
def add_two_numbers(x):
    return x + bar()

# Test File
def test_add_two_numbers(monkeypatch):
    def new_bar(): print('patched'); return 10
    print(add_two_numbers(3)) # Output = 8
    monkeypatch.setattr('BasePath.Module.SubModule.B.bar',  # < -- IMPORTANT, you load it from B.py not A.py!!!!!!!
    new_bar)
    print(add_two_numbers(3)) # Prints 'Patched' & Outputs = 13

    
# CapSys or capfd (Capture the print)

def test_print_10(capsys): # or replace capsys w/capfd - capfd also captures libraries & subprocesses
    print("10")
    sys.stderr.write("20")
    out, err = capsys.readouterr()  # readouterr captures all prints till now. (then resets it)
    assert '10\n' == out # prints go to out
    assert '20' == err # sys.stderr goes to err
    print("30")
    out, err = capsys.readouterr()
    assert '30\n' == out
