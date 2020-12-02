import re 
import random

while True:
    reply = 'Beckham : '
    lis = ['Hello','Yoo!','hi','yo','Hola',"Bonjeur",'Guten tag','Nihao','Hey,There!','Salam']
    
    s=input('USER : ')
    
    q=re.search(pattern = r'when', string = s)
    m=re.search(pattern = r'my .*', string = s)
    n=re.search(pattern = r"I'm .*", string = s)
    w=re.search(pattern = r"(w|W)eather", string = s)
    b=re.search(pattern = r"bore(d)?", string = s)
    l=re.search(pattern = r"create(d)?", string = s)
    y=re.search(pattern = r".*(y|Y)our.*(n|N)ame" , string = s)
    z=re.search(pattern = r"(G|g)ood\s?(b|B)ye" , string = s)
    t=re.search(pattern = r"(T|t)hank" , string = s)
    hi=re.search(pattern = r"[y|Y]o|[h|H]ey|[h|H]ello|[h|H]i|[M|m]orning|[A|a]fternoon" , string = s)
    
    if q:
        reply+="speicfy the time,please?"
    elif m: 
        s = re.sub(pattern= 'my', repl='YOUR', string=m.group())
        s = re.sub(pattern= 'me', repl='YOU', string=s)
        reply+=s.upper()+"!!!"
    elif n:
        s = re.sub(pattern= "I'm", repl='YOU ARE', string=n.group(0))
        reply+="I'm Sorry to hear " + s.upper()
    elif w:
        reply+="yeah I Know!"
    elif b:
        reply+="Please have a solo music? click the following link: https://www.youtube.com/watch?v=5rX8m2mlQEA"
    elif y:
        reply+="My name is Beckham"
    elif l:
        l1=re.search(pattern = "(w|W)ho",string =s)
        l2=re.search(pattern="(W|w)hy",string =s)
        if l1:
            reply+="obvioiusly my master.Mohibillah & Arjon"
        elif l2:
            reply+="For Annajiat Sir"
    elif t:
        reply+="You're Welcome!"
    elif hi:
        reply+=random.choice(lis)
    elif z:
        print ("Beckham : Have a nice Day! I am gonna sleep.")
        break
           
    else:
        reply+=("please,clarify your query")
    
    print(reply)
    
        
    