def smallestSubsequence(self, s: str) -> str: 
        st=[] #stack declared
        d={} #dictionary for storing the last indeces of every unique character
        
        #storing last indeces
        for i in range(len(s)):
            d[s[i]]=i
            
        #loop for operations in stack
        for i in range(len(s)):
            
            #if stack empty insert the character
            if len(st)==0:
                st.append(s[i])
                
            #if character already present in stack, skip
            if s[i] in st:
                continue
                
            #if current character is bigger than the top of the stack, insert in stack
            elif st[-1]<s[i]:
                st.append(s[i])
                
            #if current character is smaller than the top of the stack, then compare the current character 
            #to the top of stack if top of stack character's index is not the last one according to the d 
            #and still bigger than the current character then pop top from stack st
            else:
                while len(st)!=0 and st[-1]>s[i] and d[st[-1]]>i:
                    st.pop()
                    
                #if current character not in st (or condition can be what if that character is last in s) , insert it
                if s[i] not in st:
                    st.append(s[i])
                    
        #return the stack st in string form
        return "".join(st)
