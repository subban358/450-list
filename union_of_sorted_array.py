def doUnion(a,n,b,m):
    i, j = 0, 0
    count = 0
    res = []
    
    while i < n and j < m:
        if i > 0 and a[i] == a[i-1]:
            i += 1
            continue
        
        if j >0 and b[j] == b[j-1]:
            j += 1
            continue
        
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
            count += 1
        elif a[i] > b[j]:
            res.append(b[j])
            j += 1
            count += 1
        else:
            res.append(a[i])
            i += 1
            j += 1
            count += 1
            
    while i < n:
        if i > 0 and a[i] != a[i-1]:
            res.append(a[i])
            i += 1
            count += 1
            
    while j < m:
        if j > 0 and b[j] != b[j-1]:
            res.append(b[j])
            j += 1
            count += 1
            
    return count
