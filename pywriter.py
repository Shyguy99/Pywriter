import speech_recognition as sr
import pyautogui as key_bo
import time
r = sr.Recognizer()

keywords={"minus":"-","plus":"+","divide":"/","multiply":"*","equal":"==","equals":"==","modulus":"%","floor":"//","string":"str(","integer":"int(","length":"len(","dot":".","power":"**","bracket":"()","(":"()","less":"<","greater":">","one":"1","zero":"0","hundred":"100"}
def lis(r):

    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening....")
            audio = r.listen(source,phrase_time_limit=10)
            print("Got instruction",end="")
            try:
                data = r.recognize_google(audio,language='en-US')

                break
            except:
                pass
    return data
def assi_con():
    con = ""
    while "next line" not in con:
        out = ""

        con = lis(r)
        con = con.lower()

        con_l = list(con.split())
        tr = 0
        if "next line" in con:
            l_con = len(con_l) - 2
        else:
            l_con = len(con_l)
        while tr < l_con:
            c = con_l[tr]
            if c in keywords:
                if c == "less":
                    if "equal" in con_l[tr + 2]:
                        out += "<="
                        tr += 4
                    else:
                        out += "<"
                        tr += 2
                elif c == "greater":
                    if "equal" in con_l[tr + 2]:
                        out += ">="
                        tr += 4
                    else:
                        out += ">"
                        tr += 2
                elif "equal" in c:
                    out += "=="
                    if con_l[tr + 1] == "to":
                        tr += 2
                    else:
                        tr += 1
                elif c == "length":
                    out += "len(" + con_l[tr + 2] + ")"
                    tr += 3
                elif c == "string":
                    temp = con_l[tr + 1:]
                    s = " "
                    out += "\"" + s.join(temp) + "\""
                    tr += len(con_l)

                elif c == "integer":
                    tr += 1
                elif c == "modulus":
                    out += "%"
                    tr += 1
                elif c == "minus" or c == "plus" or c == "multiply" or c == "divide":
                    d = {"minus": "-", "plus": "+", "divide": "/", "multiply": "*"}
                else:
                    out += keywords[c] + " "
                    tr += 1
            else:
                if c == "x" and con_l[tr + 1].isnumeric():
                    out += "*"
                    tr += 1
                else:
                    out += " " + c
                    tr += 1
        key_bo.write(out, interval=0.15)


to_space=0
time.sleep(4)
while True:
    print("Program Started")
    text=lis(r)
    text=text.lower()
    print(text)
    print("run" in text)
    if ("initialise" or "initialize" ) in text or "add" in text:
        print("initialize command")
        out=""
        sp=list(map(str,text.split()))
        out+=sp[-1]+"="

        key_bo.write(out, interval=0.25)
        out=""
        if "integer" in text:
            if "empty" in text:
                 out+="0"
                 key_bo.press("enter")

            else:
                assi_con()
                key_bo.press("enter")

        elif "string" in text:
            if "empty" in text:
                out += "\"\""
                key_bo.press("enter")

            else:
                assi_con()
                key_bo.press("enter")

        elif "list" in text:
            if "empty" in text:
                out+="[]"
                key_bo.write(out)
                key_bo.press("enter")
            else:
                data=lis(r)
                if data=="empty":
                    out += "[]"
                    key_bo.press("enter")

                else:
                    data=list(data.split())
                    out+="["
                    for i in data:
                        try:
                            chk=int(i)
                        except:
                            i="\""+i+"\""
                        out+=i+","
                    out=out[:len(out)-1]+"]"
                key_bo.write(out, interval=0.25)
                key_bo.press("enter")


    elif "create" in text or "insert" in text or "call" in text:
        out=""
        if "loop" in text and "for" in text:
            to_space+=4
            text=text.lower()
            tex = list(text.split())
            i_in = tex.index("loop") + 1
            i = tex[i_in]
            if "from" in tex:

               f_to=tex.index("to")
               a=tex[f_to-1]
               b=tex[f_to+1]
               if not a.isnumeric() and tex[f_to-3]=="length":
                       a="len("+a+")"
               if not b.isnumeric() and b == "length":
                   b = "len(" + tex[f_to+3] + ")"
               if "gap" in text or "jump" in text:
                    c_in=tex.index("gap")
                    if tex[c_in+1]=="of":
                        c=tex[c_in+2]
                    else:
                        c=tex[c_in+1]
                    out="for "+i+" in"+" range("+a+","+b+","+c+"):"
               else:
                   out = "for " + i + " in" + " range(" + a + "," + b +"):"
            elif "on" in tex:
                on_in=tex.index("on")+1
                on=tex[on_in]
                out = "for " + i + " in " +on+ "):"
            key_bo.write(out, interval=0.25)
            time.sleep(1)
            key_bo.press("enter")

        elif "while" in text or "else if" in text or "if" in text:
               to_space+=4
               if "while" in text:
                   out="while"
               elif "else if" in text:
                   out="elif"
               else:
                   out="if"

               key_bo.write(out,interval=0.25)

               assi_con()

               key_bo.write(":")
               time.sleep(1)
               key_bo.press("enter")
        elif "else" in text:
            out="else:"
            key_bo.write(out)
            time.sleep(1)
            key_bo.press("enter")

        elif "function" in text:
            out=""
            if "call" not in text:
                to_space += 4
                out="def "
            con=list(text.split())
            f_in=con.index("function")
            out+=con[f_in+1]+"("
            key_bo.write(out)
            co=""
            out=""
            while "next line" not in co:
                co=lis(r)
                con=list(co.split())
                tr=0
                while tr<len(con):
                    if con[tr] =="next" and (tr+1<=len(con)-1) and con[tr+1]=="line":
                        print("aya")
                        break
                    else:
                          out+=con[tr]
                          key_bo.write(con[tr]+",")
                          tr+=1
            if len(out)>0:
                 key_bo.press("backspace")
            key_bo.write(")")
            if "call" not in text:
                key_bo.write(":")
            time.sleep(1)
            key_bo.press("enter")
    elif "run" in text:
        key_bo.hotkey('alt','shift','f10')
    elif "print" in text:
         out="print("
         key_bo.write(out)

         assi_con()

         key_bo.write(")")
         time.sleep(1)
         key_bo.press("enter")




    elif "finish" in text or "end" in text:
        if to_space>=4:
            key_bo.press(["left","left","left","left"])
            to_space-=4









