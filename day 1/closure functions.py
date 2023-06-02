def mul():
    def tab(n):
        for i in range(1,11):
            ans=n*i
            print(n,"*",i,"=",ans)
    for j in range(2,11):
        tab(j)
mul()
