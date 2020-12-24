import tkinter as tk
from tkinter import ttk
from pynput.keyboard import Key, Controller

# Creating Keyboad
Keyboard=Controller()
key = tk.Tk()  
key.title('IATH Keyboard')
Capital=True
def Cpital_lower(letter):
	if Capital:
		return letter.upper()
	else:
		return letter.lower()

def press(letter):
	if type(letter)==str:
		letter= Cpital_lower(letter)
	Keyboard.press(letter)
	Keyboard.release(letter)
	print(letter)






# Size window size
key.geometry('1010x250')		 # normal size
key.maxsize(width=1010, height=230)	  # maximum size
key.minsize(width= 1010 , height = 230)	 # minimum size


key.configure(bg = 'Gray')	

# entry box
equation = tk.StringVar()
Dis_entry = ttk.Label(key,textvariable = equation)
Dis_entry.grid(row= 0 , columnspan = 100, ipadx = 999 , ipady = 0)


q = ttk.Button(key,text = Cpital_lower('Q') , width = 6, command = lambda : press('Q'))
q.grid(row = 1 , column = 0, ipadx = 6 , ipady = 10)

w = ttk.Button(key,text = Cpital_lower('W') , width = 6, command = lambda : press('W'))
w.grid(row = 1 , column = 1, ipadx = 6 , ipady = 10)

E = ttk.Button(key,text = Cpital_lower('E') , width = 6, command = lambda : press('E'))
E.grid(row = 1 , column = 2, ipadx = 6 , ipady = 10)

R = ttk.Button(key,text = Cpital_lower('R') , width = 6, command = lambda : press('R'))
R.grid(row = 1 , column = 3, ipadx = 6 , ipady = 10)

T = ttk.Button(key,text = Cpital_lower('T') , width = 6, command = lambda : press('T'))
T.grid(row = 1 , column = 4, ipadx = 6 , ipady = 10)

Y = ttk.Button(key,text = Cpital_lower('Y') , width = 6, command = lambda : press('Y'))
Y.grid(row = 1 , column = 5, ipadx = 6 , ipady = 10)

U = ttk.Button(key,text = Cpital_lower('U') , width = 6, command = lambda : press('U'))
U.grid(row = 1 , column = 6, ipadx = 6 , ipady = 10)

I = ttk.Button(key,text = Cpital_lower('I') , width = 6, command = lambda : press('I'))
I.grid(row = 1 , column = 7, ipadx = 6 , ipady = 10)

O = ttk.Button(key,text = Cpital_lower('O') , width = 6, command = lambda : press('O'))
O.grid(row = 1 , column = 8, ipadx = 6 , ipady = 10)

P = ttk.Button(key,text = Cpital_lower('P') , width = 6, command = lambda : press('P'))
P.grid(row = 1 , column = 9, ipadx = 6 , ipady = 10)

cur = ttk.Button(key,text = '{' , width = 6, command = lambda : press('{'))
cur.grid(row = 1 , column = 10 , ipadx = 6 , ipady = 10)

cur_c = ttk.Button(key,text = '}' , width = 6, command = lambda : press('}'))
cur_c.grid(row = 1 , column = 11, ipadx = 6 , ipady = 10)

back_slash = ttk.Button(key,text = '\\' , width = 6, command = lambda : press('\\'))
back_slash.grid(row = 1 , column = 12, ipadx = 6 , ipady = 10)


clear = ttk.Button(key,text = 'Clear' , width = 6, command = lambda : press(Key.backspace))
clear.grid(row = 1 , column = 13, ipadx = 20 , ipady = 10)

# Second Line Button



A = ttk.Button(key,text = Cpital_lower('a') , width = 6, command = lambda : press(Cpital_lower('a').lower()))
A.grid(row = 2 , column = 0, ipadx = 6 , ipady = 10)



S = ttk.Button(key,text = Cpital_lower('S') , width = 6, command = lambda : press('S'))
S.grid(row = 2 , column = 1, ipadx = 6 , ipady = 10)

D = ttk.Button(key,text = Cpital_lower('D') , width = 6, command = lambda : press('D'))
D.grid(row = 2 , column = 2, ipadx = 6 , ipady = 10)

F = ttk.Button(key,text = Cpital_lower('F') , width = 6, command = lambda : press('F'))
F.grid(row = 2 , column = 3, ipadx = 6 , ipady = 10)


G = ttk.Button(key,text = Cpital_lower('G') , width = 6, command = lambda : press('G'))
G.grid(row = 2 , column = 4, ipadx = 6 , ipady = 10)


H = ttk.Button(key,text = Cpital_lower('H') , width = 6, command = lambda : press('H'))
H.grid(row = 2 , column = 5, ipadx = 6 , ipady = 10)


J = ttk.Button(key,text = Cpital_lower('J') , width = 6, command = lambda : press('J'))
J.grid(row = 2 , column = 6, ipadx = 6 , ipady = 10)


K = ttk.Button(key,text = Cpital_lower('K') , width = 6, command = lambda : press('K'))
K.grid(row = 2 , column = 7, ipadx = 6 , ipady = 10)

