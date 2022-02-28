test_str="Mississippi"
res={}
for keys in test_str:
	res[keys]=res.get(keys,0)+1
sorted_dict= dict(sorted(res.items(),key=lambda item:item[1],reverse=True))
for key,value in sorted_dict.items():
	print(key,'=',value)