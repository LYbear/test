
import matplotlib.pyplot as plt
fracs = [2,2,1,1,1]
labels = 'houqin', 'jiemian', 'zhengjiehong','baogan','dadaima'
explode = [ 0,0,0,0,0]
plt.axes(aspect=1)
plt.pie(x=fracs, labels=labels, explode=explode,autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle = 90,pctdistance = 0.6)
plt.show()
