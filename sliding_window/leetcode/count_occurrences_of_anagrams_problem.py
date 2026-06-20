txt = "forxxorfxdofr"
pat = "for"



counter={}

for right in range(len(pat)):
    
    counter[pat[right]]=counter.get(pat[right],0)+1
    
    
    
left=0
window={}
count=0
for right in range(len(txt)):
    window[txt[right]]=window.get(txt[right],0)+1
    
    while len(window)>3:
        window[txt[left]]-=1
        
        if window[txt[left]]==0:
            del window[txt[left]]
            
        left+=1
        
    if counter==window:
        count+=1
        
        
print(count)