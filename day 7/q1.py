#wap in one statement to combine and print elemetns of twolist using list comprehension
#l1=[10,20,30]
#l2=[30,10,40]
#output=[(10,30),(10,40),.....,(30,40)]

print([(i,j) for i in [10,20,30]  for j in [30,10,40] if i!=j])
                                                                                                                                                                                                                                        