L = ttk.Button(key,text = Cpital_lower('L') , width = 6, command = lambda : press('L'))
L.grid(row = 2 , column = 8, ipadx = 6 , ipady = 10)


semi_co = ttk.Button(key,text = ';' , width = 6, command = lambda : press(';'))
semi_co.grid(row = 2 , column = 9, ipadx = 6 , ipady = 10)


d_colon = ttk.Button(key,text = '"' , width = 6, command = lambda : press('"'))
d_colon.grid(row = 2 , column = 10, ipadx = 6 , ipady = 10)


enter = ttk.Button(key,text = 'Enter' , width = 6, command = lambda : press(Key.enter) )
enter.grid(row = 2 ,column=11, columnspan = 3, ipadx = 85 , ipady = 10)

Z = ttk.Button(key,text = Cpital_lower('Z') , width = 6, command = lambda : press('Z'))
Z.grid(row = 3 , column = 0, ipadx = 6 , ipady = 10)


X = ttk.Button(key,text = Cpital_lower('X') , width = 6, command = lambda : press('X'))
X.grid(row = 3 , column = 1, ipadx = 6 , ipady = 10)


C = ttk.Button(key,text = Cpital_lower('C') , width = 6, command = lambda : press('C'))
C.grid(row = 3 , column = 2, ipadx = 6 , ipady = 10)


V = ttk.Button(key,text = Cpital_lower('V') , width = 6, command = lambda : press('V'))
V.grid(row = 3 , column = 3, ipadx = 6 , ipady = 10)

B = ttk.Button(key, text= Cpital_lower('B') , width = 6 , command = lambda : press('B'))
B.grid(row = 3 , column = 4 , ipadx = 6 ,ipady = 10)


N = ttk.Button(key,text = Cpital_lower('N') , width = 6, command = lambda : press('N'))
N.grid(row = 3 , column = 5, ipadx = 6 , ipady = 10)


M = ttk.Button(key,text = Cpital_lower('M') , width = 6, command = lambda : press('M'))
M.grid(row = 3 , column = 6, ipadx = 6 , ipady = 10)


left = ttk.Button(key,text = '<' , width = 6, command = lambda : press('<'))
left.grid(row = 3 , column = 7, ipadx = 6 , ipady = 10)


right = ttk.Button(key,text = '>' , width = 6, command = lambda : press('>'))
right.grid(row = 3 , column = 8, ipadx = 6 , ipady = 10)


slas = ttk.Button(key,text = '/' , width = 6, command = lambda : press('/'))
slas.grid(row = 3 , column = 9, ipadx = 6 , ipady = 10)


q_mark = ttk.Button(key,text = '?' , width = 6, command = lambda : press('?'))
q_mark.grid(row = 3 , column = 10, ipadx = 6 , ipady = 10)


coma = ttk.Button(key,text = ',' , width = 6, command = lambda : press(','))
coma.grid(row = 3 , column = 11, ipadx = 6 , ipady = 10)

dot = ttk.Button(key,text = '.' , width = 6, command = lambda : press('.'))
dot.grid(row = 3 , column = 12, ipadx = 6 , ipady = 10)

shift = ttk.Button(key,text = 'Shift' , width = 6, command = lambda : press(Key.shift))
shift.grid(row = 3 , column = 13, ipadx = 20 , ipady = 10)

#Fourth Line Button


ctrl = ttk.Button(key,text = 'Ctrl' , width = 6, command = lambda : press(Key.ctrl))
ctrl.grid(row = 4 , column = 0, ipadx = 6 , ipady = 10)


Fn = ttk.Button(key,text = 'Fn' , width = 6, command = lambda : press('Fn'))
Fn.grid(row = 4 , column = 1, ipadx = 6 , ipady = 10)


window = ttk.Button(key,text = 'Window' , width = 6, command = lambda : press(Key.cmd))
window.grid(row = 4 , column = 2 , ipadx = 6 , ipady = 10)

Alt = ttk.Button(key,text = 'Alt' , width = 6, command = lambda : press(Key.alt))
Alt.grid(row = 4 , column = 3 , ipadx = 6 , ipady = 10)

space = ttk.Button(key,text = 'Space' , width = 6, command = lambda : press(Key.space))
space.grid(row = 4 ,column=4,columnspan = 6 , ipadx = 200 , ipady = 10)

Alt_gr = ttk.Button(key,text = 'Alt Gr' , width = 6, command = lambda : press(Key.alt_gr))
Alt_gr.grid(row = 4 , column = 10 , ipadx = 6 , ipady = 10)

open_b = ttk.Button(key,text = '(' , width = 6, command = lambda : press('('))
open_b.grid(row = 4 , column = 11 , ipadx = 6 , ipady = 10)

close_b = ttk.Button(key,text = ')' , width = 6, command = lambda : press(')'))
close_b.grid(row = 4 , column = 12 , ipadx = 6 , ipady = 10)


tap = ttk.Button(key,text = 'Tab' , width = 6, command = lambda : press(Key.tab))
tap.grid(row = 4 , column = 13 , ipadx = 20 , ipady = 10)



key.mainloop()
